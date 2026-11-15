"""Combine reviewer findings (handoff/batches/<batch>/review-group*.json) into a Markdown report.
Usage: python scripts/review_report.py handoff/batches/20261115-v16
"""
import collections
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
batch = ROOT / sys.argv[1]
rows = []
for f in sorted(batch.glob('review-group*.json')):
    if f.name.endswith('.ids.json'):
        continue
    rows += json.loads(f.read_text(encoding='utf-8'))
papers = {p['id']: p for p in json.loads((ROOT / 'public/data/papers.json').read_text(encoding='utf-8'))}
verdicts = collections.Counter(r['verdict'] for r in rows)
findings = [(r, f) for r in rows for f in r.get('findings', [])]
sev = collections.Counter(f.get('severity', 'minor') for _, f in findings)
cat = collections.Counter(f.get('category', 'other') for _, f in findings)
out = [f'# 轉寫比對報告（{batch.name}）', '',
       '其他 AI 轉寫的整卷，逐卷逐題與原卷頁面比對。major＝會改變數學內容／答案或無法作答；minor＝措辭、標點、難度標籤等。',
       '', '## 總覽', '',
       f'- 比對試卷：{len(rows)} 份；結果 ' + '、'.join(f'{k} {v}' for k, v in sorted(verdicts.items())),
       f'- 發現問題：{len(findings)} 處（major {sev.get("major", 0)}、minor {sev.get("minor", 0)}）',
       '- 類別：' + '、'.join(f'{k} {v}' for k, v in cat.most_common()), '',
       '| 試卷 | 學校 | 學年-學期-年級-次 | 結果 | 檢查題數 | major | minor |', '|---|---|---|---|---|---|---|']
for r in sorted(rows, key=lambda r: (r['verdict'] == 'pass', r['paperId'])):
    p = papers.get(r['paperId'], {})
    slot = f'{p.get("year")}-{p.get("semester")}-{p.get("grade")}-{p.get("exam")}'
    c = collections.Counter(f.get('severity', 'minor') for f in r.get('findings', []))
    out.append(f'| `{r["paperId"]}` | {p.get("school", r.get("school", ""))} | {slot} | {r["verdict"]} | {r.get("questionsChecked", "")} | {c.get("major", 0)} | {c.get("minor", 0)} |')
out += ['', '## 逐題問題與處理', '']
for r in rows:
    if not r.get('findings'):
        continue
    p = papers.get(r['paperId'], {})
    out.append(f'### {p.get("school", "")} {p.get("year")}-{p.get("semester")} {p.get("grade")}年級第{p.get("exam")}次（`{r["paperId"]}`）')
    out.append('')
    for f in r['findings']:
        out.append(f'- **{f.get("question", "")}**［{f.get("severity", "")}／{f.get("category", "")}］原卷：{f.get("original", "")}；轉寫：{f.get("transcribed", "")}；處理：{f.get("action", "")}')
    out.append('')
(batch / 'REVIEW_REPORT.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
print(f'{len(rows)} papers, {len(findings)} findings -> {batch / "REVIEW_REPORT.md"}')
