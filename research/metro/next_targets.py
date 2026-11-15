"""List the best untranscribed PDF paper for every open region × grade × semester × exam slot.
Usage: python research/metro/next_targets.py [grade] [--render]"""
import json
import pathlib
import sys

import pymupdf as fitz

ROOT = pathlib.Path(__file__).resolve().parents[2]
P = json.loads((ROOT / 'public/data/papers.json').read_text(encoding='utf-8'))
inv = json.loads((ROOT / 'research/metro/metro-inventory.json').read_text(encoding='utf-8'))
local = {f['id']: f for v in inv['sources'].values() for f in v['files'] if f.get('id')}
PREF = {'taipei': ['誠正國中', '興福國中'], 'new_taipei': ['中正國中', '三和國中', '鷺江國中', '福和國中', '新莊國中', '五峰國中', '永和國中', '溪崑國中'],
        'taoyuan': ['自強國中'], 'taichung': ['向上國中', '大業國中', '大華國中'], 'kaohsiung': ['大灣國中', '美濃國中']}
grades = [int(sys.argv[1])] if len(sys.argv) > 1 and sys.argv[1].isdigit() else [7, 8, 9]
render = '--render' in sys.argv
out = []
for g in grades:
    for s in (1, 2):
        for e in (1, 2, 3):
            for r, schools in PREF.items():
                slot = [p for p in P if p['region'] == r and p['grade'] == g and p['semester'] == s and p['exam'] == e]
                if any(p['file'] for p in slot):
                    continue
                cands = [p for p in slot if local.get(p['id'], {}).get('format') == 'pdf']
                cands.sort(key=lambda p: (schools.index(p['school']) if p['school'] in schools else 99, -p['year']))
                if not cands:
                    print(f'{g}{"上下"[s-1]}{e} {r:10s} -- no PDF')
                    continue
                p = cands[0]
                f = local[p['id']]
                pages = len(fitz.open(ROOT / f['localPath']))
                out.append(p['id'])
                print(f'{g}{"上下"[s-1]}{e} {r:10s} {p["school"]} {p["year"]} {pages}p {p["id"]} {f["sha256"]}')
                if render:
                    doc = fitz.open(ROOT / f['localPath'])
                    for i, pg in enumerate(doc):
                        pg.get_pixmap(matrix=fitz.Matrix(1.6, 1.6)).save(ROOT / f'research/metro/render/{p["id"]}-p{i + 1}.png')
