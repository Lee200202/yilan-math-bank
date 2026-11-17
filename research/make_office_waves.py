"""Like make_waves.py but for papers that exist only as Word (.docx) or ODT (incl. .zip that holds an ODT).
Extracts text / LaTeX formulas / images with research/metro/office_extract.py into research/targets/office/<paperId>/
and writes research/targets/<wave>-<k>.json plus CLAIMS entries.
Usage: python -X utf8 research/make_office_waves.py <wave> <helpers> <per-helper> [region ...]
Metro regions only by default (Yilan is another AI's lane). .doc (binary Word) is NOT handled: needs a real converter.
"""
import collections
import datetime
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
wave, helpers, per = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
regions = sys.argv[4:] or ['taipei', 'new_taipei', 'taoyuan', 'kaohsiung', 'taichung']
papers = json.loads((ROOT / 'public/data/papers.json').read_text(encoding='utf-8'))
inv = json.loads((ROOT / 'research/metro/metro-inventory.json').read_text(encoding='utf-8'))
local = {f['id']: f['localPath'] for s in inv['sources'].values() for f in s['files'] if f.get('localPath')}
claims = json.loads((ROOT / 'handoff/CLAIMS.json').read_text(encoding='utf-8'))
taken = {c['paperId'] for c in claims['claims'] if c['status'] not in ('source-issue-reported',)}
taken |= {f.stem for d in ('research/metro/transcribed', 'research/yilan/transcribed') for f in (ROOT / d).glob('*.json')}
issues = {f.stem for f in (ROOT / 'handoff/source-issues').glob('*.json')}
cand = []
for x in papers:
    if x['region'] not in regions or x.get('transcriptionStatus', '').startswith('complete') or x['id'] in taken or x['id'] in issues:
        continue
    if x['format'] not in ('docx', 'odt', 'doc'):
        continue
    path = local.get(x['id'])
    extract_from = path
    if x['format'] == 'doc':  # legacy Word: use the .docx made by scripts/word_convert_batch.py (SHA stays that of the original .doc)
        conv = 'research/metro/converted/' + x['id'] + '.docx'
        extract_from = conv if (ROOT / conv).exists() else None
    if path and extract_from and (ROOT / path).exists():
        cand.append({'paperId': x['id'], 'region': x['region'], 'school': x['school'], 'year': x['year'], 'semester': x['semester'],
                     'grade': x['grade'], 'exam': x['exam'], 'source': path, 'extractFrom': extract_from, 'format': x['format'],
                     'outFile': 'research/metro/transcribed/' + x['id'] + '.json'})
# drop odt duplicates: when the same school/slot exists as .docx/.doc and as .odt, the Word version is more reliable
slots = collections.defaultdict(set)
for c in cand:
    slots[(c['school'], c['year'], c['semester'], c['grade'], c['exam'])].add(c['format'])
cand = [c for c in cand if not (c['format'] == 'odt' and slots[(c['school'], c['year'], c['semester'], c['grade'], c['exam'])] & {'docx', 'doc'})]
PRIORITY = {(8, 1): 0, (8, 2): 1, (9, 1): 2, (9, 2): 3, (7, 1): 4, (7, 2): 4}
rank = lambda t: PRIORITY.get((t['grade'], t['semester']), 9)
ridx = {r: i for i, r in enumerate(regions)}
order = sorted(cand, key=lambda t: (rank(t), -t['year'], ridx[t['region']], t['exam']))
chosen = order[:helpers * per]
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
for t in chosen:
    d = ROOT / 'research/targets/office' / t['paperId']
    r = subprocess.run([sys.executable, '-X', 'utf8', str(ROOT / 'research/metro/office_extract.py'), str(ROOT / t['extractFrom']), str(d)],
                       capture_output=True, text=True, encoding='utf-8')
    t['office'] = f"research/targets/office/{t['paperId']}/text.md"
    t['extract'] = (r.stdout.strip().splitlines() or [r.stderr[-200:]])[-1][:120]
for h in range(helpers):
    mine = chosen[h::helpers]
    (ROOT / f'research/targets/{wave}-{h + 1}.json').write_text(json.dumps(mine, ensure_ascii=False, indent=1), encoding='utf-8')
    for t in mine:
        claims['claims'].append({'agent': f'claude-helper-{wave}-{h + 1}', 'paperId': t['paperId'], 'status': 'in-progress', 'batch': wave})
    print(f'{wave}-{h + 1}:', [f"{t['school']}{t['year']}-{t['semester']}-G{t['grade']}-E{t['exam']}({t['format']})" for t in mine])
claims['updatedAt'] = now
(ROOT / 'handoff/CLAIMS.json').write_text(json.dumps(claims, ensure_ascii=False, indent=1), encoding='utf-8')
print(len(chosen), 'claimed;', len(order) - len(chosen), 'more docx/odt papers queued')
