"""Complete visual transcription of requested Zhonghua 111/1/2 grade-8 paper."""
from pathlib import Path
from html import escape
import json,hashlib
R=Path(__file__).resolve().parent
PID='1iyB3B1cD03i2Y7-dfLBsGr5ecMVdWb6F'
PDF=R/'requested-20261114'/f'{PID}.pdf'
SHA=hashlib.sha256(PDF.read_bytes()).hexdigest()
assert SHA=='2d49a893e0d09acab15c64579e41a4f8cd3b4fd223cb181bf6f09a636f442de1'
C=[];T=[]
def text(s):return {'type':'text','text':s}
def svg(content,w,h):return {'type':'svg','svg':f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-10 -10 {w+20} {h+20}" role="img"><g font-family="serif" font-size="15" fill="#111" stroke-linecap="round" stroke-linejoin="round">{content}</g></svg>'}
def label(x,y,s,size=15):return f'<text x="{x}" y="{y}" font-size="{size}">{escape(s)}</text>'
def line(x,y,u,v,dash=None):return f'<line x1="{x}" y1="{y}" x2="{u}" y2="{v}" stroke="#111" stroke-width="1.4"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>'
def path(d,fill='none',color='#111',dash=None):return f'<path d="{d}" fill="{fill}" stroke="{color}" stroke-width="1.4"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>'
def Q(n,page,rect,difficulty,*blocks,kind='fill'):
 qid=f'zh-111-1-2-8-{kind}-{n}'
 C.append({'id':qid,'paperId':PID,'sourceSha256':SHA,'page':page,'rect':rect,'type':kind,'number':f'填充{n}' if kind=='fill' else f'非選{n}','difficulty':difficulty,'reviewed':True})
 T.append({'id':qid,'blocks':[text(b) if isinstance(b,str) else b for b in blocks],'verified':True,'sourceSha256':SHA})

altitude=svg(line(35,200,285,200)+line(35,200,195,80)+line(195,80,285,200)+line(195,80,195,200)+path('M187.8 85.4L193.2 92.6L200.4 87.2')+path('M195 191H204V200')+path('M35 206Q160 260 285 206')+label(187,69,'A')+label(16,208,'B')+label(290,208,'C')+label(188,221,'D')+label(91,125,'24')+label(151,253,'30'),325,270)
numberline=svg(line(35,180,330,180)+path('M330 180L321 175L321 185Z','#111')+line(180,180,240,180)+line(240,180,240,120)+line(180,180,240,120)+line(240,120,197.574,77.574)+line(180,180,197.574,77.574)+path('M197.574 77.574A103.923 103.923 0 0 0 76.077 180','none','#1296e8','4 4')+path('M232 180V172H240')+path('M234.343 125.657L228.686 120L234.343 114.343')+label(173,201,'O')+label(233,201,'A')+label(247,119,'B')+label(196,67,'C')+label(69,201,'D')+label(247,155,'1')+label(222,89,'1'),355,220)
wall=svg(line(45,200,225,200)+line(225,200,225,30)+line(80,200,225,30),255,225)
baseball=svg(path('M15 160C15 -40 345 -40 345 160')+path('M87 118Q180 22 273 118')+line(35,90,180,235)+line(325,90,180,235)+path('M180 235L95 150L180 65L265 150Z')+''.join(path(f'M{x} {y-5}L{x+5} {y}L{x} {y+5}L{x-5} {y}Z','white') for x,y in [(180,235),(95,150),(180,65),(265,150)])+path('M165 163A20 20 0 1 1 195 163')+'<rect x="172" y="151" width="16" height="4" fill="white" stroke="#111"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="5"/>'+label(tx,ty,s,20) for x,y,tx,ty,s in [(75,60,8,65,'左翼手'),(180,25,150,52,'中堅手'),(285,60,300,65,'右翼手'),(125,100,55,99,'游擊手'),(235,100,250,99,'二壘手'),(80,140,10,145,'三壘手'),(280,140,295,145,'一壘手'),(180,145,160,185,'投手'),(200,228,220,230,'打者'),(180,267,160,295,'捕手')]),390,315)

