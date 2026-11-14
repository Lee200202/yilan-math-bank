"""Exact PDF-point crops, manually checked against all four source pages."""
from pathlib import Path
import pymupdf,json,hashlib,sys
from PIL import Image,ImageDraw
ROOT=Path(__file__).parent;OUT=ROOT/'review-zhonghua79';OUT.mkdir(exist_ok=True)
catalog=json.loads((ROOT/'zhonghua_catalog.json').read_text(encoding='utf-8'))
papers={x['grade']:x for x in catalog if x['year']==115 and x['kind']=='question' and x['grade'] in [7,9]}
rows=[]
def add(grade,page,kind,section,items):
    paper=papers[grade]
    for num,rect,diff in items:
        rows.append({'id':f'zh-115-1-1-{grade}-{section}-{num}','paperId':paper['id'],'page':page,'rect':rect,'type':kind,'number':num,'difficulty':diff,'reviewed':'--approve' in sys.argv,'school':'中華國中','originalSection':section,'difficultyBasis':'編輯依運算步驟、概念整合與圖表閱讀判定；非官方難度','sourceSha256':paper['sha256']})
add(7,0,'fill','basic',[(1,[87,217,417,237],'easy'),(2,[87,253,417,273],'easy'),(3,[87,289,417,327],'medium'),(4,[87,379,417,922],'medium')])
add(7,0,'fill','fill',[(1,[87,1009,417,1101],'medium'),(2,[428,163,770,309],'medium'),(3,[428,379,770,527],'medium'),(4,[428,577,770,723],'hard'),(5,[428,766,770,903],'medium'),(6,[428,937,770,1047],'medium')])
add(7,1,'fill','fill',[(7,[87,71,417,254],'medium'),(8,[87,413,417,524],'medium')])
add(7,1,'written','written',[(1,[87,737,417,902],'hard'),(2,[428,71,770,110],'hard'),(3,[428,413,770,470],'medium'),(4,[428,737,770,794],'hard')])
add(9,0,'fill','fill',[(1,[26,322,356,360],'easy'),(2,[26,375,356,412],'easy'),(3,[26,427,356,465],'easy'),(4,[26,494,356,548],'medium'),(5,[26,578,356,616],'easy'),(6,[26,662,356,700],'medium'),(7,[26,746,356,802],'medium'),(8,[26,848,356,905],'medium'),(9,[26,951,356,989],'medium'),(10,[383,114,716,154],'easy'),(11,[383,209,716,351],'medium'),(12,[383,446,716,559],'medium'),(13,[383,625,716,723],'hard'),(14,[383,803,716,957],'hard')])
add(9,1,'fill','fill',[(15,[26,24,356,82],'easy'),(16,[26,157,356,215],'medium'),(17,[26,329,356,386],'easy'),(18,[26,462,356,611],'hard'),(19,[26,671,356,841],'hard'),(20,[383,24,716,155],'medium'),(21,[383,290,716,418],'hard'),(22,[383,501,716,536],'hard'),(23,[383,633,716,796],'hard')])
for r in rows:
    if '-7-' in r['id']:
        r['sourceInstruction']='答案請化成最簡；同題子題須全部作答。' if r['type']=='fill' else '需列出計算過程。'
    else:r['sourceInstruction']='所有比請化成最簡整數比。'
docs={g:pymupdf.open(ROOT.parent/p['localPath']) for g,p in papers.items()}
for r in rows:
    g=7 if '-7-' in r['id'] else 9
    pix=docs[g][r['page']].get_pixmap(matrix=pymupdf.Matrix(1.8,1.8),clip=pymupdf.Rect(r['rect']),alpha=False)
    pix.save(OUT/(r['id']+'.png'))
for start in range(0,len(rows),6):
    tiles=[]
    for r in rows[start:start+6]:
        im=Image.open(OUT/(r['id']+'.png')).convert('RGB');im.thumbnail((760,1100))
        tile=Image.new('RGB',(790,im.height+36),'white');tile.paste(im,(12,30));ImageDraw.Draw(tile).text((10,7),r['id'],fill='black');tiles.append(tile)
    heights=[max(tiles[i].height,tiles[i+1].height if i+1<len(tiles) else 0) for i in range(0,len(tiles),2)]
    sheet=Image.new('RGB',(1580,sum(heights)+len(heights)*8),'#dce2e0');y=0
    for i in range(0,len(tiles),2):
        sheet.paste(tiles[i],(0,y))
        if i+1<len(tiles):sheet.paste(tiles[i+1],(790,y))
        y+=heights[i//2]+8
    sheet.save(OUT/f'sheet-{start//6+1}.png')
(ROOT/'curated-zhonghua79.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
exclusions=[{'paperId':papers[9]['id'],'originalType':'是非題','numbers':[1,2,3,4,5,6],'reason':'本網站題型目前僅單選、填充、非選；原卷是非題共享「三角形相似性質」指示，未擅改為單選或合併為新題。'}, {'paperId':papers[7]['id'],'note':'基礎第4題保留原八小題同一大題，填充第4/5題保留原填充身分及全部A–D選項；未偽作單選。'}]
(OUT/'review-report.json').write_text(json.dumps({'questionCount':len(rows),'reviewed':'--approve' in sys.argv,'sourcePagesInspected':4,'contactSheets':7,'excluded':exclusions,'notes':['所有rectangle均為原PDF point座標，page由0起算。','題幹內原題號仍保留；新卷外層題號應另排。','原七年級與九年級卷無標準單選，九年級無計算題。']},ensure_ascii=False,indent=2),encoding='utf-8')
print('crops',len(rows),'reviewed','--approve' in sys.argv)
