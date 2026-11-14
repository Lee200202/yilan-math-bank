from pathlib import Path
import json
ROOT=Path(__file__).parent
rows=[]
curated=[]
for f in ROOT.glob('curated-*.json'):
    data=json.loads(f.read_text(encoding='utf8'))
    if isinstance(data,list):curated+=data
byid={q['id']:q for q in curated}
def add(qid,text,options=None,svg=None):
    q=byid[qid];blocks=[{'type':'text','text':text}]
    if options:blocks.append({'type':'options','items':options})
    r={'id':qid,'blocks':blocks,'verified':True,'sourceSha256':q['sourceSha256']}
    if svg:r['diagramSvg']=svg
    rows.append(r)
def line105():
    s='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 90"><path d="M20 44H640m-9-5 9 5-9 5" fill="none" stroke="#111" stroke-width="1.4"/>'
    for i in range(16):
        x=30+i*38;s+=f'<path d="M{x} 37V51" stroke="#111"/>'
    for i,t in [(2,'B'),(5,'D'),(9,'A'),(12,'C')]:
        x=30+i*38;s+=f'<circle cx="{x}" cy="44" r="3.3" fill="#111"/><text x="{x}" y="28" text-anchor="middle" font-family="serif" font-size="18">{t}</text>'
    return s+'</svg>'
def line106():
    s='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 490 105"><path d="M20 50H470m-10-6 10 6-10 6" fill="none" stroke="#111" stroke-width="1.5"/>'
    for i in range(9):
        x=36+i*50;s+=f'<path d="M{x} 40V60" stroke="#111" stroke-width="1.3"/>'
    for i,t in [(1,'A'),(4,'O'),(6,'B'),(8,'C')]:
        x=36+i*50;s+=f'<circle cx="{x}" cy="50" r="3.5" fill="#111"/><text x="{x}" y="29" text-anchor="middle" font-family="serif" font-size="18">{t}</text>'
    for i,t in [(4,'0'),(5,'1'),(6,'2')]:
        x=36+i*50;s+=f'<text x="{x}" y="83" text-anchor="middle" font-family="serif" font-size="18">{t}</text>'
    return s+'</svg>'
