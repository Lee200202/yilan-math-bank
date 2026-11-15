"""Write ordered transcription target lists, one per helper, to research/targets/<group>.json.

Order: round-robin over the 18 slots (grade 7-9 x semester 1-2 x exam 1-3), slots with the
fewest finished papers first; within a slot, newest year first and rotating schools.
Only PDF originals that are not yet complete are listed.
Usage: python research/make_targets.py
"""
import collections
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
GROUPS = {'yilan': ['yilan'], 'taipei_taoyuan': ['taipei', 'taoyuan'], 'new_taipei': ['new_taipei'],
          'taichung': ['taichung'], 'kaohsiung': ['kaohsiung']}
papers = json.loads((ROOT / 'public/data/papers.json').read_text(encoding='utf-8'))
inv = json.loads((ROOT / 'research/metro/metro-inventory.json').read_text(encoding='utf-8'))
local = {f['id']: f['localPath'] for s in inv['sources'].values() for f in s['files'] if f.get('localPath')}
done_files = {f.stem for d in ('research/metro/transcribed', 'research/yilan/transcribed') for f in (ROOT / d).glob('*.json')}
out = ROOT / 'research/targets'
out.mkdir(exist_ok=True)
for group, regions in GROUPS.items():
    lists = []
    for region in regions:
        pool = [p for p in papers if p['region'] == region]
        done = collections.Counter((p['grade'], p['semester'], p['exam']) for p in pool
                                   if p.get('transcriptionStatus', '').startswith('complete') or p['id'] in done_files)
        slots = collections.defaultdict(list)
        for p in pool:
            if p['id'] in done_files or p.get('transcriptionStatus', '').startswith('complete'):
                continue
            if region == 'yilan':
                pdf = p['file'].removeprefix('./') if p['format'] == 'pdf' and p['file'].endswith('.pdf') else None
                pdf = f'public/{pdf}' if pdf else None
            else:
                pdf = local.get(p['id']) if p['format'] == 'pdf' else None
            if not pdf:
                continue
            slots[(p['grade'], p['semester'], p['exam'])].append({
                'paperId': p['id'], 'region': region, 'school': p['school'], 'year': p['year'],
                'semester': p['semester'], 'grade': p['grade'], 'exam': p['exam'], 'pdf': pdf.replace('\\', '/'),
                'existingQuestions': p.get('questionCount', 0),
                'outFile': f'research/{"yilan" if region == "yilan" else "metro"}/transcribed/{p["id"]}.json'})
        for key, rows in slots.items():
            rows.sort(key=lambda r: (r['existingQuestions'] > 0, -r['year']))
            # rotate schools within the slot
            by_school = collections.defaultdict(list)
            for r in rows:
                by_school[r['school']].append(r)
            mixed = []
            while any(by_school.values()):
                for s in list(by_school):
                    if by_school[s]:
                        mixed.append(by_school[s].pop(0))
            slots[key] = mixed
        order = sorted(slots, key=lambda k: (done[k], k))
        ranked = []
        depth = 0
        while any(len(slots[k]) > depth for k in order):
            ranked += [slots[k][depth] for k in order if len(slots[k]) > depth]
            depth += 1
        lists.append(ranked)
    merged = [r for tup in __import__('itertools').zip_longest(*lists) for r in tup if r]
    (out / f'{group}.json').write_text(json.dumps(merged, ensure_ascii=False, indent=1), encoding='utf-8')
    print(group, len(merged), [f"{r['grade']}-{r['semester']}-{r['exam']}" for r in merged[:18]])
