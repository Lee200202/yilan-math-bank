"""Content-only first-pass unit tags, followed by explicit per-question review overrides.
Never consult year, grade, semester, exam, paper ID or filename to infer a unit.
"""
from pathlib import Path
from collections import Counter
from html import unescape
import hashlib,json,re,xml.etree.ElementTree as ET
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr,standard_transformations,implicit_multiplication_application
R=Path(__file__).resolve().parent
def U(g,s,c,n):return f'nanyi-{g}-{s}-{c}-{n}'
def txt(q):
 a=[]
 for b in q.get('blocks',[]):
  if b['type']=='text':a.append(b['text'])
  elif b['type']=='options':a.extend(b['items'])
  elif b['type']=='table':a.extend(str(v) for row in b['rows'] for v in row)
  elif b['type']=='svg':a.extend(re.findall(r'<text\b[^>]*>(.*?)</text>',b['svg'],re.S))
 if q.get('diagramSvg'):a.extend(re.findall(r'<text\b[^>]*>(.*?)</text>',q['diagramSvg'],re.S))
 return unescape(' | '.join(a))
def factor_unit(s):
 ms=re.findall(r'\$([^$]+)\$',s)
 f=next((m.split('=')[0] for m in ms if re.search(r'[xya-b]',m)),None)
 if not f:return U(8,1,3,1)
 if '\\' in f:return U(8,1,3,1)
 try:
  e=parse_expr(f.replace('^','**').replace('{','(').replace('}',')'),transformations=standard_transformations+(implicit_multiplication_application,))
  sy=e.free_symbols
  if len(sy)==1:
   var=next(iter(sy));p=sp.Poly(sp.expand(e),var)
   if p.degree()==2 and p.TC()!=0 and len(p.terms())==3:
    fac=sp.factor_list(e)[1]
    if not any(k>1 for _,k in fac):return U(8,1,3,2)
  return U(8,1,3,1)
 except Exception:return U(8,1,3,1)
