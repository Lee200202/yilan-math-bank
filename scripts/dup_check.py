"""Flag transcripts that look like the same paper as an already transcribed one (same school/year/semester/grade).

Usage: python -X utf8 scripts/dup_check.py <id> [<id> ...]   (ids of NEW transcripts; compared with all other transcripts)
Prints, for each new id, the most similar other paper and the share of question stems that match (normalized prefix).
A share >= 0.6 means: very probably the same exam published twice (e.g. a PDF and a Word copy). Keep only one.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]


def stems(t):
    out = set()
    for q in t['questions']:
        text = ''
        for b in q.get('blocks', []):
            if b.get('type') == 'text':
                text += b.get('text', '')
        text = re.sub(r'[\s$\\{}()（）：，。、？?＿_]', '', text)
        if len(text) >= 8:
            out.add(text[:24])
    return out


def load_all():
    res = {}
    for d in ('metro', 'yilan'):
        for f in (ROOT / f'research/{d}/transcribed').glob('*.json'):
            try:
                t = json.loads(f.read_text(encoding='utf-8'))
                res[f.stem] = t
            except Exception:
                pass
    return res


def main(ids):
    allt = load_all()
    papers = {p['id']: p for p in json.loads((ROOT / 'public/data/papers.json').read_text(encoding='utf-8'))}
    for i in ids:
        if i not in allt or i not in papers:
            print(i, 'n/a')
            continue
        a, p = stems(allt[i]), papers[i]
        best = (0, None)
        for j, t in allt.items():
            if j == i or j not in papers:
                continue
            q = papers[j]
            if (q['school'], q['year'], q['semester'], q['grade']) != (p['school'], p['year'], p['semester'], p['grade']):
                continue
            b = stems(t)
            if not a or not b:
                continue
            share = len(a & b) / min(len(a), len(b))
            if share > best[0]:
                best = (share, j)
        flag = 'DUPLICATE?' if best[0] >= 0.6 else ''
        print('%s  best match %s  share %.2f %s' % (i, best[1], best[0], flag))


if __name__ == '__main__':
    main(sys.argv[1:])
