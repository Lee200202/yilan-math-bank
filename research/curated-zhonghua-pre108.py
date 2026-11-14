from pathlib import Path
from PIL import Image,ImageDraw
import pymupdf,json,sys
ROOT=Path(__file__).parent;OUT=ROOT/'review-zhonghua-pre108';OUT.mkdir(exist_ok=True)
cat={x['id']:x for x in json.loads((ROOT/'zhonghua-pre108-catalog.json').read_text(encoding='utf8'))};ids={105:'1k-T9wedtWmZ4qTyP7Vomjl25Xpox6ymv',106:'123lGBiDXT7Brx1TJah7SZy7MHrfWNKw9',107:'1WSY16qjhQvFsIfCt4Bo48yXfgEE0DYJG'}
docs={y:pymupdf.open(ROOT.parent/cat[pid]['renderPath']) for y,pid in ids.items()};rows=[]
def add(y,p,t,side,items):
    for n,y0,y1,d in items:
        rect=([40,y0,378,y1] if side=='left' else [389,y0,724,y1])
        rows.append({'id':f'zh-{y}-1-1-7-{t}-{n}','paperId':ids[y],'page':p,'rect':rect,'type':t,'number':n,'difficulty':d,'reviewed':'--approve' in sys.argv,'school':'中華國中','sourceSha256':cat[ids[y]]['sha256'],'difficultyBasis':'編輯依運算步驟與概念整合判斷；非官方難度'})
add(105,0,'fill','left',[(1,155,289,'medium'),(2,367,516,'medium')])
add(105,1,'fill','left',[(4,322,432,'hard'),(5,528,632,'hard'),(6,747,860,'hard')])
add(105,1,'written','right',[(1,104,126,'medium'),(2,290,314,'medium'),(3,484,528,'medium'),(4,705,815,'medium')])
add(106,0,'fill','left',[(1,507,603,'easy'),(2,684,794,'easy'),(3,881,953,'easy')])
add(106,0,'fill','right',[(4,132,225,'medium'),(5,350,415,'easy'),(6,508,593,'easy'),(7,702,768,'medium'),(8,856,900,'easy')])
add(106,1,'fill','left',[(9,55,95,'medium'),(10,208,251,'medium')])
add(107,0,'fill','left',[(1,366,410,'easy'),(2,428,447,'easy'),(3,463,482,'easy'),(4,499,522,'easy'),(5,539,559,'medium'),(6,577,681,'medium'),(7,726,745,'medium'),(8,790,902,'medium'),(9,923,943,'medium')])
add(107,0,'fill','right',[(10,138,193,'medium')])
for r in rows:
    y=cat[r['paperId']]['year'];pix=docs[y][r['page']].get_pixmap(matrix=pymupdf.Matrix(1.8,1.8),clip=pymupdf.Rect(r['rect']),alpha=False);pix.save(OUT/(r['id']+'.png'))
for start in range(0,len(rows),6):
    tiles=[]
    for r in rows[start:start+6]:
        im=Image.open(OUT/(r['id']+'.png')).convert('RGB');im.thumbnail((760,1100));tile=Image.new('RGB',(790,im.height+36),'white');tile.paste(im,(12,30));ImageDraw.Draw(tile).text((10,7),r['id'],fill='black');tiles.append(tile)
    hs=[max(tiles[i].height,tiles[i+1].height if i+1<len(tiles) else 0) for i in range(0,len(tiles),2)];sheet=Image.new('RGB',(1580,sum(hs)+len(hs)*8),'#dce2e0');y=0
    for i in range(0,len(tiles),2):
        sheet.paste(tiles[i],(0,y))
        if i+1<len(tiles):sheet.paste(tiles[i+1],(790,y))
        y+=hs[i//2]+8
    sheet.save(OUT/f'curated-sheet-{start//6+1}.png')
(ROOT/'curated-zhonghua-pre108.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
(OUT/'curated-review.json').write_text(json.dumps({'reviewed':'--approve' in sys.argv,'questions':len(rows),'excluded':[{'year':105,'number':3,'reason':'14子題跨頁，不拆大題、不以單一矩形跨頁。'},{'year':106,'section':'是非題','reason':'本次三類組卷不擅改是非題型。'},{'year':107,'number':'綜合1','reason':'Word衍生圖未能確認數線原點與單位標示，不採用。'}],'scope':'105九個完整題組；106與107各十個完整填充題，保留原卷來源供後續轉寫。'},ensure_ascii=False,indent=2),encoding='utf8')
print('questions',len(rows))
