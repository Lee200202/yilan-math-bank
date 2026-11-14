import json,pathlib,hashlib
import pymupdf as f
from PIL import Image,ImageDraw
R=pathlib.Path(__file__).resolve().parent
src=R/'raw/ld-112-1-2-7.pdf';doc=f.open(src);sha=hashlib.sha256(src.read_bytes()).hexdigest()
spec=[(0,'fill',i+1,a,b) for i,(a,b) in enumerate([(150,177),(178,204),(205,231),(232,258),(258,285),(286,312),(313,336),(337,374),(374,412),(412,503),(504,938),(939,991)])]
spec += [(1,'fill',n,a,b) for n,a,b in [(13,42,78),(14,78,200),(15,201,239),(16,240,336),(17,337,419)]]
spec += [(1,'written',n,a,b) for n,a,b in [(1,458,568),(2,575,721),(3,727,1004)]]
out=R/'review-luodong112';out.mkdir(exist_ok=True);rows=[];parts=[]
for page,t,n,a,b in spec:
    rect=[48,a,683,b];qid=f'ld-112-1-2-7-{t}-{n}'
    q={'id':qid,'paperId':'ld-112-1-2-7','page':page,'rect':rect,'type':t,'number':n,'difficulty':('easy' if n<=6 else 'medium' if n<=14 else 'hard') if t=='fill' else ('medium' if n==1 else 'hard'),'reviewed':True,'sourceSha256':sha,'sourceSection':'填充題' if t=='fill' else '計算題','difficultyBasis':'編輯依運算步驟與整合推理估計，非官方難度'}
    rows.append(q);p=doc[page].get_pixmap(matrix=f.Matrix(1.25,1.25),clip=f.Rect(rect));im=Image.frombytes('RGB',[p.width,p.height],p.samples);parts.append((qid,im))
for offset in range(0,len(parts),5):
    sub=parts[offset:offset+5];w=max(im.width for _,im in sub)+30;h=sum(im.height+40 for _,im in sub)+20;sheet=Image.new('RGB',(w,h),'#ecefe8');draw=ImageDraw.Draw(sheet);y=10
    for qid,im in sub:draw.text((12,y),qid,fill='black');y+=25;sheet.paste(im,(10,y));y+=im.height+15
    sheet.save(out/f'contact-{offset//5+1}.png')
(R/'curated-luodong112.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
print('20 question crop candidates and contact sheets generated')
