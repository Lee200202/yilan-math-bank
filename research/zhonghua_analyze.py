import json,re
from pathlib import Path
from collections import Counter,defaultdict
import pymupdf
ROOT=Path(__file__).parent; TXT=ROOT/'zhonghua_text';TXT.mkdir(exist_ok=True)
rows=json.loads((ROOT/'zhonghua_math.json').read_text(encoding='utf-8'));catalog=[];errors=[]
def identify(x):
    n=x['name']; p='/'.join(x['path'])
    year=int(re.match(r'(\d{3})',x['path'][0])[1])
    grade=re.search(r'([789])數',n)
    grade=int(grade[1]) if grade else None
    if grade is None:
        gm=re.search(r'([七八九])(?:數|年級)',p)
        if gm:grade={'七':7,'八':8,'九':9}[gm[1]]
    semester=None;exam=None
    m=re.match(r'\d{3}([上下])[-_]?([123])[-段_]+([789])',n)
    if m:semester=1 if m[1]=='上' else 2;exam=int(m[2]);grade=int(m[3])
    m=re.match(r'\d{3}-([12])-([123])-([789])',n)
    if m:semester,exam,grade=map(int,m.groups())
    if not semester:
        semester=1 if ('上學期' in p or '第1學期' in p) else (2 if ('下學期' in p or '第2學期' in p) else None)
    if not exam:
        em=re.search(r'第([123一二三])次',p)
        if em:exam={'一':1,'二':2,'三':3,'1':1,'2':2,'3':3}[em[1]]
    kind='answer' if ('解答' in p or ('答案' in n and '答案卷' not in n)) else ('answer_sheet' if '答案卷' in n else 'question')
    out={**x,'school':'中華國中','schoolId':'024502','year':year,'semester':semester,'exam':exam,'grade':grade,'kind':kind,'sourcePage':'https://www.chjh.ilc.edu.tw/','metadataBasis':'官方資料夾及檔名；未逐份人工核對卷首'}
    name_year=re.match(r'(\d{3})',n)
    if name_year and int(name_year[1])!=year:out['metadataWarning']='檔名學年與所在資料夾不一致，待卷首確認；暫沿用資料夾學年。'
    if x.get('downloadStatus')=='ok' and x['localPath'].endswith('.pdf'):
        try:
            d=pymupdf.open(ROOT.parent/x['localPath']);text='\n'.join(p.get_text() for p in d)
            out.update(pages=len(d),textChars=len(text),hasTextLayer=len(text)>100)
            (TXT/(x['id']+'.txt')).write_text(text,encoding='utf-8')
        except Exception as e:out['analysisError']=str(e)
    return out
for x in rows:
    out=identify(x);catalog.append(out)
    if None in [out['grade'],out['semester'],out['exam']]:errors.append({'id':out['id'],'name':out['name'],'path':out['path']})
catalog.sort(key=lambda x:(x['year'],x['semester'] or 0,x['exam'] or 0,x['grade'] or 0,x['kind'],x['name']))
(ROOT/'zhonghua_catalog.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2),encoding='utf-8')
coverage=[]
for year in range(108,116):
    group=[x for x in catalog if x['year']==year]
    question=[x for x in group if x['kind']=='question']
    cells={f"{x['semester']}-{x['exam']}-{x['grade']}" for x in question}
    coverage.append({'year':year,'files':len(group),'questionFiles':len(question),'questionSlots':sorted(cells),'answers':sum(x['kind']=='answer' for x in group),'answerSheets':sum(x['kind']=='answer_sheet' for x in group),'textQuestionPdf':sum(bool(x.get('hasTextLayer')) for x in question),'note':'有檔案不代表已逐題切分或全縣完整；九下通常僅兩次段考，115尚在進行。'})
report={'school':'中華國中','checkedAt':'2026-11-14','mathFiles':len(catalog),'downloaded':sum(x.get('downloadStatus')=='ok' for x in catalog),'pdfFiles':sum(x['name'].lower().endswith('.pdf') for x in catalog),'metadataParseErrors':errors,'coverage':coverage}
(ROOT/'zhonghua_coverage.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=True))