add('zh-105-1-1-7-fill-1','日本超長壽漫畫《烏龍派出所》日前結束四十年的連載，作者秋本治「每週按時交稿，四十年完全沒有休刊」享譽漫畫界。以每年五十二週、一週連載一回、一本單行本收錄十三回、一本單行本博客來賣新台幣100元來計算，小兆要準備＿＿＿＿元才能把整套《烏龍派出所》買回家。')
add('zh-105-1-1-7-fill-2',r'依下圖回答下列問題：\n(1) 若 $A$ 點坐標為 $2$，$C$ 點坐標為 $5$，則 $D$ 點坐標是＿＿＿＿？\n(2) 若 $D$ 點為原點，$B$ 點坐標為 $-1.5$，則 $A$ 點坐標為＿＿＿＿？',svg=line105())
add('zh-105-1-1-7-fill-4','《航海王》船醫喬巴發現M．凱薩克勞恩的《氣體果實》能力會使空氣中的病毒每經過30秒變成原本數量的兩倍。在和魯夫的戰鬥中，一開始原本M．凱薩克勞恩就放了十隻病毒，每經過1分鐘再放入1隻。第三分三十秒時，場上一共有＿＿＿＿隻病毒。')
add('zh-105-1-1-7-fill-5','下列哪些結果是正的？請寫代號。',options=[r'$(-2)^6\times2^5$',r'$(-2^6)\times(-2)^5$',r'$(-2)^7\times(-2^{98})\times(-2)$',r'$(-2^7)\times(-2)$'])
add('zh-105-1-1-7-fill-6',r'小兆勵志成為《Pokemon Go》的寶可夢訓練大師，他利用假日到宜蘭市中山公園內成一直線的5個補給點巡邏。5個補給點的座標分別是 $A(-5)$、$B(7)$、$C(-1)$、$D(2)$、$E(-3)$，從 $D$ 點出發，走完5個補給站的最短距離是＿＿＿＿。')
add('zh-105-1-1-7-written-1',r'計算 $(-129)\div3-3\times[(-9)\times(-7)-8^2]+|-299+1|$。')
add('zh-105-1-1-7-written-2',r'計算 $(-1)^0-(-1^4)-(-2)^3+(-2^3)+(-2^2)^3$。')
add('zh-105-1-1-7-written-3',r'$A=4^{10}$，$B=8^7$，$C=16^5$，請利用指數律，比較 $A$、$B$、$C$ 的大小。')
add('zh-105-1-1-7-written-4','小兆想跟媽媽要零用錢，跟媽媽談好條件說：「媽媽你第一天給我1元，第二天給我2元，第三天給我4元，第四天8元之後每一天都給我前一天的兩倍，給我十二天就好。」請問第十二天，媽媽要給小兆多少錢呢？（可用指數表示不用乘開）')
add('zh-106-1-1-7-fill-1','下列各數中哪些是整數？請寫代號。',options=[r'$1.5$',r'$-3.6$',r'$38$',r'$0$',r'$-21$',r'$19$',r'$2.8$',r'$\frac53$'])
add('zh-106-1-1-7-fill-2',r'寫出下面數線上 $A$ 點的坐標：$A(\underline{\qquad})$。',svg=line106())
add('zh-106-1-1-7-fill-3','若以中午12時為基準，上午8時記為+8，則下午3時可記為何？')
add('zh-106-1-1-7-fill-4','將數線上表示−3和−4兩點之間的線段分成7等分，所得的6個等分點中，由左向右數第3個等分點所代表的數為何？')
add('zh-106-1-1-7-fill-5',r'數線上有 $A(-5)$、$B$ 兩點，且的中點坐標為 $7$，則 $B$ 點的坐標為何？')
add('zh-106-1-1-7-fill-6',r'數線上 $A$ 點的坐標為 $-11$，小明由 $A$ 點出發，先向左移動6個單位，再向右移動5個單位，最後再向左移動4個單位，則此時小明所在的坐標為何？')
add('zh-106-1-1-7-fill-7',r'已知 $a>b$、$c<d$、$c>a$、$a<d$、$c>b$、$e>d$，則 $a$、$b$、$c$、$d$、$e$ 中最大的是哪一個數？')
add('zh-106-1-1-7-fill-8',r'計算 $(-25)+(-96)+(-17)+(-84)+(-73)$。')
add('zh-106-1-1-7-fill-9',r'計算 $5\times(-11)\times(-125)\times4\times(-2)\times25\times(-7)\times(-8)$。')
add('zh-106-1-1-7-fill-10',r'計算 $|988-9873|-|9874-567|+|456-999|$。')
add('zh-107-1-1-7-fill-1','在同一天內，以中午12:00為基準，若下午3:00記為+3，則上午9:00記為＿＿＿＿。')
add('zh-107-1-1-7-fill-2',r'計算 $(-28)+16$。')
add('zh-107-1-1-7-fill-3',r'計算 $(-15)-23$。')
add('zh-107-1-1-7-fill-4',r'$2^{-4}$ 之值＝＿＿＿＿。')
add('zh-107-1-1-7-fill-5',r'若 $3^3\times(3^2)^4\div3^5=3^a$，則 $a=$＿＿＿＿。')
add('zh-107-1-1-7-fill-6',r'$A$、$B$、$C$、$D$ 分別代表下列各數：$A=-3$、$B=-2\frac14$、$C=-(-2)$、$D=-2\frac13$。請比較 $A$、$B$、$C$、$D$ 的大小，並請填代號由大至小排列：＿＿＿＿＞＿＿＿＿＞＿＿＿＿＞＿＿＿＿。')
add('zh-107-1-1-7-fill-7',r'若 $|x+7|=8$，則 $x=$＿＿＿＿。')
add('zh-107-1-1-7-fill-8','下列敘述何者正確？',options=[r'$a\div(b-c)=a\div b-a\div c$，$b-c\ne0$、$bc\ne0$',r'$a\div(b\times c)=a\div b\times c$，$bc\ne0$',r'$(a+b)\div c=a\div c+b\div c$，$c\ne0$',r'$a\div b\div c=a\div(b\div c)$，$bc\ne0$'])
add('zh-107-1-1-7-fill-9',r'計算 $|5-(-17)|+(-12)\div2$。')
add('zh-107-1-1-7-fill-10',r'計算 $(-982)-[(-73)-982]+[(-74)-199]$。')

mapped=json.loads((ROOT/'transcribed-zhonghua-early-map.json').read_text(encoding='utf8'))
def item(n,text,options=None,svg=None):add(mapped[n-1]['id'],text,options,svg)
def axis108():
    s='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 95"><path d="M20 42H620m-10-5 10 5-10 5" fill="none" stroke="#111" stroke-width="1.5"/>'
    for v in [-3,-2,-1,0,1,2,3,-2.75,-2.5,-2.25,1/3,2/3]:
        x=310+v*80;s+=f'<path d="M{x:.2f} 35V49" stroke="#111" stroke-width="1.3"/>'
    for v in [-3,-2,-1,0,1,2,3]:
        x=310+v*80;s+=f'<text x="{x}" y="76" text-anchor="middle" font-family="serif" font-size="18">{v}</text>'
    for v,t in [(-2.75,'A'),(-1.5,'B'),(2/3,'C')]:
        x=310+v*80;s+=f'<circle cx="{x:.2f}" cy="42" r="4" fill="#111"/><text x="{x:.2f}" y="25" text-anchor="middle" font-family="serif" font-size="19">{t}</text>'
    return s+'</svg>'
