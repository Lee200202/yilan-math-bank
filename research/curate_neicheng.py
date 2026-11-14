"""Manually bounded crops after inspection of all source pages; coordinates in PDF points."""
from pathlib import Path
import json,hashlib
import pymupdf as fitz
from PIL import Image,ImageDraw

ROOT=Path(__file__).resolve().parent
rows=[]
def add(paper,page,kind,items):
    for number,rect,diff in items:
        rows.append(dict(id=f'{paper}-{kind}-{number}',paperId=paper,page=page,rect=rect,type=kind,number=number,difficulty=diff,reviewed=True,school='內城國民中小學',difficultyBasis='編輯依運算步驟、概念整合與圖表閱讀判定；非官方難度',sourceSha256=hashlib.sha256((ROOT/'raw'/f'{paper}.pdf').read_bytes()).hexdigest()))

p='nc-110-1-2-8'
add(p,0,'fill',[
 (1,[40,201,560,222.3],'easy'),(2,[40,222.5,560,254],'easy'),(3,[40,255,560,276.5],'easy'),(4,[40,276.5,560,307],'easy'),
 (5,[40,308,560,327.5],'easy'),(6,[40,327.5,560,345],'easy'),(7,[40,345,560,362],'easy'),(8,[40,362,560,380],'medium'),
 (9,[40,380,560,398],'medium'),(10,[40,398,560,417],'easy'),(11,[40,471,560,489.5],'medium'),(12,[40,489.5,560,508],'medium'),
 (13,[40,508,560,541],'medium'),(14,[40,542,560,621],'easy'),(15,[40,623,560,733],'medium')])
add(p,1,'fill',[
 (16,[40,60,560,110],'medium'),(17,[40,113,560,182],'easy'),(18,[40,183,560,385],'hard'),(19,[40,402,560,451],'medium'),
 (20,[40,455,560,474.5],'medium'),(21,[40,474.5,560,495],'medium'),(22,[40,509,560,530],'easy'),(23,[40,545,560,566],'easy'),
 (24,[40,581,560,602],'medium'),(25,[40,617,560,638],'medium'),(26,[40,653,560,674],'medium'),(27,[40,689,560,710],'hard'),
 (28,[40,725,560,746],'medium'),(29,[40,761,560,783],'hard')])

p='nc-110-1-1-8'
add(p,0,'choice',[(1,[40,183,560,218],'easy'),(2,[40,219,560,286],'medium'),(3,[40,289,560,339],'medium'),(4,[40,341,560,402],'easy'),(5,[40,406,560,449],'easy'),(6,[40,451,560,492],'medium'),(7,[40,492,560,529],'medium')])
add(p,0,'fill',[(8,[40,538,560,557],'easy'),(9,[40,569,560,588],'easy'),(10,[40,593,560,613],'medium'),(11,[40,621,560,641],'easy'),(12,[40,676,560,712],'medium')])
add(p,1,'fill',[(13,[40,65,560,238],'medium'),(14,[40,243,560,279],'medium'),(15,[40,289,560,343],'easy'),(16,[40,369,560,393],'medium'),(17,[40,432,560,484],'medium'),(18,[40,534,560,556],'hard'),(19,[40,605,560,633],'easy'),(20,[40,649,560,672],'easy')])
add(p,1,'written',[(1,[40,710,560,733],'medium')])
rows[-1]['sourceNote']='僅取題目卷非選題；原空白答案卷除式誤印為x−3，題目卷為x−2。未提供核對解答。'

p='nc-110-1-3-8'
add(p,0,'choice',[(1,[40,181,560,216],'easy'),(2,[40,228,560,279],'easy'),(3,[40,290,560,388],'medium'),(4,[40,401,560,438],'easy'),(5,[40,448,560,500],'easy'),(6,[40,511,560,562],'easy'),(7,[40,573,560,765],'medium')])
add(p,1,'choice',[(8,[40,70,560,247],'easy'),(9,[40,258,560,410],'medium'),(10,[36,421,560,506],'easy')])
add(p,2,'choice',[(12,[36,194,560,358],'medium')])
add(p,2,'fill',[(1,[40,402,560,438],'medium'),(2,[40,464,560,484],'medium'),(3,[40,510,560,531],'easy'),(4,[40,558,560,579],'easy'),(5,[40,605,560,626],'hard'),(6,[40,652,560,673],'easy'),(7,[40,700,560,720],'medium'),(8,[40,747,560,767],'easy')])
add(p,3,'fill',[(9,[40,54,560,75],'medium'),(10,[40,113,560,134],'medium')])
add(p,3,'written',[(1,[40,218,560,256],'medium'),(2,[40,403,595,445],'medium')])

(ROOT/'curated-neicheng.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')

# Contact sheets show every exact rectangle, including vector figures and full options.
out=ROOT/'curated-review';out.mkdir(exist_ok=True)
docs={p:fitz.open(ROOT/'raw'/f'{p}.pdf') for p in set(r['paperId'] for r in rows)}
for chunk,start in enumerate(range(0,len(rows),12)):
    subset=rows[start:start+12];tiles=[]
    for r in subset:
        pix=docs[r['paperId']][r['page']].get_pixmap(matrix=fitz.Matrix(1.5,1.5),clip=fitz.Rect(r['rect']),alpha=False)
        im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
        im.thumbnail((760,420))
        tile=Image.new('RGB',(790,im.height+36),'white');tile.paste(im,(12,30))
        ImageDraw.Draw(tile).text((10,7),r['id'],fill='black');tiles.append(tile)
    heights=[max(tiles[i].height,tiles[i+1].height if i+1<len(tiles) else 0) for i in range(0,len(tiles),2)]
    sheet=Image.new('RGB',(1580,sum(heights)+len(heights)*8),'#dce2e0');y=0
    for ri in range(0,len(tiles),2):
        sheet.paste(tiles[ri],(0,y))
        if ri+1<len(tiles):sheet.paste(tiles[ri+1],(790,y))
        y+=heights[ri//2]+8
    sheet.save(out/f'sheet-{chunk+1}.png')
print('curated',len(rows))
