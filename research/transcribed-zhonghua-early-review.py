from pathlib import Path
from PIL import Image,ImageDraw
import json,pymupdf
ROOT=Path(__file__).parent;OUT=ROOT/'transcribed-zhonghua-early-review';OUT.mkdir(exist_ok=True)
cat={x['id']:x for x in json.loads((ROOT/'zhonghua_catalog.json').read_text(encoding='utf8'))};qs=[]
for f in ['curated-zhonghua-earlier.json','curated-zhonghua-completion.json']:
    qs += [q for q in json.loads((ROOT/f).read_text(encoding='utf8')) if cat[q['paperId']]['year']<=110]
(ROOT/'transcribed-zhonghua-early-map.json').write_text(json.dumps(qs,ensure_ascii=False,indent=2),encoding='utf8')
docs={k:pymupdf.open(ROOT.parent/v['localPath']) for k,v in cat.items() if k in {q['paperId'] for q in qs}}
for start in range(0,len(qs),6):
    tiles=[]
    for i,q in enumerate(qs[start:start+6],start+1):
        pix=docs[q['paperId']][q['page']].get_pixmap(matrix=pymupdf.Matrix(1.7,1.7),clip=pymupdf.Rect(q['rect']),alpha=False);im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples);im.thumbnail((760,1100));tile=Image.new('RGB',(790,im.height+36),'white');tile.paste(im,(12,30));ImageDraw.Draw(tile).text((10,7),f'ITEM {i} / '+q['paperId']+' / '+q['type']+' / '+str(q['number']),fill='black');tiles.append(tile)
    hs=[max(tiles[i].height,tiles[i+1].height if i+1<len(tiles) else 0) for i in range(0,len(tiles),2)];sheet=Image.new('RGB',(1580,sum(hs)+len(hs)*8),'#dce2e0');y=0
    for i in range(0,len(tiles),2):
        sheet.paste(tiles[i],(0,y))
        if i+1<len(tiles):sheet.paste(tiles[i+1],(790,y))
        y+=hs[i//2]+8
    sheet.save(OUT/f'sheet-{start//6+1}.png')
print('items',len(qs))
