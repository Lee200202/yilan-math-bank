from pathlib import Path
from collections import Counter
import json
import pymupdf as f
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parent;O=R/'review-luodong-pre108';O.mkdir(exist_ok=True)
C={x['id']:x for x in json.loads((R/'luodong-pre108-papers.json').read_text(encoding='utf8'))};Q=[]
def add(p,items):
 for n,rect,diff in items:
  Q.append(dict(id=f'{p}-fill-{n}',paperId=p,page=0,rect=rect,type='fill',number=n,difficulty=diff,reviewed=True,school='羅東國民中學',sourceSection='填充',sourceSha256=C[p]['sha256'],difficultyBasis='編輯依運算步驟、概念整合及圖表判讀判定；非官方難度',sourceNote='保留原卷填充題身分、原數字及必要圖形；105–107為108課綱以前試卷。'))
add('ld-105-1-1-7',[(1,[34,137,562,169],'medium'),(2,[34,176,562,216],'medium'),(3,[34,223,562,243],'medium'),(4,[34,267,562,287],'easy'),(5,[34,309,562,330],'easy'),(6,[34,348,562,369],'easy'),(7,[34,393,562,414],'easy'),(8,[34,437,562,458],'easy'),(9,[34,484,562,505],'medium'),(10,[34,533,562,554],'medium'),(11,[34,579,562,601],'medium'),(12,[34,624,562,648],'medium'),(13,[34,672,562,734],'medium'),(14,[34,760,562,782],'medium')])
add('ld-106-1-1-7',[(1,[44,152,564,174],'easy'),(2,[44,181,564,203],'medium'),(3,[44,211,564,233],'easy'),(4,[44,240,564,263],'easy'),(5,[44,269,564,292],'easy'),(6,[44,299,564,323],'medium'),(7,[44,329,564,353],'easy'),(8,[44,359,564,383],'medium'),(9,[44,389,564,413],'easy'),(10,[44,418,564,442],'easy'),(11,[44,450,564,474],'medium'),(12,[44,479,564,504],'medium'),(13,[44,509,564,534],'easy'),(14,[44,539,564,565],'medium'),(15,[44,569,564,594],'easy'),(16,[44,599,564,624],'medium'),(17,[44,629,564,654],'easy'),(18,[44,659,564,705],'medium'),(19,[44,714,564,740],'medium')])
add('ld-107-1-1-7',[(1,[46,227,703,277],'easy'),(2,[46,286,703,344],'easy'),(3,[46,351,703,376],'easy'),(4,[46,382,703,409],'easy'),(5,[46,417,703,443],'easy'),(6,[46,453,703,479],'easy'),(7,[46,489,703,515],'medium'),(8,[46,525,703,552],'easy'),(9,[46,562,703,588],'medium'),(10,[46,600,703,626],'easy'),(11,[46,635,703,699],'medium'),(12,[46,707,703,768],'hard'),(13,[43,777,703,863],'medium'),(14,[46,867,703,894],'medium'),(15,[46,903,703,930],'medium')])
(R/'curated-luodong-pre108.json').write_text(json.dumps(Q,ensure_ascii=False,indent=2),encoding='utf8')
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
