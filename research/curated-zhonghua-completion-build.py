from pathlib import Path
from collections import Counter
import json
import pymupdf as f
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parent;O=R/'review-zhonghua-completion';O.mkdir(exist_ok=True)
C={(x['year'],x['semester']):x for x in json.loads((O/'selected.json').read_text(encoding='utf8'))}
Q=[]
def add(year,semester,page,typ,sec,items):
 p=C[year,semester]
 for n,rect,diff in items:
  Q.append(dict(id=f"{p['id']}-{typ}-{sec}-{n}",paperId=p['id'],page=page,rect=rect,type=typ,number=f'{sec}{n}',difficulty=diff,reviewed=True,school='中華國民中學',sourceSection=sec,sourceSha256=p['sha256'],difficultyBasis='編輯依運算步驟、概念整合及圖表閱讀判定；非官方難度',sourceNote='原題組及必要子題完整保留，未轉錄或改寫。'))
add(110,1,0,'choice','單選',[(1,[40,201,378,266],'easy'),(2,[40,273,378,371],'medium'),(3,[40,385,378,528],'medium'),(4,[40,540,378,660],'medium'),(5,[40,672,378,791],'hard')])
add(110,1,0,'fill','基礎填充',[(1,[40,883,378,1002],'medium'),(2,[389,154,735,176],'easy'),(3,[389,189,735,213],'medium'),(4,[389,222,735,256],'medium'),(5,[389,263,735,286],'easy'),(6,[389,297,735,321],'easy'),(7,[389,334,735,381],'medium'),(8,[389,394,735,417],'medium'),(9,[389,429,735,501],'medium'),(10,[389,513,735,537],'medium'),(11,[389,549,735,597],'medium')])
add(110,1,0,'fill','進階填充',[(1,[389,644,735,846],'medium'),(2,[389,861,735,907],'medium'),(3,[389,918,735,943],'hard'),(4,[389,954,735,1002],'hard')])
add(110,1,1,'fill','進階填充',[(5,[40,58,378,264],'hard'),(6,[40,271,378,345],'hard')])
add(110,1,1,'written','計算',[(1,[40,426,378,786],'hard'),(2,[389,58,735,489],'hard')])

add(108,2,0,'fill','超基本填充',[(1,[40,156,378,332],'easy'),(2,[40,355,378,523],'easy'),(3,[40,543,378,632],'easy'),(4,[40,633,378,681],'medium'),(5,[40,728,378,752],'easy')])
add(108,2,0,'choice','選擇',[(1,[40,801,378,872],'easy'),(2,[40,895,378,966],'easy'),(3,[389,129,735,320],'medium'),(4,[389,342,735,414],'easy'),(5,[389,446,735,604],'medium'),(6,[389,609,735,788],'medium')])
add(108,2,0,'fill','填充',[(1,[389,813,735,837],'medium'),(2,[389,899,735,951],'medium')])

add(109,2,0,'choice','選擇',[(1,[40,152,378,328],'medium'),(2,[40,353,378,449],'medium'),(3,[40,471,378,567],'easy'),(4,[40,589,378,779],'medium'),(5,[40,803,378,954],'medium')])
add(109,2,0,'fill','基礎',[(1,[389,152,735,200],'easy'),(2,[389,247,735,321],'easy'),(3,[389,368,735,442],'medium'),(4,[389,489,735,538],'easy'),(5,[389,585,735,673],'medium'),(6,[389,719,735,768],'easy'),(7,[389,812,735,886],'medium'),(8,[389,933,735,982],'easy')])

add(110,2,0,'fill','填充',[(1,[40,171,378,309],'medium'),(3,[40,669,378,851],'medium'),(4,[40,871,378,1001],'medium'),(5,[389,109,748,174],'medium'),(6,[389,194,748,348],'medium'),(7,[389,401,748,500],'medium'),(8,[389,564,748,590],'medium'),(9,[389,661,748,926],'hard'),(10,[389,931,748,997],'medium')])

