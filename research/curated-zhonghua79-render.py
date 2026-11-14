import pymupdf,json
from pathlib import Path
ROOT=Path(__file__).parent
OUT=ROOT/'review-zhonghua79';OUT.mkdir(exist_ok=True)
catalog=json.loads((ROOT/'zhonghua_catalog.json').read_text(encoding='utf-8'))
for row in catalog:
    if row['year']==115 and row['kind']=='question' and row['grade'] in [7,9]:
        d=pymupdf.open(ROOT.parent/row['localPath'])
        for i,p in enumerate(d):
            p.get_pixmap(matrix=pymupdf.Matrix(1.6,1.6)).save(OUT/f"g{row['grade']}-p{i+1}.png")
            lines=[]
            for block in p.get_text('dict')['blocks']:
                for line in block.get('lines',[]):
                    text=''.join(x['text'] for x in line['spans'])
                    lines.append({'rect':[round(x,2) for x in line['bbox']],'text':text})
            (OUT/f"g{row['grade']}-p{i+1}-lines.json").write_text(json.dumps(lines,ensure_ascii=False,indent=2),encoding='utf-8')
            print(row['grade'],i,p.rect)