item(1,'下列敘述何者正確？',options=['當「＋、－」是表示數的正負時，稱之為運算符號','當「＋、－」是表示加、減法時，稱之為性質符號','0不是正數也非負數','正整數和負整數合稱為整數'])
item(2,r'下列各數中，與 $-2.4$ 是同號數的有幾個？\n$-3.6$、$-4\frac23$、$0$、$-21$、$2\frac45$、$(-2)^4$、$-2^4$',options=['2個','3個','4個','5個'])
item(3,'數線的要素不包含下列何者？',options=['正向','原點','單位長','負向'])
item(4,r'下列描述中正確的有幾個？\n甲：$13$ 的相反數是 $\frac1{13}$。\n乙：$-\frac1{17}$ 的相反數是 $\frac1{17}$。\n丙：$0$ 沒有相反數。\n丁：$-(-8.5)$ 的相反數是 $8.5$。',options=['1個','2個','3個','4個'])
item(5,r'絕對值小於或等於 $9.3$ 的整數有幾個？',options=['9個','10個','18個','19個'])
item(6,r'數線上有 $A(9)$、$B(-3)$、$C$ 三點，其中 $B$ 為 $A$ 和 $C$ 的中點，試問 $C$ 點座標為何？',options=[r'$21$',r'$3$',r'$-9$',r'$-15$'])
item(7,r'在筆直的商店街上有五家店 $A(-3)$、$B(-2)$、$O(0)$、$C(3)$、$D(5)$，若小雪距離 $D$ 店3單位，距離 $B$ 店4單位，則她在哪兩家相鄰的店之間？',options=[r'$A$ 和 $B$',r'$B$ 和 $O$',r'$O$ 和 $C$',r'$C$ 和 $D$'])
item(8,'下列各算式中，何者不一定成立？',options=[r'$(a+b)\times c=a\times c+b\times c$',r'$c\times(a-b)=c\times a-c\times b$',r'$(a-b)\div c=a\div c-b\div c$',r'$c\div(a+b)=c\div a+c\div b$'])
item(9,r'已知 $a$ 為正整數，若 $6.25\times10^a$ 乘開後是8位數；$b$ 為負整數，$5.22\times10^b$ 乘開後，小數點後第9位開始不為零。求 $a+b=$？',options=[r'$-2$',r'$-1$',r'$0$',r'$1$'])
item(10,r'寫出下圖各點的座標：$A($＿＿＿＿$)$、$B($＿＿＿＿$)$、$C($＿＿＿＿$)$。',svg=axis108())
item(11,r'(1) 將 $-3.5$、$0$、$-6$、$-(-\frac17)$、$|-8|$ 這五個數由大至小排列。\n(2) $A=9.1\times10^{-4}$、$B=5.6\times10^{-3}$、$C=6.08\times10^{-6}$、$D=3.2\times10^{-4}$。請將 $A$、$B$、$C$、$D$ 依大小順序排列。')
item(12,'數線上有一隻小白兔，從原點開始進行跳躍活動，第一次向左跳1單位（停在−1），第二次接著再向右跳2單位（停在1），然後第三次再向左跳3單位，第四次再向右跳4單位⋯⋯以此類推，小白兔跳完第2019次之後，距離原出發點有多少單位長？')
item(13,'下列敘述何者錯誤？',options=[r'$(a+b)(c+d)=ac+ad+bc+bd$',r'$(a+b)^2=a^2+2ab+b^2$',r'$(a-b)^2=a^2+2ab-b^2$',r'$(a+b)(a-b)=a^2-b^2$'])
item(14,r'下列何者是 $x$ 的多項式？',options=[r'$\frac3{2x}+2$',r'$2x^2+7$',r'$|5x|-5$',r'$3x^2+4x=5$'])
item(15,r'若 $A$ 為 $x$ 的三次多項式，$B$ 為 $x$ 的一次多項式，則下列敘述何者正確？',options=[r'$A+B$ 為 $x$ 的四次多項式',r'$A-B$ 為 $x$ 的二次多項式',r'$A\times B$ 為 $x$ 的四次多項式',r'$A\div B$ 為 $x$ 的三次多項式'])
item(16,'下列敘述何者正確？',options=['任意整數均有二個平方根',r'$\sqrt{16}$ 的平方根是4和−4','0.3是0.9的平方根','0的平方根是0'])
item(17,r'下列何者是將 $7x^2+4x^3+5-2x$ 按升冪排列？',options=[r'$5-2x+7x^2+4x^3$',r'$4x^3+7x^2-2x+5$',r'$7x^2+5+4x^3-2x$',r'$-2x+4x^3+5+7x^2$'])
item(18,r'$-3x^2-8x+2x^3-5$ 的一次項係數為＿＿＿＿。')

