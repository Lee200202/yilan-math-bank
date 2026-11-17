"""Create an isolated, incomplete transcription draft; never used in the build."""
import json
from pathlib import Path

rows = [
('fill','如圖，$AB$ 為圓 $O$ 的一弦，若 $AB$ 的弦心距 $OP=3$、$AB=8$，求圓 $O$ 的半徑：______。',True),
('fill','如圖，四邊形 $ABCD$ 為圓 $O$ 的外切四邊形，$AB=2x+1$，$BC=2x+3$，$CD=4x-2$，$AD=3x-2$，求 $x=$______。',True),
('fill','如圖，正五邊形 $ABCDE$ 的頂點均在圓 $O$ 上，則 $\\angle AOB=$______ 度。',True),
('fill','如圖，$\\angle ABC$ 為圓 $O$ 的一個弦切角，若弧 $AB=100^\\circ$，則 $\\angle ABC=$______ 度。',True),
('choice','下列四邊形中，何者不一定有外接圓？',False),
('fill','如圖，$AB$、$CD$ 為圓 $O$ 的兩弦，且 $AB\\parallel CD$，若 [原 DOC EQ 疊印 BE，符號尚未確證] $=46^\\circ$，$\\angle AEC=37^\\circ$，則 $\\angle ECD=$______ 度。',True),
('choice','下列敘述哪一個正確？',False),
('fill','如圖，$A$、$B$、$C$、$D$ 為圓上四點，且 $AB$、$CD$ 交於圓外一點 $P$，$AC$、$BD$ 交於圓內 $E$ 點。 (1) 若 $AB=10$，$BP=8$，$CP=9$，則 $PD=$______。 (2) 已知弧 $AD=100^\\circ$，弧 $BC=30^\\circ$，則 $\\angle AED=$______ 度。',True),
('fill','如圖，$AB$ 切圓 $O$ 於 $B$，$AO$ 交圓 $O$ 於 $C$，若 $AB=6$，$AC=4$，則圓 $O$ 的半徑為______。',True),
('fill','有一個平行四邊形為圓內接四邊形，已知此四邊形的相鄰兩邊分別為 $\\sqrt{5}$ 和 $\\sqrt{7}$，則此圓的面積為______。',False),
('fill','如圖，圓 $O_1$、圓 $O_2$ 的半徑分別為 12、8，內公切線 $AB$ 交 $O_1O_2$ 於 $P$，若 $AB=15$，則 $O_1O_2=$______。',True),
('fill','如圖，有一個圓通過 $\\triangle ABC$ 的三個頂點，且 $BC$ 的中垂線與弧 $AC$ 相交於 $D$ 點，若弧 $AD=36^\\circ$，$\\angle C=42^\\circ$，則弧 $BC$ 的度數為______度。',True),
('fill','如圖，圓 $O_1$ 和圓 $O_2$ 兩圓外切，半徑分別為 5 和 3，直線 $L$ 與兩圓分別切於 $A$、$B$ 兩點。 (1) $AB=$______。 (2) 過 $C$ 點作圓 $O_1$ 和圓 $O_2$ 的內公切線交 $AB$ 於 $D$ 點，求 $CD=$______。',True),
('fill','如圖，$A$、$B$、$C$ 三點在圓上，過 $B$ 點之切線交弦 $AC$ 之延長線於 $D$ 點，若 $\\angle BAC=40^\\circ$，$\\angle ADB=35^\\circ$，則 $\\angle ABC=$______ 度。',True),
('fill','如圖，已知圓 $O$ 的半徑為 3，$\\angle ACB=\\angle BDC$，則 $BC=$______。',True),
('fill','如圖，$AD$、$BC$、$CD$ 分別切圓於 $A$、$B$、$E$ 三點，$AB$ 為圓 $O$ 的直徑，已知 $AD=3$、$BC=7$，$\\triangle COD$ 的面積是 20，求 $OD=$______。',True),
('fill','如圖，$A$、$B$、$C$ 三點共線，以 $AC$、$BC$ 為直徑的兩個半圓中，$AD$ 切小半圓於 $P$ 點，若 $AC=20$，$BC=15$，則 $AD=$______。',True),
('fill','如圖，已知圓 $O_1$、圓 $O_2$ 和圓 $O_3$ 的半徑都是 4，圓 $O_1$ 和圓 $O_3$ 外切於 $O_2$，則 $AB=$______。',True),
('written','已知圓 $O_1$ 半徑為 10，圓 $O_2$ 半徑為 6，請將各連心距 16、2、10、4、20 與兩圓位置關係「外離、外切、交於兩點、內切、內離」配對。',False),
('written','如圖，$BC$ 為圓 $O$ 的直徑，且 $AB$ 和 $AC$ 分別交圓 $O$ 於 $D$、$E$ 兩點，連接 $BE$ 和 $CD$ 交於 $F$ 點。 (1) 圖中有哪些三角形和 $\\triangle CEF$ 相似？ (2) 若 $DF=FC$，$BF=4$，$EF=1$，則 $\\angle A$ 的度數為何？',True),
]
options={5:['正方形','矩形','菱形','等腰梯形'],7:['圓 $O$ 的直徑為 6，若 $OP=4$，則 $P$ 點在圓 $O$ 上。','在同一圓中，弦心距越長，則所對應的弦越長。','同一圓中，度數越大的弧，其長度越長。','$AB$、$CD$ 為圓 $O$ 的兩弦，若 $AB\\parallel CD$，則弧 $AB=$弧 $CD$。']}
def fig(body, labels, width=160, height=125):
    ts=''.join(f'<text x="{x}" y="{y}">{s}</text>' for x,y,s in labels)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}"><g fill="none" stroke="black" stroke-width="1.5">{body}</g><g fill="black" font-size="12" font-family="serif">{ts}</g></svg>'
