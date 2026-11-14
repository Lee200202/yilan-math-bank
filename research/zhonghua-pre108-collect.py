"""Separate 105–107 collection; preserves the newer catalogue unchanged."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,as_completed
import requests,re,json,hashlib
from zhonghua_collect import listing
ROOT=Path(__file__).parent;RAW=ROOT/'zhonghua_old_raw';RAW.mkdir(exist_ok=True)
def save(name,data):(ROOT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
top=listing('0B-2YnWjsnzalMm84ck9yRUtPTG8',[])
cache=ROOT/'zhonghua-pre108-files.json'
if cache.exists():files=json.loads(cache.read_text(encoding='utf8'));todo=[];folders=[]
else:files=[];todo=[x for x in top if re.match(r'10[567]',x['name'])];folders=[]
with ThreadPoolExecutor(max_workers=6) as ex:
    while todo:
        futs={ex.submit(listing,x['id'],x['path']):x for x in todo};todo=[]
        for f in as_completed(futs):
            parent=futs[f]
            try:
                rows=f.result();folders.append({'id':parent['id'],'path':parent['path'],'status':'ok','items':len(rows)})
                for x in rows:
                    if x['mime']=='application/vnd.google-apps.folder':todo.append(x)
                    else:files.append(x)
            except Exception as e:folders.append({'id':parent['id'],'path':parent['path'],'status':'error','error':str(e)})
        save('zhonghua-pre108-files.json',files);save('zhonghua-pre108-folders.json',folders)
        print('folders',len(folders),'all files',len(files),'pending',len(todo),flush=True)
math=[x for x in files if '數' in x['name']]
def dl(x):
    ext=Path(x['name']).suffix.lower() or {'application/pdf':'.pdf','application/msword':'.doc'}.get(x['mime'],'.bin')
    target=RAW/(x['id']+ext)
    try:
        oldtarget=RAW/(x['id']+'.bin')
        content=target.read_bytes() if target.exists() else (oldtarget.read_bytes() if oldtarget.exists() else requests.get('https://drive.usercontent.google.com/download?id='+x['id']+'&export=download&authuser=0&confirm=t',timeout=45).content)
        if not(content.startswith(b'%PDF') or content[:2]==b'PK' or content[:4]==bytes.fromhex('d0cf11e0')):content=requests.get('https://drive.google.com/uc?export=download&id='+x['id'],timeout=45).content
        if content.startswith(b'%PDF') or content[:2]==b'PK' or content[:4]==bytes.fromhex('d0cf11e0'):
            target.write_bytes(content);x.update(localPath=str(target.relative_to(ROOT.parent)).replace('\\','/'),downloadStatus='ok',bytes=len(content),sha256=hashlib.sha256(content).hexdigest())
        else:x.update(downloadStatus='not_document')
    except Exception as e:x.update(downloadStatus='error',error=str(e))
    n=x['name'];p='/'.join(x['path']);year=int(re.match(r'(\d{3})',x['path'][0])[1]);grade=None;semester=None;exam=None
    gm=re.search(r'([789])數',n)
    if gm:grade=int(gm[1])
    else:
        gm=re.search(r'([七八九])(?:數|年級)',p)
        if gm:grade={'七':7,'八':8,'九':9}[gm[1]]
        else:
            gm=re.search(r'([789一二三])年級',p)
            if gm:grade={'7':7,'8':8,'9':9,'一':7,'二':8,'三':9}[gm[1]]
            else:
                gm=re.fullmatch(r'數([123])\.pdf',n)
                if gm:grade=int(gm[1])+6
    m=re.match(r'\d{3}([上下])[-_]?([123])[-段_]*([789])',n)
    if m:semester=1 if m[1]=='上' else 2;exam=int(m[2]);grade=int(m[3])
    m=re.match(r'\d{3}-([12])-([123])-([789])',n)
    if m:semester,exam,grade=map(int,m.groups())
    if not semester:semester=1 if ('上學期' in p or '第1學期' in p) else (2 if ('下學期' in p or '第2學期' in p) else None)
    if not exam:
        em=re.search(r'第([123一二三])次',p)
        if em:exam={'一':1,'二':2,'三':3,'1':1,'2':2,'3':3}[em[1]]
    kind='answer' if ('解答' in p or any(q=='答案' for q in x['path']) or ('答案' in n and '答案卷' not in n)) else ('answer_sheet' if '答案卷' in n else 'question')
    x.update(school='中華國中',schoolId='024502',year=year,semester=semester,exam=exam,grade=grade,kind=kind,sourcePage='https://www.chjh.ilc.edu.tw/',metadataBasis='官方資料夾及檔名；未逐份人工核對卷首',curriculum108=False)
    pe=re.search(r'第([123一二三])次',p)
    if pe and exam and {'一':1,'二':2,'三':3,'1':1,'2':2,'3':3}[pe[1]]!=exam:x['metadataWarning']='檔名段考次數與所在資料夾不一致；待卷首確認，暫依檔名。'
    return x
out=[]
with ThreadPoolExecutor(max_workers=6) as ex:
    for f in as_completed([ex.submit(dl,x) for x in math]):
        out.append(f.result());save('zhonghua-pre108-catalog.json',sorted(out,key=lambda x:(x['year'],x.get('semester') or 0,x.get('exam') or 0,x.get('grade') or 0,x['kind'],x['name'])))
print('math',len(out),'downloaded',sum(x.get('downloadStatus')=='ok' for x in out),flush=True)
