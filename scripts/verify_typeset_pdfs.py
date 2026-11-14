import json,pathlib,re,collections
import pymupdf as fitz
from PIL import Image,ImageDraw
root=pathlib.Path(__file__).resolve().parents[1];folder=root/'qa/typeset';report=json.loads((folder/'report.json').read_text(encoding='utf-8'));results=[];thumbs=[]
for batch in report['reports']:
    d=fitz.open(folder/batch['file']);text='\n'.join(p.get_text() for p in d);images=sum(len(p.get_images(full=True)) for p in d)
    assert images==0,(batch['file'],'Raster images found')
    assert not re.search(r'班級＿|姓名＿|座號＿|來源：|蘭卷・第',text),(batch['file'],'Unwanted metadata in paper')
    numbered=re.findall(r'(?m)^\d+\.（\d+分）',text);assert len(numbered)==len(batch['ids']),(batch['file'],len(numbered),len(batch['ids']))
    sizes=collections.Counter(round(s['size'],2) for p in d for b in p.get_text('dict')['blocks'] if b['type']==0 for l in b['lines'] for s in l['spans'])
    assert set(sizes).issubset({10.5,11.5,12.5,14.0}),(batch['file'],sizes)
    for i,p in enumerate(d):
        name=f'{pathlib.Path(batch["file"]).stem}-p{i+1:02}.png';pix=p.get_pixmap(matrix=fitz.Matrix(1.2,1.2));pix.save(folder/name);im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples);im.thumbnail((357,505));thumbs.append((name,im.copy()))
    results.append({'file':batch['file'],'questions':len(batch['ids']),'pages':len(d),'rasterImages':images,'fontSizes':dict(sizes),'questionNumbering':'PASS'})
for start in range(0,len(thumbs),6):
    subset=thumbs[start:start+6];sheet=Image.new('RGB',(3*377,2*535),'#e8ece4');draw=ImageDraw.Draw(sheet)
    for j,(name,im) in enumerate(subset):x=(j%3)*377+10;y=(j//3)*535+25;draw.text((x,y-18),name,fill='black');sheet.paste(im,(x,y))
    sheet.save(folder/f'contact-{start//6+1:02}.png')
(folder/'pdf-report.json').write_text(json.dumps({'questions':sum(r['questions'] for r in results),'pages':sum(r['pages'] for r in results),'documents':results},ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps({'questions':sum(r['questions'] for r in results),'pages':sum(r['pages'] for r in results),'rasterImages':0,'contactSheets':(len(thumbs)+5)//6}))
