from pathlib import Path
import json,hashlib
import fitz
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).parent
SOURCE=ROOT/'requested-20261114/ld-112-1-2-8.pdf'
SHA='7b7993d35c10493b1f05c2ff079fcd5faa496b304bb85336886c139fe24192b2'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==SHA
PAPER='ld-112-1-2-8'
doc=fitz.open(SOURCE)
curated=[];transcribed=[]
OUT=ROOT/'requested-ld112-1-2-8-review';OUT.mkdir(exist_ok=True)

def figure8():
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 350 210"><path d="M40 40H300V160H40ZM40 160 125 40 300 160" fill="none" stroke="#111" stroke-width="1.6"/><path d="m117 51 11 8 8-11" fill="none" stroke="#111" stroke-width="1.2"/><g font-family="serif" font-size="21"><text x="23" y="35">A</text><text x="23" y="185">B</text><text x="301" y="185">C</text><text x="303" y="35">D</text><text x="120" y="30">E</text></g></svg>'

def figure14():
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 290 280"><path d="M40 40H240V240H40ZM40 40 150 240M40 40 240 150" fill="none" stroke="#111" stroke-width="1.6"/><g font-family="serif" font-size="21"><text x="23" y="35">A</text><text x="23" y="263">B</text><text x="243" y="263">C</text><text x="244" y="35">D</text><text x="143" y="265">M</text><text x="247" y="155">N</text></g></svg>'

def figure15():
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 290 285"><defs><pattern id="ld112hatch15" width="6" height="6" patternUnits="userSpaceOnUse"><path d="M-2 0 6 8M4-2 12 6" stroke="#444" stroke-width=".8"/></pattern></defs><rect x="40" y="40" width="200" height="200" fill="url(#ld112hatch15)" stroke="#111" stroke-width="1.6"/><path d="M40 140 80 40 180 80 140 180Z" fill="white" stroke="#111" stroke-width="1.6"/><g font-family="serif" font-size="21"><text x="23" y="35">A</text><text x="23" y="264">B</text><text x="243" y="264">C</text><text x="243" y="35">D</text><text x="20" y="145">P</text><text x="133" y="204">Q</text><text x="187" y="84">R</text><text x="75" y="31">S</text></g></svg>'

def figurew3():
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 290 285"><path d="M40 40H240V240H40ZM40 183 183 240 240 97 97 40Z" fill="none" stroke="#111" stroke-width="1.6"/><g font-family="serif" font-size="21"><text x="23" y="35">A</text><text x="23" y="264">B</text><text x="243" y="264">C</text><text x="243" y="35">D</text><text x="19" y="188">P</text><text x="176" y="265">Q</text><text x="246" y="102">R</text><text x="91" y="31">S</text></g></svg>'

def add(number,page,box,text,difficulty='medium',kind='fill',svg=None,sourceIssue=None):
    # box uses the exact supplied 966x1340 review PNG coordinate system.
    pw,ph=doc[page].rect.width,doc[page].rect.height
    x0,y0,x1,y1=box;rect=[round(x0*pw/966,3),round(y0*ph/1340,3),round(x1*pw/966,3),round(y1*ph/1340,3)]
    safe_number=str(number).replace('(','-').replace(')','')
    qid=f'{PAPER}-{kind}-{safe_number}'
    curated.append({'id':qid,'paperId':PAPER,'page':page,'rect':rect,'type':kind,'number':number,'difficulty':difficulty,'reviewed':True,'school':'羅東國中','sourceSha256':SHA,'difficultyBasis':'編輯依運算步驟、概念整合與圖表閱讀判定；非官方難度','sourceScan':True})
    row={'id':qid,'blocks':[{'type':'text','text':text.replace('\\n','\n')}],'verified':True,'sourceSha256':SHA}
    if svg:row['diagramSvg']=svg
    if '(' in str(number):
        parent,sub=str(number).replace(')','').split('(')
        curated[-1].update(sourceNumber=str(number),parentNumber=int(parent),originalSubnumber=int(sub))
    if sourceIssue:row['sourceNote']=sourceIssue
    transcribed.append(row)
    sourcepng=Image.open(ROOT/f'requested-20261114/{PAPER}-p{page+1}.png')
    crop=sourcepng.crop(box);crop.save(OUT/f'{kind}-{number}.png')