item(19,r'計算下列各式的值：\n(1) $295^2-5^2=$＿＿＿＿。\n(2) $497^2+2\times497\times3+3^2=$＿＿＿＿。\n(3) $\sqrt{121}+\sqrt{(-6)^2}-(\sqrt5)^2=$＿＿＿＿。')
item(20,r'計算下列各式：\n(1) $(5x^2+2x+4)+(x-3)=$＿＿＿＿。\n(2) $(3x+8x^2+6)-(4x^2+6)=$＿＿＿＿。\n(3) $(x+4)(3x-2)=$＿＿＿＿。')
item(21,r'若多項式 $A$ 除以 $3x+1$ 的商式為 $2x^2+5$，餘式為 $9$，則此多項式 $A$ 為＿＿＿＿。')
item(22,r'若 $(1019-19)^2=1019^2-19a$，則 $a=$＿＿＿＿。')
item(23,r'若多項式 $(5-a)x^3+(b-4)x^2-(c-20)x+(d-10000)$ 是 $x$ 的常數多項式，則 $\sqrt{abc}=$＿＿＿＿。')
item(24,'無忌班上數學考試平均分數為67分，若以此分數為基準，無忌的成績比平均分數低4分，記為−4；敏敏的成績73分，該記為＿＿＿＿。')
item(25,r'數線上代表 $k$ 的點與原點的距離是 $11$，則 $k-6=$＿＿＿＿。')
item(26,r'計算下列各式的值：\n(1) $(-2019)-[(-709)+(-2020)]=$＿＿＿＿。\n(2) $2009\times(-37)-9\times(-37)=$＿＿＿＿。\n(3) $(-24)\div[(-6)\div3]=$＿＿＿＿。\n(4) $11\times(-12)\times13\times(-14)\times15\times0\times17\times(-18)-19=$＿＿＿＿。\n(5) $(-13)+[(-2)-(-17)]-|-35|=$＿＿＿＿。\n(6) $5^2-[(-3)^2\times(-2)^3-7^2]=$＿＿＿＿。\n(7) $-30^2+(-20)^3-(-10)^4=$＿＿＿＿。')
item(27,r'將下列各數以科學記號表示：\n(1) $60300000=$＿＿＿＿。\n(2) $0.00042=$＿＿＿＿。')
item(28,r'從 $(-1)$、$2$、$(-3)$、$4$、$(-5)$、$6$、$(-7)$、$8$、$(-9)$ 等數字之中挑選四個出來相乘，乘積最小為＿＿＿＿。')
item(29,r'若 $a=\sqrt{18^2+2\times18\times2+2^2}$、$b=\sqrt{23^2-2\times23\times2+2^2}$、$c=\sqrt{22\times18}$、$d=\sqrt{22^2-18^2}$，比較 $a$、$b$、$c$、$d$ 四數的大小，並由大排到小：＿＿＿＿＞＿＿＿＿＞＿＿＿＿＞＿＿＿＿。')
item(30,r'已知 $-8$ 是 $-4x+3y$ 的一個平方根，且 $8x-3y$ 的平方根為 $\pm4$，則 $\sqrt{x+y}$ 的整數部分為＿＿＿＿。')
item(31,r'化簡 $5(2x+3)^2-[4(3x-1)^2\div(3x-1)-(3x-1)]=$＿＿＿＿。')
item(32,r'若 $\frac1{a^2}+\frac1{b^2}=5$，$ab=2$，則 $a-b=$＿＿＿＿。')
item(33,r'若 $A=(20x^3-10x+9)(x^2-3x+5)+4(x^2-2x+3)+5(x-7)$，則 $A$ 除以 $x^2-3x+5$ 的餘式為＿＿＿＿。')
item(34,r'計算 $(6x^2-7x+8)\div(3x+1)$ 的商式和餘式。')
item(35,r'已知 $(4x-1):(3x+2)=3:2$，則 $\sqrt{4x^2-36x+81}$ 的值為何？')
item(36,r'計算 $\sqrt{103\times101\times99\times97+16}$ 的值為何？')

def axis110():
    s='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 100"><path d="M20 45H400m-10-5 10 5-10 5" fill="none" stroke="#111" stroke-width="1.5"/>'
    for i,t in enumerate('ABCDE'):
        x=50+i*75;s+=f'<path d="M{x} 36V54" stroke="#111"/><text x="{x}" y="26" text-anchor="middle" font-family="serif" font-size="20">{t}</text><text x="{x}" y="82" text-anchor="middle" font-family="serif" font-size="20">{i}</text>'
    return s+'</svg>'