add(111,2,0,'choice','選擇',[(1,[40,542,378,612],'medium'),(2,[40,637,378,708],'easy'),(3,[40,733,378,829],'hard'),(5,[389,275,748,441],'medium')])
add(111,2,0,'fill','填充',[(1,[389,539,748,585],'easy'),(2,[389,611,748,633],'easy'),(3,[389,664,748,717],'medium'),(4,[389,745,748,818],'medium'),(5,[389,879,748,925],'medium')])

add(112,2,0,'choice','選擇',[(1,[40,157,378,287],'easy'),(2,[40,307,378,455],'medium'),(3,[40,483,378,622],'medium'),(4,[40,633,378,834],'easy'),(5,[40,853,378,965],'hard')])
add(112,2,0,'fill','填充',[(1,[389,154,748,243],'easy'),(2,[389,264,748,353],'medium'),(3,[389,381,748,509],'medium'),(4,[389,572,748,652],'medium'),(5,[389,700,748,771],'medium'),(6,[389,839,748,1011],'medium')])

add(113,2,0,'fill','填充',[(1,[40,542,378,657],'medium'),(2,[40,692,378,715],'easy'),(3,[40,760,378,783],'medium'),(4,[40,826,378,879],'easy'),(5,[40,914,378,1029],'hard'),(6,[391,115,748,162],'easy'),(7,[391,204,748,271],'medium'),(8,[391,315,748,369],'easy'),(9,[391,403,748,515],'medium'),(10,[391,561,748,692],'easy'),(11,[391,715,748,892],'medium')])

add(114,2,0,'fill','填充',[(1,[40,158,378,254],'easy'),(2,[40,284,378,333],'medium'),(3,[40,353,378,402],'easy'),(4,[40,449,378,498],'easy'),(5,[40,521,378,570],'easy'),(6,[40,617,378,806],'medium'),(7,[40,825,378,874],'easy'),(8,[40,921,378,970],'medium'),(9,[389,130.5,748,177],'medium'),(10,[389,224,748,273],'easy'),(11,[389,320,748,394],'medium'),(12,[389,439,748,613],'medium'),(13,[389,632,748,778],'medium'),(14,[389,812,748,860],'hard'),(15,[389,902,748,972],'medium')])

assert len(Q)==len({q['id'] for q in Q})
(R/'curated-zhonghua-completion.json').write_text(json.dumps(Q,ensure_ascii=False,indent=2),encoding='utf8')
D={p['id']:f.open(R.parent/p['localPath']) for p in C.values()}
for chunk,start in enumerate(range(0,len(Q),8)):
 tiles=[]
 for idx,q in enumerate(Q[start:start+8],start):
  pix=D[q['paperId']][q['page']].get_pixmap(matrix=f.Matrix(1.8,1.8),clip=f.Rect(q['rect']),alpha=False)
  im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples);im.thumbnail((620,800))
  tile=Image.new('RGB',(650,im.height+35),'white');tile.paste(im,(10,30))
  label=next(f'{y}-{s}' for (y,s),p in C.items() if p['id']==q['paperId'])
  ImageDraw.Draw(tile).text((10,8),f"{label} {q['type']} item-{idx+1}",fill='black');tiles.append(tile)
 heights=[max(tiles[i].height,tiles[i+1].height if i+1<len(tiles) else 0) for i in range(0,len(tiles),2)]
 sheet=Image.new('RGB',(1300,sum(heights)+len(heights)*8),'#dce2e0');y=0
 for i in range(0,len(tiles),2):
  sheet.paste(tiles[i],(0,y))
  if i+1<len(tiles):sheet.paste(tiles[i+1],(650,y))
  y+=heights[i//2]+8
 sheet.save(O/f'crops-{chunk+1}.png')
print('Curated',len(Q),'byType',Counter(q['type'] for q in Q),'byYearSemester',Counter(next(k for k,p in C.items() if p['id']==q['paperId']) for q in Q))
