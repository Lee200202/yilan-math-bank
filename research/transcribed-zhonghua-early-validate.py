from pathlib import Path
import json,hashlib,re,xml.etree.ElementTree as ET
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).parent
rows=json.loads((ROOT/'transcribed-zhonghua-early.json').read_text(encoding='utf8'))
old=json.loads((ROOT/'curated-zhonghua-pre108.json').read_text(encoding='utf8'))
mapped=json.loads((ROOT/'transcribed-zhonghua-early-map.json').read_text(encoding='utf8'))
expected={q['id']:q for q in old+mapped}
assert len(rows)==len(expected)==125
assert {r['id'] for r in rows}==set(expected)
assert len({r['id'] for r in rows})==len(rows)
for r in rows:
    assert r['verified'] is True and r['sourceSha256']==expected[r['id']]['sourceSha256'],r['id']
    for b in r['blocks']:
        texts=[b['text']] if b['type']=='text' else b['items'] if b['type']=='options' else [str(t) for a in b.get('rows',[]) for t in a]
        for t in texts:assert t.count('$')%2==0,(r['id'],t)
    if 'diagramSvg' in r:
        ET.fromstring(r['diagramSvg'])
        assert '<image' not in r['diagramSvg'] and 'base64' not in r['diagramSvg']
out=ROOT/'transcribed-zhonghua-early-review'
diagrams=[r for r in rows if 'diagramSvg' in r]
html='<meta charset="utf-8"><style>body{margin:15px;font-family:Arial}main{display:grid;grid-template-columns:repeat(2,640px);gap:12px}article{border:1px solid #888;padding:12px;width:610px;break-inside:avoid}svg{max-width:100%;height:250px;display:block;margin:auto}h3{font-size:15px;overflow-wrap:anywhere}</style><main>'
for n,r in enumerate(diagrams):html+=f'<article><h3>{n+1}. {r["id"]}</h3>'+r['diagramSvg']+'</article>'
html+='</main>'
(out/'vector-review.html').write_text(html,encoding='utf8')
with sync_playwright() as p:
    browser=p.chromium.launch(channel='chrome',headless=True)
    page=browser.new_page(viewport={'width':1340,'height':1000},device_scale_factor=1)
    page.goto((out/'vector-review.html').resolve().as_uri())
    page.screenshot(path=str(out/'vector-review.png'),full_page=True)
    page.evaluate('window.MathJax={startup:{typeset:false},tex:{packages:{"[+]": ["noerrors"]}}}')
    page.add_script_tag(path=str(ROOT.parent/'public/vendor/tex-svg-full.js'))
    page.evaluate('MathJax.startup.promise')
    formulas=[]
    for r in rows:
        for b in r['blocks']:
            texts=[b['text']] if b['type']=='text' else b['items'] if b['type']=='options' else [str(t) for a in b.get('rows',[]) for t in a]
            for t in texts:
                for tex in re.findall(r'\$(.*?)\$',t):formulas.append({'id':r['id'],'tex':tex})
    errors=page.evaluate('''items=>items.flatMap(q=>{try{const n=MathJax.tex2svg(q.tex);return n.querySelector('[data-mml-node="merror"]')?[q]:[]}catch(e){return [{...q,error:String(e)}]}})''',formulas)
    assert not errors,errors
    browser.close()
report={'transcriptions':len(rows),'expected':len(expected),'missing':[], 'shaMatches':len(rows),'vectorDiagrams':len(diagrams),'sourceIssues':[{'id':r['id'],'sourceIssue':r['sourceIssue'],'usable':r.get('usable')} for r in rows if 'sourceIssue' in r], 'noRasterDiagrams':True,'mathDelimiterCheck':True,'mathJaxFormulas':len(formulas),'mathJaxErrors':errors}
(ROOT/'transcribed-zhonghua-early-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(report,ensure_ascii=False))
