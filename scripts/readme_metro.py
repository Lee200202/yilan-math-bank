"""Regenerate the README「都會區題庫」section from public/data/coverage.json + papers.json."""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
cov = json.loads((ROOT / 'public/data/coverage.json').read_text(encoding='utf-8'))
papers = json.loads((ROOT / 'public/data/papers.json').read_text(encoding='utf-8'))
done = [p for p in papers if p.get('region', 'yilan') != 'yilan' and p['file']]
order = ['taipei', 'new_taipei', 'taoyuan', 'taichung', 'kaohsiung']
rows = sorted(cov['metro'], key=lambda s: (order.index(s['region']), -s['questionFiles']))
lines = ['## 都會區題庫', '',
         f"查核日期：{cov['checkedAt']}。外部指南給的網址先逐一重驗，空頁或無目錄的不採用；改以實際點進官網「歷屆試題／段考題庫」找到的入口全量列舉（含 Google Drive 多層資料夾、JS 開關清單與整包 zip）。", '',
         '| 地區 | 學校 | 數學試題卷 | 已全卷轉寫 |', '| --- | --- | --- | --- |']
for s in rows:
    years = f"{s['years'][0]}–{s['years'][-1]}" if s['years'] else '—'
    mine = [p for p in done if p['school'] == s['school']]
    tr = '、'.join(f"{p['year']}{'上' if p['semester'] == 1 else '下'}第{p['exam']}次{p['grade']}年級・{p['questionCount']}題" for p in sorted(mine, key=lambda p: (p['year'], p['exam']))) or '—'
    extra = f"；另 {s['archivesNotExtracted']} 個 7z/rar 未解壓" if s.get('archivesNotExtracted') else ''
    lines.append(f"| {s['regionLabel']} | {s['officialName']} | {s['questionFiles']} 份（{years}）{extra} | {tr} |")
total_files = sum(s['questionFiles'] for s in rows)
total_q = sum(p['questionCount'] for p in done)
lines += ['', f"{total_files} 份都會區原卷在「歷屆考卷」以官方原檔連結呈現，不另存本站；已完成 {len(done)} 份全卷文字轉寫（共 {total_q} 題可組卷），其餘待逐卷轉寫，不以少量範例代表全部。卷首年度須與清單一致才上架。流程與注意事項見 [都會區來源](skills/school-exam-collection/references/metro-sources.md)。", '']
readme = ROOT / 'README.md'
text = readme.read_text(encoding='utf-8')
new = re.sub(r'## 都會區題庫\n.*?(?=## 單元與配比)', '\n'.join(lines) + '\n', text, flags=re.S)
readme.write_text(new, encoding='utf-8')
print(total_files, len(done), total_q)