def shape54():
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 390 320"><path d="M90 90H230V20H315V140H165V260H90Z" fill="none" stroke="#111" stroke-width="1.5"/><g fill="none" stroke="#666" stroke-dasharray="3 3"><path d="M88 90Q20 175 88 260"/><path d="M230 20Q190 55 230 90"/><path d="M317 20Q375 80 317 140"/><path d="M167 140Q230 200 167 260"/></g><g fill="#111" font-family="serif" font-size="20" text-anchor="middle"><text x="48" y="180" font-style="italic">a</text><text x="206" y="62" font-style="italic">b</text><text x="355" y="86" font-style="italic">c</text><text x="204" y="206">5</text><text x="127" y="290">3x</text><text x="243" y="171">4x − 1</text></g></svg>'
item(37,r'設 $n$ 為正整數，$n$ 加上36是一個完全平方數；$n$ 加上120又得到另一個完全平方數，則 $n$ 為何？')
item(38,r'若 $A$ 為 $x$ 的二次多項式，$B$ 為 $x$ 的零次多項式，則 $A\times B$ 為 $x$ 的幾次多項式？',options=['二次','一次','零次','不一定'])
item(39,r'若 $a=\frac{11}3$，$b=3.3$，$c=\sqrt{11}$，則 $a$、$b$、$c$ 三數的大小關係為何？',options=[r'$a<b<c$',r'$a<c<b$',r'$b<c<a$',r'$c<a<b$'])
item(40,r'如下圖，$12-\sqrt{110}$ 在數線上的位置應在哪兩點之間？',options=[r'$A$ 點和 $B$ 點',r'$B$ 點和 $C$ 點',r'$C$ 點和 $D$ 點',r'$D$ 點和 $E$ 點'],svg=axis110())
item(41,r'多項式 $6y^3+9y^2-3y-15$ 中，若 $y^3$ 項的係數為 $a$，$y^2$ 項的係數為 $b$，$y$ 項的係數為 $c$，常數項為 $d$，且多項式的次數為 $e$ 次多項式，則 $a+b-c+d-e$ 之值為何？',options=[r'$3$',r'$0$',r'$-6$',r'$36$'])
item(42,r'已知等式如下：$(x-3)(x-1)(x+1)(x+3)+20=(x^2-5)^2$，利用此等式得 $27\times29\times31\times33+20=A^2$，則 $A=$？',options=[r'$801025$',r'$895$',r'$-895$',r'$\pm895$'])
item(43,r'填入適當的式子：\n(1) $6x\cdot($＿＿＿＿$)=48x^2$。\n(2) $(3x^2-2x^3+5)-(7x^3-3x+6)=$＿＿＿＿。\n(3) $(2x^2+5)(x-7)=$＿＿＿＿。\n(4) $(x+10)^2-(x-10)^2=$＿＿＿＿。')
item(44,'正方形面積為13，其邊長可記為＿＿＿＿。')
item(45,r'計算 $\sqrt{(-8)^2}-\sqrt{7^2}+(\sqrt{49})^2=$＿＿＿＿。')
item(46,r'計算 $(30\frac13)^2=$＿＿＿＿。')
item(47,r'化簡 $\sqrt{42.25}=$＿＿＿＿。')
item(48,r'計算 $707^2-2\times707\times7+7^2=$＿＿＿＿。')
item(49,r'若 $x$ 為正整數，則滿足 $\sqrt{110}<x<\sqrt{2021}$ 的 $x$ 值共有＿＿＿＿個。')
item(50,r'若 $6x+7$ 的負平方根是 $-1$，求 $x$ 的值＝＿＿＿＿。')
item(51,r'已知多項式 $x^2-7x-3$ 減去一個多項式的差為 $-3x^2+6x+9$，則此多項式以升冪排列為＿＿＿＿。')
item(52,r'求 $(4x^2+1)\div(4x+1)$ 的餘式為＿＿＿＿。')
item(53,r'已知 $15x^2-14x-15$ 除以多項式 $A$ 得商式為 $5x+2$，餘式為 $-7$，則多項式 $A$ 為＿＿＿＿。')
item(54,r'下圖的周長是 $14x+20$，則 $a+b+c=$＿＿＿＿。',svg=shape54())

def fold58():
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 240"><path d="M40 30H300V190H40ZM200 30V190" fill="none" stroke="#111" stroke-width="1.5"/><path d="M40 190 200 30" stroke="#111" stroke-width="1.5" stroke-dasharray="6 5"/><path d="M60 50Q125 60 145 120m-10-7 10 7 2-12" fill="none" stroke="#666" stroke-width="1.5"/><g font-family="serif" font-size="20" text-anchor="middle"><text x="30" y="24">A</text><text x="200" y="23">B</text><text x="309" y="24">C</text><text x="310" y="215">D</text><text x="30" y="215">E</text><text x="200" y="215">F</text></g></svg>'

def whale60():
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 610 300"><path d="M60 150 250 40V136H280V40H520V260H280V164H250V260Z" fill="none" stroke="#111" stroke-width="1.5"/><circle cx="60" cy="150" r="43" fill="none" stroke="#111" stroke-width="1.5" stroke-dasharray="4 4"/><circle cx="520" cy="150" r="43" fill="none" stroke="#111" stroke-width="1.5" stroke-dasharray="4 4"/></svg>'

def plane62():
    s='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 300">'
    for k in range(-5,6):
        p=145+k*23;s+=f'<path d="M30 {p}H260M{p} 30V260" stroke="#aaa" stroke-width=".6"/>'
    s+='<path d="M20 145H278m-8-4 8 4-8 4M145 275V16m-4 8 4-8 4 8" fill="none" stroke="#111" stroke-width="1.5"/><g font-family="serif" font-size="16"><text x="283" y="151">x</text><text x="151" y="20">y</text><text x="130" y="163">O</text><text x="164" y="164">1</text><text x="152" y="128">1</text></g>'
    for x,y,t,dx,dy in [(2,4,'A',8,-5),(0,2,'B',8,-3),(-3,-1,'C',-18,16),(-2,0,'D',-8,-10)]:
        px=145+x*23;py=145-y*23;s+=f'<circle cx="{px}" cy="{py}" r="3.5" fill="#111"/><text x="{px+dx}" y="{py+dy}" font-family="serif" font-size="18">{t}</text>'
    return s+'</svg>'

