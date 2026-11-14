from pathlib import Path
from PIL import Image,ImageDraw
import pymupdf,json,sys,hashlib
ROOT=Path(__file__).parent;OUT=ROOT/'review-zhonghua-extra79';OUT.mkdir(exist_ok=True)
cat={x['id']:x for x in json.loads((ROOT/'zhonghua_catalog.json').read_text(encoding='utf8'))}
A='1TW_2Q6LrYs-pzosnM38erf4q7vKbWPyQ';B='1wFwXlVeoTh8-P8yIEY27hWIXMXFDOtoF';C='1bdGpm3tyY5N9Rpe-j_GGslCHhBDMNV6s';D='1B5pbQux_YE1p_hTMPFeIxPgzknbLuixF'
docs={k:pymupdf.open(ROOT.parent/cat[k]['localPath']) for k in [A,B,C,D]};rows=[]
def add(pid,page,kind,section,side,items):
    x0,x1=([26,360] if side=='left' else [383,714]) if pid==D else ([40,378.8] if side=='left' else [389,756])
    for num,y0,y1,diff in items:
        rect=[x0,y0,x1,y1]
        # Tighten blank margins inside a manually chosen band only; never cross a question boundary.
        pix=docs[pid][page].get_pixmap(matrix=pymupdf.Matrix(2,2),clip=pymupdf.Rect(rect),alpha=False)
        im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples)
        box=im.convert('L').point(lambda v:255 if v<235 else 0).getbbox()
        if box:rect=[max(x0,x0+box[0]/2-2),max(y0,y0+box[1]/2-2),min(x1,x0+box[2]/2+2),min(y1,y0+box[3]/2+2)]
        p=cat[pid];qid=f"zh-{p['year']}-{p['semester']}-{p['exam']}-{p['grade']}-{section}-{num}"
        row={'id':qid,'paperId':pid,'page':page,'rect':rect,'type':kind,'number':num,'difficulty':diff,'reviewed':'--approve' in sys.argv,'school':'中華國中','originalSection':section,'sourceSha256':p['sha256'],'difficultyBasis':'編輯依運算步驟、概念整合與圖表閱讀判定；非官方難度'}
        if kind=='written':row['sourceInstruction']='需有完整計算過程，否則不予計分。' if pid!=C else '使用尺規作圖。'
        if pid==A and kind=='fill':row['sourceInstruction']='若答案不止一個，全對才給分。'
        if pid==B:row['sourceInstruction']='答案若為分數，請一律化為最簡分數，否則不予計分。'+('需有完整計算過程。' if kind=='written' else '')
        rows.append(row)
