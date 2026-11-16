"""Validate whole-paper transcription files without rebuilding the site.

Usage: python scripts/check_transcript.py research/metro/transcribed/<id>.json [...]
       python scripts/check_transcript.py research/yilan/transcribed/<id>.json

Checks exactly what scripts/prepare_data.py will enforce (printed slot, source SHA,
type counts, unit IDs, vector-only SVG, control characters, balanced $), plus glyph
coverage against the full CNS Kai font so the PDF never shows tofu. Writes nothing.
"""
import copy
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
import prepare_metro  # noqa: E402

papers = {p['id']: p for p in json.loads((ROOT / 'public/data/papers.json').read_text(encoding='utf-8'))}
units = {u['id'] for u in json.loads((ROOT / 'research/nanyi-units.json').read_text(encoding='utf-8'))}
cmap = None
font = ROOT / 'research/fonts/TW-Kai.ttf'
if font.exists():
    from fontTools.ttLib import TTFont
    cmap = set(TTFont(font, lazy=True).getBestCmap())

# Characters rendered by the math engine or by ASCII fallback, not the Kai font.
SKIP = set(range(0x20, 0x7f)) | {0x2212, 0x00d7, 0x00f7, 0x00b1, 0x2264, 0x2265, 0x2260, 0x221a, 0x03c0, 0x00b0, 0x2220, 0x25b3, 0x22a5, 0x2225}
bad = 0
for arg in sys.argv[1:]:
    path = pathlib.Path(arg)
    try:
        t = json.loads(path.read_text(encoding='utf-8'))
        if path.stem != t['paperId']:
            raise ValueError('file name must equal paperId')
        paper = copy.deepcopy(papers.get(t['paperId']))
        if not paper:
            raise ValueError('paperId not found in public/data/papers.json')
        region = 'yilan' if 'yilan' in path.parts else 'metro'
        if (region == 'yilan') != (paper['region'] == 'yilan'):
            raise ValueError(f'wrong folder for region {paper["region"]}')
        import inline_svg_css
        css = [q['sourceNumber'] for q in t['questions'] for b in q['blocks']
               if b['type'] in ('svg', 'optionFigures') and inline_svg_css.needs_inline(b['svg'])]
        if css:
            raise ValueError(f'SVG uses <style>/class/style CSS (prints as black shapes) in questions {css}: '
                             f'run python scripts/inline_svg_css.py --write {path}')
        import xml.dom.minidom
        for q in t['questions']:
            for b in q['blocks']:
                if b['type'] in ('svg', 'optionFigures'):
                    try:
                        xml.dom.minidom.parseString(b['svg'].encode('utf-8'))
                    except Exception as e:
                        raise ValueError(f'SVG is not well-formed XML in {q["type"]}-{q["sourceNumber"]}: {e}')
        rows = prepare_metro.rows_from_transcript(t, paper, units, str(path))
        missing = set()
        for q in t['questions']:
            for b in q['blocks']:
                texts = [b.get('text', '')] + b.get('items', []) + [c for r in b.get('rows', []) for c in r]
                texts += re.findall(r'>([^<]+)<', b.get('svg', ''))
                for s in texts:
                    plain = re.sub(r'\$[^$]*\$', '', s)
                    missing |= {ch for ch in plain if ord(ch) not in SKIP and cmap is not None and ord(ch) not in cmap}
        if missing:
            raise ValueError(f'characters not in the Kai font (replace them): {"".join(sorted(missing))}')
        types = {k: sum(q['type'] == k for q in t['questions']) for k in ('choice', 'fill', 'written')}
        diff = {k: sum(q['difficulty'] == k for q in t['questions']) for k in ('easy', 'medium', 'hard')}
        print(f'OK  {path.name}  {paper["school"]} {paper["year"]}-{paper["semester"]} G{paper["grade"]} E{paper["exam"]}  '
              f'usable {len(rows)}/{len(t["questions"])}  types {types}  difficulty {diff}')
    except Exception as e:  # report every file, then fail
        bad += 1
        print(f'FAIL {path.name}: {e}')
sys.exit(1 if bad else 0)
