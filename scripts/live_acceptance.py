"""Operational acceptance of a deployed (or local) site, driven through the real UI.

Checks: version string, bank size vs coverage.json, region pills, library filters (ready-only,
school, grade/semester/exam), whole-paper preview for chosen papers, single-question swap keeps
order and scores, PDF export -> restore round trip, fresh random composition for each grade,
phone viewport overflow. Writes a JSON report and prints a summary; exit code 1 on any failure.

Usage: python scripts/live_acceptance.py <base_url> <report.json> [paperId ...]
"""
import base64
import json
import pathlib
import random
import sys
import urllib.request

from playwright.sync_api import sync_playwright

base = sys.argv[1].rstrip('/')
report_path = pathlib.Path(sys.argv[2])
sample_ids = sys.argv[3:]
fresh = f'?fresh={random.randint(1, 10**9)}'
report = {'base': base, 'checks': [], 'errors': []}


def check(name, ok, detail=''):
    report['checks'].append({'name': name, 'ok': bool(ok), 'detail': str(detail)})
    print(('PASS ' if ok else 'FAIL ') + name, detail if not ok or detail else '')


def get(path):
    with urllib.request.urlopen(f'{base}/{path}{fresh}', timeout=60) as r:
        return r.read().decode('utf-8')


html = get('index.html')
version = html.split('app.mjs?v=')[1].split('"')[0]
coverage = json.loads(get('data/coverage.json'))
papers = {p['id']: p for p in json.loads(get('data/papers.json'))}
check('version string present', bool(version), version)
check('coverage question count', coverage['reviewedQuestions'] > 0, coverage['reviewedQuestions'])

with sync_playwright() as pw:
    browser = pw.chromium.launch(channel='chrome', headless=True)
    page = browser.new_page(viewport={'width': 1440, 'height': 1000})
    page.on('pageerror', lambda e: report['errors'].append(str(e)))
    page.on('console', lambda m: report['errors'].append(m.text) if m.type == 'error' else None)
    page.goto(f'{base}/{fresh}', wait_until='networkidle')
    page.wait_for_function('() => window.lanjuan')
    bank = page.evaluate('() => lanjuan.getBank().length')
    check('browser bank equals coverage', bank == coverage['reviewedQuestions'], f'{bank} vs {coverage["reviewedQuestions"]}')
    check('page loaded the new version', version in page.content())

    # region pills
    regions = page.evaluate('''() => [...document.querySelectorAll('[data-region-btn]')].map(b => [b.dataset.regionBtn, b.textContent.replace(/\\s+/g, ' ').trim()])''')
    check('six region choices (all + yilan + 5 metro)', len(regions) >= 7, regions)
    for key, _ in regions:
        page.locator(f'[data-region-btn="{key}"]').first.click()
        page.wait_for_timeout(250)
        text = page.locator('#available-count').inner_text()
        check(f'region {key} shows availability', '題' in text, text.strip()[:60])

    # library filters
    page.locator('button[data-view="library"]').click()
    page.wait_for_timeout(400)
    total = page.locator('#library-count').inner_text()
    page.locator('#library-ready').check()
    page.wait_for_timeout(400)
    ready = page.locator('#library-count').inner_text()
    check('library ready-only toggle narrows list', ready != total, f'{total} -> {ready}')
    for grade in ('7', '8', '9'):
        page.select_option('#library-grade', grade)
        page.wait_for_timeout(300)
        cards = page.locator('#library-list > *').count()
        check(f'library grade {grade} lists papers', cards > 0, cards)
    page.select_option('#library-grade', '')
    page.locator('#library-ready').uncheck()
    page.locator('button[data-view="compose"]').click()

    # whole-paper previews
    for pid in sample_ids:
        p = papers[pid]
        page.goto(f'{base}/?paper={pid}&fresh={random.randint(1, 10**9)}', wait_until='networkidle')
        page.wait_for_function('() => window.lanjuan')
        page.locator(f'[data-preview-paper="{pid}"]').click()
        page.wait_for_function('n => lanjuan.getSession().items.length === n', arg=p['questionCount'], timeout=10000)
        page.evaluate('async () => { await MathJax.startup.promise; await MathJax.typesetPromise(); }')
        items = page.evaluate('() => lanjuan.getSession().items.length')
        bad = page.locator('#paper-preview [data-mml-node="merror"], #paper-preview img').count()
        check(f'whole paper {pid} loads all questions', items == p['questionCount'] and not bad, f'{items}/{p["questionCount"]} errors={bad}')

        # swap the first question: order and scores of the others must be kept
        before = page.evaluate('() => lanjuan.getSession().items.map(i => [i.id, i.score])')
        swap = page.locator('[data-swap]').first
        if swap.count():
            swap.click()
            page.wait_for_timeout(600)
            after = page.evaluate('() => lanjuan.getSession().items.map(i => [i.id, i.score])')
            same_len = len(before) == len(after)
            others = same_len and all(b == a for b, a in list(zip(before, after))[1:])
            check(f'swap one question in {pid} keeps the rest', same_len and others and before[0][1] == after[0][1])
        # export -> restore
        b64 = page.evaluate("""async () => { const b = await lanjuan.createPdf(); let s=''; for (let i=0;i<b.length;i+=32768) s+=String.fromCharCode(...b.subarray(i,i+32768)); return btoa(s); }""")
        pdf = pathlib.Path(report_path.parent / f'{pid}.live.pdf')
        pdf.write_bytes(base64.b64decode(b64))
        want = page.evaluate('() => lanjuan.getSession().items.map(i => [i.id, i.score])')
        page.locator('#restore-input').set_input_files(str(pdf))
        page.wait_for_timeout(1500)
        got = page.evaluate('() => lanjuan.getSession().items.map(i => [i.id, i.score])')
        check(f'PDF of {pid} restores the same ids and scores', got == want and pdf.stat().st_size > 20000, f'{len(got)} items, {pdf.stat().st_size // 1024} KB')
        pdf.unlink()

    # random fresh composition per grade
    page.goto(f'{base}/{fresh}', wait_until='networkidle')
    page.wait_for_function('() => window.lanjuan')
    for grade in ('7', '8', '9'):
        page.select_option('#grade', grade)
        page.wait_for_timeout(300)
        page.locator('#generate-button').click()
        page.wait_for_timeout(1200)
        n = page.evaluate('() => lanjuan.getSession() ? lanjuan.getSession().items.length : 0')
        check(f'compose grade {grade} generates questions', n > 0, n)

    # phone viewport
    phone = browser.new_page(viewport={'width': 390, 'height': 844})
    phone.goto(f'{base}/{fresh}', wait_until='networkidle')
    overflow = phone.evaluate('() => document.documentElement.scrollWidth > window.innerWidth + 1')
    check('phone viewport has no horizontal overflow', not overflow)
    browser.close()

report['pass'] = all(c['ok'] for c in report['checks']) and not report['errors']
report_path.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding='utf-8')
print('console/page errors:', report['errors'][:5])
print('ALL PASS' if report['pass'] else 'FAILURES PRESENT')
sys.exit(0 if report['pass'] else 1)
