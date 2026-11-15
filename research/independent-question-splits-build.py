"""Explicitly reviewed standalone subquestions. Does not modify the original bank."""
import json,pathlib,collections
R=pathlib.Path(__file__).resolve().parent
source=json.loads((R.parent/'public/data/questions.json').read_text(encoding='utf8'))
bank={q['id']:q for q in source};splits=[]
def plan(parentId,reason,children):
    p=bank[parentId]
    assert p.get('typesetVerified') and p.get('reviewed')
    splits.append({'parentId':parentId,'reason':reason,'children':[{'suffix':str(i),'blocks':[{'type':'text','text':t}],'difficulty':level,'sourceNumber':f'{p["number"]}({i})'} for i,(t,level) in enumerate(children,1)]})

plan('ld-110-1-1-8-fill-1','四個數值計算式各自給定全部資料，答案彼此無關。',[
(r'求 $299^2$ 的值：＿＿＿＿。','easy'),
(r'求 $\frac{285^2-115^2}{285^2-230\times285+115^2}$ 的值：＿＿＿＿。','medium'),
(r'求 $\sqrt{4.41}$ 的值：＿＿＿＿。','easy'),
(r'求 $995^2-\sqrt{(-25)^2}$ 的值：＿＿＿＿。','medium')])
plan('ld-110-1-1-8-fill-4','四式為互不依賴的多項式加、乘、除與化簡，各式已含全部必要條件。',[
(r'計算 $(5+2x^2+3x)+(-2+x^2+x)=$＿＿＿＿。','easy'),
(r'計算 $3x(5x-8)=$＿＿＿＿。','easy'),
(r'計算 $(24x^2+4x)\div(4x)=$＿＿＿＿。','easy'),
(r'計算 $(2x+5)^2-(2x-5)^2-3x(x-7)=$＿＿＿＿。','medium')])
plan('ld-112-1-2-7-fill-10','兩個指數空格各自由本式決定，沒有共同未知數的連立條件或前題結果依賴。',[
(r'在空格中填入適當的數：$4^5\times4^3\div(4^2)^3=4^{\square}$，$\square=$＿＿＿＿。','easy'),
(r'在空格中填入適當的數：$6^8\div(2^2\times3^2)=6^{\square}$，$\square=$＿＿＿＿。','easy')])
plan('ld-112-1-2-7-fill-11','六個分數算式互不依賴；每個子題均完整複製化為最簡分數的作答要求。',[
(r'計算下式的值，並化成最簡分數：$-\frac53-(-\frac16)=$＿＿＿＿。','easy'),
(r'計算下式的值，並化成最簡分數：$-\frac47-(\frac{13}{11}-1\frac47)=$＿＿＿＿。','medium'),
(r'計算下式的值，並化成最簡分數：$[(\frac38)\times(-\frac{32}9)]^0=$＿＿＿＿。','easy'),
(r'計算下式的值，並化成最簡分數：$(-\frac7{13})\times3\frac57\div(-2\frac23)=$＿＿＿＿。','medium'),
(r'計算下式的值，並化成最簡分數：$\frac{11^2}{4^3}\times[(\frac{11}3)^2]^3\times(\frac6{11})^7=$＿＿＿＿。','hard'),
(r'計算下式的值，並化成最簡分數：$-9\frac14-\frac23\times[\frac78-(\frac12-\frac34)]=$＿＿＿＿。','hard')])
plan('nc-110-1-1-8-fill-15','兩個平方差計算式沒有共用數值或答案；每題保留原本提供的平方差公式。',[
(r'利用平方差公式 $(a+b)(a-b)=a^2-b^2$，計算 $402\times398$ 的值：＿＿＿＿。','easy'),
(r'利用平方差公式 $(a+b)(a-b)=a^2-b^2$，計算 $56^2-44^2$ 的值：＿＿＿＿。','easy')])
plan('nc-110-1-1-8-fill-19','四個數各自求平方根，不共用前題結果。',[
('求 100 的平方根：＿＿＿＿。','easy'),('求 0.0196 的平方根：＿＿＿＿。','medium'),('求 1 的平方根：＿＿＿＿。','easy'),('求 6 的平方根：＿＿＿＿。','easy')])
plan('nc-110-1-1-8-fill-20','兩個根式值各自由本式決定。',[
(r'計算 $-\sqrt{400}$ 的值：＿＿＿＿。','easy'),
(r'計算 $\sqrt{3^2\times5^2\times7^2}$ 的值：＿＿＿＿。','easy')])