figures={
2: fig('<circle cx="75" cy="60" r="35"/><path d="M53 25 L19.32 95 H115.83 L105 25 Z"/><circle cx="75" cy="60" r="1.5" fill="black"/>',[(47,20,'A'),(9,105,'B'),(117,105,'C'),(105,20,'D'),(67,68,'O')]),
3: fig('<circle cx="75" cy="62" r="42"/><path d="M117 62 L88 22 L41 37 L41 87 L88 102 Z M75 62 L117 62 M75 62 L88 22"/>',[(121,66,'A'),(88,18,'B'),(29,37,'C'),(29,94,'D'),(87,117,'E'),(64,72,'O')]),
4: fig('<circle cx="75" cy="60" r="40"/><path d="M109.6 40 L75 100 M20 100 H135"/><circle cx="75" cy="60" r="1.7" fill="black"/>',[(111,38,'A'),(71,115,'B'),(137,104,'C'),(63,62,'O')]),
6: fig('<circle cx="75" cy="60" r="40"/><path d="M37.53 46 H112.47 M39.81 79 H110.19 M37.53 46 L75 20 L39.81 79"/><circle cx="75" cy="60" r="1.5" fill="black"/>',[(26,47,'A'),(114,47,'B'),(28,88,'C'),(112,88,'D'),(75,16,'E'),(78,67,'O')]),
8: fig('<circle cx="60" cy="60" r="40"/><path d="M33.9 29.7 L135 60 L33.9 90.3 M33.9 29.7 L98.5 71 M33.9 90.3 L98.5 49"/>',[(24,29,'A'),(99,46,'B'),(99,82,'C'),(23,99,'D'),(64,61,'E'),(138,64,'P')]),
9: fig('<circle cx="58" cy="65" r="36"/><path d="M58 29 H130 L58 65"/><circle cx="58" cy="65" r="1.7" fill="black"/>',[(51,25,'B'),(132,30,'A'),(89,51,'C'),(46,74,'O')]),
11: fig('<circle cx="50" cy="60" r="30"/><circle cx="135" cy="60" r="20"/><path d="M17 60 H155 M55 27 L150 96"/><circle cx="50" cy="60" r="1.5" fill="black"/><circle cx="135" cy="60" r="1.5" fill="black"/>',[(43,76,'O₁'),(134,76,'O₂'),(65,27,'A'),(122,90,'B'),(98,73,'P')],175,115),
12: fig('<circle cx="75" cy="65" r="43"/><path d="M32 65 H118 M75 15 V109 M44 35 L32 65 M44 35 L118 65"/>',[(35,32,'A'),(21,72,'B'),(120,72,'C'),(77,16,'D')]),
13: fig('<circle cx="55" cy="50" r="40"/><circle cx="117" cy="66" r="24"/><path d="M14 90 H155 M55 50 L117 66 M55 50 V90 M117 66 V90 M93.75 60 L86 90"/>',[(46,48,'O1'),(119,65,'O2'),(50,106,'A'),(118,106,'B'),(94,56,'C'),(79,106,'D'),(156,94,'L')],170,115),
14: fig('<circle cx="65" cy="60" r="40"/><path d="M45 25.36 L65 100 L142 100 L45 25.36 M65 100 L103.6 70.5"/><circle cx="65" cy="60" r="1.5" fill="black"/>',[(34,24,'A'),(60,114,'B'),(105,71,'C'),(143,104,'D'),(54,61,'O')],160,120),
15: fig('<circle cx="75" cy="60" r="40"/><path d="M46.7 31.7 L103.3 88.3 L36.4 70.35 L75 20 L103.3 88.3"/><circle cx="75" cy="60" r="1.5" fill="black"/>',[(36,30,'A'),(25,78,'B'),(104,100,'C'),(73,16,'D'),(65,67,'O')]),
16: fig('<circle cx="70" cy="61.65" r="36.65"/><path d="M70 25 V98.3 M70 25 H94 L126 98.3 H70 M70 61.65 L94 25 M70 61.65 L126 98.3"/>',[(65,20,'A'),(65,113,'B'),(128,104,'C'),(94,20,'D'),(104,45,'E'),(58,66,'O')]),
17: fig('<path d="M20 100 A60 60 0 0 1 140 100 M50 100 A45 45 0 0 1 140 100 M20 100 H140 M20 100 L96.8 42.4"/>',[(10,114,'A'),(46,114,'B'),(141,114,'C'),(98,40,'D'),(64,62,'P')],160,120),
18: fig('<circle cx="55" cy="60" r="30"/><circle cx="85" cy="60" r="30"/><circle cx="115" cy="60" r="30"/><path d="M25 60 H115 M25 60 L100 34"/>',[(14,64,'A'),(101,29,'B'),(48,75,'O1'),(78,75,'O2'),(111,75,'O3')],160,110),
20: fig('<circle cx="75" cy="80" r="45"/><path d="M30 80 H120 L102.42 7.58 L30 80 M30 80 L115 59.4 M75 35 L120 80"/>',[(100,7,'A'),(19,85,'B'),(122,85,'C'),(65,32,'D'),(120,57,'E'),(91,65,'F'),(72,95,'O')],150,135),
}
qs=[]
for i,(kind,prompt,needs_figure) in enumerate(rows,1):
    num=str(i if i<=18 else i-18)
    blocks=[{'type':'text','text':prompt}]
    if i in options: blocks.append({'type':'options','items':options[i]})
    q={'type':kind,'sourceNumber':num,'page':1 if i<=12 else 2,'difficulty':'medium','primaryUnitId':'nanyi-9-1-2-2','unitIds':['nanyi-9-1-2-2'],'unitAssignmentBasis':'圓的性質；草稿待複核細分','blocks':blocks}
    q['difficulty'] = 'easy' if i in {1,3,4,5,7,19} else 'hard' if i in {8,11,13,16,17,20} else 'medium'
    q['primaryUnitId'] = 'nanyi-9-1-2-1' if i in {1,2,7,9,11,13,16,17,18,19} else 'nanyi-9-1-2-2'
    q['unitIds'] = [q['primaryUnitId']]
    q['unitAssignmentBasis'] = '圓與切線、兩圓位置或弦心距。' if q['primaryUnitId'].endswith('2-1') else '弧、圓周角及圓內接圖形。'
    if i in figures:
        q['blocks'].append({'type':'svg','svg':figures[i]})
        if i != 6: needs_figure=False
    if i == 1:
        q['difficulty']='easy'
        q['primaryUnitId']='nanyi-9-1-2-1'
        q['unitIds']=['nanyi-9-1-2-1']
        q['unitAssignmentBasis']='圓的弦心距及直角三角形。'
        q['blocks'].append({'type':'svg','svg':'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 150 130"><circle cx="75" cy="60" r="45" fill="none" stroke="black" stroke-width="1.5"/><path d="M39 87 H111 M75 60 V87 M68 87 V80 H75" fill="none" stroke="black" stroke-width="1.5"/><circle cx="75" cy="60" r="2"/><g font-size="13" font-family="serif"><text x="67" y="55">O</text><text x="28" y="91">A</text><text x="114" y="91">B</text><text x="72" y="103">P</text></g></svg>'})
        needs_figure=False
    if needs_figure:
        q['usable']=False
        q['sourceIssue']='46 度前 BE 的疊印符號未確認' if i==6 else '必要題圖尚未完成向量重繪'
    qs.append(q)
draft={'paperId':'ld-108-1-2-9','sourceSha256':'155e0f8a8bf37dceae98a0d91ae454a2a9a508cd4df858ec1c5a66407f5a2760','printedHeader':'宜蘭縣立羅東國中108學年度第一學期九年級數學科第二次段考試卷','printedSlot':{'year':108,'semester':1,'grade':9,'exam':2},'printedCounts':'填充題 18 題（共 20 格，其中第 5、7 題為單選）、綜合題 2 題。','visualReviewComplete':False,'reviewNote':'僅供續作，題圖、難度和部分公式尚未核對，禁止發布。','expectedTypes':{'choice':2,'fill':16,'written':2},'questions':qs}
out=Path('research/word-reference/drafts/yilan/ld-108-1-2-9.json');out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(draft,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(out)