# 113 upper first, grade 7: all five choice questions, six basic groups, ten fill, two written.
add(A,0,'choice','choice','left',[(1,187,367,'medium'),(2,367,501,'easy'),(3,501,727,'medium'),(4,727,867,'medium'),(5,867,1005,'medium')])
add(A,0,'fill','basic','right',[(1,225,297,'easy'),(2,297,675,'easy'),(3,675,765,'easy'),(4,765,855,'medium'),(5,855,948,'medium'),(6,948,1005,'medium')])
add(A,1,'fill','fill','left',[(1,119,195,'easy'),(2,195,367,'hard'),(3,367,484,'medium'),(4,484,581,'medium'),(5,581,664,'medium'),(6,664,781,'medium'),(7,781,884,'medium'),(8,884,984,'medium'),(9,984,1005,'hard')])
add(A,1,'fill','fill','right',[(10,59,190,'medium')])
add(A,1,'written','written','right',[(1,259,505,'medium'),(2,660,840,'medium')])
# 114 upper third, grade 7: all five choice, six basic groups, seven fill and two written.
add(B,0,'choice','choice','left',[(1,244,330,'easy'),(2,330,415,'easy'),(3,415,551,'medium'),(4,551,767,'hard'),(5,767,1008,'hard')])
add(B,0,'fill','basic','right',[(1,185,241,'easy'),(2,241,297,'easy'),(3,297,494,'easy'),(4,494,878,'easy'),(5,878,954,'medium'),(6,954,1008,'easy')])
add(B,1,'fill','fill','left',[(1,77,288,'medium'),(2,288,540,'medium'),(3,540,684,'hard'),(4,684,805,'hard'),(5,805,1008,'hard')])
add(B,1,'fill','fill','right',[(6,55,250,'medium'),(7,257,350,'hard')])
add(B,1,'written','written','right',[(1,487,660,'hard'),(2,776,862,'hard')])
# 113 upper first, grade 9: a ruler-and-compass construction plus twenty fill groups.
add(C,0,'written','construction','left',[(1,147,253,'medium')])
add(C,0,'fill','fill','left',[(1,402.5,625,'medium'),(2,640,751,'easy'),(3,760,900,'hard')])
add(C,0,'fill','fill','right',[(4,130,270,'easy'),(5,283,390,'medium'),(6,397,530,'medium'),(7,539,701,'medium'),(8,705,810,'medium'),(9,829,984,'medium')])
add(C,1,'fill','fill','left',[(10,55,190,'medium'),(11,194,350,'medium'),(12,361,550,'medium'),(13,563,752,'hard'),(14,811,1024,'hard')])
add(C,1,'fill','fill','right',[(15,57,226,'hard'),(16,230,370,'hard'),(17,374,550,'hard'),(18,562,716,'hard'),(19,723,860,'hard'),(20,868,950,'hard')])
# 114 lower first, grade 9: eight genuine choice questions and independent fill questions.
add(D,0,'choice','choice','left',[(1,137,215,'easy'),(2,215,345,'easy'),(3,345,563,'easy'),(4,563,703,'medium'),(5,703,843,'medium'),(6,843,977,'medium')])
add(D,0,'choice','choice','right',[(7,112,285,'medium'),(8,298,410,'medium')])
add(D,0,'fill','fill','right',[(9,472,630,'medium'),(10,645,775,'medium'),(11,785,890,'medium'),(12,910,975,'easy')])
add(D,1,'fill','fill','left',[(13,25,200,'easy'),(14,237,335,'medium'),(15,385,450,'easy'),(16,503,670,'medium'),(17,677,821,'medium'),(18,845,907,'medium'),(19,925,985,'medium')])
add(D,1,'fill','fill','right',[(20,27,200,'hard'),(21,240,330,'easy'),(23,474,545,'hard'),(24,580,650,'medium'),(25,700,765,'hard')])
for r in rows:
    if r['id']=='zh-113-1-1-9-fill-11':r['rect'][0]=33
    pix=docs[r['paperId']][r['page']].get_pixmap(matrix=pymupdf.Matrix(1.8,1.8),clip=pymupdf.Rect(r['rect']),alpha=False);pix.save(OUT/(r['id']+'.png'))
for start in range(0,len(rows),6):
    tiles=[]
    for r in rows[start:start+6]:
        im=Image.open(OUT/(r['id']+'.png')).convert('RGB');im.thumbnail((760,1100));tile=Image.new('RGB',(790,im.height+36),'white');tile.paste(im,(12,30));ImageDraw.Draw(tile).text((10,7),r['id'],fill='black');tiles.append(tile)
    heights=[max(tiles[i].height,tiles[i+1].height if i+1<len(tiles) else 0) for i in range(0,len(tiles),2)];sheet=Image.new('RGB',(1580,sum(heights)+len(heights)*8),'#dce2e0');y=0
    for i in range(0,len(tiles),2):
        sheet.paste(tiles[i],(0,y))
        if i+1<len(tiles):sheet.paste(tiles[i+1],(790,y))
        y+=heights[i//2]+8
    sheet.save(OUT/f'sheet-{start//6+1}.png')
(ROOT/'curated-zhonghua-extra79.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
report={'reviewed':'--approve' in sys.argv,'questions':len(rows),'sourcePages':8,'contactSheets':(len(rows)+5)//6,'papers':[{k:cat[pid][k] for k in ['id','year','semester','exam','grade','sha256']} for pid in [A,B,C,D]],'excluded':[{'paperId':D,'number':22,'reason':'依賴第21題共同情境（原文「承上題」），未獨立切分，也未把兩個原編號題合併。'}],'notes':['113上1與114上3七年級基礎題、填充題全部依原大題保留，子題不拆散。','113上1九年級第8與15題雖有字母選項，原身分仍是填充；沒有改成標準單選。','保留原卷圖示與原選項；難度為編輯判斷，非官方。']}
(OUT/'review-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print('crops',len(rows),'reviewed',report['reviewed'])
