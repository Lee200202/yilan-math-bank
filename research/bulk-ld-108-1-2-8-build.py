import importlib.util,math
from pathlib import Path
s=importlib.util.spec_from_file_location('bulkhelper',Path(__file__).with_name('bulk-priority-helper.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
Paper,svg,path,labels=m.Paper,m.svg,m.path,m.labels
p=Paper('ld-108-1-2-8','宜蘭縣立羅東國中108學年度第一學期八年級數學科第二次段考試卷')
cube=svg(path('M110 40H270L215 95H55ZM55 95V255H215V95M270 40V200L215 255M110 40 215 95')+path('M110 40V200H270M110 200 55 255M110 40 215 255','stroke-dasharray="5 5"')+labels([(100,30,'A'),(274,30,'B'),(223,99,'C'),(32,99,'D'),(212,280,'E')]),330,305)
cable=svg('<path d="M35 250 59 143 90 164 121 207 145 196 185 226 222 97 268 53 290 107 317 76 345 213 345 260H35Z" fill="#eff8ee" stroke="#799a77" stroke-width="1"/>'+path('M60 140 280 50M35 260H345')+path('M60 140V260M280 50V260','stroke-dasharray="5 5"')+'<circle cx="60" cy="260" r="3"/><circle cx="280" cy="260" r="3"/>'+labels([(46,133,'B'),(274,38,'A'),(50,285,'C'),(273,285,'D')]),385,315)
f8=svg(path('M180 25V280L285.88 223.53ZM180 25 108 191 180 280M108 191 180 95M108 191 180 245M114 183l8 6-6 8M281.18 214.71l-8.82 4.7 4.7 8.82')+labels([(185,20,'A'),(184,306,'B'),(290,231,'C'),(85,197,'D'),(184,101,'E'),(184,251,'F')]),350,330)
land=svg(path('M180 50H360V230H180ZM180 50 72 86 180 230')+path('M72 86 360 230','stroke-dasharray="6 5"')+labels([(164,39,'A'),(48,84,'B'),(164,257,'C'),(362,257,'D'),(362,39,'E')]),410,290)
rect=svg(path('M50 40H310V240H50Z')+'<circle cx="225" cy="145" r="4"/>'+labels([(30,35,'A'),(313,35,'B'),(313,265,'C'),(30,265,'D'),(204,170,'K')]),360,295)

def spaceship():
 c=(310,70);outer=[(30,70),(170,210),(310,210),(380,140),(380,70),(345,35),(310,35),(292.5,52.5),(292.5,70)]
 s=''
 for i in range(8):
  a,b=outer[i],outer[i+1];s+=path(f'M{c[0]} {c[1]} {a[0]} {a[1]} {b[0]} {b[1]}Z')
  # The source marks each of the eight outer right angles.
  u=(c[0]-b[0],c[1]-b[1]);v=(a[0]-b[0],a[1]-b[1]);ul=math.hypot(*u);vl=math.hypot(*v);k=min(7,ul*.2,vl*.2)
  ux,uy=u[0]/ul*k,u[1]/ul*k;vx,vy=v[0]/vl*k,v[1]/vl*k
  s+=path(f'M{b[0]+ux:.2f} {b[1]+uy:.2f}l{vx:.2f} {vy:.2f} {-ux:.2f} {-uy:.2f}')
 s+=path('M30 70H380')
 for x,y in [outer[0],outer[-1],c,outer[4]]:s+=f'<circle cx="{x}" cy="{y}" r="2.8"/>'
 return svg(s+labels([(22,58,'A'),(271,58,'B'),(313,92,'C'),(385,77,'D')]),430,250)

fw2=svg(path('M45 230 228 50 320 230Z M228 218H240V230')+path('M228 50V230','stroke-dasharray="5 4"')+labels([(220,37,'A'),(23,253,'B'),(324,253,'C'),(220,257,'D')]),380,285)
p.add(1,0,[80,445,486,502],r'$\frac{\sqrt2}{\sqrt7}$ 的最簡根式為＿＿＿＿。','easy')
p.add('2(1)',0,[98,564,432,600],r'計算並將結果化為最簡根式：$\sqrt3\times\sqrt7=$＿＿＿＿。','easy')
p.add('2(2)',0,[448,564,830,600],r'計算並將結果化為最簡根式：$(7-\sqrt3)^2=$＿＿＿＿。','easy')
p.add('2(3)',0,[98,606,449,670],r'計算並將結果化為最簡根式：$\sqrt{\frac25}\div\sqrt{\frac65}=$＿＿＿＿。','easy')
p.add('2(4)',0,[453,618,908,668],r'計算並將結果化為最簡根式：$(\sqrt2-1)(6+\sqrt3)=$＿＿＿＿。','easy')
p.add(3,0,[80,680,980,712],r'若某一個直角三角形的斜邊長為10，其中一股的長為7，則另一股的長為＿＿＿＿。','easy')
p.add('4(1)',0,[97,780,432,818],r'因式分解：$5x^2+x=$＿＿＿＿。','easy')
p.add('4(2)',0,[678,780,1141,818],r'因式分解：$x(2x+1)+(2x+1)=$＿＿＿＿。','easy')
p.add('4(3)',0,[97,847,568,883],r'因式分解：$2x(x-1)+3(1-x)=$＿＿＿＿。')
p.add('4(4)',0,[678,847,1083,883],r'因式分解：$2x^3-3x^2-4x+6=$＿＿＿＿。')
p.add('4(5)',0,[97,910,430,947],r'因式分解：$x^4-81=$＿＿＿＿。')
p.add(5,0,[75,974,1058,1016],r'已知坐標平面上兩點 $A(-6,-4)$、$B(3,-2)$，則坐標平面上兩點的距離 $\overline{AB}=$＿＿＿＿。','easy')
p.add(6,0,[75,1040,919,1080],r'下圖為一個邊長12公分的正方體，則 $\overline{AE}$ 的長是多少？答：＿＿＿＿公分。',diagram=cube,figureRect=[151,1376,325,1550])
p.add(7,0,[75,1099,1166,1247],r'如圖，在瑞士的「菲斯特高空飛索」（圖中的 $\overline{AB}$）全長820公尺，旅客走上海拔2168公尺的 $A$ 點高台站乘坐飛索，會快速滑落到海拔1988公尺的 $B$ 點高台站。則兩個高台站相對於地面兩點（圖中 $C$、$D$ 點）間的距離 $\overline{CD}$ 為＿＿＿＿公尺。',diagram=cable,figureRect=[420,1380,764,1554])
p.add(8,0,[75,1264,1163,1360],r'如圖，已知 $\triangle ABC$ 與 $\triangle DEF$ 都是直角三角形。若 $\overline{BC}=8$、$\overline{AC}=15$、$\overline{DE}=8$、$\overline{DF}=6$，則 $\triangle ADE$ 面積與 $\triangle BDF$ 的面積總和為＿＿＿＿平方單位。','hard',diagram=f8,figureRect=[854,1338,1065,1578])
p.add(9,1,[75,73,891,381],'下列哪些敘述是正確的？＿＿＿＿。',options=[r'$2x^2+4x+1$ 可因式分解為 $2(x^2+2x)+1$。',r'若 $3x^2+2x-8$ 可因式分解為 $(x+2)(3x-4)$，則 $(x+2)$ 為 $3x^2+2x-8$ 的因式。',r'$3x^2+2x-8$ 是 $\frac13(3x-4)$ 的倍式。','若一個直角三角形的兩個邊長為5和12，則第三個邊長必為13。',r'有一長方形的面積為 $\sqrt{54}$，若其長為 $\sqrt6$，則其寬為3。'])
p.add(10,1,[75,396,659,435],r'因式分解 $9x^2-36y^2+1+7x^2-16x+3=$＿＿＿＿。')
p.add(11,1,[75,440,1170,531],r'如圖，爸爸有兩塊土地，一塊是面積為25平方公里的正方形 $ACDE$ 土地，另一塊是面積為7.5平方公里的 $\triangle ABC$ 土地，爸爸並在 $B$、$C$、$D$ 各蓋一間農舍。已知 $B$、$C$ 農舍的距離為5公里，則 $B$、$D$ 農舍的距離為＿＿＿＿公里。','hard',diagram=land,figureRect=[145,865,356,1056])
p.add(12,1,[75,533,1173,689],r'年終購物季來臨，各家物流業者都很忙碌，白貓宅配也不例外。如圖，白貓宅配擁有一個超大長方形的物流園區，在它的四個頂點設立了 $A$、$B$、$C$、$D$ 四個倉庫，而園區內部的分揀中心為 $K$ 點，且 $K$ 點與圍牆 $\overline{AB}$、$\overline{BC}$ 的垂直距離都是2公里。已知 $\overline{KA}=4$ 公里、$\overline{KC}=3$ 公里，則此分揀中心 $K$ 與倉庫 $D$ 的距離 $\overline{KD}$ 為＿＿＿＿公里。','hard',diagram=rect,figureRect=[486,859,708,1054])
p.add(13,1,[75,697,1173,837],r'下圖是未來太空船的側面圖，它利用了8個形狀為等腰直角三角形的特殊材料作為外殼，由大到小來看的話，是將每個較大直角三角形的一股連接到另一個較小直角三角形的斜邊上（如圖所示）。已知 $A$、$B$、$C$、$D$ 四點位於同一直線上，而 $C$ 點是這8個三角形的共同頂點。若甲板 $\overline{AB}$ 的長度為 $30\sqrt3$ 公尺，則操控艙 $\overline{CD}$ 長為＿＿＿＿公尺。','hard',diagram=spaceship(),figureRect=[762,845,1152,1061])
p.add(1,1,[83,1153,424,1222],r'計算並化簡 $\frac8{\sqrt6-\sqrt2}+\frac{\sqrt6+\sqrt{14}}{\sqrt7+\sqrt3}$。',kind='written')
stem=r'如圖，在 $\triangle ABC$ 中，若 $\overline{AC}=5$、$\overline{BC}=7$、$\overline{AB}=6$。若由 $A$ 點向下作 $\overline{BC}$ 邊上的高 $\overline{AD}$，且假設 $\overline{CD}$ 長為 $x$，'
p.add('2(1)',1,[619,1153,1155,1430],stem+r'請以 $x$ 表示 $\overline{AD}$ 的長度。',kind='written',diagram=fw2)
p.add('2(2)',1,[619,1153,1155,1430],stem+r'請先以 $x$ 表示 $\overline{AD}$ 的長度，再利用此結果算出 $x$ 的值。','hard',kind='written',diagram=fw2,note='原第2小題引用第1小題；獨立拆題後重帶第1小題的求式指示，不提供求式結果或答案。')
p.save(23,{'fill':20,'written':3})
