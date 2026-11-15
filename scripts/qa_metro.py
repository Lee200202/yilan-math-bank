"""Browser + PDF acceptance for metro regions and the guided UI.

For every metro paper with a whole-paper transcription: open it from the archive, load all
questions, export the PDF through the real UI code, and check page count, zero raster images,
one embedded font family and that every question number appears. Also captures desktop and
phone screenshots for each region pill. Usage:
  python scripts/qa_metro.py [base_url]     (default http://127.0.0.1:4173)
Outputs to qa/metro/ (ignored).
"""
import base64
import argparse
import hashlib
import io
import json
import pathlib
import sys

import pymupdf as fitz
from playwright.sync_api import sync_playwright
from fontTools.ttLib import TTFont

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / 'qa/metro'
OUT.mkdir(parents=True, exist_ok=True)
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('base', nargs='?', default='http://127.0.0.1:4173')
parser.add_argument('--ids-file')
parser.add_argument('--changed', action='store_true')
parser.add_argument('--report-file', default='qa/metro/report.json')
args = parser.parse_args()
BASE = args.base
# Whole-paper transcriptions (metro and Yilan). --changed: only files not yet committed.
papers = [p for p in json.loads((ROOT / 'public/data/papers.json').read_text(encoding='utf-8'))
          if str(p.get('completionEvidence') or '').startswith(('research/metro/transcribed/', 'research/yilan/transcribed/'))]
if args.ids_file:
    ids = {pathlib.Path(line.strip()).stem for line in pathlib.Path(args.ids_file).read_text(encoding='utf-8').splitlines() if line.strip()}
    papers = [p for p in papers if p['id'] in ids]
    missing = ids - {p['id'] for p in papers}
    if missing:
        raise ValueError(f'QA targets missing whole-paper evidence: {sorted(missing)}')
if args.changed:
    import subprocess
    status = subprocess.run(['git', 'status', '--porcelain', '--untracked-files=all', 'research/metro/transcribed', 'research/yilan/transcribed'],
                            cwd=ROOT, capture_output=True, text=True, encoding='utf-8').stdout
    changed = {pathlib.Path(line[3:].strip().strip('"')).stem for line in status.splitlines()}
    papers = [p for p in papers if p['id'] in changed]
report = {'base': BASE, 'papers': [], 'regions': [], 'errors': []}
sha = lambda path: hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()
bank_sha = sha(ROOT / 'public/data/questions.json')
report['fontSha256'] = sha(ROOT / 'public/fonts/TW-Kai-subset.ttf')
report['typesetterSha256'] = sha(ROOT / 'public/typesetter.mjs')
if not papers:
    raise ValueError('No papers selected for PDF acceptance')

with sync_playwright() as pw:
    browser = pw.chromium.launch(channel='chrome', headless=True)
    page = browser.new_page(viewport={'width': 1440, 'height': 1000})
    page.on('pageerror', lambda e: report['errors'].append(str(e)))
    for p in papers:
        page.goto(f"{BASE}/?paper={p['id']}", wait_until='networkidle')
        page.wait_for_function('() => window.lanjuan')
        page.locator(f'[data-preview-paper="{p["id"]}"]').click()
        page.wait_for_function('n => lanjuan.getSession().items.length === n', arg=p['questionCount'], timeout=8000)
        page.evaluate('async () => { await MathJax.startup.promise; await MathJax.typesetPromise(); }')
        if page.locator('#paper-preview img, #paper-preview svg image, #paper-preview [data-mml-node="merror"]').count():
            raise ValueError(f'Raster or formula error in preview: {p["id"]}')
        initial = page.evaluate('() => lanjuan.getSession()')
        escaped_diagrams = page.locator('#paper-preview .typed-diagram > svg').evaluate_all('''svgs => svgs.flatMap((svg, i) => {
            const v=svg.viewBox.baseVal, b=svg.getBBox(), tolerance=8;
            return b.x<v.x-tolerance || b.y<v.y-tolerance || b.x+b.width>v.x+v.width+tolerance || b.y+b.height>v.y+v.height+tolerance
                ? [{diagram:i,viewBox:[v.x,v.y,v.width,v.height],bounds:[b.x,b.y,b.width,b.height]}] : [];
        })''')
        items = page.evaluate('() => lanjuan.getSession().items.length')
        b64 = page.evaluate("""async () => { const b = await lanjuan.createPdf(); let s=''; for (let i=0;i<b.length;i+=32768) s+=String.fromCharCode(...b.subarray(i,i+32768)); return btoa(s); }""")
        pdf_path = OUT / f"{p['id']}.pdf"
        pdf_path.write_bytes(base64.b64decode(b64))
        layout = page.evaluate('() => lanjuan.lastLayout')
        overflow = [b for b in layout if b['yBottom'] < 31.9 or b['yTop'] > 806]
        page.locator('#restore-input').set_input_files(str(pdf_path))
        page.wait_for_function('n => lanjuan.getSession().items.length === n', arg=items)
        restored = page.evaluate('() => lanjuan.getSession()')
        roundtrip = initial['items'] == restored['items']
        doc = fitz.open(pdf_path)
        text = ''.join(pg.get_text() for pg in doc)
        images = sum(len(pg.get_images()) for pg in doc)
        fonts = sorted({f[3] for pg in doc for f in pg.get_fonts()})
        # Extractable text can still have broken glyf offsets and invisible glyphs.
        for xref in {f[0] for pg in doc for f in pg.get_fonts()}:
            embedded = TTFont(io.BytesIO(doc.extract_font(xref)[3]))
            if 'glyf' in embedded:
                for glyph in embedded.getGlyphOrder():
                    embedded['glyf'][glyph].getCoordinates(embedded['glyf'])
        for i, pg in enumerate(doc):
            pg.get_pixmap(matrix=fitz.Matrix(1.6, 1.6)).save(OUT / f"{p['id']}-p{i + 1}.png")
        missing = [n for n in range(1, items + 1) if f'{n}.' not in text]
        row = {'id': p['id'], 'school': p['school'], 'region': p['region'], 'questions': items,
               'expected': p['questionCount'], 'pages': len(doc), 'rasterImages': images, 'fonts': fonts,
               'missingNumbers': missing, 'kb': round(pdf_path.stat().st_size / 1024),
               'sourceSha256': p['sha256'], 'pdfRoundtrip': roundtrip, 'overflowBlocks': overflow,
               'transcriptSha256': sha(ROOT / p['completionEvidence']), 'pdfSha256': sha(pdf_path),
               'renderedPages': [{'file': f'qa/metro/{p["id"]}-p{i+1}.png', 'sha256': sha(OUT / f'{p["id"]}-p{i+1}.png')} for i in range(len(doc))],
               'escapedDiagrams': escaped_diagrams, 'embeddedGlyphsDecoded': True,
               'visualReview': 'pending: inspect every rendered page before publishing'}
        row['ok'] = items == p['questionCount'] and images == 0 and not missing and len(fonts) == 1 and roundtrip and not overflow and not escaped_diagrams
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

report['bankUnchangedDuringRun'] = bank_sha == sha(ROOT / 'public/data/questions.json')
report_path = ROOT / args.report_file
report_path.parent.mkdir(parents=True, exist_ok=True)
report_path.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding='utf-8')
bad = [r for r in report['papers'] if not r['ok']] + [r for r in report['regions'] if r['overflowX']]
print('regions:', [(r['viewport'], r['region'], r['available']) for r in report['regions']])
print('errors:', report['errors'])
sys.exit(1 if bad or report['errors'] or not report['bankUnchangedDuringRun'] else 0)