def assign(s):
 def ret(uid,reason,*secondary):return [uid,*[x for x in secondary if x!=uid]],reason
 hasroot='\\sqrt' in s or '√' in s
 if re.search(r'四分位|盒狀|Q_[13]|Q[13]|全距|四等分.*資料',s):return ret(U(9,2,2,1),'題幹要求四分位數、盒狀圖或全距等資料分布指標。')
 if re.search(r'機率|樣本空間|擲.*骰|抽.*球.*可能',s):return ret(U(9,2,2,2),'題幹實際描述機率或隨機試驗。')
 if re.search(r'相對次數|累積次數|累積相對|累積.*折線',s):return ret(U(8,1,5,1),'題幹明示相對或累積次數分配圖表。')
 if re.search(r'平均數|中位數|眾數',s):return ret(U(7,2,6,2),'題幹要求平均數、中位數或眾數的資料分析。')
 if re.search(r'次數分配|直方圖|長條圖|圓形圖|扇形圖|折線圖',s):return ret(U(7,2,6,1),'題幹明示統計圖表，未要求四分位或累積次數。')
 if re.search(r'二次函數|拋物線',s):
  if re.search(r'最大值|最小值|最高|最低|頂點坐標.*為＿＿',s):return ret(U(9,2,1,2),'題幹考二次函數頂點或最大、最小值。',U(9,2,1,1))
  return ret(U(9,2,1,1),'題幹明示二次函數／拋物線及圖形。')
 if re.search(r'等差級數|級數|前.*項.*和|a_1.*S_|S_n',s):return ret(U(8,2,1,2),'題幹要求數列項的和或明示等差級數。')
 if re.search(r'等比數列',s):return ret(U(8,2,1,3),'題幹明示等比數列。')
 if re.search(r'等差|數列|公差',s):return ret(U(8,2,1,1),'題幹明示數列或公差／等差數列。')
 if re.search(r'一次函數|函數',s):return ret(U(8,2,2,1),'題幹明示函數及其圖形或函數值。')
 if re.search(r'三視圖',s):return ret(U(7,2,1,1),'題幹要求三視圖及立體模型的視圖。')
 if re.search(r'連比|x:y:z|x：y：z|a:b:c|a：b：c|x:y=.+x:z=|x:y=.+y:z=',s):return ret(U(9,1,1,1),'題幹要求三量連比或由兩組比整合成連比。')
 if re.search(r'相似|\\sim|縮放|縮小.*倍|放大.*倍',s):
  if re.search(r'面積|影長|實際|比例尺|測量|應用|縮放|縮小|放大',s):return ret(U(9,1,1,4),'題幹以相似／縮放處理面積、測量或倍率的應用。',U(9,1,1,3))
  return ret(U(9,1,1,3),'題幹明示相似形或對應角、對應邊的相似判定。')
 if re.search(r'圓周角|圓心角|弧.*度|半圓.*角',s):return ret(U(9,1,2,2),'題幹考弧、圓周角或圓心角。')
 if re.search(r'切線|切點|割線|圓心.*距離',s):return ret(U(9,1,2,1),'題幹考點、直線與圓的位置或切線。')
 if re.search(r'外心|內心|重心',s):return ret(U(9,1,3,2),'題幹明示三角形外心、內心或重心。')
 if re.search(r'全等',s):return ret(U(8,2,3,4) if re.search(r'求|證明|長度|面積',s) else U(8,2,3,3),'題幹實際涉及三角形全等判定或應用。')
 if re.search(r'尺規|作圖',s) and not re.search(r'坐標|座標',s):return ret(U(8,2,3,2),'題幹明示尺規作圖。')
 if re.search(r'內角|外角',s) and not re.search(r'三角形.*面積',s):return ret(U(8,2,3,1),'題幹要求多邊形內角或外角。')
 if re.search(r'三等分|四等分|中點|\\parallel|平行',s) and re.search(r'比例|面積比|:[0-9a-z]|:\\|比.*[0-9]|\\dfrac|\\triangle',s) and not re.search(r'平行四邊形|特殊四邊形',s):return ret(U(9,1,1,2),'圖形題以平行、等分或中點條件求比例線段。')
 if re.search(r'平行四邊形',s):return ret(U(8,2,4,2),'題幹明示平行四邊形的性質。')
 if re.search(r'平行線|同位角|內錯角|同側內角',s):return ret(U(8,2,4,1),'題幹明示平行線及截線角的性質。')
 if re.search(r'對角線|斜邊|畢氏|直角三角形|竹竿|玻棒|溜滑梯|木板.*門|棒球場',s):return ret(U(8,1,2,3),'題幹要求直角三角形邊長、高、對角線或畢氏定理的應用。')
 if re.search(r'坐標平面|座標平面|直角坐標|直角座標',s) and (re.search(r'距離|長度|\\overline\{|平方|面積|正方形',s)):return ret(U(8,1,2,3),'坐標題要求兩點距離、線段長或以邊長求面積，主要使用畢氏定理。',U(7,2,3,1))
 if re.search(r'向東|向西|向南|向北',s) and re.search(r'距離|直線',s):return ret(U(8,1,2,3),'題幹把東西／南北位移組合成直線距離，主要使用畢氏定理。')
 if re.search(r'正三角形|等腰三角形|正六邊形',s) and re.search(r'面積|高|邊長',s):return ret(U(8,1,2,3),'題幹由正三角形等圖形的邊長、高或面積建立直角三角形計算。')
 if re.search(r'正方形|矩形|長方形',s) and re.search(r'\\perp|垂直|90\^|90°|坐標|座標|根號|\\sqrt',s):return ret(U(8,1,2,3),'圖形含垂直／直角或根式邊長，主要以畢氏定理求長度或面積。')
 if re.search(r'柱體|錐體|圓錐|圓柱|體積|表面積',s):return ret(U(9,2,3,1),'題幹要求立體圖形的幾何性質、體積或表面積。')
 if re.search(r'線對稱|對稱軸|摺紙|摺痕|對折',s):return ret(U(7,2,1,1),'題幹實際涉及線對稱或對折的幾何圖形。')
 if re.search(r'二元一次|聯立',s):
  if re.search(r'應用|買|賣|年齡|公尺|元|速度|每',s):return ret(U(7,2,2,3),'題幹以二元一次聯立方程式處理實際數量關係。',U(7,2,2,2))
  return ret(U(7,2,2,2),'題幹明示二元一次或聯立方程式的求解。')
 if re.search(r'不等式',s):return ret(U(7,2,5,2) if re.search(r'解|求|至少|至多',s) else U(7,2,5,1),'題幹明示一元一次不等式或其求解。')
 if re.search(r'一元二次|配方法|公式解|判別式|重根',s):
  if re.search(r'配方法|配成|公式解|判別式|重根|沒有解|根的個數',s):return ret(U(8,1,4,2),'題幹明示配方法、公式解、判別式或重根。')
  if re.search(r'應用|童軍|商品|賣價|售價|年齡|長方形.*長',s):return ret(U(8,1,4,3),'題幹以一元二次方程式處理應用數量。')
  return ret(U(8,1,4,1),'題幹明示一元二次方程式及根／解。')
 if re.search(r'完全平方式|完全平方|和的平方|差的平方|平方差',s):return ret(U(8,1,3,1),'題幹實際考完全平方或平方差等乘法公式的因式分解／配項。')
 if re.search(r'十字交乘',s):return ret(U(8,1,3,2),'題幹明示十字交乘法。')
 if '因式分解' in s:return ret(factor_unit(s),'題幹明示因式分解；依實際式型區分公因式／乘法公式與二次三項式十字交乘。')
 if re.search(r'公因式|因式|倍式',s):return ret(U(8,1,3,1),'題幹要求多項式因式、倍式或公因式的判別。')
 if re.search(r'科學記號|科學記法',s):return ret(U(7,1,1,4),'題幹明示科學記號或科學記法。')
 if re.search(r'最小公倍數|最大公因數|公因數|公倍數|互質',s):return ret(U(7,1,2,2),'題幹要求公因數、公倍數或互質。')
 if re.search(r'質因數|質數|合數|因數|倍數',s) and not re.search(r'多項式|因式',s):return ret(U(7,1,2,1),'題幹明示質數、合數、因數倍數或質因數分解。')
 if re.search(r'指數律|同底數|指數的運算|乘方的乘方',s):return ret(U(7,1,2,4),'題幹明示指數律、同底數運算或乘方。')
 if re.search(r'平方根|算術方根|近似值|最接近|小數部分|小數部份|整數部分|整數部份|四捨五入',s) and hasroot:return ret(U(8,1,2,1),'題幹要求平方根概念、根式近似值或整數／小數部分。')
 if hasroot:return ret(U(8,1,2,2),'實際算式含平方根的化簡、根式四則或有理化分母。')
 if re.search(r'乘法公式',s):return ret(U(8,1,1,1),'題幹明示乘法公式的運用。')
 if re.search(r'多項式',s):
  if re.search(r'除|商|餘式|乘法|積',s):return ret(U(8,1,1,3),'題幹考多項式乘除、商或餘式。')
  return ret(U(8,1,1,2),'題幹考多項式次數、係數或加減。')
 if re.search(r'一元一次',s):
  if re.search(r'應用|成本|商品|年齡|體重|每|元',s):return ret(U(7,1,3,3),'題幹以一元一次方程式處理實際數量關係。')
  return ret(U(7,1,3,2),'題幹明示一元一次方程式及求解。')
 if re.search(r'數線|相反數|絕對值|正數|負數|原點|整數.*最大|整數.*最小',s):return ret(U(7,1,1,1),'題幹考正負數、絕對值或數線上位置。')
 if re.search(r'正比|反比',s):return ret(U(7,2,4,2),'題幹明示正比或反比。')
 if re.search(r'比例式|最簡整數比|最簡分數比|比值|成比例',s):return ret(U(7,2,4,1),'題幹要求比、比值或比例式。')
 if re.search(r'象限|坐標|座標',s):return ret(U(7,2,3,1),'題幹要求坐標或象限的位置概念，未明示距離。')
 ms=re.findall(r'\$([^$]+)\$',s);math=' '.join(ms)
 if re.search(r'方程式|解.*[xya].*=|[xya].*的解',s):
  if re.search(r'[xya](?:\^\{?2|²)',math):return ret(U(8,1,4,1),'實際待解方程式含二次未知數。')
  return ret(U(7,1,3,2),'實際題幹要求未知數方程式的求解。')
 if re.search(r'[a-z]',math) and re.search(r'簡記|化簡|代入|式子|含.*式|表示|求.*值',s) and not re.search(r'\^\{?[2-9]',math):return ret(U(7,1,3,1),'實際題幹為一次代數式的簡記、化簡或代入求值。')
 if re.search(r'計算|化簡|＝|=$',s) and math and not re.search(r'[a-zA-Z]',math.replace('dfrac','').replace('frac','').replace('times','').replace('div','').replace('left','').replace('right','').replace('cdot','')):
  if '\\dfrac' in math or '\\frac' in math:return ret(U(7,1,2,3),'實際數值算式含分數四則運算。')
  if '^' in math:return ret(U(7,1,1,4),'實際數值算式含指數記法或乘方。')
  return ret(U(7,1,1,3) if re.search(r'\\times|\\div|×|÷',math) else U(7,1,1,2),'實際數值算式為整數乘除混合運算或加減。')
 return [],'尚無足夠明確的內容證據，保留unknown待逐題核對；不以段考或年度推定。'

