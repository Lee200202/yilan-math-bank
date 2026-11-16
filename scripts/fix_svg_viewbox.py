"""Widen SVG viewBoxes whose drawn content escapes them in the real preview.

The preview redraws SVG <text> at a fixed physical size, so bounds can only be measured in
the actual whole-paper preview. For each paper ID: open it like qa_metro.py, measure every
.typed-diagram svg (in session order = question order, blocks in order), and expand the
viewBox of escaping figures to the content bounds plus padding. Repeats until stable.
Drawing coordinates are untouched. Usage:
  python scripts/fix_svg_viewbox.py [--base URL] PAPER_ID [...]
"""
import json
import pathlib
import re
import sys

from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[1]
args = sys.argv[1:]
base = 'http://127.0.0.1:4173'
if args and args[0] == '--base':
    base, args = args[1], args[2:]
VB = re.compile(r'viewBox="([-\d. ]+)"')
fmt = lambda v: str(round(v, 1)).removesuffix('.0')


def measure(page, pid, count):
    page.goto(f'{base}/?paper={pid}', wait_until='networkidle')
    page.wait_for_function('() => window.lanjuan')
    page.locator(f'[data-preview-paper="{pid}"]').click()
    page.wait_for_function('n => lanjuan.getSession().items.length === n', arg=count, timeout=8000)
    ids = page.evaluate('() => lanjuan.getSession().items.map(i => i.id)')
    boxes = page.locator('#paper-preview .typed-diagram > svg').evaluate_all(
        'svgs => svgs.map(s => { const v=s.viewBox.baseVal, b=s.getBBox(); return [[v.x,v.y,v.width,v.height],[b.x,b.y,b.width,b.height]]; })')
    return ids, boxes


with sync_playwright() as pw:
    browser = pw.chromium.launch(channel='chrome', headless=True)
    page = browser.new_page(viewport={'width': 1440, 'height': 1000})
    papers = {p['id']: p for p in json.loads((ROOT / 'public/data/papers.json').read_text(encoding='utf-8'))}
    for pid in args:
        path = ROOT / papers[pid]['completionEvidence']
        for rnd in range(4):
            t = json.loads(path.read_text(encoding='utf-8'))
            byid = {f'{pid}-{q["type"]}-{q["sourceNumber"]}': q for q in t['questions']}
            ids, boxes = measure(page, pid, papers[pid]['questionCount'])
            blocks = [b for i in ids for b in byid[i]['blocks'] if b['type'] in ('svg', 'optionFigures')]
            if len(blocks) != len(boxes):
                raise SystemExit(f'{pid}: {len(blocks)} svg blocks but {len(boxes)} rendered diagrams')
            changed = 0
            for b, ((x, y, w, h), (bx, by, bw, bh)) in zip(blocks, boxes):
                if bx < x - 2 or by < y - 2 or bx + bw > x + w + 2 or by + bh > y + h + 2:
                    pad = max(4, 0.03 * max(w, h))
                    nx, ny = min(x, bx - pad), min(y, by - pad)
                    nx2, ny2 = max(x + w, bx + bw + pad), max(y + h, by + bh + pad)
                    new = ' '.join(fmt(v) for v in (nx, ny, nx2 - nx, ny2 - ny))
                    m = VB.search(b['svg'])
                    b['svg'] = b['svg'][:m.start(1)] + new + b['svg'][m.end(1):]
                    changed += 1
                    print(f'{pid} round {rnd + 1}: viewBox {fmt(x)} {fmt(y)} {fmt(w)} {fmt(h)} -> {new}')
            if not changed:
                break
            path.write_text(json.dumps(t, ensure_ascii=False, indent=1), encoding='utf-8')
            # the preview reads built data: rebuild only this paper's rows quickly
            import subprocess
            # re-approve the edited bytes (release policy pins the SHA), then rebuild data
            subprocess.run([sys.executable, 'scripts/release_queue.py', pid], cwd=ROOT, check=True, capture_output=True)
            subprocess.run([sys.executable, 'scripts/prepare_data.py'], cwd=ROOT, check=True, capture_output=True)
        else:
            print(f'{pid}: still escaping after 4 rounds')
    browser.close()