def plane69():
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 250"><path d="M20 165H235m-8-4 8 4-8 4M160 235V20m-4 8 4-8 4 8M35 225 212 42" stroke="#111" stroke-width="1.5" fill="none"/><g fill="#111"><circle cx="160" cy="96" r="3.5"/><circle cx="111" cy="147" r="3.5"/><circle cx="63" cy="215" r="3.5"/><circle cx="205" cy="202" r="3.5"/></g><g font-family="serif" font-size="19"><text x="168" y="108">A</text><text x="92" y="141">B</text><text x="70" y="228">C</text><text x="197" y="229">D</text><text x="138" y="189">O</text><text x="240" y="170">x</text><text x="152" y="15">y</text><text x="212" y="37">L</text></g></svg>'

def symbols88():
    s='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 125">'
    syms=['○','×','▲','■']
    for i in range(11):
        x=10+i*34;s+=f'<rect x="{x}" y="10" width="34" height="34" fill="none" stroke="#111"/><text x="{x+17}" y="34" font-family="serif" font-size="22" text-anchor="middle">{syms[i%4]}</text>'
    s+='<text x="397" y="35" font-family="serif" font-size="22">⋯⋯</text>'
    for i,t in enumerate(syms):
        x=30+i*110;s+=f'<text x="{x-22}" y="97" font-family="serif" font-size="18">({chr(65+i)})</text><rect x="{x+15}" y="73" width="34" height="34" fill="none" stroke="#111"/><text x="{x+32}" y="98" font-family="serif" font-size="22" text-anchor="middle">{t}</text>'
    return s+'</svg>'

def intersections92():
    s='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 650 110">'
    for n,start in [(1,15),(2,150),(3,355)]:
        for i in range(n):
            x=start+i*70;s+=f'<path d="M{x} 12h70v44h-70ZM{x} 12l70 44m-70 0 70-44" stroke="#7065a7" stroke-width="1.7" fill="none"/>'
            s+=f'<circle cx="{x+35}" cy="34" r="2.8" fill="white" stroke="#111"/>'
        for i in range(n+1):
            for y in [12,56]:s+=f'<circle cx="{start+i*70}" cy="{y}" r="2.8" fill="white" stroke="#111"/>'
        s+=f'<text x="{start+n*35}" y="85" font-family="serif" font-size="18" text-anchor="middle">圖{["","一","二","三"][n]}</text>'
    return s+'<text x="592" y="45" font-size="22">⋯⋯</text></svg>'

def crossword95():
    s='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 430 320">'
    for i in range(9):s+=f'<rect x="{20+42*i}" y="136" width="42" height="42" fill="none" stroke="#111"/>'
    for j in [0,1,2,4,5,6]:s+=f'<rect x="188" y="{10+42*j}" width="42" height="42" fill="none" stroke="#111"/>'
    for x,y,t in [(209,38,'22'),(209,164,'42'),(41,164,'b'),(377,164,'70'),(209,290,'a')]:s+=f'<text x="{x}" y="{y}" text-anchor="middle" font-family="serif" font-size="20">{t}</text>'
    return s+'</svg>'

