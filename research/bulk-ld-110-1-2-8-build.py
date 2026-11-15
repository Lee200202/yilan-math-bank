import importlib.util,math
from pathlib import Path
s=importlib.util.spec_from_file_location('bulkhelper',Path(__file__).with_name('bulk-priority-helper.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
Paper,svg,path,labels=m.Paper,m.svg,m.path,m.labels
p=Paper('ld-110-1-2-8','宜蘭縣立羅東國中110學年度第一學期八年級數學科第二次段考試卷')
f12=svg(path('M20 220H340m-9-5 9 5-9 5 M170 220H260V130L215 85Z M170 220 260 130 M250 220V210H260m-8-82-8-8 8-8')+path('M215 85A142.3 142.3 0 0 0 27.7 220','stroke-dasharray="5 5"')+labels([(159,245,'O'),(252,245,'A'),(264,135,'B'),(207,76,'C'),(16,245,'D'),(269,178,'2'),(239,102,'1')]),370,275)
f14=svg(path('M30 50H150V170H30ZM150 50 348.165 109.45 330 170H150M330 170 390.55 188.165 408.715 127.615 348.165 109.45M150 158H162V170M338.58 106.58l-2.87 9.58 9.58 2.87')+labels([(146,39,'A'),(143,195,'B'),(321,195,'C'),(351,100,'D'),(77,121,'甲'),(375,160,'乙')]),450,230)

def tree():
 shapes=[]
 def square(a,b,depth):
  ax,ay=a;bx,by=b;nx,ny=by-ay,-(bx-ax);d=(ax+nx,ay+ny);c=(bx+nx,by+ny)
  pts=[a,b,c,d];shapes.append('<polygon points="'+' '.join(f'{x:.2f},{y:.2f}' for x,y in pts)+'" fill="#d3d3d3" stroke="#555" stroke-width="1.2"/>')
  if depth:
   apex=((d[0]+c[0])/2+nx/2,(d[1]+c[1])/2+ny/2)
   shapes.append('<polygon points="'+' '.join(f'{x:.2f},{y:.2f}' for x,y in [d,c,apex])+'" fill="#ededed" stroke="#555" stroke-width="1.2"/>')
   square(d,apex,depth-1);square(apex,c,depth-1)
 square((210,360),(310,360),3)
 return svg(''.join(shapes)+'<circle cx="210" cy="360" r="3.5"/><circle cx="310" cy="360" r="3.5"/>'+labels([(195,386,'A'),(313,386,'B')]),520,405)

fw1=svg('<path d="M50 200V40L330 200Z" fill="#eee" stroke="#111" stroke-width="1.5"/>'+path('M50 200 118.92 79.38M50 188H62V200m51-111 10 5 5-10')+labels([(32,225,'A'),(32,33,'B'),(333,225,'C'),(120,72,'D')]),380,260)
p.add(1,0,[94,364,802,452],r'下列哪一組數無法作為直角三角形的三邊長？答：＿＿＿＿。','easy',options=[r'$\sqrt1$、$\sqrt2$、$\sqrt3$','3、4、5',r'$3^2$、$4^2$、$5^2$','5、12、13'])
p.add(2,0,[94,470,1180,574],r'已知 $2x^2+10x+12=2(x+2)(x+3)$，則下列哪些式子是 $2x^2+10x+12$ 的因式？答：＿＿＿＿。','easy',options=[r'$x+3$',r'$2x+6$',r'$2x+4$',r'$2x+2$',r'$2x^2+10x+12$'])
p.add('3(1)',0,[126,633,454,709],r'計算並化為最簡根式：$\sqrt6\times\sqrt{\frac73}=$＿＿＿＿。','easy')
p.add('3(2)',0,[126,722,411,793],r'計算並化為最簡根式：$\frac{\sqrt3}{\sqrt5}=$＿＿＿＿。','easy')
p.add('3(3)',0,[126,804,537,865],r'計算並化為最簡根式：$(\sqrt6+3)^2(\sqrt6-3)^2=$＿＿＿＿。')
p.add('3(4)',0,[126,875,538,946],r'計算並化為最簡根式：$\frac{\sqrt6}{2+\sqrt3}+\frac{\sqrt3+\sqrt2}{\sqrt3-\sqrt2}=$＿＿＿＿。')
p.add(4,0,[94,956,500,1002],r'因式分解：$4x^2+x=$＿＿＿＿。','easy')
p.add(5,0,[94,1015,534,1060],r'因式分解：$7x^2-5x-2=$＿＿＿＿。','easy')
p.add(6,0,[94,1074,573,1120],r'因式分解：$-21x^2+26x+15=$＿＿＿＿。')
p.add(7,0,[94,1135,636,1180],r'因式分解：$(3x-1)^2-(1-3x)(4-x)=$＿＿＿＿。')
p.add(8,0,[94,1196,834,1241],r'已知坐標平面上 $A(2,6)$、$B(-2,1)$ 兩點，求 $\overline{AB}$ 的長。答：＿＿＿＿。','easy')
p.add(9,0,[94,1257,982,1299],r'已知 $\sqrt{17}\doteq4.1$。利用根式的運算規則，計算 $\sqrt{1700}+\sqrt{68}$ 的近似值。答：＿＿＿＿。','easy')
p.add(10,0,[94,1306,1205,1349],r'已知一個直角三角形的兩邊長分別是8、15，則第三邊長可以是那些數值？答：＿＿＿＿。')
p.add(11,0,[94,1361,912,1399],r'已知 $x$ 是正整數，$x^2-6x-16$ 為質數，求此質數的值。答：＿＿＿＿。')
p.add(12,0,[94,1406,1198,1575],r'如圖，在直角三角形 $OAB$ 與直角三角形 $OBC$ 中，$O$ 點為數線上的原點，$A$ 點的坐標為2，$\overline{AB}=2$、$\overline{BC}=1$，若數線上有一點 $D$，且 $\overline{OD}=\overline{OC}$，連結 $B$ 點、$D$ 點，請問 $\overline{BD}$ 的長度為何？答：＿＿＿＿。','hard',diagram=f12)
p.add(13,1,[93,102,1190,189],r'有一個長方形的面積是 $(2x^2+11x+15)$ 平方單位，若長方形的寬為 $(x+3)$，則此長方形的周長為何？答：＿＿＿＿。','easy')
p.add(14,1,[93,206,1190,367],r'如圖，四邊形 $ABCD$ 中，$\angle B=\angle D=90^\circ$，$\overline{AD}=10$、$\overline{BC}=7$，分別以 $\overline{AB}$、$\overline{AC}$ 的邊作正方形，依序得兩個正方形甲和乙，則甲和乙面積相差是多少？答：＿＿＿＿。',diagram=f14,note='原稿題幹印AB、AC作正方形，但原圖乙正方形在CD邊，文字與圖不一致；忠實保留，不自行更正。')
p.t[-1].update(sourceIssue=p.t[-1]['sourceNote'],usable=False)
p.add(15,1,[93,389,1192,472],r'已知多項式 $(20x+7)(29x-17)-(29x-17)(13x-10)+(29x-17)(3x+10)$ 可因式分解成 $(ax+b)(10x+c)$，其中 $a$、$b$、$c$ 均為整數，則 $a+b+c=$＿＿＿＿。')
p.add(16,1,[93,572,770,648],r'計算 $\left(\frac{21^2+5\times21+6}{23\times19}\right)\times\left(\frac{21^2+2\times21-8}{21^2+2\times21-3}\right)$ 之值。答：＿＿＿＿。')
p.add(17,1,[93,720,1193,931],r'如圖所示，圖中所有的三角形都是直角三角形，所有四邊形都是正方形。如果圖中所有正方形面積總和是320平方公分，則最大正方形邊長 $\overline{AB}$ 是多少公分？答：＿＿＿＿。','hard',diagram=tree())
stem=r'直角三角形 $ABC$ 中，$\angle BAC=90^\circ$，$\overline{AD}\perp\overline{BC}$，若 $\overline{AB}=\sqrt{17}-3$、$\overline{AC}=\sqrt{17}+3$，'
p.add('1(1)',1,[66,1030,1133,1146],stem+r'求 $\overline{BC}$ 的長。',kind='written',diagram=fw1)
p.add('1(2)',1,[66,1030,1133,1146],stem+r'求 $\overline{AD}$ 的長。','hard',kind='written',diagram=fw1)
stem2=r'已知甲、乙、丙均為 $x$ 的一次多項式，且其一次項的係數皆為正整數，常數項皆為整數。若甲與乙相乘為 $(6x^2-11x-10)$，乙與丙相乘為 $(10x^2-31x+k)$，'
p.add('2(1)',1,[66,1311,1118,1447],stem2+'找出多項式乙。',kind='written')
p.add('2(2)',1,[66,1311,1118,1447],stem2+r'求出 $k$ 值。',kind='written')
p.add('2(3)',1,[66,1311,1118,1447],stem2+'求多項式甲和丙相加是多少。',kind='written')
p.save(25,{'fill':20,'written':5})
