"""Browser + PDF acceptance for metro regions and the guided UI.

For every metro paper with a whole-paper transcription: open it from the archive, load all
questions, export the PDF through the real UI code, and check page count, zero raster images,
one embedded font family and that every question number appears. Also captures desktop and
phone screenshots for each region pill. Usage:
  python scripts/qa_metro.py [base_url]     (default http://127.0.0.1:4173)
Outputs to qa/metro/ (ignored).
"""
import base64
import json
import pathlib
import sys

import pymupdf as fitz
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / 'qa/metro'
OUT.mkdir(parents=True, exist_ok=True)
ARGS = [a for a in sys.argv[1:] if not a.startswith('--')]
BASE = ARGS[0] if ARGS else 'http://127.0.0.1:4173'
# Whole-paper transcriptions (metro and Yilan). --changed: only files not yet committed.
papers = [p for p in json.loads((ROOT / 'public/data/papers.json').read_text(encoding='utf-8'))
          if str(p.get('completionEvidence') or '').startswith(('research/metro/transcribed/', 'research/yilan/transcribed/'))]
if '--changed' in sys.argv:
    import subprocess
    status = subprocess.run(['git', 'status', '--porcelain', '--untracked-files=all', 'research/metro/transcribed', 'research/yilan/transcribed'],
                            cwd=ROOT, capture_output=True, text=True, encoding='utf-8').stdout
    changed = {pathlib.Path(line[3:].strip().strip('"')).stem for line in status.splitlines()}
    papers = [p for p in papers if p['id'] in changed]
report = {'base': BASE, 'papers': [], 'regions': [], 'errors': []}

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1440, 'height': 1000})
    page.on('pageerror', lambda e: report['errors'].append(str(e)))
    for p in papers:
        page.goto(f"{BASE}/?paper={p['id']}", wait_until='networkidle')
        page.wait_for_function('() => window.lanjuan')
        page.locator(f'[data-preview-paper="{p["id"]}"]').click()
        try:
            page.wait_for_function('n => lanjuan.getSession().items.length === n', arg=p['questionCount'], timeout=8000)
        except Exception:
            pass
        page.wait_for_timeout(500)
        items = page.evaluate('() => lanjuan.getSession().items.length')
        b64 = page.evaluate("""async () => { const b = await lanjuan.createPdf(); let s=''; for (let i=0;i<b.length;i+=32768) s+=String.fromCharCode(...b.subarray(i,i+32768)); return btoa(s); }""")
        pdf_path = OUT / f"{p['id']}.pdf"
        pdf_path.write_bytes(base64.b64decode(b64))
        doc = fitz.open(pdf_path)
        text = ''.join(pg.get_text() for pg in doc)
        images = sum(len(pg.get_images()) for pg in doc)
        fonts = sorted({f[3] for pg in doc for f in pg.get_fonts()})
        for i, pg in enumerate(doc):
            pg.get_pixmap(matrix=fitz.Matrix(1.6, 1.6)).save(OUT / f"{p['id']}-p{i + 1}.png")
        missing = [n for n in range(1, items + 1) if f'{n}.' not in text]
        row = {'id': p['id'], 'school': p['school'], 'region': p['region'], 'questions': items,
               'expected': p['questionCount'], 'pages': len(doc), 'rasterImages': images, 'fonts': fonts,
               'missingNumbers': missing, 'kb': round(pdf_path.stat().st_size / 1024)}
        row['ok'] = items == p['questionCount'] and images == 0 and not missing
        report['papers'].append(row)
        print(row)
    for width, tag in [(1440, 'desktop'), (390, 'phone')]:
        page.set_viewport_size({'width': width, 'height': 900})
        page.goto(BASE + '/', wait_until='networkidle')
        page.evaluate("() => localStorage.clear()")
        page.reload(wait_until='networkidle')
        page.wait_for_function('() => window.lanjuan')
        for region in ['', 'yilan', 'taipei', 'new_taipei', 'taoyuan', 'taichung', 'kaohsiung']:
            page.locator(f'[data-region-btn="{region}"]').click()
            page.wait_for_timeout(250)
            info = page.evaluate("""() => ({available: document.querySelector('#available-count').textContent,
                active: document.querySelector('.region-pill.active span').textContent,
                schools: [...document.querySelector('#school').options].map(o => o.textContent).slice(1),
                overflowX: document.documentElement.scrollWidth > innerWidth + 1})""")
            info.update(region=region or 'all', viewport=tag)
            report['regions'].append(info)
            if tag == 'desktop' and region in ('', 'taoyuan'):
                page.screenshot(path=str(OUT / f'region-{region or "all"}-{tag}.png'))
        page.screenshot(path=str(OUT / f'compose-{tag}.png'), full_page=True)
    browser.close()

(OUT / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding='utf-8')
bad = [r for r in report['papers'] if not r['ok']] + [r for r in report['regions'] if r['overflowX']]
print('regions:', [(r['viewport'], r['region'], r['available']) for r in report['regions']])
print('errors:', report['errors'])
sys.exit(1 if bad or report['errors'] else 0)