item(55,r'若 $a$ 為整數，且 $a<-\sqrt{160}<a+1$，則 $a=$＿＿＿＿。')
item(56,r'計算 $7524\times7422-7473^2+1=$＿＿＿＿。')
item(57,r'若 $a^2=9$，則 $(a+1)(a-1)(a^2-a+1)(a^2+a+1)$ 的值為＿＿＿＿。')
item(58,r'如下圖，在矩形 $ACDE$ 中，如果長 $AC=5x+3$，寬 $AE=2x-1$，若將 $AE$ 摺疊到 $ED$ 上，使得 $A$ 與 $F$ 重合，則矩形 $BCDF$ 的面積為＿＿＿＿。',svg=fold58())
item(59,r'若多項式 $3x^2+4x-5=a(x-5)(x-4)+b\times(x-4)(x-3)+c(x-3)(x-5)$，則 $a+b+c=$＿＿＿＿。')
item(60,r'下圖是正三角形、正方形和圓形組成的「鯨魚圖形」，中間的空隙像是一塊邊長為 $y$ 的正方形。已知鯨魚圖形的總面積 $A=x^4+4x^3+6x^2+ax+b$，大三角形與大正方形邊長為 $x+1$。\n(1) 實線圖形周長為何？（不包括圓形）\n(2) 當「鯨魚圖形的總面積」除以「大正方形面積」的餘式為 $x$，則 $a$、$b$ 值各為何？',svg=whale60())
item(61,'《尚氣與十環傳奇》中，尚氣的爸爸為十環幫幫主，手中持有的十環上均刻有不同的式子（如下），透過投射出十環對敵人造成物理及精神上的打擊，尚氣若要反制十環的攻擊，必須憑空結印出一個三次多項式，讓不懂數學的爸爸頭暈而使不出十環攻擊。已知結印的多項式可以被十環中的所有最高次係數為1的多項式整除，試求此多項式並以降冪排列表示。')
rows[-1]['blocks'].append({'type':'table','header':False,'rows':[[r'$x+2$',r'$4x+3$',r'$\sqrt{2x+1}$',r'$|x-1|$',r'$x-\frac12$'],[r'$3x+6$',r'$\frac{2x}{2x-1}$',r'$5x-3$',r'$x-1$',r'$\frac3{4x}$']]})
item(62,r'寫出附圖坐標平面上 $A$、$B$、$C$、$D$ 的坐標：$A($＿＿＿＿$)$、$B($＿＿＿＿$)$、$C($＿＿＿＿$)$、$D($＿＿＿＿$)$。',svg=plane62())
item(63,'判別下列各點分別在哪一象限內或哪一坐標軸上？並將答案填入空格中。')
rows[-1]['blocks'].append({'type':'table','header':True,'rows':[['坐標',r'$(-6,0)$',r'$(\frac17,-8)$',r'$(-4,-5)$',r'$(1,3.8)$'],['象限或坐標軸','＿＿＿＿','＿＿＿＿','＿＿＿＿','＿＿＿＿']]})
item(64,r'設 $x$、$y$ 皆不為 $0$：\n(1) 若 $7x=4y$，則 $x:y=$＿＿＿＿。\n(2) 若 $\frac{x}7=\frac{y}4$，則 $x:y=$＿＿＿＿。')
item(65,r'若坐標平面上一點 $(m,n)$ 在直線 $2x-3y=-2$ 上，也在直線 $4x+3y=14$ 上，則 $m-n=$＿＿＿＿。')
item(66,r'請寫出 $x$ 軸方程式：＿＿＿＿。')
item(67,r'坐標平面上，下列哪個點，與 $x$ 軸距離最近？',options=[r'$(5,-2)$',r'$(1,3)$',r'$(-3,5)$',r'$(0,-4)$'])
item(68,'下列哪一條直線必通過原點？',options=[r'$4x+y-5=0$',r'$2x-5y+3=0$',r'$x-3y=-2$',r'$4x=0$'])
item(69,r'如附圖，直線 $L$ 的方程式為 $x-y+k=0$，則 $A$、$B$、$C$、$D$ 四點中，哪些點的坐標是此方程式的解？',options=[r'只有 $A$ 點',r'只有 $A$、$B$ 兩點',r'只有 $C$、$D$ 兩點',r'$A$、$B$、$C$、$D$ 四點都是'],svg=plane69())
item(70,r'下列何者與 $30:20$ 不是相等的比？',options=[r'$3:2$',r'$\frac32:1$',r'$\frac34:\frac98$',r'$0.6:0.4$'])
item(71,r'已知 $ad=bc$，且 $a$、$b$、$c$、$d$ 均不為 $0$，則下列哪一個性質不一定成立？',options=[r'$\frac ac=\frac bd$',r'$a:b=c:d$',r'$a:c=b:d$',r'$a:d=b:c$'])
item(72,'下列敘述何者正確？',options=[r'一天24小時中，設晝長為 $x$ 小時，夜長為 $y$ 小時，晝長則夜短，所以 $x$ 和 $y$ 成反比。',r'若 $x$ 的值愈大，$y$ 的值也隨之愈大，則表示 $x$ 和 $y$ 成正比。',r'媽媽購買每斤400元的櫻桃 $x$ 斤，總價為 $y$ 元，此時 $y$ 與 $x$ 成正比。',r'若 $y=-2x$ 成立，表示 $x$ 與 $y$ 成反比。'])
item(73,r'若 $(-x+5):(3x-6)=2:3$，則 $x=$＿＿＿＿。')
item(74,r'若 $y$ 與 $x$ 成正比，且 $y=6$ 時，$x=-3$，則 $y=-2$ 時，$x=$＿＿＿＿。')
item(75,'下列敘述何者正確？',options=[r'因為20、21、4、8沒有規律，所以不是數列',r'$1$、$2$、$4$、$8$、$16$ 是等差數列',r'$\sqrt2$、$\sqrt2$、$\sqrt2$、$\sqrt2$ 不是等差數列',r'一個等差數列的公差是 $d$，若將此數列的每一項都加10得一個新的數列，則此數列是等差數列，且公差依然為 $d$'])
item(76,'已知一等差級數前20項和為100，若將每一項都加上10，則新的等差級數和為何？',options=['100','200','300','400'])
item(77,'已知一等比數列的公比為10，若將每一項都乘上5，則新的等比數列的公比為何？',options=['5','10','15','50'])
item(78,r'下列 $x$ 與 $y$ 的關係中，何者 $y$ 不是 $x$ 的函數？',options=[r'閏年中，$x$ 表示天數，$y$ 表示 $x$ 天所對應月份',r'一長方形的面積24，長為 $x$、寬為 $y$',r'小舞有500元，買書花掉 $x$ 元，剩下 $y$ 元',r'華氏溫度 $=\frac95\times$ 攝氏溫度 $+32$，若 $x$ 代表攝氏溫度、$y$ 代表華氏溫度'])
item(79,r'已知一次函數 $y=ax+b$，其中 $a>0$、$b<0$，則其圖形不通過第幾象限？',options=['第一象限','第二象限','第三象限','第四象限'])
item(80,r'觀察下列數列的規律，在空格中填入適當的數：\n$1$、$3$、$6$、$10$、$15$、＿＿＿＿、$28$。')
item(81,r'已知數列 $5$、$5$、$5$、$5$、$5$、$5$，\n(1) 若其為等差數列，則公差＝＿＿＿＿。\n(2) 若其為等比數列，則公比＝＿＿＿＿。')
item(82,r'已知數列 $4$、$a$、$16$，\n(1) 若其為等差數列，則 $a=$＿＿＿＿。\n(2) 若其為等比數列，則 $a=$＿＿＿＿。')
item(83,'已知等差數列的首項為32，公差為−2，則第10項為＿＿＿＿。')
item(84,r'已知等比數列的首項為 $\frac1{128}$，公比為 $2$，則：\n(1) 第5項為＿＿＿＿。\n(2) 若該數列第 $m$ 項為 $1$，則 $m=$＿＿＿＿。')
item(85,r'求等差級數 $(-15)+(-18)+(-21)+(-24)+(-27)+(-30)=$＿＿＿＿。')
item(86,r'已知等差級數 $16+12+\cdots+(-40)$，則：\n(1) 此級數共有＿＿＿＿項。\n(2) 此級數的和＝＿＿＿＿。')
item(87,'已知一等差數列前19項和為140，前20項和為150，則此等差數列第20項為＿＿＿＿。')
item(88,r'觀察下列數列或圖形的規律，在空格中填入正確答案。\n(1) $1$、$1$、$2$、$3$、$5$、$8$、$13$、＿＿＿＿。\n(2) 依下面圖形的規律，第103格的圖形為何？＿＿＿＿。',svg=symbols88())
item(89,r'甲、乙、丙的對應關係中，哪些 $y$ 不是 $x$ 的函數？\n甲：面積為1的長方形，長為 $x$ 時，寬為 $y$。\n乙：某次數學小考考 $x$ 分的同學，其座號為 $y$ 號。\n丙：$y^2=x$。',options=['甲、乙','甲、丙','乙、丙','甲、乙、丙'])
item(90,r'有一個長方體，長為 $x$ 公分，寬為5公分，高為8公分。以函數表示此長方體的表面積，則下列何者為此函數的關係式？',options=[r'$y=40x$',r'$y=26x+80$',r'$y=13x+40$',r'$y=13x+80$'])
item(91,'若一個等差數列的第20項為−198，公差為3，求此等差數列的首項＝＿＿＿＿。')
item(92,r'下圖中，圖一有5個交點，圖二有8個交點，圖三有11個交點，……。觀察其規律，求圖 $n$ 的交點個數＝＿＿＿＿。（用 $n$ 的式子表示）',svg=intersections92())
item(93,r'有一個皮球自離地面243公尺高處落下，若不計任何阻力影響，可知每次反彈高度為其前次反彈高度的 $\frac23$，則第6次反彈後的高度是＿＿＿＿公尺。')
item(94,r'求等差級數 $8+10+12+\cdots+208$ 的和＝＿＿＿＿。')
item(95,r'如圖，橫列有9個方格，直列有7個方格。若將每個方格內都填入一個數字，使得橫列方格內的數字由左到右成等差數列，直列方格內的數字由上到下也成等差數列。已知共同方格內的數字是42，求 $a-b=$＿＿＿＿。',svg=crossword95())
item(96,r'有一個等比數列為 $\sqrt5$、$-5$、$5\sqrt5$、……，求此數列的第9項＝＿＿＿＿。')

def write():
    for r in rows:
        if r['id']=='zh-106-1-1-7-fill-3':r.update(sourceIssue='原稿以中午12時為基準卻把上午8時記為+8，題意矛盾；忠實轉寫但不供組卷。',usable=False)
        if r['id']=='zh-106-1-1-7-fill-5':r.update(sourceIssue='原稿印為「且的中點」，中點主體缺詞；忠實轉寫但不供組卷。',usable=False)
    for row in rows:
        for b in row['blocks']:
            if b['type']=='text':b['text']=b['text'].replace('\\n','\n')
    (ROOT/'transcribed-zhonghua-early.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
    print('verified transcriptions',len(rows))
if __name__=='__main__':write()