add('1(1)',0,[85,236,425,282],r'計算並化簡至最簡根式：$2\sqrt5\times5\sqrt3=$＿＿＿＿。','easy')
add('1(2)',0,[85,290,490,334],r'計算並化簡至最簡根式：$3\sqrt6+4\sqrt6-5\sqrt6=$＿＿＿＿。','easy')
add('1(3)',0,[85,340,470,400],r'計算並化簡至最簡根式：$\sqrt{\frac{15}2}\div\sqrt{\frac38}=$＿＿＿＿。','easy')
add('1(4)',0,[85,410,465,468],r'計算並化簡至最簡根式：$\frac{\sqrt{50}+\sqrt{32}}{\sqrt2}=$＿＿＿＿。','easy')
add(2,0,[55,484,850,525],r'矩形的周長為 $28$ cm，若長比寬多 $2$ cm，則此矩形的對角線長＝＿＿＿＿cm。')
add(3,0,[55,540,800,584],r'已知坐標平面上的兩點 $A(-2,7)$ 和 $B(3,3)$，則 $\overline{AB}=$＿＿＿＿。','easy')
add(4,0,[55,595,915,679],r'$\triangle ABC$ 中，若 $\angle ABC=90^\circ$，$\overline{AB}=3$、$\overline{AC}=4$，且 $\overline{BD}$ 為 $\triangle ABC$ 斜邊上的高，求 $\overline{BD}=$＿＿＿＿。')
add('5(1)',0,[85,712,450,754],r'因式分解：$4x^2+12x=$＿＿＿＿。','easy')
add('5(2)',0,[85,763,650,807],r'因式分解：$(2x-3)(3x+1)-(2x-3)(2x+3)=$＿＿＿＿。')
add('5(3)',0,[85,816,480,859],r'因式分解：$25x^2-20x+4=$＿＿＿＿。','easy')
add('5(4)',0,[85,866,485,910],r'因式分解：$x^2-18x+56=$＿＿＿＿。','easy')
add('5(5)',0,[85,915,495,959],r'因式分解：$39x^2-5x-14=$＿＿＿＿。')
add(6,0,[55,972,735,1010],r'$x^2-5x+6$ 可因式分解成 $(x+a)(x+b)$，則 $a+b=$＿＿＿＿。','easy')
add(7,0,[55,1013,645,1075],r'計算 $\frac{2\sqrt{48}}3-\sqrt{\frac43}+\sqrt{16\frac13}=$＿＿＿＿。')
add(8,0,[55,1078,910,1171],r'如右圖，四邊形 $ABCD$ 是一個矩形，$\overline{BE}\perp\overline{CE}$，$\overline{BE}=4$、$\overline{BC}=7$，則矩形 $ABCD$ 的面積為＿＿＿＿平方公分。','hard',svg=figure8())
add(9,0,[55,1173,855,1216],r'若 $6x^2-ax-2$ 與 $3x^2-8x+b$ 有共同的因式 $3x-2$，則 $a+b=$＿＿＿＿。')
add(10,0,[55,1220,760,1267],r'因式分解 $5(4x^2-9)-3(4x^2+12x+9)=$＿＿＿＿。')
add(11,1,[55,63,915,140],r'有一矩形的長、寬分別為 $ax+b$ 及 $cx-d$，面積為 $12x^2-19x-21$，其中 $a$、$b$、$c$、$d$ 皆為正整數，則 $a+b+c+d=$＿＿＿＿。')
add(12,1,[55,148,655,189],r'若 $4x^2-3x-10$ 為質數，則此時 $x=$＿＿＿＿。',sourceIssue='原稿未明列x為整數；忠實保留原題條件，未自行補入。')
add(13,1,[55,194,695,236],r'若 $2x^2+x-6$ 與 $2x^2-x+a$ 有公因式，則 $a=$＿＿＿＿。')
# The figure for question14 is placed alongside questions12–14 in the scan.
# Use a text-only crop for its question body; pure SVG below retains its full figure.
add(14,1,[55,240,705,341],r'如右圖，正方形 $ABCD$ 的邊長為 $21$，$\overline{AM}$ 與 $\overline{AN}$ 將此正方形面積分成三等份，試求 $\overline{AN}=$＿＿＿＿。','hard',svg=figure14())
curated[-1]['sourceFigureRect']=[round(715*doc[1].rect.width/966,3),round(145*doc[1].rect.height/1340,3),round(878*doc[1].rect.width/966,3),round(287*doc[1].rect.height/1340,3)]
add(15,1,[55,350,900,476],r'如右圖，$ABCD$、$PQRS$ 皆為正方形，$\overline{AS}:\overline{SD}=1:4$，$P$ 為 $\overline{AB}$ 的中點，若 $\overline{AB}=10$，則斜線部分的面積為＿＿＿＿。','hard',svg=figure15())
add(1,1,[55,523,440,605],r'計算並化簡 $\frac{1+\sqrt3+\sqrt2}{\sqrt3+\sqrt2}$。',kind='written')
add(2,1,[55,755,885,805],r'設多項式 $A=x^2-2x-8$，多項式 $B=x^2+3x+2$，利用十字交乘法因式分解 $3A-B$。',kind='written')
add(3,1,[55,958,910,1214],r'如圖，正方形 $ABCD$，其邊長為 $\sqrt{147}$，在其四邊上分別取 $\overline{AP}=\overline{BQ}=\overline{CR}=\overline{DS}=\sqrt{75}$，試求正方形 $PQRS$ 的對角線 $\overline{PR}$ 為多少？','hard',kind='written',svg=figurew3())

(ROOT/'curated-requested-ld112-1-2-8.json').write_text(json.dumps(curated,ensure_ascii=False,indent=2),encoding='utf8')
(ROOT/'transcribed-requested-ld112-1-2-8.json').write_text(json.dumps(transcribed,ensure_ascii=False,indent=2),encoding='utf8')
font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',20)
for start in range(0,len(curated),6):
    tiles=[]
    for q in curated[start:start+6]:
        pic=Image.open(OUT/f'{q["type"]}-{q["number"]}.png');pic.thumbnail((880,510))
        tile=Image.new('RGB',(920,pic.height+45),'white');ImageDraw.Draw(tile).text((12,10),q['id'],font=font,fill='black');tile.paste(pic,(15,42));tiles.append(tile)
    totalh=sum(max(tiles[j].height,tiles[j+1].height if j+1<len(tiles) else 0) for j in range(0,len(tiles),2))
    sheet=Image.new('RGB',(1840,totalh),'#ddd');y=0
    for j in range(0,len(tiles),2):
        sheet.paste(tiles[j],(0,y))
        if j+1<len(tiles):sheet.paste(tiles[j+1],(920,y))
        y+=max(tiles[j].height,tiles[j+1].height if j+1<len(tiles) else 0)
    sheet.save(OUT/f'sheet-{start//6+1}.png')
print('curated',len(curated),'transcribed',len(transcribed))