def main():
 qs=json.loads((R.parent/'public/data/questions.json').read_text('utf8'));qs=[q for q in qs if not q.get('selectionHidden') and q.get('usable',True) and q.get('reviewed') and q.get('typesetVerified')]
 overrides_path=R/'question-unit-overrides.json';overrides=json.loads(overrides_path.read_text('utf8')) if overrides_path.exists() else {}
 reviewed_path=R/'question-unit-reviewed-content.json';reviewed_content=json.loads(reviewed_path.read_text('utf8')) if reviewed_path.exists() else {}
 units={x['id'] for x in json.loads((R/'nanyi-units.json').read_text('utf8'))};out=[];review=[]
 for i,q in enumerate(qs):
  s=txt(q);ids,basis=assign(s)
  if q['id'] in overrides:ids=overrides[q['id']]['unitIds'];basis=overrides[q['id']]['assignmentBasis']
  assert set(ids)<=units
  body={'blocks':q.get('blocks') or [],'diagramSvg':q.get('diagramSvg') or None};raw=json.dumps(body,ensure_ascii=False,separators=(',',':'))
  row={'id':q['id'],'primaryUnitId':ids[0] if ids else 'unknown','unitIds':list(dict.fromkeys(ids)),'status':'assigned' if ids else 'unknown','assignmentBasis':basis,'contentSha256':hashlib.sha256(raw.encode()).hexdigest(),'reviewed':reviewed_content.get(q['id'])==hashlib.sha256(raw.encode()).hexdigest()}
  out.append(row);review.append({'index':i,'id':q['id'],'unitIds':ids,'text':s})
 (R/'question-unit-tags.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),'utf8')
 (R/'question-unit-review.json').write_text(json.dumps(review,ensure_ascii=False,indent=2),'utf8')
 print('active',len(qs),'unknown',sum(x['status']=='unknown' for x in out));print(Counter(x['primaryUnitId'] for x in out))
if __name__=='__main__':main()
