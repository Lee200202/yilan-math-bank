from pathlib import Path
from collections import Counter
import json
import pymupdf as f
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parent;O=R/'review-luodong9';O.mkdir(exist_ok=True)
C={x['id']:x for x in json.loads((R/'luodong-papers.json').read_text(encoding='utf8'))};Q=[]
def add(p,items):
 for n,rect,diff in items:
  Q.append(dict(id=f'{p}-fill-{n}',paperId=p,page=0,rect=rect,type='fill',number=n,difficulty=diff,reviewed=True,school='羅東國民中學',sourceSection='填充',sourceSha256=C[p]['sha256'],difficultyBasis='編輯依運算步驟、概念整合與圖形判讀判定；非官方難度',sourceNote='影像原卷之完整單題裁切；有選項仍按原卷填充題身分。'))
add('ld-112-1-1-9',[(1,[36,146,560,165],'easy'),(2,[36,168,560,200],'medium'),(3,[36,204,560,222],'medium'),(4,[36,233,560,255],'easy'),(5,[36,263,560,345],'hard'),(6,[36,347,560,384],'easy'),(7,[36,390,560,422],'medium'),(12,[36,674,560,697],'medium'),(13,[36,702,560,721],'medium'),(14,[36,721.5,560,801],'hard')])
add('ld-110-1-1-9',[(5,[28,551,715,624],'medium'),(6,[28,631,715,731],'hard'),(7,[28,735,715,755],'easy'),(8,[28,759,715,806],'medium'),(9,[28,810,715,839],'medium'),(10,[28,841,715,865],'medium'),(11,[28,869,715,943],'hard'),(12,[28,945,715,981],'medium')])
(R/'curated-luodong9.json').write_text(json.dumps(Q,ensure_ascii=False,indent=2),encoding='utf8')
D={p:f.open(R/'raw'/f'{p}.pdf') for p in {q['paperId'] for q in Q}}
for chunk,start in enumerate(range(0,len(Q),8)):
 tiles=[]
 for idx,q in enumerate(Q[start:start+8],start):
  pix=D[q['paperId']][0].get_pixmap(matrix=f.Matrix(1.8,1.8),clip=f.Rect(q['rect']),alpha=False)
  im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples);im.thumbnail((860,600))
  tile=Image.new('RGB',(890,im.height+35),'white');tile.paste(im,(10,30));ImageDraw.Draw(tile).text((10,8),f"{q['paperId']} fill-{q['number']} item{idx+1}",fill='black');tiles.append(tile)
 heights=[max(tiles[i].height,tiles[i+1].height if i+1<len(tiles) else 0) for i in range(0,len(tiles),2)]
 sheet=Image.new('RGB',(1780,sum(heights)+len(heights)*8),'#dce2e0');y=0
 for i in range(0,len(tiles),2):
  sheet.paste(tiles[i],(0,y))
  if i+1<len(tiles):sheet.paste(tiles[i+1],(890,y))
  y+=heights[i//2]+8
 sheet.save(O/f'crops-{chunk+1}.png')
print(len(Q),Counter(q['paperId'] for q in Q))
