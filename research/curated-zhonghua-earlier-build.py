from pathlib import Path
from collections import Counter
import json
import pymupdf as f
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parent;O=R/'review-zhonghua-earlier';O.mkdir(exist_ok=True)
C={x['year']:x for x in json.loads((O/'selected.json').read_text(encoding='utf8'))}
Q=[]
def add(year,page,typ,sec,items):
    p=C[year]
    for n,rect,diff in items:
        Q.append(dict(id=f"{p['id']}-{typ}-{sec}-{n}",paperId=p['id'],page=page,rect=rect,type=typ,number=f'{sec}{n}',difficulty=diff,reviewed=True,school='中華國民中學',sourceSection=sec,sourceSha256=p['sha256'],difficultyBasis='編輯依運算步驟、概念整合及圖表閱讀判定；非官方難度',sourceNote='原題組及必要子題完整保留，未轉錄或改寫。'))
add(108,0,'choice','單選',[(1,[40,164,378,328],'easy'),(2,[40,344,378,448],'medium'),(3,[40,464,378,520],'easy'),(4,[40,536,378,760],'medium'),(5,[40,776,378,832],'medium'),(7,[389,173,735,266],'medium'),(8,[389,281,735,410],'medium'),(9,[389,425,735,590],'medium'),(10,[389,604,735,735],'hard')])
add(108,0,'fill','填充',[(1,[389,821,735,924],'easy')])
add(108,1,'written','計算',[(1,[40,777,378,952],'medium'),(2,[389,65,735,231],'hard')])
add(109,0,'choice','選擇',[(1,[42,152,377,277],'easy'),(2,[42,303,377,440],'easy'),(3,[42,470,377,630],'medium'),(4,[42,668,377,805],'medium'),(5,[42,843,377,968],'easy')])
add(109,0,'fill','填充',[(1,[389,183,735,204],'easy'),(2,[389,263,735,465],'medium'),(3,[389,523,735,725],'medium'),(4,[389,777,735,825],'medium'),(5,[389,882,735,905],'medium'),(6,[389,962,735,1005],'hard')])
add(111,0,'fill','填充',[(1,[40,626,378,928],'medium'),(2,[40,970,378,991],'easy'),(3,[388,151,735,172],'easy'),(4,[388,219,735,240],'medium'),(5,[388,299,735,347],'medium'),(6,[388,407,735,456],'medium'),(7,[388,527,735,680],'hard'),(8,[388,755,735,817],'medium'),(9,[388,890,735,912],'hard')])
add(111,1,'written','綜合',[(1,[40,90,378,113],'medium'),(2,[40,460,378,848],'hard'),(3,[388,87,735,325],'hard'),(4,[388,686,735,710],'hard')])
add(112,0,'choice','選擇',[(1,[40,160,378,249],'easy'),(2,[40,252,378,321],'easy'),(3,[40,324,378,466],'medium'),(4,[40,470,378,625],'medium'),(5,[40,630,378,773],'medium')])
add(112,0,'fill','基礎填充',[(1,[40,823,378,991],'easy'),(2,[389,131,748,313],'easy'),(3,[389,337,748,468],'medium'),(4,[389,513,748,688],'medium'),(5,[389,711,748,754],'medium'),(6,[389,839,748,1024],'medium')])
add(113,0,'fill','基礎填充',[(1,[88,199,419,521],'easy'),(2,[88,541,419,650],'medium')])
add(113,0,'fill','填充',[(1,[88,710,419,739],'medium'),(2,[88,844,419,869],'easy'),(3,[88,951,419,994],'medium'),(4,[429,151,757,203],'medium'),(5,[429,308,757,348],'hard'),(6,[429,451,757,562],'medium'),(7,[429,574,757,618],'medium'),(8,[429,685,757,724],'medium'),(9,[429,829,757,886],'medium'),(10,[429,915,757,959],'medium')])
# Remaining complete question groups, appended without changing existing IDs.
add(108,1,'fill','填充',[(2,[40,75,378,177],'easy'),(3,[40,217,378,242],'medium'),(4,[40,265,378,573],'medium'),(5,[40,595,378,639],'medium'),(6,[40,661,378,705],'hard')])
add(109,1,'fill','填充',[(7,[40,56,378,133],'medium'),(8,[40,224,378,275],'hard'),(9,[40,369,378,418],'medium'),(10,[40,509,378,548],'hard'),(11,[40,639,378,689],'hard')])
add(109,1,'written','計算',[(1,[40,802,378,831],'medium'),(2,[389,52,735,82],'hard'),(3,[389,353,735,378],'medium'),(4,[389,648,735,698],'hard')])
add(112,1,'fill','填充',[(1,[40,83,378,257],'hard'),(2,[40,281,378,346],'medium'),(3,[40,457,378,501],'medium'),(4,[40,631,378,748],'medium'),(5,[40,847,378,898],'hard')])
add(112,1,'written','計算',[(1,[389,89,735,140],'medium'),(2,[389,338,735,382],'medium'),(3,[389,646,735,698],'hard')])
add(113,1,'fill','填充',[(11,[88,69,419,111],'medium'),(12,[88,247,419,291],'easy'),(13,[88,391,419,435],'medium'),(14,[88,560,419,615],'hard'),(15,[88,790,419,813],'medium'),(16,[88,916,419,939],'hard'),(17,[429,69,757,129],'hard'),(18,[429,250,757,309],'hard')])
add(113,1,'written','計算',[(1,[429,395,757,454],'medium'),(2,[429,733,757,760],'hard')])
(R/'curated-zhonghua-earlier.json').write_text(json.dumps(Q,ensure_ascii=False,indent=2),encoding='utf8')
D={p['id']:f.open(R.parent/p['localPath']) for p in C.values()}
for chunk,start in enumerate(range(0,len(Q),8)):
    tiles=[]
    for idx,q in enumerate(Q[start:start+8],start):
        pix=D[q['paperId']][q['page']].get_pixmap(matrix=f.Matrix(1.8,1.8),clip=f.Rect(q['rect']),alpha=False)
        im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples);im.thumbnail((620,760))
        tile=Image.new('RGB',(650,im.height+35),'white');tile.paste(im,(10,30))
        yr=next(y for y,p in C.items() if p['id']==q['paperId'])
        ImageDraw.Draw(tile).text((10,8),f"{yr} {q['type']} item-{idx+1}",fill='black');tiles.append(tile)
    heights=[max(tiles[i].height,tiles[i+1].height if i+1<len(tiles) else 0) for i in range(0,len(tiles),2)]
    sheet=Image.new('RGB',(1300,sum(heights)+len(heights)*8),'#dce2e0');y=0
    for i in range(0,len(tiles),2):
        sheet.paste(tiles[i],(0,y))
        if i+1<len(tiles):sheet.paste(tiles[i+1],(650,y))
        y+=heights[i//2]+8
    sheet.save(O/f'crops-{chunk+1}.png')
print('Curated',len(Q),'byType',Counter(q['type'] for q in Q),'byYear',Counter(next(y for y,p in C.items() if p['id']==q['paperId']) for q in Q))
