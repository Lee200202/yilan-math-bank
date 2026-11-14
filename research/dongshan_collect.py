import requests,re,json,hashlib
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,as_completed
from zhonghua_collect import listing
ROOT=Path(__file__).parent;RAW=ROOT/'dongshan_raw';RAW.mkdir(exist_ok=True)
def save(name,data):(ROOT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
todo=[{'id':'1T_6KbnSiS_-xmCGAqKpccdEVzV9qB63k','path':[]}];files=[];logs=[]
with ThreadPoolExecutor(max_workers=5) as ex:
    while todo:
        futs={ex.submit(listing,x['id'],x['path']):x for x in todo};todo=[]
        for f in as_completed(futs):
            x=futs[f]
            try:
                rows=f.result();logs.append({'path':x['path'],'status':'ok','items':len(rows)})
                for row in rows:
                    if row['mime']=='application/vnd.google-apps.folder':
                        y=re.search(r'(1\d{2})',row['name'])
                        if len(row['path'])!=1 or not y or int(y[1])>=108:todo.append(row)
                    else:files.append(row)
            except Exception as e:logs.append({'path':x['path'],'status':'error','error':str(e)})
        save('dongshan_files.json',files);save('dongshan_folders.json',logs)
        print('folders',len(logs),'files',len(files),'pending',len(todo),flush=True)
math=[x for x in files if '數' in '/'.join(x['path'])]
def dl(x):
    target=RAW/(x['id']+(Path(x['name']).suffix or '.bin'))
    try:
        if target.exists():content=target.read_bytes()
        else:
            r=requests.get('https://drive.usercontent.google.com/download?id='+x['id']+'&export=download&authuser=0&confirm=t',timeout=45);content=r.content
        if content.startswith(b'%PDF') or content[:2]==b'PK' or content[:4]==bytes.fromhex('d0cf11e0'):
            target.write_bytes(content);x.update(localPath=str(target.relative_to(ROOT.parent)).replace('\\','/'),downloadStatus='ok',bytes=len(content),sha256=hashlib.sha256(content).hexdigest())
        else:x.update(downloadStatus='not_document')
    except Exception as e:x.update(downloadStatus='error',error=str(e))
    return x
out=[]
with ThreadPoolExecutor(max_workers=5) as ex:
    for f in as_completed([ex.submit(dl,x) for x in math]):out.append(f.result());save('dongshan_math.json',out)
print('math',len(out),'downloaded',sum(x.get('downloadStatus')=='ok' for x in out),flush=True)