plan('1C8OHjkXiEXjJwe0tFeSHI_eIDbPVySAS-fill-基礎填充-1','四個填式/多項式計算各自獨立；不需要借用其他子題的任何條件。',[
(r'填入適當的式子：$6x\cdot(\underline{\qquad})=48x^2$。','easy'),
(r'填入適當的式子：$(3x^2-2x^3+5)-(7x^3-3x+6)=$＿＿＿＿。','medium'),
(r'填入適當的式子：$(2x^2+5)(x-7)=$＿＿＿＿。','medium'),
(r'填入適當的式子：$(x+10)^2-(x-10)^2=$＿＿＿＿。','easy')])
plan('12qTzBXv1TN3qhRIt0gGZSugu3m7UQzh1-fill-超基本填充-3','兩個比例題分別提出不同的等式；只共用一般非零條件，已完整複製至每個子題。',[
(r'設 $x$、$y$ 皆不為 $0$。若 $7x=4y$，則 $x:y=$＿＿＿＿。','easy'),
(r'設 $x$、$y$ 皆不為 $0$。若 $\frac{x}7=\frac{y}4$，則 $x:y=$＿＿＿＿。','easy')])
plan('16M1pIRwvx2OortGNbafUIAN2NgpSx5f0-fill-填充-1','兩個數列各自完整呈現，並非同一數列的連續提問。',[
(r'觀察數列的規律，在空格中填入適當的數：$25,36,49,64,81,$ ＿＿。','easy'),
(r'觀察數列的規律，在空格中填入適當的數：$2,3,5,8,13,21,34,55,$ ＿＿。','easy')])
plan('16M1pIRwvx2OortGNbafUIAN2NgpSx5f0-fill-填充-2','兩個等差數列分別求公差，數列資料不同且無前後相依。',[
(r'求等差數列 $2,4,6,8,10$ 的公差：＿＿＿＿。','easy'),
(r'求等差數列 $4a+b,\ a+3b,\ -2a+5b,\ -5a+7b$ 的公差：＿＿＿＿。','medium')])
plan('1apVXWg6tdPwOUMCRnKeC7ZG5pgs6X2kR-fill-填充-1','三個觀察規律填數題各有完整而不同的數列。',[
(r'觀察數列的規律，在空格中填入適當的數：$1,4,7,$ ＿＿$,13,16$。','easy'),
(r'觀察數列的規律，在空格中填入適當的數：$1,4,16,$ ＿＿$,256,1024$。','easy'),
(r'觀察數列的規律，在空格中填入適當的數：$1,1,2,3,5,$ ＿＿$,13,21,34$。','easy')])
plan('1fZgUOvgrGdIYaDepzfHHDlItMPfhbJSc-written-計算-1','兩組排序題使用不同的數值集合，每組均完整帶入自身資料與排序要求。',[
(r'將 $-3.5$、$0$、$-6$、$-(-\frac17)$、$|-8|$ 這五個數由大至小排列。','easy'),
(r'$A=9.1\times10^{-4}$、$B=5.6\times10^{-3}$、$C=6.08\times10^{-6}$、$D=3.2\times10^{-4}$。請將 $A$、$B$、$C$、$D$ 依大小順序排列。','medium')])
plan('1ZASDtBiRnEoXShkcBvn-r9gbCo6txlYo-fill-填充-2','三個數值計算式各自給定全部數字與符號。',[
(r'計算 $295^2-5^2=$＿＿＿＿。','easy'),
(r'計算 $497^2+2\times497\times3+3^2=$＿＿＿＿。','easy'),
(r'計算 $\sqrt{121}+\sqrt{(-6)^2}-(\sqrt5)^2=$＿＿＿＿。','medium')])
plan('1ZASDtBiRnEoXShkcBvn-r9gbCo6txlYo-fill-填充-3','三個多項式計算式互不依賴。',[
(r'計算 $(5x^2+2x+4)+(x-3)=$＿＿＿＿。','easy'),
(r'計算 $(3x+8x^2+6)-(4x^2+6)=$＿＿＿＿。','easy'),
(r'計算 $(x+4)(3x-2)=$＿＿＿＿。','medium')])
plan('1JjJd7L0_nBPPPFPg4IcbaFW3DhuyHAAa-fill-填充-1','五個多項式算式各自獨立，每題保留原本的展開合併及降冪排列要求。',[
(r'計算 $(3x^2+7)+(8x+x^2)=$＿＿＿＿。（展開合併後請依降冪排列書寫）','easy'),
(r'計算 $(4x^2+9)-(3x^2+1-3x)=$＿＿＿＿。（展開合併後請依降冪排列書寫）','easy'),
(r'計算 $(x-2)(x+2)=$＿＿＿＿。（展開合併後請依降冪排列書寫）','easy'),
(r'計算 $(2x-3)^2=$＿＿＿＿。（展開合併後請依降冪排列書寫）','easy'),
(r'計算 $(4x^2+7)(3-x)=$＿＿＿＿。（展開合併後請依降冪排列書寫）','medium')])
plan('1JjJd7L0_nBPPPFPg4IcbaFW3DhuyHAAa-written-綜合-2','兩個利用乘法公式的數值計算式沒有連續推理或共用資料。',[
(r'利用乘法公式計算 $\dfrac{7470^2+2\times7470\times1983+1983^2}{7470^2-1983^2}$ 的值。','hard'),
(r'利用乘法公式計算 $\sqrt{\dfrac14-678+678^2}$ 的值。','hard')])
plan('1j7D2rr1uOywcRO0fDNN3twKp5MDomb5--fill-基礎填充-2','四個根式計算各自獨立。',[
(r'計算 $\sqrt{\dfrac{16}{49}}=$＿＿＿＿。','easy'),
(r'計算 $\sqrt{1225}=$＿＿＿＿。','medium'),
(r'計算 $\sqrt{2^2\times3^2\times7^2}=$＿＿＿＿。','easy'),
(r'計算 $-\sqrt{3^6}=$＿＿＿＿。','easy')])
plan('1j7D2rr1uOywcRO0fDNN3twKp5MDomb5--fill-基礎填充-3','三個乘法公式數值題沒有共用未知數或答案。',[
(r'利用乘法公式計算 $997^2+2\times997\times3+3^2=$＿＿＿＿。','easy'),
(r'利用乘法公式計算 $9.9^2=$＿＿＿＿。','easy'),
(r'利用乘法公式計算 $67^2-33^2=$＿＿＿＿。','easy')])
plan('1j7D2rr1uOywcRO0fDNN3twKp5MDomb5--fill-基礎填充-4','四個多項式算式互不相依。',[
(r'計算 $(4x+1)+(2x^2+6x-8)=$＿＿＿＿。','easy'),
(r'計算 $(7-x^2)-(2x-4x^3+6)=$＿＿＿＿。','medium'),
(r'計算 $(2x-1)(-3x+5)=$＿＿＿＿。','medium'),
(r'計算 $(-14x^2)\div49x=$＿＿＿＿。','easy')])
plan('1j2SHwbR9iEF5tfo1g-PvmfyCLHYfrcJv-fill-基礎填充-1','六個根式/平方根題均有自己的完整被運算數，重複數值並非答案相依。',[
(r'計算 $(\sqrt{31})^2=$＿＿＿＿。','easy'),
(r'計算 $\sqrt{16}=$＿＿＿＿。','easy'),
(r'計算 $\sqrt{5.76}=$＿＿＿＿。','easy'),
(r'計算 $\sqrt{2\dfrac14}=$＿＿＿＿。','easy'),
(r'求 $\sqrt{16}$ 的平方根：＿＿＿＿。','easy'),
(r'求 $\sqrt{2^4\times3^2\times5^2}$ 的平方根：＿＿＿＿。','medium')])
plan('1j2SHwbR9iEF5tfo1g-PvmfyCLHYfrcJv-fill-基礎填充-2','兩組比較各自給定完整數值，沒有共同未知數的條件。',[
(r'在空格中填入 $>$、$<$ 或 $=$：$-\sqrt5$ ＿＿ $-\sqrt7$。','easy'),
(r'在空格中填入 $>$、$<$ 或 $=$：$(\sqrt{\dfrac53})^2$ ＿＿ $\sqrt{2^2}$。','medium')])
plan('1fZgUOvgrGdIYaDepzfHHDlItMPfhbJSc-fill-填充-4','七個整數/指數計算式各自含有完整資料。',[
(r'計算 $(-2019)-[(-709)+(-2020)]=$＿＿＿＿。','easy'),
(r'計算 $2009\times(-37)-9\times(-37)=$＿＿＿＿。','easy'),
(r'計算 $(-24)\div[(-6)\div3]=$＿＿＿＿。','easy'),
(r'計算 $11\times(-12)\times13\times(-14)\times15\times0\times17\times(-18)-19=$＿＿＿＿。','easy'),
(r'計算 $(-13)+[(-2)-(-17)]-|-35|=$＿＿＿＿。','easy'),
(r'計算 $5^2-[(-3)^2\times(-2)^3-7^2]=$＿＿＿＿。','medium'),
(r'計算 $-30^2+(-20)^3-(-10)^4=$＿＿＿＿。','medium')])
plan('1fZgUOvgrGdIYaDepzfHHDlItMPfhbJSc-fill-填充-5','兩個科學記號轉換題各有不同且完整的數字。',[
(r'將 $60300000$ 以科學記號表示：＿＿＿＿。','easy'),
(r'將 $0.00042$ 以科學記號表示：＿＿＿＿。','easy')])
plan('zh-113-1-1-7-basic-2','五個整數計算互不依賴。',[
(r'計算 $(-12)-(-8)=$＿＿＿＿。','easy'),
(r'計算 $5+(-10)=$＿＿＿＿。','easy'),
(r'計算 $4\times(-2024)\times(-25)=$＿＿＿＿。','easy'),
(r'計算 $39\div(-3)=$＿＿＿＿。','easy'),
(r'計算 $-2^4=$＿＿＿＿。','easy')])
plan('zh-114-1-3-7-basic-3','兩個多項式化簡題互不依賴。',[
(r'化簡 $7x-(-x)=$＿＿＿＿。','easy'),
(r'化簡 $(2x-3)+(5x+4)=$＿＿＿＿。','easy')])
plan('zh-114-1-3-7-basic-4','四個一元一次方程式各自獨立求解，不是聯立方程或同一未知數的共同限制。',[
(r'解一元一次方程式 $10x=5x$。','easy'),
(r'解一元一次方程式 $x\div(-3)=-6$。','easy'),
(r'解一元一次方程式 $x+4=9$。','easy'),
(r'解一元一次方程式 $3x-1=2x-5$。','easy')])
plan('zh-114-1-3-7-fill-1','兩個代數化簡式各自包含完整的運算。',[
(r'化簡 $2(3x-4)-3(x-5)=$＿＿＿＿。','easy'),
(r'化簡 $\dfrac{3x-5}{2}-\dfrac{3x-2}{4}-1=$＿＿＿＿。','medium')])
plan('zh-114-1-3-7-fill-2','兩個不同的一元一次方程式互不相依。',[
(r'解一元一次方程式 $2(x-4)-(3x+4)=20+7x$。','medium'),
(r'解一元一次方程式 $\dfrac{x+4}{3}+0.4(2+x)=8$。','medium')])
plan('zh-113-1-1-9-fill-3','四個連比例式題各自使用獨立的假設，並非共用一組數值的連續小題；各自條件完整複製。',[
(r'設 $3x=2y=5z$，求 $x:y:z=$＿＿＿＿。','medium'),
(r'設 $x:y=3:4$，$y:z=6:5$，求 $4x:3y:2z=$＿＿＿＿。','medium'),
(r'設 $3xy=4xz=6yz$，求 $x:y:z=$＿＿＿＿。','hard'),
(r'已知 $x$、$y$、$z$ 皆不等於 $0$，若 $(x-1):(y+2):(z-3)=4:5:6$，且 $x+y+z=62$，求 $x+y-z=$＿＿＿＿。','hard')])
plan('zh-115-1-1-7-basic-4','八個整數算式互不依賴，分拆後每題仍有完整運算符號。',[
(r'計算 $7-16=$＿＿＿＿。','easy'),
(r'計算 $-31-19=$＿＿＿＿。','easy'),
(r'計算 $-42-(-11)=$＿＿＿＿。','easy'),
(r'計算 $9+(-2)\times[18-(-3)\times2]\div4=$＿＿＿＿。','medium'),
(r'計算 $0\div(-123)=$＿＿＿＿。','easy'),
(r'計算 $125\times92\times(-8)=$＿＿＿＿。','easy'),
(r'計算 $(-126)\div6\div(-3)=$＿＿＿＿。','easy'),
(r'計算 $(-1)^{10}\times2+(-3)^3\div9=$＿＿＿＿。','medium')])
plan('zh-115-1-1-7-fill-1','兩組科學記號比較各自有完整數值。',[
(r'比較大小，在空格填入 $<$、$=$ 或 $>$：$7.3\times10^8$ ＿＿ $3.1\times10^9$。','easy'),
(r'比較大小，在空格填入 $<$、$=$ 或 $>$：$2.7\times10^{-5}$ ＿＿ $8\times10^{-6}$。','medium')])
plan('zh-115-1-1-7-fill-2','兩個整數/指數運算式各自獨立。',[
(r'計算 $3^3-(-5)^2-2^6\div2^3=$＿＿＿＿。','medium'),
(r'計算 $-29\times75-29\times25+|29\times(-110)|=$＿＿＿＿。','medium')])
plan('zh-115-1-1-7-fill-3','兩個科學記號轉換題各有自己的數值。',[
(r'將 $0.00000653$ 以科學記號表示：＿＿＿＿。','easy'),
(r'將 $\dfrac1{250000}$ 以科學記號表示：＿＿＿＿。','medium')])
plan('1aDSOOkqBVHxfjza6Y2Di4qnEI_Kcr2gn-fill-基礎-5','多項式加法與分配律兩式互不依賴。',[
(r'計算 $(7x^2-4x)+(6-5x)=$＿＿＿＿。','easy'),
(r'計算 $-3x\cdot(-2x+9)=$＿＿＿＿。','easy')])
plan('1aDSOOkqBVHxfjza6Y2Di4qnEI_Kcr2gn-fill-基礎-6','三個乘法公式/帶分數計算各自使用完整且不同的數值。',[
(r'計算 $86^2+2\times14\times86+14^2=$＿＿＿＿。','easy'),
(r'計算 $54^2-46^2=$＿＿＿＿。','easy'),
(r'計算 $36\dfrac45\times10\dfrac23=$＿＿＿＿。','medium')])
plan('1wUCFV5eX0oZw3IM_zpkfB2QdFavSGydG-fill-填充-1','六個多項式或根式計算各自給定全部資料，除法題中的商式/餘式仍保留在同一子題。',[
(r'計算 $(3x^2-4x+11)-(-4x^2+x-9)=$＿＿＿＿。','easy'),
(r'計算 $(x-1)-[(8-2x^2+x)+(x^2-5+7x)]=$＿＿＿＿。','medium'),
(r'計算 $(2x-3)(2x+3)=$＿＿＿＿。','easy'),
(r'求 $(4x^2-7x+3)\div(3x-6)$ 的商式為＿＿，餘式為＿＿。','medium'),
(r'計算 $-\sqrt{169}=$＿＿＿＿。','easy'),
(r'計算 $\sqrt{2^4\times3^2\times11^2}=$＿＿＿＿。','easy')])

assert len({p['parentId'] for p in splits})==len(splits)
for p in splits:
    assert len(p['children'])>=2
    assert len({c['suffix'] for c in p['children']})==len(p['children'])
    assert all(c['difficulty'] in ('easy','medium','hard') for c in p['children'])
(R/'independent-question-splits.json').write_text(json.dumps(splits,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'parents':len(splits),'children':sum(len(p['children']) for p in splits),'netNewGenerationItems':sum(len(p['children'])-1 for p in splits),'sourceCount':len(source)},ensure_ascii=False))
