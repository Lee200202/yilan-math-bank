from pathlib import Path
import json,re,hashlib,collections,html,xml.etree.ElementTree as ET
import fitz
from PIL import Image,ImageDraw,ImageFont
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).parent
CAT={q['id']:q for q in json.loads((ROOT.parent/'public/data/papers.json').read_text(encoding='utf8'))}

def svg(content,w=360,h=280):return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">{content}</svg>'
def path(d,extra=''):return f'<path d="{d}" fill="none" stroke="#111" stroke-width="1.5" {extra}/>'
def labels(points):return '<g font-family="serif" font-size="20">'+''.join(f'<text x="{x}" y="{y}">{html.escape(str(t))}</text>' for x,y,t in points)+'</g>'

class Paper:
 def __init__(self,pid,header):
    self.pid=pid;self.meta=CAT[pid];self.sha=self.meta['sha256'];self.doc=fitz.open(ROOT.parent/'public'/self.meta['file'].removeprefix('./'));assert hashlib.sha256((ROOT.parent/'public'/self.meta.get('originalFile',self.meta['file']).removeprefix('./')).read_bytes()).hexdigest()==self.sha
    self.c=[];self.t=[];self.header=header;self.out=ROOT/f'bulk-{pid}-review';self.out.mkdir(exist_ok=True)
 def add(self,number,page,rect,text,difficulty='medium',kind='fill',diagram=None,options=None,blocks=None,note=None,figureRect=None):
    # rect coordinates follow supplied 1.7x PDF page render.
    safe=str(number).replace('(','-').replace(')','');qid=f'{self.pid}-{kind}-{safe}'
    rawrect=rect
    if getattr(self,'imageRotation',0)==90:
      rawwidth=Image.open(self.out/f'page-{page+1}.png').width;x0,y0,x1,y1=rect;rawrect=[rawwidth-y1,x0,rawwidth-y0,x1]
    q={'id':qid,'paperId':self.pid,'page':page,'rect':[round(a/1.7,3) for a in rawrect],'type':kind,'number':number,'sourceNumber':str(number),'difficulty':difficulty,'reviewed':True,'school':self.meta['school'],'sourceSha256':self.sha,'difficultyBasis':'編輯依實際運算步驟、概念整合與圖表閱讀判定；非官方難度','sourceScan':not bool(self.doc[page].get_text().strip())}
    if '(' in str(number):
      a,b=str(number).replace(')','').split('(');q.update(parentNumber=int(a),originalSubnumber=int(b))
    if figureRect:
      rawfig=figureRect
      if getattr(self,'imageRotation',0)==90:
       a,b,c,d=figureRect;rawfig=[rawwidth-d,a,rawwidth-b,c]
      q['sourceFigureRect']=[round(a/1.7,3) for a in rawfig]
    r={'id':qid,'blocks':[{'type':'text','text':text.replace('\\n','\n')}],'verified':True,'sourceSha256':self.sha}
    if options:r['blocks'].append({'type':'options','items':options})
    if blocks:r['blocks']+=blocks
    if diagram:r['diagramSvg']=diagram
    if note:r['sourceNote']=note
    self.c.append(q);self.t.append(r)
    suffix='-upright' if getattr(self,'imageRotation',0) else ''
    pic=Image.open(self.out/f'page-{page+1}{suffix}.png');pic.crop(rect).save(self.out/f'{kind}-{safe}.png')
    if figureRect:pic.crop(figureRect).save(self.out/f'{kind}-{safe}-figure.png')
 def save(self,expected,types):
    assert len(self.c)==expected and dict(collections.Counter(q['type'] for q in self.c))==types
    assert len({q['id'] for q in self.c})==expected
    (ROOT/f'curated-bulk-{self.pid}.json').write_text(json.dumps(self.c,ensure_ascii=False,indent=2),encoding='utf8')
    (ROOT/f'transcribed-bulk-{self.pid}.json').write_text(json.dumps(self.t,ensure_ascii=False,indent=2),encoding='utf8')
    font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',18)
    for start in range(0,len(self.c),6):
      tiles=[]
      for q in self.c[start:start+6]:
       safe=str(q['number']).replace('(','-').replace(')','');pic=Image.open(self.out/f'{q["type"]}-{safe}.png');pic.thumbnail((900,520));tile=Image.new('RGB',(930,pic.height+40),'white');ImageDraw.Draw(tile).text((8,8),q['id'],font=font,fill='black');tile.paste(pic,(8,38));tiles.append(tile)
      h=sum(max(tiles[j].height,tiles[j+1].height if j+1<len(tiles) else 0) for j in range(0,len(tiles),2));sheet=Image.new('RGB',(1860,h),'#ddd');y=0
      for j in range(0,len(tiles),2):
       sheet.paste(tiles[j],(0,y))
       if j+1<len(tiles):sheet.paste(tiles[j+1],(930,y))
       y+=max(tiles[j].height,tiles[j+1].height if j+1<len(tiles) else 0)
      sheet.save(self.out/f'crops-{start//6+1}.png')
    formulas=[]
    for q in self.t:
      for b in q['blocks']:
       strings=[b['text']] if b['type']=='text' else b['items'] if b['type']=='options' else [str(x) for row in b.get('rows',[]) for x in row]
       for s in strings:
        assert s.count('$')%2==0,(q['id'],s)
        formulas.extend({'id':q['id'],'tex':v} for v in re.findall(r'\$(.*?)\$',s))
      if 'diagramSvg' in q:ET.fromstring(q['diagramSvg']);assert '<image' not in q['diagramSvg'] and 'base64' not in q['diagramSvg']
    layout='<meta charset="utf-8"><style>body{font-family:"Microsoft JhengHei",sans-serif;font-size:19px;line-height:1.75;margin:24px}main{max-width:1100px;margin:auto}article{border-bottom:1px solid #aaa;padding:10px;margin-bottom:16px}h3{font-size:13px;color:#666;font-weight:400}p{white-space:pre-wrap}article>svg{display:block;width:340px;max-height:280px;margin:8px auto}mjx-container{max-width:100%}</style><main>'
    for q in self.t:
      layout+=f'<article><h3>{q["id"]}</h3>'
      for b in q['blocks']:
       if b['type']=='text':layout+='<p>'+html.escape(b['text'])+'</p>'
       elif b['type']=='options':layout+='<ol type="A">'+''.join('<li>'+html.escape(s)+'</li>' for s in b['items'])+'</ol>'
       elif b['type']=='table':layout+='<table>'+''.join('<tr>'+''.join('<td>'+html.escape(str(x))+'</td>' for x in row)+'</tr>' for row in b['rows'])+'</table>'
      layout+=q.get('diagramSvg','')+'</article>'
    layout+='</main>';(self.out/'transcribed-review.html').write_text(layout,encoding='utf8')
    with sync_playwright() as p:
      browser=p.chromium.launch(channel='chrome',headless=True);page=browser.new_page(viewport={'width':1220,'height':1000});page.goto((self.out/'transcribed-review.html').resolve().as_uri());page.evaluate('window.MathJax={startup:{typeset:false},tex:{inlineMath:[["$","$"]]}}');page.add_script_tag(path=str(ROOT.parent/'public/vendor/tex-svg-full.js'));page.evaluate('MathJax.startup.promise')
      errors=page.evaluate('''items=>items.flatMap(q=>{try{let n=MathJax.tex2svg(q.tex);return n.querySelector('[data-mml-node="merror"]')?[q]:[]}catch(e){return [{...q,error:String(e)}]}})''',formulas);assert not errors,errors
      page.evaluate('MathJax.typesetPromise()')
      for start in range(0,len(self.t),6):
       page.evaluate('(n)=>document.querySelectorAll("article").forEach((a,i)=>a.style.display=i>=n&&i<n+6?"block":"none")',start);page.screenshot(path=str(self.out/f'transcribed-{start//6+1}.png'),full_page=True)
      browser.close()
    report={'paperId':self.pid,'sourceSha256':self.sha,'sourceHeader':self.header,'expectedQuestions':expected,'types':types,'difficulty':dict(collections.Counter(q['difficulty'] for q in self.c)),'actualQuestions':len(self.c),'evidence':{'originalPages':[str(self.out.relative_to(ROOT)/f'page-{i+1}.png') for i in range(len(self.doc))],'sourceCrops':str(self.out.relative_to(ROOT))+'/crops-*.png','transcribedProof':str(self.out.relative_to(ROOT))+'/transcribed-*.png'},'formulaCount':len(formulas),'formulaErrors':errors,'vectorDiagrams':sum('diagramSvg' in q for q in self.t),'visualReviewComplete':False,'notes':[{'id':q['id'],'note':q['sourceNote']} for q in self.t if 'sourceNote' in q]}
    (ROOT/f'proof-bulk-{self.pid}.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
    print(self.pid,len(self.c),types,len(formulas),'formulas')
