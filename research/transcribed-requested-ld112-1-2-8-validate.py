from pathlib import Path
import json,re,collections,xml.etree.ElementTree as ET
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).parent
c=json.loads((ROOT/'curated-requested-ld112-1-2-8.json').read_text(encoding='utf8'))
t=json.loads((ROOT/'transcribed-requested-ld112-1-2-8.json').read_text(encoding='utf8'))
assert len(c)==len(t)==25
assert len({q['id'] for q in c})==25
assert collections.Counter(q['type'] for q in c)=={'fill':22,'written':3}
assert {q['id'] for q in c}=={q['id'] for q in t}
assert all(q['reviewed'] and q['difficulty'] in ['easy','medium','hard'] for q in c)
assert all(q['verified'] and q['sourceSha256']=='7b7993d35c10493b1f05c2ff079fcd5faa496b304bb85336886c139fe24192b2' for q in t)
formulas=[]
for q in t:
    for b in q['blocks']:
        assert b['text'].count('$')%2==0
        formulas.extend({'id':q['id'],'tex':x} for x in re.findall(r'\$(.*?)\$',b['text']))
    if 'diagramSvg' in q:
        ET.fromstring(q['diagramSvg']);assert '<image' not in q['diagramSvg'] and 'base64' not in q['diagramSvg']
out=ROOT/'requested-ld112-1-2-8-review'
html='<meta charset="utf-8"><style>body{font-family:"Microsoft JhengHei",sans-serif;font-size:19px;line-height:1.8;margin:24px}main{max-width:1100px;margin:auto}article{border-bottom:1px solid #aaa;margin-bottom:20px;padding:10px}svg{display:block;max-width:350px;max-height:260px;margin:10px auto}h3{font-size:13px;font-weight:400;color:#666}p{white-space:pre-wrap}mjx-container svg{display:inline;max-width:none;max-height:none;margin:0}</style><main>'
for q in t:html+=f'<article><h3>{q["id"]}</h3><p>'+q['blocks'][0]['text']+'</p>'+q.get('diagramSvg','')+'</article>'
html+='</main>'
(out/'transcribed-review.html').write_text(html,encoding='utf8')
with sync_playwright() as p:
    browser=p.chromium.launch(channel='chrome',headless=True)
    page=browser.new_page(viewport={'width':1220,'height':1000},device_scale_factor=1)
    page.goto((out/'transcribed-review.html').resolve().as_uri())
    page.evaluate('window.MathJax={startup:{typeset:false},tex:{inlineMath:[["$","$"]]}}')
    page.add_script_tag(path=str(ROOT.parent/'public/vendor/tex-svg-full.js'))
    page.evaluate('MathJax.startup.promise')
    errors=page.evaluate('''items=>items.flatMap(q=>{try{let n=MathJax.tex2svg(q.tex);return n.querySelector('[data-mml-node="merror"]')?[q]:[]}catch(e){return [{...q,error:String(e)}]}})''',formulas)
    assert not errors,errors
    page.evaluate('MathJax.typesetPromise()')
    for start in range(0,25,6):
        page.evaluate('(n)=>document.querySelectorAll("article").forEach((a,i)=>a.style.display=i>=n&&i<n+6?"block":"none")',start)
        page.screenshot(path=str(out/f'transcribed-review-{start//6+1}.png'),full_page=True)
    browser.close()
report={'questions':25,'types':dict(collections.Counter(q['type'] for q in c)),'difficulty':dict(collections.Counter(q['difficulty'] for q in c)),'formulaCount':len(formulas),'mathJaxErrors':errors,'vectorDiagrams':sum('diagramSvg' in q for q in t),'idAndShaChecks':True,'sourceNote':[q for q in t if 'sourceNote' in q]}
(ROOT/'transcribed-requested-ld112-1-2-8-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print('Validated',len(c),'questions;',len(formulas),'formulas;',sum('diagramSvg' in q for q in t),'SVG diagrams')
