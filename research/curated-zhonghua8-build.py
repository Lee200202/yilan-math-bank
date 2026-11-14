from pathlib import Path
import json,hashlib
import pymupdf as f
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parent
O=R/'review-zhonghua8';O.mkdir(exist_ok=True)
rows=[]
catalog={x['id']:x for x in json.loads((R/'zhonghua_catalog.json').read_text(encoding='utf8'))}
def add(paper,page,typ,section,items):
    for n,rect,diff in items:
        rows.append(dict(id=f'{paper}-{typ}-{section}-{n}',paperId=paper,page=page,rect=rect,type=typ,number=f'{section}{n}',difficulty=diff,reviewed=True,school='中華國民中學',difficultyBasis='編輯依運算步驟、概念整合與圖表閱讀判定；非官方難度',sourceSha256=catalog[paper]['sha256'],sourceSection=section))
p='1aDSOOkqBVHxfjza6Y2Di4qnEI_Kcr2gn'
add(p,0,'fill','基礎',[(1,[40,227,378,284],'easy'),(2,[40,299,378,370],'easy'),(3,[40,383,378,404],'easy'),(4,[40,418,378,441],'easy'),(5,[40,455,378,548],'easy'),(6,[40,563,378,708],'medium'),(7,[40,823,378,885],'medium'),(8,[40,929,378,1007],'medium')])
add(p,0,'fill','進階',[(1,[389,197,735,292],'medium'),(2,[389,307,735,382],'medium'),(3,[389,431,735,478],'medium'),(4,[389,549,735,600],'medium'),(5,[389,664,735,831],'hard'),(6,[386,837,735,887],'hard')])
add(p,1,'fill','進階',[(7,[40,62,378,104],'medium'),(8,[40,223,378,245],'medium'),(9,[40,374,378,416],'hard'),(10,[40,628,378,846],'hard'),(11,[389,63,735,124],'hard')])
add(p,1,'written','計算',[(1,[389,340,735,436],'hard'),(2,[389,698,735,760],'medium')])

p='1wUCFV5eX0oZw3IM_zpkfB2QdFavSGydG'
add(p,0,'choice','選擇',[(1,[40,710,378,915],'medium')])
add(p,0,'fill','填充',[(1,[389,496,735,955],'medium')])
add(p,1,'fill','填充',[(2,[40,59,378,146],'medium'),(3,[40,206,378,303],'medium'),(4,[40,350,378,411],'medium'),(5,[40,502,378,550],'hard'),(6,[40,663,378,723],'medium'),(7,[40,812,378,838],'medium'),(8,[40,933,378,979],'hard')])
add(p,1,'written','計算',[(1,[389,92,735,166],'hard'),(2,[389,419,735,697],'medium')])

(R/'curated-zhonghua8.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
docs={p:f.open(R.parent/catalog[p]['localPath']) for p in {r['paperId'] for r in rows}}
for chunk,start in enumerate(range(0,len(rows),8)):
    tiles=[]
    for r in rows[start:start+8]:
        pix=docs[r['paperId']][r['page']].get_pixmap(matrix=f.Matrix(1.7,1.7),clip=f.Rect(r['rect']),alpha=False)
        im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
        im.thumbnail((600,820))
        tile=Image.new('RGB',(630,im.height+36),'white');tile.paste(im,(10,30))
        label=f"{catalog[r['paperId']]['year']}-{r['type']}-{r['sourceSection']}-{r['number']}"
        # Use ASCII for labels; JSON gives exact Chinese section names.
        label=f"{catalog[r['paperId']]['year']}-{r['type']}-item{start+len(tiles)+1}"
        ImageDraw.Draw(tile).text((10,8),label,fill='black');tiles.append(tile)
    heights=[max(tiles[i].height,tiles[i+1].height if i+1<len(tiles) else 0) for i in range(0,len(tiles),2)]
    sheet=Image.new('RGB',(1260,sum(heights)+len(heights)*8),'#dce2e0');y=0
    for i in range(0,len(tiles),2):
        sheet.paste(tiles[i],(0,y))
        if i+1<len(tiles):sheet.paste(tiles[i+1],(630,y))
        y+=heights[i//2]+8
    sheet.save(O/f'crops-{chunk+1}.png')
print('Curated',len(rows))