Q(1,0,[40,214,372,239],'easy',r'已知 $\sqrt7=2.646$，則 $\sqrt{28}$ 大約等於＿＿。')
Q(2,0,[40,295,372,322],'easy',r'計算 $3\sqrt6\times(-2\sqrt7)=$ ＿＿。')
Q(3,0,[40,378,372,403],'medium',r'計算 $3\sqrt{125}\times(-\sqrt2)+5\sqrt{10}=$ ＿＿。')
Q(4,0,[40,485,372,530],'medium',r'有理化分母並計算根式 $\dfrac{3\sqrt2+2}{\sqrt2-1}=$ ＿＿。')
Q(5,0,[40,626,372,651],'easy',r'計算 $7\sqrt3-5\sqrt3=$ ＿＿。')
Q(6,0,[40,708,372,856],'medium',r'如圖，直角三角形 $ABC$ 中，$\overline{AD}$ 為斜邊上的高，且 $\overline{AB}=24$，$\overline{BC}=30$，求斜邊上高 $\overline{AD}=$ ＿＿。',altitude)
Q(7,0,[40,912,372,962],'easy',r'已知直角三角形的一股長為 $6$，斜邊長為 $7$，另一股長為＿＿。')
Q(8,0,[389,152,734,330],'medium',r'如圖，$O$ 點為數線上的原點，$A$ 點的坐標為 $1$，在直角三角形 $OAB$ 與直角三角形 $OBC$ 中，$\overline{AB}=\overline{BC}=1$，若數線上有一點 $D$，且 $\overline{OD}=\overline{OC}$，則 $D$ 點的坐標為＿＿。',numberline)
Q(9,0,[389,382,734,430],'easy',r'已知坐標平面上 $R(-3,5)$、$S(3,2)$ 兩點，求 $\overline{RS}$ 的長度為＿＿。')
Q(10,0,[389,489,734,750],'medium',r'阿慶老師想要將一根 $1.5$ 公尺的竹竿擺放在牆邊，與牆面、地面形成一個直角三角形，且竹竿底部離牆面 $0.9$ 公尺。一段時間後，竹竿忽然往下滑動到竹竿底部距離牆面底部 $1.2$ 公尺後停止，此時竹竿頂部下滑了＿＿公尺。',wall)
Q(11,0,[389,760,734,814],'medium',r'若 $12x^2-x-6$ 可以被因式分解成 $(4x-3)(ax+b)$，則 $a+b=$ ＿＿。')
Q(12,0,[389,870,734,898],'easy',r'因式分解 $x-3x^2=$ ＿＿。')
Q(13,0,[389,952,734,985],'easy',r'因式分解 $(5x-3)^2-(5x-3)(4x-5)=$ ＿＿。')
Q(14,1,[40,58,374,105],'medium',r'將 $49x^2-ax+25$ 因式分解，可得 $(7x-b)^2$ 的型式。若 $a$ 為正整數，則 $b$ 的值是＿＿。')
Q(15,1,[40,162,374,238],'easy',r'已知 $(x+3)(4x-3)=4x^2+9x-9$，試問下列的式子中，$4x^2+9x-9$ 的因式有哪些？答：＿＿。',{'type':'options','items':[r'$4x^2+9x-9$',r'$4x-3$',r'$x+3$',r'$4x+3$']})
Q(16,1,[40,294,374,320],'easy',r'因式分解 $x^2+2x-35=$ ＿＿。')
Q(17,1,[40,378,374,405],'easy',r'因式分解 $-6x^2-15x-9=$ ＿＿。')
Q(18,1,[40,465,374,512],'hard',r'因式分解 $(x-1)(x-2)(x-3)(x-4)-120=$ ＿＿。')
Q(19,1,[40,573,374,669],'medium','利用平方差、和的平方或差的平方公式，在下列空格中填入適當的正數或符號：',r'$4x^2+12x+(\underline{\qquad})$',r'$=(2x)^2+2\cdot2x\cdot(\underline{\qquad})+(\underline{\qquad})^2$',r'$=[2x+(\underline{\qquad})]^2$')
Q(20,1,[40,730,374,776],'hard',r'已知 $x$、$y$ 皆為整數且 $0<x<y$，若 $\sqrt{369}=\sqrt x+\sqrt y$，則 $x+y=$ ＿＿。')
Q(21,1,[40,837,374,888],'medium',r'已知一正方形與一正三角形的周長相等，且該三角形面積為 $\sqrt3$，則該正方形面積為＿＿。')
Q(22,1,[40,945,374,994],'hard',r'已知直角三角形的三邊長是 $a$、$a-b$、$a+b$，且 $a$、$b$ 為整數，則這個直角三角形的的最小面積是＿＿。')
Q(1,1,[389,217,734,260],'hard',r'化簡 $\dfrac{8-\sqrt6-\sqrt{10}+2\sqrt{15}}{\sqrt5+\sqrt3-\sqrt2}$。',kind='written')
baseball_shared=r'某棒球場是每邊 $90$ 英尺的正方形場地，每一個角上放一白色包墊，就是壘。補手所在之處稱為本壘，由本壘順序逆時針數，其它壘分別稱為一、二、三壘。'
Q('2-1',1,[389,428,734,738],'medium',baseball_shared,baseball,'一壘到三壘之間的距離為多少英尺？',kind='written')
C[-1].update(number='2(1)',parentNumber=2,originalSubnumber=1)
Q('2-2',1,[389,428,734,936],'hard',baseball_shared,baseball,r'若一位跑者由二壘跑向三壘的途中，就被三壘手封殺，此時本壘補手與跑者的距離為 $102$ 英尺，則該跑者被封殺前跑了多遠？',kind='written')
C[-1].update(number='2(2)',parentNumber=2,originalSubnumber=2)
assert len(C)==25 and len(T)==25 and len({q['id'] for q in C})==25
(R/'curated-requested-zh111-1-2-8.json').write_text(json.dumps(C,ensure_ascii=False,indent=2),encoding='utf8')
(R/'transcribed-requested-zh111-1-2-8.json').write_text(json.dumps(T,ensure_ascii=False,indent=2),encoding='utf8')
print('Saved 22 fill questions + 3 written questions; baseball subquestions independently selectable.')
