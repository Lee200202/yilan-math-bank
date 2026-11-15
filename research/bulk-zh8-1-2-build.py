from pathlib import Path
from html import escape
from collections import Counter
import hashlib,json
R=Path(__file__).resolve().parent
def tx(x,y,s,size=17):return f'<text x="{x}" y="{y}" font-size="{size}">{escape(s)}</text>'
def ln(x,y,u,v,dash=None):return f'<line x1="{x}" y1="{y}" x2="{u}" y2="{v}" stroke="#111" stroke-width="1.4"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>'
def pa(d,fill='none'):return f'<path d="{d}" fill="{fill}" stroke="#111" stroke-width="1.4"/>'
def SV(content,w=320,h=210):return {'type':'svg','svg':f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-12 -14 {w+24} {h+28}" role="img"><g fill="#111" font-family="serif" font-size="17" stroke-linecap="round" stroke-linejoin="round">{content}</g></svg>'}
def OPT(*a):return {'type':'options','items':list(a)}
def PTS(p,segs,offsets=None,w=320,h=220,extra=''):
 return SV(''.join(ln(*p[a],*p[b]) for a,b in segs)+''.join(tx(x+(offsets or {}).get(k,(-7,-10))[0],y+(offsets or {}).get(k,(-7,-10))[1],k) for k,(x,y) in p.items())+extra,w,h)
def start(pid,year):
 global PID,YEAR,SHA,C,T
 PID=pid;YEAR=year;SHA=hashlib.sha256((R.parent/'public/papers'/f'{pid}.pdf').read_bytes()).hexdigest();C=[];T=[]
def Q(kind,n,page,rect,level,*blocks,sub=None,section=None,issue=None,keyprefix=''):
 key=f'{kind}-'+(keyprefix+'-' if keyprefix else '')+f'{n}'+(f'-{sub}' if sub is not None else '')
 qid=f'zh-bulk-{PID}-{key}';num=str(n)+(f'({sub})' if sub is not None else '')
 sourceNumber=(f'{section}、' if section else '')+num
 meta={'id':qid,'paperId':PID,'sourceId':qid,'sourceNumber':sourceNumber,'parentNumber':n,'subnumber':sub,'sourceSha256':SHA,'page':page,'rect':rect,'type':kind,'number':num,'difficulty':level,'reviewed':True}
 typed={'id':qid,'sourceId':qid,'sourceNumber':sourceNumber,'parentNumber':n,'subnumber':sub,'blocks':[{'type':'text','text':b} if isinstance(b,str) else b for b in blocks],'sourceSha256':SHA,'verified':True}
 if issue:meta.update(usable=False,sourceIssue=issue);typed.update(usable=False,sourceIssue=issue)
 C.append(meta);T.append(typed)
def save(expected,types,evidence):
 assert len(C)==expected and dict(Counter(q['type'] for q in C))==types and len({q['id'] for q in C})==expected
 old_path=R/f'completeness-bulk-{PID}.json'
 old_proof=json.loads(old_path.read_text('utf8')) if old_path.exists() else {}
 (R/f'curated-bulk-{PID}.json').write_text(json.dumps(C,ensure_ascii=False,indent=2),'utf8')
 (R/f'transcribed-bulk-{PID}.json').write_text(json.dumps(T,ensure_ascii=False,indent=2),'utf8')
 proof={'paperId':PID,'sourcePrintedYear':YEAR,'sourceSha256':SHA,'expectedQuestions':expected,'expectedTypes':types,'actualQuestions':len(C),'actualTypes':dict(Counter(q['type'] for q in C)),'difficultyCounts':dict(Counter(q['difficulty'] for q in C)),'sourceMapping':[{'id':q['id'],'sourceNumber':q['sourceNumber'],'page':q['page'],'type':q['type'],'usable':q.get('usable',True)} for q in C],'evidence':evidence,'issues':[{'id':q['id'],'issue':q['sourceIssue']} for q in C if 'sourceIssue' in q]}
 proof['transcriptionSha256']=hashlib.sha256((R/f'transcribed-bulk-{PID}.json').read_bytes()).hexdigest()
 proof['visualReviewComplete']=bool(old_proof.get('visualReviewComplete') and old_proof.get('transcriptionSha256')==proof['transcriptionSha256'])
 if proof['visualReviewComplete']:
  for key in ['visualReviewEvidence','renderCheck','allIdsAndSourceHashesMatch']:
   if key in old_proof:proof[key]=old_proof[key]
 (R/f'completeness-bulk-{PID}.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2),'utf8');print(PID,len(C),types,flush=True)

start('1gzl-H9fya361mVJw816gQO8w80e7g3Sq',106)
for i,form,rect,lev in [
 (1,r'\dfrac12\sqrt3\times\dfrac13\sqrt{27}',[42,250,375,291],'easy'),
 (2,r'\sqrt{\dfrac25}\div\sqrt{\dfrac4{15}}',[42,317,375,359],'medium'),
 (3,r'(\sqrt{24}+\sqrt{96})(\sqrt3-\sqrt2)',[42,385,375,411],'medium'),
 (4,r'\dfrac32\sqrt{12}+\dfrac23\sqrt{72}-\dfrac{10}3\sqrt{2\dfrac14}-\dfrac72\sqrt{48}',[42,435,375,481],'hard'),
 (5,r'\dfrac4{\sqrt2+1}+(\sqrt6-\sqrt3)^2',[42,512,375,558],'medium')]:Q('fill',1,0,rect,lev,'計算下列各式：',f'${form}=$ ＿＿。',sub=i,section='一')
for i,form,rect,lev in [
 (1,r'4x^2-8x',[42,621,375,648],'easy'),
 (2,r'(x+1)(2x-1)-(x+1)(3x-4)',[42,651,375,703],'easy'),
 (3,r'(3x-2)-(3x-2)^2',[42,704,375,757],'easy'),
 (4,r'(ax^2-10)+(5x-2ax)',[42,758,375,812],'medium'),
 (5,r'(x+5)^2-(y-2)^2',[42,813,375,866],'easy'),
 (6,r'x^2+4x+4-25y^2',[42,868,375,921],'medium'),
 (7,r'(ax-bx)^2-(b-a)^3x',[42,922,375,976],'hard'),
 (8,r'x^4-625',[42,977,375,1004],'medium')]:Q('fill',2,0,rect,lev,f'因式分解 ${form}=$ ＿＿。',sub=i,section='一')
Q('fill',3,0,[389,158,733,185],'easy',r'若 $\sqrt{45}+\sqrt{20}=\sqrt a$，則 $a=$ ＿＿。',section='一')
Q('fill',4,0,[389,220,733,287],'medium',r'若 $x$、$12$、$13$ 為直角三角形的三邊長，則 $x=$ ＿＿。',section='一')
Q('fill',5,0,[389,334,733,402],'medium',r'設 $x-1$ 是 $5x^2-11x+a$ 的因式，也是 $x^2+bx-2$ 的因式，則 $a+b=$ ＿＿。',section='一')
Q('fill',6,0,[389,454,733,520],'easy',r'已知坐標平面上 $C(-1,1)$、$D(7,-9)$ 兩點，求 $\overline{CD}=$ ＿＿。',section='一')
Q('fill',7,0,[389,565,733,599],'medium',r'已知 $4x^2+12x+b^2$ 為完全平方式，則 $b=$ ＿＿。',section='一')
rect_be=PTS({'A':(40,87.69),'B':(40,180),'C':(300,180),'D':(300,87.69),'E':(78.46,87.69)},[('A','B'),('B','C'),('C','D'),('D','A'),('B','E'),('C','E')],{'A':(-19,-5),'B':(-19,13),'C':(5,13),'D':(5,-5),'E':(-3,-10)},335,215,pa('M75.3 95.1L82.7 98.2L85.8 90.8'))
Q('fill',8,0,[389,639,733,792],'medium',r'如圖，四邊形 $ABCD$ 是一個矩形，$\overline{BE}\perp\overline{CE}$，$\overline{BE}=5$，$\overline{CE}=12$，則矩形 $ABCD$ 的面積為＿＿平方公分。',rect_be,section='一')
Q('fill',9,0,[389,814,733,919],'easy',r'阿翰和黑人兩人在相同位置，若阿翰向西走 $3$ 單位，再向北走 $2$ 單位，黑人向東走 $4$ 單位，再向南走 $3$ 單位，則此時兩人距離為＿＿。',section='一')
box=PTS({'A':(85,35),'B':(50,65),'C':(260,65),'D':(295,35),'E':(85,135),'F':(50,165),'G':(260,165),'H':(295,135)},[('A','B'),('B','C'),('C','D'),('D','A'),('B','F'),('C','G'),('D','H'),('F','G'),('G','H')],{'A':(-5,-10),'B':(-18,0),'C':(-17,18),'D':(5,-8),'E':(0,-5),'F':(-17,15),'G':(0,18),'H':(5,3)},330,200,ln(85,35,85,135,'4 4')+ln(85,135,50,165,'4 4')+ln(85,135,295,135,'4 4'))
Q('written',1,1,[40,102,375,252],'medium',r'圖中為一長方體盒子，$\overline{AB}=4$，$\overline{BF}=4$，$\overline{FG}=12$，則＝？',box,section='三',issue='原卷實際渲染及文字層均只有「則＝？」；等號前要求的線段／數量缺漏，不能推定體對角線，暫停組卷。')
poly_ef=PTS({'A':(45,30),'B':(45,210),'C':(149,210),'D':(205,210),'E':(205,106),'F':(117.96,156.28)},[('A','B'),('B','D'),('D','E'),('E','A'),('A','C'),('E','F')],{'A':(-18,-8),'B':(-18,15),'C':(-5,20),'D':(4,15),'E':(4,-8),'F':(-16,5)},325,245,pa('M45 199H56V210M194 210V199H205M113.46 148.49L121.25 143.99L125.75 151.78'))
Q('written',2,1,[40,444,375,637],'hard',r'如圖，$\overline{AE}=5\sqrt2$，$\overline{AB}=4\sqrt3$，$\overline{BC}=\overline{DE}=4$，$\overline{EF}=5$，試計算 $\overline{CD}$ 長度？',poly_ef,section='三')
Q('written',3,1,[40,772,375,816],'medium',r'$3\sqrt2$ 的小數部分為 $a$，求 $a^2+\dfrac2a=$ ？',section='三')
Q('written',4,1,[389,77,733,132],'hard',r'已知 $a$、$b$ 皆不為 $0$，當 $ab=x$ 時，$a^2b-2a-2ab+4=0$，求 $x=$ ？',section='三')
Q('written',5,1,[389,422,733,477],'hard',r'直角三角形中，一股為 $\sqrt{71}$，另一股及斜邊皆為整數，則斜邊為何？',section='三')
save(25,{'fill':20,'written':5},['已實際開啟兩頁原卷PNG；填充1有5子題、填充2有8子題、填充3–9共7題；計算1–5共5題，總25個獨立作答單位。','原卷每格／題4分，25單位合100分，可交叉核對無漏題。','計算1原卷問項缺漏，保留研究記錄但usable=false。','全部共同命令複製入各子題；SVG保留矩形、長方體及EF幾何條件，不含raster。'])

start('1wkOiRZzblQh9zawh0rGg9lbtWdOQX-Kh',110)
Q('fill',1,0,[26,133,351,174],'easy',r'比較 $7\sqrt2$ 與 $3\sqrt{11}$ 的大小關係。答：$7\sqrt2$ ＿＿ $3\sqrt{11}$。',section='一')
Q('fill',2,0,[26,209,351,249],'easy',r'計算 $\sqrt{75}\div\sqrt3$，並將結果化為最簡根式。答：＿＿。',section='一')
Q('fill',3,0,[26,285,351,326],'easy',r'計算 $6\sqrt2-8\sqrt2+3\sqrt3$，並將結果化為最簡根式。答：＿＿。',section='一')
Q('fill',4,0,[26,361,351,402],'medium',r'計算 $(\sqrt5-\sqrt7)^2$，並將結果化為最簡根式。答：＿＿。',section='一')
Q('fill',5,0,[26,437,351,479],'easy',r'已知一直角三角形的兩股長分別為 $7$、$12$，求斜邊長 $=$ ＿＿。',section='一')
Q('fill',6,0,[26,514,351,547],'easy',r'將 $\sqrt{540}$ 化為最簡根式。答：＿＿。',section='一')
rod=SV(ln(40,215,245,215)+ln(245,215,245,20)+ln(100,215,245,20)+ln(110,231,245,231)+ln(110,226,110,236)+ln(245,226,245,236)+tx(159,253,'1.2')+tx(151,121,'2'),285,275)
Q('fill',7,0,[26,590,351,792],'easy',r'如圖，翰翰把長 $2$ 公尺的筆直竹竿放在離牆腳 $1.2$ 公尺處。則竹竿頂離地面多少公尺？答：＿＿公尺。',rod,section='一')
Q('fill',8,0,[26,799,351,934],'medium',r'已知 $6x^2+x-35=(2x+5)(3x-7)$，判別下列敘述哪些是正確的？答：＿＿。',OPT(r'$6x^2+x-35$ 是 $2x+5$ 的倍式。',r'$3x-7$ 是 $6x^2+x-35$ 的因式。',r'$3x-7$ 是 $2x+5$ 的倍式。',r'$2x+5$ 是 $3x-7$ 的因式。'),section='一')
Q('fill',9,0,[26,933,351,975],'easy',r'因式分解：$7x^2+6x=$ ＿＿。',section='一')
Q('fill',10,0,[382,113,709,144],'easy',r'將 $\sqrt{5.4}$ 化為最簡根式。答：＿＿。',section='一')
Q('fill',11,0,[382,209,709,290],'medium',r'已知 $\sqrt7\fallingdotseq2.6458$，$\sqrt{70}\fallingdotseq8.3666$，試計算 $\sqrt{700}$ 的近似值。答：＿＿。（以四捨五入法求到小數點後第一位）',section='一')
Q('fill',12,0,[382,361,709,422],'medium',r'計算 $\sqrt{128}-5\sqrt{64}+\sqrt{288}$，並將結果化為最簡根式。答：＿＿。',section='一')
Q('fill',13,0,[382,513,709,595],'medium',r'計算 $\dfrac6{\sqrt7-\sqrt5}+\dfrac3{\sqrt5}$，並將結果化為最簡根式。答：＿＿。',section='一')
routes=PTS({'A':(40,170),'C':(40,50),'B':(320,50),'D':(258.73,240.37)},[('A','C'),('C','B'),('B','D'),('D','A')],{'A':(-18,12),'C':(-18,-5),'B':(5,-5),'D':(0,22)},360,280,pa('M40 60H50V50M250.17 237.62L252.92 229.06L261.48 231.8')+tx(16,118,'6')+tx(173,38,'14')+tx(310,157,'10'))
Q('fill',14,0,[382,666,709,917],'medium',r'如圖，快遞業者將貨物從 $A$ 點送到 $B$ 點有兩條運輸路線可選擇，一條在轉運中心 $C$ 轉運，另一條在轉運中心 $D$ 轉運。已知貨物從轉運點出發後的路線，皆與原路線互相垂直，則貨物從 $A$ 點送到 $B$ 點，經過哪一點轉運的路徑總和較短？答：＿＿。',routes,section='一')
slide=PTS({'A':(91.47,94.12),'B':(35,200),'C':(290,200),'D':(91.47,200)},[('A','B'),('B','C'),('C','A'),('A','D')],{'A':(-5,-10),'B':(-17,13),'C':(5,13),'D':(-6,22)},325,235,pa('M91.47 190H101.47V200M86.76 102.94L95.59 107.65L100.29 98.82'))
Q('fill',15,1,[26,23,351,178],'medium',r'下圖是一個溜滑梯的側面圖，滑道與樓梯成直角，若 $\overline{AB}=8$、$\overline{BC}=17$。求溜滑梯的高 $\overline{AD}=$ ＿＿。',slide,section='一')
cup=SV(pa('M75 100V245C75 271 225 271 225 245V100')+'<ellipse cx="150" cy="100" rx="75" ry="18" fill="white" stroke="#111" stroke-width="1.4"/>'+pa('M75 245C75 219 225 219 225 245')+ln(100,3,225,245)+'<circle cx="150" cy="100" r="3"/>',275,290)
Q('fill',16,1,[26,232,351,472],'medium',r'實驗室有一個直圓柱體的杯子，上方杯蓋中央有一小孔，將一支長 $30$ 公分的玻棒從中央小孔插入杯中底部邊緣，杯子底圓半徑 $8$ 公分，高度 $15$ 公分。如圖，則玻棒露出杯口外的長度為多少公分？答：＿＿。',cup,section='一')
Q('fill',17,1,[26,480,351,522],'easy',r'已知坐標平面上 $A(6,7)$、$B(-5,4)$、$C(1,-4)$ 三點。求 $\overline{BC}$ 的長 $=$ ＿＿。',section='一')
for n,form,rect,lev in [(18,r'(2x+5)^2-16',[26,575,351,615],'easy'),(19,r'x^2+21x+54',[26,670,351,711],'easy'),(20,r'x^2-16x-57',[26,766,351,806],'medium'),(21,r'11x^2+16x-12',[26,861,351,902],'medium'),(22,r'12x^2+60x-72',[382,23,709,64],'medium'),(23,r'-20x^2+31x+9',[382,137,709,179],'hard')]:Q('fill',n,1,rect,lev,f'因式分解：${form}=$ ＿＿。',section='一')
roof=SV(pa('M30 180V90L130 45L230 90V180ZM38 90V180M222 90V180M82 180V115H178V180')+ln(30,25,130,25)+ln(30,20,30,30)+ln(130,20,130,30)+tx(74,17,'2')+ln(16,45,16,90)+tx(-7,72,'1.5')+ln(30,194,230,194)+''.join(ln(x,189,x,199) for x in [30,38,82,178,222,230])+tx(45,220,'1.5')+tx(124,220,'2')+tx(187,220,'1.5')+tx(95,246,'正面圖')+pa('M290 45H505V180H290ZM290 90H505M324 113H376V140H324Z')+ln(290,194,505,194)+ln(290,189,290,199)+ln(505,189,505,199)+tx(389,220,'12')+ln(519,90,519,180)+ln(514,90,524,90)+ln(514,180,524,180)+tx(527,142,'4')+ln(519,45,519,90)+ln(514,45,524,45)+tx(378,246,'側面圖'),555,265)
Q('fill',24,1,[382,251,709,635],'medium',r'下圖是德浩家的房子設計圖，屋頂是由兩個完全相同的長方形組成，正面圖和側面圖中的尺寸是以公尺為單位，求屋頂的總面積 $=$ ＿＿平方公尺。',roof,section='一')
diagonal=SV(pa('M50 80H230V190H50ZM50 80L100 30H280L230 80M230 190L280 140V30')+ln(100,30,100,140,'4 4')+ln(100,140,50,190,'4 4')+ln(100,140,280,140,'4 4')+ln(50,190,280,30,'4 4')+tx(132,215,'a')+tx(268,185,'b')+tx(290,90,'c')+tx(157,108,'m'),320,230)
Q('fill',25,1,[382,651,709,979],'medium','長方體對角線長度：',r'設長方體的長、寬、高分別是 $a$、$b$、$c$，其對角線長度 $m$ 可用以下公式計算：$m=\sqrt{a^2+b^2+c^2}$。',diagonal,r'哈利波特想要利用郵局寄送一支長 $40$ 公分的魔杖給榮恩，請問他至少要花多少錢買郵局的瓦楞方型紙箱？答：＿＿元。','郵局供售瓦楞方型紙箱售價詳情表',{'type':'table','rows':[['','規格（cm）','售價（元）'],['大型',r'$40\times30\times40$','$45$'],['中型',r'$20\times20\times30$','$30$'],['小型',r'$20\times10\times20$','$20$']],'header':True},section='一')
save(25,{'fill':25},['已實際開啟原卷兩頁與屋頂放大圖；本卷只有一、填充題1–25，全部25題均有對應，無選擇或非選。','第8題A–D為原填充題中的判斷材料，維持fill不偽裝choice。','屋頂圖保留原尺寸2、1.5、1.5/2/1.5、側12與4，不以外觀比例推改原數值；方箱表三規格三售價全保留。','全部7幅必要數學圖純SVG，不複製裝飾人物／建物照片。'])

# The provided catalog calls this 109; the actual source heading unmistakably prints 108.
start('1ZZUkKjnXYPQn5CwCnQPqN9ayYj__D6wS',108)
Q('fill',1,0,[26,132,351,175],'easy',r'計算：$\dfrac{\sqrt{35}}{\sqrt{12}}\div\dfrac{\sqrt7}{\sqrt3}=$ ＿＿。',section='一')
Q('fill',2,0,[26,257,351,308],'easy','下列哪些是最簡根式？答：＿＿。',OPT(r'$\sqrt{2.7}$',r'$\sqrt{18}$',r'$\sqrt1$',r'$\sqrt2$'),section='一')
Q('fill',3,0,[26,374,351,395],'easy',r'計算：$2\sqrt{12}+\sqrt{18}-\sqrt{27}+\sqrt{32}+\sqrt{50}=$ ＿＿。',section='一')
Q('fill',4,0,[26,489,351,510],'medium',r'化簡：$(-6\sqrt3+\sqrt{15})\div\sqrt6=$ ＿＿。',section='一')
Q('fill',5,0,[26,571,351,612],'medium',r'將 $\dfrac{16}{\sqrt{24}+4}$ 化為最簡根式 $=$ ＿＿。',section='一')
Q('fill',6,0,[26,696,351,765],'medium',r'$\triangle ABC$ 中，$\angle B=90^\circ$，以三邊為邊長分別向外作出正方形甲、乙、丙，已知甲、乙的面積分別為 $9$、$16$，則丙的面積 $=$ ＿＿。',section='一')
Q('fill',7,0,[26,850,351,912],'medium',r'在直角三角形 $ABC$ 中，$\angle ABC$ 為直角，且 $\overline{AB}=10$、$\overline{BC}=24$，若 $\overline{BD}$ 為斜邊上的高，則 $\overline{BD}=$ ＿＿。',section='一')
Q('fill',8,0,[382,108,710,168],'easy',r'若 $A(16,14)$、$B(13,7)$ 為直角坐標平面上的兩點，則 $\overline{AB}=$ ＿＿。',section='一')
Q('fill',9,0,[382,257,710,308],'medium',r'已知多項式 $6x^2+mx+6$ 可因式分解成 $(2x+3)(3x+n)$，則 $m=$ ＿＿。',section='一')
Q('fill',10,0,[382,393,710,516],'medium',r'已知 $P$、$Q$ 兩個多項式，其中 $P=(x+5)(2x-3)$、$Q=(5x+1)(3-2x)$，則下列選項何者是 $P$ 和 $Q$ 的公因式？答：＿＿。',OPT(r'$x+5$',r'$2x-3$',r'$3-x$',r'$6x+6$'),section='一')
for n,form,rect,lev in [(11,r'2(3x-1)(7x+3)+7(7x+3)',[382,546,710,591],'easy'),(12,r'(3x-2)(x+5)+(2-3x)^2',[382,678,710,726],'medium'),(13,r'x^2-25',[382,817,710,841],'easy'),(14,r'9x^2-42x+49',[382,932,710,956],'easy'),(15,r'x^2-20x+36',[26,35,351,57],'easy'),(16,r'x^2+34x-35',[26,149,351,173],'easy'),(17,r'6x^2-7x-20',[26,239,351,263],'medium')]:Q('fill',n,0 if n<=14 else 1,rect,lev,f'因式分解：${form}=$ ＿＿。',section='一')
Q('fill',18,1,[26,379,351,426],'medium',r'有一個三角形的面積是 $15x^2+14x-8$，若底邊長為 $6x+8$，則高 $=$ ＿＿。',section='一')
Q('fill',19,1,[26,510,351,596],'hard',r'將 $18$ 片紙板（$2$ 片邊長為 $x$ 公分的正方形，$11$ 片長寬各為 $x$ 公分、$1$ 公分的長方形以及 $5$ 片邊長為 $1$ 公分的正方形）拼成一個長方形，則此長方形的周長 $=$ ＿＿。',section='一')
Q('fill',20,1,[26,658,351,707],'hard',r'設 $x-1$ 及 $3x-2$ 都是 $6x^3+ax^2-x+b$ 的因式，則 $a+5b=$ ＿＿。',section='一')
tiles=SV(''.join(pa(f'M{30+i*55} 105L{57.5+i*55} 57.3686L{85+i*55} 105V160H{30+i*55}Z') for i in range(4))+ln(30,105,250,105),280,190)
Q('fill',21,1,[26,834,351,978],'medium',r'如圖，此圖形的上半部是 $4$ 個正三角形，下半部是 $4$ 個正方形。若此圖形的面積為 $9\sqrt3+36$，則正方形的邊長 $=$ ＿＿。',tiles,section='一')
coords=PTS({'A':(70,150),'B':(120,270),'C':(240,220),'D':(190,100),'O':(70,270)},[('A','B'),('B','C'),('C','D'),('D','A')],{'A':(-23,5),'B':(-3,23),'C':(8,4),'D':(5,-9),'O':(-24,20)},295,305,ln(20,270,275,270)+pa('M275 270L266 265L266 275Z','#111')+ln(70,305,70,55)+pa('M70 55L65 64L75 64Z','#111')+tx(279,293,'x')+tx(49,56,'y'))
Q('fill',22,1,[382,35,710,250],'medium',r'如圖，已知四邊形 $ABCD$ 為一正方形，且 $A$、$B$ 兩點的坐標分別是 $(0,12)$ 和 $(5,0)$，則 $D$ 點坐標 $=$ ＿＿。',coords,section='一')
Q('fill',23,1,[382,315,710,405],'medium',r'長方形 $ABCD$ 內部有一點 $P$，其中 $\overline{PA}=5$、$\overline{PB}=6$、$\overline{PC}=7$，則 $\overline{PD}=$ ＿＿。',section='一')
alt_cd=PTS({'A':(220,102.857),'B':(253.061,180),'C':(40,180),'D':(220,180)},[('A','B'),('B','C'),('C','A'),('A','D')],{'A':(-7,-10),'B':(6,13),'C':(-20,13),'D':(-7,23)},295,215,pa('M220 171H229V180M211.73 106.40L215.27 114.67L223.54 111.13'))
Q('fill',24,1,[382,511,710,660],'medium',r'如圖，$\angle BAC$ 為直角，$\overline{AD}\perp\overline{BC}$，若 $\overline{CD}=7$，$\overline{AD}=3$，求 $\overline{DB}=$ ＿＿。',alt_cd,section='一')
Q('fill',25,1,[382,767,710,830],'hard',r'計算：$\left(1-\dfrac1{2^2}\right)\left(1-\dfrac1{3^2}\right)\left(1-\dfrac1{4^2}\right)\cdots\left(1-\dfrac1{2020^2}\right)=$ ＿＿。',section='一')
for q in C+T:q.update(sourcePrintedYear=108,catalogYearMismatch=True)
save(25,{'fill':25},['原卷兩頁標題明確為一○八學年度；指定清單稱109，需root修正年度metadata。','實際逐頁看過原卷，全卷一、填充題1–25，每題4分，共100分，25筆完整對應。','第2與10題原屬填充並附選項，維持fill。第6題原卷未附甲乙丙對應圖，照原文保留，不自行推定哪個正方形在斜邊。','三張必要圖（四正三角形＋四正方形、坐標正方形、直角三角形高）純SVG，無raster。'])

start('1OrqDrOOZikadJZffgkGupUsqpNDUZ64X',112)
Q('choice',1,0,[40,217,374,319],'easy','下列何者為最簡根式？',OPT(r'$\sqrt5$',r'$\sqrt{0.5}$',r'$5\sqrt{12}$',r'$\sqrt{\dfrac35}$'),section='一')
Q('choice',2,0,[40,343,374,426],'easy',r'下列何者是 $x^2+11x+24$ 與 $x^2-9$ 的公因式？',OPT(r'$x+8$',r'$x-8$',r'$x+3$',r'$x-3$'),section='一')
Q('choice',3,0,[40,453,374,574],'medium',r'若 $6$、$8$、$x$ 是直角三角形的三邊長，則 $x$ 可能是下列何者？',r'（甲）$10$；（乙）$2\sqrt7$；（丙）$\sqrt{14}$；（丁）$14$。',OPT('僅甲','僅甲、乙','僅甲、乙、丙','甲、乙、丙、丁都是'),section='一')
Q('choice',4,0,[40,600,374,704],'easy',r'已知 $6x^2+5x-6=(3x-2)(2x+3)$，則下列哪個不是 $6x^2+5x-6$ 的因式？',OPT(r'$-3x+2$',r'$2x-3$',r'$2x+3$',r'$(3x-2)(2x+3)$'),section='一')
Q('choice',5,0,[40,726,374,841],'medium',r'若 $100x^2-70x-8=(20x+a)(bx+c)$，其中 $a$、$b$、$c$ 均為整數，則下列敘述何者錯誤？',OPT(r'$b$ 是 $100$ 的因數。',r'$8$ 是 $c$ 的倍數。',r'$a$、$c$ 是同號數。',r'$ab>20c$'),section='一')
for n,form,pg,rect,lev in [(1,r'-\sqrt3+7\sqrt5+4\sqrt3-2\sqrt5',0,[40,883,374,916],'easy'),(2,r'5\sqrt3\times(-4\sqrt2)',0,[40,962,374,995],'easy'),(3,r'\sqrt{\dfrac{25}6}\div\sqrt{\dfrac5{18}}',0,[389,126,734,163],'easy')]:Q('fill',n,pg,rect,lev,f'計算 ${form}=$ ＿＿。',section='二',keyprefix='basic')
tri7=PTS({'A':(59.6,132.8),'B':(40,200),'C':(290,200)},[('A','B'),('B','C'),('C','A')],{'A':(-5,-10),'B':(-18,13),'C':(5,13)},325,235,pa('M57.08 141.44L65.72 143.96L68.24 135.32')+tx(21,166,'7')+tx(150,222,'25'))
Q('fill',4,0,[389,215,734,312],'easy',r'如圖，直角三角形 $ABC$ 中一股 $\overline{AC}$ 的長度 $=$ ＿＿。',tri7,section='二',keyprefix='basic')
Q('fill',5,0,[389,337,734,358],'easy',r'直角坐標平面上有 $A(-1,3)$、$B(2,7)$，則 $\overline{AB}=$ ＿＿。',section='二',keyprefix='basic')
for n,form,rect,lev in [(6,r'3x^2+9x',[389,412,734,434],'easy'),(7,r'(x-5)^2+(x-5)',[389,486,734,508],'easy'),(8,r'x^2-16x+64',[389,559,734,581],'easy'),(9,r'x^2-9x+14',[389,634,734,656],'easy'),(10,r'2x^2-3x-5',[389,708,734,730],'medium')]:Q('fill',n,0,rect,lev,f'因式分解 ${form}=$ ＿＿。',section='二',keyprefix='basic')
Q('fill',1,0,[389,813,734,837],'medium',r'計算 $(1+\sqrt{12})(\sqrt6-\sqrt2)+\sqrt8=$ ＿＿。',section='三')
Q('fill',2,0,[389,912,734,936],'medium',r'計算 $(\sqrt{99}+\sqrt{98})^{99}\times(\sqrt{99}-\sqrt{98})^{98}=$ ＿＿。',section='三')
Q('fill',3,1,[40,58,374,100],'medium',r'已知正六邊形 $ABCDEF$ 中，$\overline{AB}=10$，則此正六邊形面積為＿＿。',section='三')
Q('fill',4,1,[40,175,374,220],'medium',r'已知等腰三角形 $ABC$，$\overline{AB}=\overline{AC}=15$，$\overline{BC}=18$，若 $D$ 點在 $\overline{AC}$ 上，且 $\overline{BD}$ 垂直 $\overline{AC}$，則 $\overline{BD}=$ ＿＿。',section='三')
for n,form,rect,lev in [(5,r'(x-6)^2-3x+18',[40,294,374,316],'medium'),(6,r'34-90x-36x^2',[40,386,374,408],'medium'),(7,r'3(x-5)^2-5(x-5)-28',[40,455,374,477],'hard'),(8,r'(x-2)(x+5)+(x+1)(2x+11)-(2-x)(x+6)',[40,568,374,638],'hard')]:Q('fill',n,1,rect,lev,f'因式分解 ${form}=$ ＿＿。',section='三')
quad_ce=PTS({'A':(300,180),'B':(330.46,128.31),'C':(261.54,87.69),'D':(40,180),'E':(261.54,180)},[('A','B'),('B','C'),('C','D'),('D','A'),('C','E')],{'A':(4,13),'B':(5,-5),'C':(-5,-10),'D':(-18,13),'E':(-5,23)},365,225,pa('M325.89 136.06L318.14 131.49L322.71 123.74M261.54 171H270.54V180'))
Q('fill',9,1,[40,710,374,877],'medium',r'如圖，$\angle B=90^\circ$，$\overline{CE}$ 垂直 $\overline{AD}$，若 $\overline{AB}=6$，$\overline{BC}=8$，$\overline{CD}=24$，$\overline{AD}=26$，則 $\overline{CE}=$ ＿＿。',quad_ce,section='三')
Q('fill',10,1,[40,904,374,950],'medium',r'若 $\sqrt{10}$ 的整數部分為 $a$，小數部分為 $b$，則 $\dfrac{a}{b+2}=$ ＿＿。',section='三')
lune=SV(pa('M50 190A78 78 0 0 1 143.6 65.2A130 130 0 0 0 50 190Z','#bbb')+pa('M143.6 65.2A104 104 0 0 1 310 190A130 130 0 0 0 143.6 65.2Z','#bbb')+pa('M50 190A130 130 0 0 1 310 190')+ln(50,190,143.6,65.2)+ln(143.6,65.2,310,190)+ln(50,190,310,190)+pa('M138.2 72.4L145.4 77.8L150.8 70.6')+tx(138,54,'A')+tx(34,210,'B')+tx(315,210,'C'),350,235)
Q('written',1,1,[389,111,734,274],'hard',r'如圖，$\overline{AB}=12$、$\overline{BC}=20$，且分別以此三角形的三個邊為直徑畫半圓，求灰色部分面積。',lune,section='四')
Q('written',2,1,[389,464,734,512],'hard',r'計算 $\dfrac{(2023^2+2021)(2023^2+4046-8)\times2030}{2021\times2022\times2025\times2027}=$ ？',section='四')
save(27,{'choice':5,'fill':20,'written':2},['已實際開啟兩頁原卷；一、選擇1–5共5題，二、基礎1–10共10題，三、填充1–10共10題，四、計算1–2共2題，總27題全部對應。','配分20+30+40+10=100提供獨立完整性校對；重複題號以section及keyprefix區分。','文字層大量公式缺失，所有根式、多項式、等式與選項均按實際頁面影像人工轉寫。','必要圖：7/25直角三角形、CE高四邊形、三半圓灰色月牙，純SVG；月牙完整保留A點直角與兩塊灰色區域。'])

start('1rJYbUevjpu3lIsrQ5XYu8NUfzeMClxy5',113)
for i,form,rect,lev in [(1,r'\sqrt{2^4\times3^3}',[58,302,208,330],'easy'),(2,r'\sqrt{56}',[215,302,370,330],'easy'),(3,r'\sqrt{0.6}',[58,340,208,371],'easy'),(4,r'\dfrac1{\sqrt7+\sqrt5}',[215,338,370,373],'medium')]:Q('fill',1,0,rect,lev,f'將 ${form}$ 化為最簡根式：＿＿。',sub=i,section='第一部分',keyprefix='basic')
quad_cd=PTS({'A':(80,40),'B':(46.4,65.2),'C':(132.8,180.4),'D':(166.4,65.344)},[('A','B'),('B','C'),('C','D'),('D','A')],{'A':(-7,-10),'B':(-22,5),'C':(-6,22),'D':(6,5)},205,215,pa('M53.6 59.8L59 67L51.8 72.4M157.77 62.81L155.25 71.44L163.88 73.97'))
Q('fill',2,0,[40,412,374,534],'medium',r'四邊形 $ABCD$ 中，$\overline{AB}=7$，$\overline{BC}=24$，$\overline{AD}=15$，且 $\overline{AB}\perp\overline{BC}$，$\overline{AD}\perp\overline{CD}$，則 $\overline{CD}=$ ＿＿。',quad_cd,section='第一部分',keyprefix='basic')
Q('fill',3,0,[40,531,374,579],'easy',r'已知坐標平面上有 $A(9,1)$、$B(4,13)$ 兩點，則 $\overline{AB}=$ ＿＿。',section='第一部分',keyprefix='basic')
for i,form,rect,lev in [(1,r'x^2+7x+6',[58,601,374,626],'easy'),(2,r'4x^2+6x',[58,625,374,650],'easy'),(3,r'9x^2-24x+16',[58,649,374,674],'easy'),(4,r'18x^2-32',[58,673,374,699],'easy')]:Q('fill',4,0,rect,lev,f'因式分解 ${form}=$ ＿＿。',sub=i,section='第一部分',keyprefix='basic')
Q('fill',5,0,[40,699,374,766],'easy','下列敘述何者錯誤？答：＿＿。',OPT(r'$\sqrt8+\sqrt2=\sqrt{10}$',r'$\sqrt8-\sqrt2=\sqrt2$',r'$\sqrt8\times\sqrt2=\sqrt{16}$',r'$\sqrt8\div\sqrt2=\sqrt4$'),section='第一部分',keyprefix='basic')
tri_x=PTS({'A':(195,80),'B':(35,200),'C':(285,200)},[('A','B'),('B','C'),('C','A')],{'A':(-5,-10),'B':(-18,13),'C':(5,13)},325,235,ln(195,80,195,200)+pa('M187.8 85.4L193.2 92.6L200.4 87.2M195 191H204V200')+tx(93,129,'20')+tx(249,141,'15')+tx(201,151,'x'))
Q('fill',6,0,[40,765,374,856],'medium',r'$\triangle ACB$ 為直角三角形，$\angle BAC=90^\circ$，$x=$ ＿＿。',tri_x,section='第一部分',keyprefix='basic')
square70=PTS({'A':(160,230),'B':(250,110),'C':(250,230)},[('A','B'),('B','C'),('C','A')],{'A':(-10,22),'B':(5,-4),'C':(6,18)},295,265,pa('M160 230L40 140L130 20L250 110')+pa('M250 220H240V230')+tx(133,136,'70')+tx(265,175,'a')+tx(200,253,'b'))
Q('fill',7,0,[40,856,374,995],'easy',r'$\triangle ACB$ 為直角三角形，$\angle C=90^\circ$，$\overline{BC}=a$，$\overline{AC}=b$，若以 $\overline{AB}$ 為邊的正方形面積為 $70$ 平方單位，則 $a^2+b^2=$ ＿＿。',square70,section='第一部分',keyprefix='basic')
Q('fill',8,0,[389,149,734,252],'easy',r'已知多項式 $x^2-4x-5=(x+1)(x-5)$，請判別下列選項何者不是 $x^2-4x-5$ 的因式？答：＿＿。',OPT(r'$x^2-4x-5$',r'$2x+2$',r'$(x-1)(x+5)$',r'$-x+5$'),section='第一部分',keyprefix='basic')
Q('fill',1,0,[389,312,734,363],'medium',r'已知 $18x^2-17x-a$ 可以因式分解為 $(2x-b)(cx+5)$，其中 $a$、$b$、$c$ 都是正整數，則 $a=$ ＿＿。',section='第二部分')
tri_ade=PTS({'A':(141.538,47.692),'B':(40,220),'C':(280,220),'D':(280,120),'E':(187.692,158.462)},[('A','B'),('B','C'),('C','D'),('D','A'),('B','D'),('A','E')],{'A':(-6,-10),'B':(-20,14),'C':(5,14),'D':(5,-2),'E':(-5,22)},325,255,pa('M270 220V210H280M184.23 150.15L192.54 146.69L196 155'))
Q('fill',2,0,[389,410,734,559],'medium',r'已知 $\angle C=90^\circ$，$\overline{AE}\perp\overline{BD}$，且 $\overline{BC}=24$，$\overline{DC}=10$，$\overline{AB}=20$，$\overline{DE}=10$，則 $\overline{AD}=$ ＿＿。',tri_ade,section='第二部分')
crosswork=SV(tx(25,35,'ax')+tx(25,83,'4x')+tx(155,35,'＋(a－10)')+tx(155,83,'＋3')+ln(80,40,145,74)+ln(80,75,145,40)+ln(15,96,285,96),310,115)
Q('fill',3,0,[389,568,734,687],'medium',r'下圖是用十字交乘法因式分解 $12x^2+px+q$ 的部分過程，請問下列何者正確？答：＿＿。',crosswork,OPT(r'$a=-3$',r'$q=21$',r'$p=-37$',r'$p=-19$'),section='第二部分')
Q('fill',4,0,[389,688,734,734],'medium',r'面積為 $12$ 的等腰直角三角形，其斜邊上的高 $=$ ＿＿。',section='第二部分')
for i,form,pg,rect,lev in [(1,r'(3\sqrt2-\sqrt3)\div\sqrt6',0,[405,842,734,869],'medium'),(2,r'\sqrt{32}-\sqrt{27}-\sqrt{18}+\sqrt{75}',0,[405,938,734,965],'medium'),(3,r'\dfrac{\sqrt5}{\sqrt6}\div\dfrac{\sqrt8}{\sqrt9}\times\sqrt{\dfrac54}\div\dfrac{\sqrt3}{\sqrt5}',1,[58,57,374,94],'hard'),(4,r'(2\sqrt3+\sqrt2)(3\sqrt2-\sqrt{12})',1,[58,225,374,253],'medium'),(5,r'\left(3\sqrt{5\dfrac13}+\sqrt6\right)^2-\dfrac6{\sqrt{12}}+\dfrac4{1-\sqrt3}',1,[58,402,374,439],'hard')]:Q('fill',5,pg,rect,lev,f'計算下列各式的值：${form}=$ ＿＿。',sub=i,section='第二部分')
for i,form,rect,lev in [(1,r'5x^2-x-18',[58,625,374,653],'medium'),(2,r'(2x-3)^2+(3-2x)',[58,745,374,773],'medium'),(3,r'(3x+2)(x-1)-(x-2)^2+7',[58,865,374,893],'hard'),(4,r'-8(x+1)^2+40(x^2-1)-50(x-1)^2',[405,55,734,84],'hard')]:Q('fill',6,1,rect,lev,f'因式分解 ${form}=$ ＿＿。',sub=i,section='第二部分')
Q('fill',7,1,[389,269,734,405],'medium',r'小潁打算從家裡騎自行車前往運動公園與同學一起練習英文歌唱比賽的編舞動作。她先向東行駛 $240$ 公尺，然後向北行駛 $280$ 公尺，再向西行駛 $80$ 公尺，暫停在飲料店領取大家預訂的飲料後，再出發向北行駛 $320$ 公尺，然後向東行駛 $160$ 公尺才到達運動公園。請算出小潁家與運動公園的直線距離是＿＿公尺。',section='第二部分')
Q('fill',8,1,[389,625,734,672],'medium',r'設 $2\sqrt5=a+b$，且 $a$ 為整數部分的值，$b$ 為純小數部分的值，則 $2b^2+8b-5$ 的值 $=$ ＿＿。',section='第二部分')
save(29,{'fill':29},['已實際開啟全卷兩頁及混合根式5(5)放大圖；第一部分共14個獨立作答單位：1拆4、2/3各1、4拆4、5–8各1。','第二部分共15個單位：1–4各1、5拆5、6拆4、7/8各1；全卷總29筆，42+60=102分與原卷滿分102一致。','原卷兩部分全屬填充，含A–D的第一部分5/8與第二部分3維持fill。','所有子題有完整共同命令；5(5)實為係數3乘√(5又1/3)，平方涵蓋該項加√6，未把3誤作三次根。','五幅必要圖（雙直角四邊形、高x、面積70正方形、AE高與十字交乘）純SVG；原題中給定的因式分解過程／判斷材料完整保留。'])

start('1LvTTxqYjttEKwStLNgl83N1IGvY75Imd',114)
for i,form,rect,lev in [(1,r'(-2)\times3\sqrt5',[111,225,410,249],'easy'),(2,r'\sqrt5+\sqrt5\times\sqrt5\div\dfrac1{\sqrt5}',[111,252,410,295],'medium'),(3,r'\sqrt6\div\dfrac57',[111,290,410,331],'easy'),(4,r'(-12\sqrt6)\div(8\sqrt3)',[111,333,410,357],'easy')]:Q('fill',1,0,rect,lev,f'計算下列各式的值：${form}=$ ＿＿。',sub=i,section='一',keyprefix='basic')
for i,form,rect,lev in [(1,r'\sqrt8',[111,459,410,483],'easy'),(2,r'\dfrac3{\sqrt{32}}',[111,486,410,529],'easy'),(3,r'\sqrt{27}\times\sqrt{\dfrac1{81}}',[111,528,410,564],'easy'),(4,r'\sqrt{0.125}',[111,567,410,592],'easy')]:Q('fill',2,0,rect,lev,f'將 ${form}$ 化成最簡根式：＿＿。',sub=i,section='一',keyprefix='basic')
Q('fill',1,0,[88,693,414,774],'easy',r'選出 $\sqrt6$ 的同類方根。答：＿＿。',OPT(r'$\sqrt{12}$',r'$\sqrt{24}$',r'$\sqrt{16}$',r'$\sqrt{\dfrac23}$'),section='二')
for i,form,rect,lev in [(1,r'(-3\sqrt6+\sqrt{15})\div\sqrt3',[111,873,414,898],'medium'),(2,r'(2+\sqrt3)^4(2-\sqrt3)^5',[111,909,414,934],'medium'),(3,r'\dfrac{2025^3+4\times2025^2+6075}{2025^2+2025}',[111,943,414,989],'hard'),(4,r'\dfrac1{\sqrt7+\sqrt9}+\dfrac1{\sqrt9+\sqrt{11}}+\dfrac1{\sqrt{11}+\sqrt{13}}+\dfrac1{\sqrt{13}+\sqrt{15}}',[111,989,414,1055],'hard')]:Q('fill',2,0,rect,lev,f'化簡下列各式：${form}=$ ＿＿。',sub=i,section='二')
rotation=PTS({'O':(50,180),'A':(75,180),'B':(175,180),'C':(175,55)},[('A','B'),('B','C'),('C','A')],{'O':(-20,19),'A':(-7,22),'B':(-5,22),'C':(6,-2)},230,225,ln(20,180,220,180)+pa('M220 180L211 175L211 185Z','#111')+ln(50,215,50,20)+pa('M50 20L45 29L55 29Z','#111')+tx(221,200,'x')+tx(31,19,'y')+pa('M161 58Q154 29 120 30M120 30L128 24M120 30L128 35'))
Q('fill',3,0,[429,163,759,357],'medium',r'如圖，作標平面上有一個 $\triangle ABC$，其中 $A$、$B$、$C$ 三點的座標分別為 $(1,0)$、$(5,0)$、$(5,5)$，若固定 $A$ 點，將 $\triangle ABC$ 依逆時針方向旋轉，使得 $\overline{AC}$ 落在 $x$ 軸上，可得一新 $\triangle AB^\prime C^\prime$，其中 $C^\prime$ 點的座標為 $(a,0)$，且 $a<0$，則 $a$ 值落在哪兩個整數之間？',rotation,section='二')
Q('fill',4,0,[429,380,759,420],'hard',r'已知甲為質數，且甲 $=3a^2-10a-48$，其中 $a$ 為正整數，求甲數 $=$ ＿＿。',section='二')
for i,form,rect,lev in [(1,r'48+8x-x^2',[453,542,759,565],'medium'),(2,r'(3x+2)^2(x-3)-(3x+2)(x-3)^2',[453,563,759,587],'medium'),(3,r'4x^2-25+3(5-2x)',[453,583,759,606],'medium'),(4,r'3x^2+x',[453,603,759,628],'easy')]:Q('fill',5,0,rect,lev,f'因式分解 ${form}=$ ＿＿。',sub=i,section='二')
overlap=PTS({'A':(40,60),'B':(40,180),'C':(120,180),'D':(120,60)},[('A','B'),('B','C'),('C','D'),('D','A')],{'A':(-20,-3),'B':(-20,6),'C':(5,17),'D':(5,17)},280,285,pa('M40 180V260H120V180M120 60H240V180H120')+ln(40,180,120,60,'4 4')+tx(67,229,'甲')+tx(172,126,'乙'))
shared=r'如圖，將兩張長方形紙片疊合後，甲、乙均為正方形。若 $\overline{BD}=\sqrt{140}\,cm$，長方形 $ABCD$ 的周長為 $32\,cm$，則：'
Q('fill',6,0,[429,693,759,884],'medium',shared,overlap,'甲、乙的面積和為＿＿。',sub=1,section='二')
Q('fill',6,0,[429,693,759,884],'medium',shared,overlap,r'長方形 $ABCD$ 的面積 $=$ ＿＿。',sub=2,section='二')
Q('fill',7,0,[429,905,759,984],'hard',r'已知一正方形 $PQRS$ 紙張，先將 $P$ 對折到 $R$，再將 $Q$ 對折到 $S$，若得到的三角形周長為 $4+4\sqrt2$，則正方形 $PQRS$ 的面積為＿＿平方公分。',section='二')
squares_diff=PTS({'A':(90,30),'B':(90,105),'C':(171.3225,143.37),'D':(225,30)},[('A','B'),('B','C'),('C','D'),('D','A')],{'A':(-18,-6),'B':(-4,22),'C':(4,22),'D':(-4,-10)},380,235,pa('M90 30H15V105H90M171.3225 143.37L284.6925 197.0475L338.37 83.6775L225 30M90 39H99V30M163.18 139.53L167.03 131.39L175.17 135.23')+tx(42,74,'甲')+tx(275,105,'乙'))
Q('fill',8,1,[88,90,414,232],'medium',r'如圖，四邊形 $ABCD$ 中，已知 $\angle A=\angle C=90^\circ$，$\overline{AD}=9$，$\overline{BC}=6$，分別以 $\overline{AB}$ 和 $\overline{CD}$ 為邊作正方形甲、乙，則甲乙面積之差為＿＿。',squares_diff,section='二')
fold=PTS({'A':(240,40),'B':(240,280),'C':(0,280),'D':(120,280),'E':(240,190),'F':(140,140)},[('A','C'),('B','C'),('E','B'),('F','E'),('F','D'),('D','E')],{'A':(-18,-5),'B':(5,13),'C':(-8,21),'D':(-6,23),'E':(5,0),'F':(-20,-1)},285,315,ln(240,40,240,190,'4 4')+pa('M230 280V270H240M230 90Q277 140 231 185M231 185L239 181M231 185L230 176'))
Q('written',1,1,[88,817,414,967],'hard',r'將一等腰直角三角形的紙張折成圖，使 $A$ 點與 $\overline{BC}$ 的中點 $D$ 重合。已知 $\angle B=90^\circ$，$\overline{AB}=\overline{BC}=12$，則 $\overline{BE}=$ ？',fold,section='三')
two_squares=PTS({'O':(150,180),'A':(208,60),'B':(328,118),'C':(270,238),'D':(92,140),'E':(52,198),'F':(110,238)},[('O','A'),('A','B'),('B','C'),('C','O'),('O','D'),('D','E'),('E','F'),('F','O')],{'O':(-32,-5),'A':(-5,-10),'B':(6,0),'C':(5,18),'D':(-17,-3),'E':(-20,5),'F':(-8,22)},375,285,ln(20,180,360,180)+pa('M360 180L351 175L351 185Z','#111')+ln(150,275,150,20)+pa('M150 20L145 29L155 29Z','#111')+tx(362,200,'x')+tx(131,19,'y'))
Q('written',2,1,[429,90,759,268],'hard',r'如圖，座標平面上，四邊形 $OABC$、$ODEF$ 為正方形。若 $A$、$F$ 兩點座標分別為 $(58,120)$、$(-40,-58)$，則正方形 $OABC$ 與正方形 $ODEF$ 的面積相差多少？',two_squares,section='三')
Q('written',3,1,[429,614,759,690],'hard',r'已知座標平面上有相異三點 $P(x,y)$、$Q(2,7)$、$R(-1,3)$，若 $\overline{PQ}\perp\overline{QR}$ 於 $Q$ 點，且 $\sqrt{(x+1)^2+(y-3)^2}=13$，求 $\overline{PQ}=$ ？',section='三')
save(26,{'fill':23,'written':3},['已實際開啟兩頁全卷；一、基礎1拆4及2拆4＝8筆；二、填充1(1筆)、2(4筆)、3/4各1、5(4筆)、6(2筆)、7/8各1＝15筆；三、計算1–3＝3筆，總26筆。','原配分8×3+15×4+5+6+5=100，與完整原卷一致；第二頁左中答題格為重複作答區，不重複收題。','填6兩子題皆複製完整紙片共條件及圖，不使用承上題；填2全部四獨立式、填5全部四因式分解均拆開。','含全部五種必要圖（逆時針旋轉、甲乙疊合、兩正方形面積差、摺紙、坐標雙正方形），全部純SVG。'])
