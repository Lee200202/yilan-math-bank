"""Build non-overlapping transcription waves for helpers: one best PDF per uncovered
(region, year, grade, semester, exam) slot, skipping papers that are claimed/staged/transcribed.
Usage: python research/make_waves.py <wave-name> <helpers> <per-helper> [region ...]
Writes research/targets/<wave>-<k>.json and claims the papers in handoff/CLAIMS.json."""
import collections
import datetime
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
wave, helpers, per = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
regions = sys.argv[4:] or ['yilan', 'taipei', 'new_taipei', 'taoyuan', 'kaohsiung', 'taichung']
papers = json.loads((ROOT / 'public/data/papers.json').read_text(encoding='utf-8'))
inv = json.loads((ROOT / 'research/metro/metro-inventory.json').read_text(encoding='utf-8'))
local = {f['id']: f['localPath'] for s in inv['sources'].values() for f in s['files'] if f.get('localPath')}
claims = json.loads((ROOT / 'handoff/CLAIMS.json').read_text(encoding='utf-8'))
taken = {c['paperId'] for c in claims['claims'] if c['status'] not in ('source-issue-reported',)}
taken |= {f.stem for d in ('research/metro/transcribed', 'research/yilan/transcribed') for f in (ROOT / d).glob('*.json')}
issues = {f.stem for f in (ROOT / 'handoff/source-issues').glob('*.json')}
slots = collections.defaultdict(lambda: {'done': 0, 'todo': []})
for x in papers:
    k = (x['region'], x['year'], x['grade'], x['semester'], x['exam'])
    if x.get('transcriptionStatus', '').startswith('complete'):
        slots[k]['done'] += 1
    else:
        slots[k]['todo'].append(x)
# a slot already has a paper in flight -> skip it entirely
inflight = {k for k, v in slots.items() if any(t['id'] in taken for t in v['todo'])}
queue = collections.defaultdict(list)
for k, v in slots.items():
    if v['done'] or k in inflight or k[0] not in regions:
        continue
    for x in sorted(v['todo'], key=lambda t: t['id']):
        if x['format'] != 'pdf' or x['id'] in issues:
            continue
        path = ('public/' + x['file'].removeprefix('./')) if x['region'] == 'yilan' else local.get(x['id'])
        if path and (ROOT / path).exists():
            queue[x['region']].append({'paperId': x['id'], 'region': x['region'], 'school': x['school'], 'year': x['year'],
                                       'semester': x['semester'], 'grade': x['grade'], 'exam': x['exam'], 'pdf': path,
                                       'existingQuestions': x.get('questionCount', 0),
                                       'outFile': ('research/yilan/transcribed/' if x['region'] == 'yilan' else 'research/metro/transcribed/') + x['id'] + '.json'})
            break
# Owner's priority (2026-11-16): 八上 first, then 八下, 九上, 九下, and 七年級 last.
PRIORITY = {(8, 1): 0, (8, 2): 1, (9, 1): 2, (9, 2): 3, (7, 1): 4, (7, 2): 4}
rank = lambda t: PRIORITY.get((t['grade'], t['semester']), 9)
region_index = {r: i for i, r in enumerate(regions)}
order = sorted((t for r in queue for t in queue[r]), key=lambda t: (rank(t), -t['year'], region_index[t['region']], t['exam']))
chosen = order[:helpers * per]
# helper k takes every helpers-th paper so each helper gets a mix of regions at the same priority
queue = {'rest': order[helpers * per:]}
out = ROOT / 'research/targets'
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
for h in range(helpers):
    mine = chosen[h::helpers]
    (out / f'{wave}-{h + 1}.json').write_text(json.dumps(mine, ensure_ascii=False, indent=1), encoding='utf-8')
    for t in mine:
        claims['claims'].append({'agent': f'claude-helper-{wave}-{h + 1}', 'paperId': t['paperId'], 'status': 'in-progress', 'batch': wave})
    print(f'{wave}-{h + 1}:', [f"{t['school']}{t['year']}-{t['semester']}-G{t['grade']}-E{t['exam']}" for t in mine])
claims['updatedAt'] = now
(ROOT / 'handoff/CLAIMS.json').write_text(json.dumps(claims, ensure_ascii=False, indent=1), encoding='utf-8')
print(len(chosen), 'claimed;', sum(len(v) for v in queue.values()) + len(order) - len(chosen), 'more queued')
