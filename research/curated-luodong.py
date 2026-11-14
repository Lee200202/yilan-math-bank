from pathlib import Path
from PIL import Image,ImageDraw
import pymupdf,json,sys,hashlib
ROOT=Path(__file__).parent;OUT=ROOT/'review-luodong';OUT.mkdir(exist_ok=True)
cat={x['id']:x for x in json.loads((ROOT/'luodong-papers.json').read_text(encoding='utf8'))}
rows=[];docs={}
def add(pid,page,kind,items):
    if pid not in docs:docs[pid]=pymupdf.open(ROOT.parent/cat[pid]['localPath'])
    for num,rect,diff in items:
        rows.append({'id':f'{pid}-{kind}-{num}','paperId':pid,'page':page,'rect':rect,'type':kind,'number':num,'difficulty':diff,'reviewed':'--approve' in sys.argv,'school':'羅東國中','sourceSha256':cat[pid]['sha256'],'difficultyBasis':'編輯依運算步驟、概念整合與圖表閱讀判定；非官方難度','sourceScan':True,**({'sourceInstruction':'請寫出解題過程。'} if kind=='written' else {})})
def full(pid,page,kind,items,x0=32,x1=566):add(pid,page,kind,[(n,[x0,y0,x1,y1],d) for n,y0,y1,d in items])
p='ld-108-1-2-7'
full(p,0,'fill',[(1,166,190,'easy'),(2,194,215,'easy'),(3,222,242,'easy'),(4,250,270,'easy'),(5,278,298,'easy'),(6,306,326,'medium'),(7,334,355,'easy'),(8,362,383,'medium'),(9,390,425,'medium'),(10,427,460,'medium'),(11,468,516,'medium'),(12,518,548,'medium'),(13,550,586,'medium'),(14,588,633,'medium'),(15,641,673,'medium'),(16,674,705,'medium'),(17,707,756,'hard')])
full(p,1,'fill',[(18,45,108,'hard'),(19,125,177,'hard'),(20,188,218,'hard')],24,568)
add(p,1,'written',[(1,[25,279,286,451],'hard'),(2,[292,271,565,432],'hard')])
p='ld-110-1-1-7'
full(p,0,'fill',[(1,197,212,'easy'),(2,218,235,'easy'),(3,240,258,'easy'),(4,262,280,'medium'),(5,281,304,'medium'),(6,306,325,'medium'),(7,328,347,'medium'),(8,350,370,'easy'),(9,373,391,'easy'),(10,394,414,'medium'),(11,417,436,'easy'),(12,439,458,'medium'),(13,461,504,'medium'),(14,505,615,'medium'),(15,616,716,'hard'),(16,717,764,'medium'),(17,765,806,'easy')],46,563)
full(p,1,'fill',[(18,58,135,'medium'),(19,137,201,'medium'),(20,226,333,'hard')],38,550)
add(p,1,'written',[(1,[38,390.5,286,480],'medium'),(2,[292,390.5,539,427],'medium'),(3,[37,565,539,650],'hard')])
p='ld-110-1-1-8'
full(p,0,'fill',[(1,216,324,'medium'),(2,350,415,'medium'),(3,430,475,'medium'),(4,494,667,'medium'),(5,677,717,'hard'),(6,728,749,'easy'),(7,762,790,'easy'),(8,802,829,'medium'),(9,839,866,'medium'),(10,882,910,'medium'),(11,927,949,'hard')],78,690)
p='ld-112-1-1-8'
full(p,0,'fill',[(1,146,189,'easy'),(2,200,219,'easy'),(3,225,249,'easy'),(4,258,279,'easy'),(5,290,312,'easy'),(6,320,344,'easy'),(7,352,378,'easy'),(8,385,414,'easy'),(9,420,442,'easy'),(10,452,476,'medium'),(11,485,509,'medium'),(12,515,543,'easy'),(13,546,578,'medium'),(14,585,609,'medium'),(15,618,642,'medium'),(16,648,674,'medium'),(17,680,708,'hard'),(18,714,741,'medium'),(19,745,776,'medium'),(20,778,802,'medium')],43,590)

def output():
    for r in rows:
        pix=docs[r['paperId']][r['page']].get_pixmap(matrix=pymupdf.Matrix(2,2),clip=pymupdf.Rect(r['rect']),alpha=False);pix.save(OUT/(r['id']+'.png'))
    for start in range(0,len(rows),6):
        tiles=[]
        for r in rows[start:start+6]:
            im=Image.open(OUT/(r['id']+'.png')).convert('RGB');im.thumbnail((760,1100));tile=Image.new('RGB',(790,im.height+36),'white');tile.paste(im,(12,30));ImageDraw.Draw(tile).text((10,7),r['id'],fill='black');tiles.append(tile)
        heights=[max(tiles[i].height,tiles[i+1].height if i+1<len(tiles) else 0) for i in range(0,len(tiles),2)];sheet=Image.new('RGB',(1580,sum(heights)+len(heights)*8),'#dce2e0');y=0
        for i in range(0,len(tiles),2):
            sheet.paste(tiles[i],(0,y))
            if i+1<len(tiles):sheet.paste(tiles[i+1],(790,y))
            y+=heights[i//2]+8
        sheet.save(OUT/f'curated-sheet-{start//6+1}.png')
    (ROOT/'curated-luodong.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
    (OUT/'curated-review.json').write_text(json.dumps({'reviewed':'--approve' in sys.argv,'questionCount':len(rows),'paperCounts':{p:sum(x['paperId']==p for x in rows) for p in docs},'sourceInstruction':'原填充區即使含O/X或A–D選項仍保留原填充身分，未偽作標準單選。','contentMethod':'原掃描PDF座標裁切，保持原文字公式與圖形，不虛構OCR文字。'},ensure_ascii=False,indent=2),encoding='utf8')
    print('crops',len(rows),'reviewed','--approve' in sys.argv)
if __name__=='__main__':output()
