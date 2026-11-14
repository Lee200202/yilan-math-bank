import json,pathlib,hashlib
import pymupdf as f
from PIL import Image,ImageDraw
R=pathlib.Path(__file__).resolve().parent;src=R/'raw/nc-109-1-1-8.pdf';sha=hashlib.sha256(src.read_bytes()).hexdigest();doc=f.open(src)
spec=[('choice',n+1,a,b) for n,(a,b) in enumerate([(230,264),(264,319),(319,399),(399,559),(559,613),(613,641),(641,722),(722,778)])]
spec += [('fill',n+1,a,b) for n,(a,b) in enumerate([(803,832),(832,858),(858,886),(886,912),(912,939),(939,963)])]
rows=[];images=[]
for typ,n,y0,y1 in spec:
    q={'id':f'nc-109-1-1-8-{typ}-{n}','paperId':'nc-109-1-1-8','page':0,'rect':[70,y0,685,y1],'type':typ,'number':n,'difficulty':('easy' if typ=='fill' or n in [1,2,6,7] else 'medium' if n in [3,4,5] else 'hard'),'reviewed':True,'school':'內城國民中小學','sourceSha256':sha,'difficultyBasis':'編輯依步驟、概念整合與推理需求估計，非官方答對率','reviewNote':'原卷109學年上學期八年級第一次段考卷首及首頁完整題幹/選項已視覺核對。'}
    rows.append(q);pix=doc[0].get_pixmap(matrix=f.Matrix(1.1,1.1),clip=f.Rect(q['rect']));images.append((q['id'],Image.frombytes('RGB',(pix.width,pix.height),pix.samples)))
(R/'curated-neicheng109.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
for part,start in enumerate([0,8]):
    sub=images[start:start+8];w=720;h=sum(im.height+42 for _,im in sub)+20;sheet=Image.new('RGB',(w,h),'#edf0e9');draw=ImageDraw.Draw(sheet);y=10
    for name,im in sub:draw.text((10,y),name,fill='black');y+=25;sheet.paste(im,(10,y));y+=im.height+17
    sheet.save(R/f'transcribed-other-schools-nc109-crops-{part+1}.png')
print('14 whole questions curated')
