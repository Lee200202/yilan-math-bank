import json,pymupdf
from pathlib import Path
ROOT=Path(__file__).parent;OUT=ROOT/'review-zhonghua-extra79';OUT.mkdir(exist_ok=True)
SELECT=['1TW_2Q6LrYs-pzosnM38erf4q7vKbWPyQ','1bdGpm3tyY5N9Rpe-j_GGslCHhBDMNV6s','1B5pbQux_YE1p_hTMPFeIxPgzknbLuixF','1wFwXlVeoTh8-P8yIEY27hWIXMXFDOtoF']
cat=json.loads((ROOT/'zhonghua_catalog.json').read_text(encoding='utf8'))
for row in cat:
    if row['id'] not in SELECT:continue
    d=pymupdf.open(ROOT.parent/row['localPath']);key=f"g{row['grade']}-{row['year']}-{row['semester']}-{row['exam']}"
    for i,p in enumerate(d):
        p.get_pixmap(matrix=pymupdf.Matrix(1.5,1.5)).save(OUT/f'{key}-p{i}.png')
        lines=[]
        for b in p.get_text('dict')['blocks']:
            for l in b.get('lines',[]):
                t=''.join(s['text'] for s in l['spans'])
                if t.strip():lines.append({'rect':[round(v,2) for v in l['bbox']],'text':t})
        (OUT/f'{key}-p{i}-lines.json').write_text(json.dumps(lines,ensure_ascii=False,indent=2),encoding='utf8')
    print(key,'pages',len(d),'rect',d[0].rect)
