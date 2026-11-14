"""Collect the publicly shared exam folders linked from Zhonghua's official site."""
import requests,re,json,hashlib,time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
ROOT=Path(__file__).parent
RAW=ROOT/'zhonghua_raw'; RAW.mkdir(exist_ok=True)
START='0B-2YnWjsnzalMm84ck9yRUtPTG8'
session=requests.Session()
def listing(fid,path):
    r=session.get('https://drive.google.com/drive/folders/'+fid,timeout=40);r.raise_for_status();r.encoding='utf-8'
    m=re.search(r"window\['_DRIVE_ivd'\] = '((?:\\.|[^'])*)';",r.text)
    if not m: raise ValueError('No public listing '+fid)
    enc=m.group(1).replace('\\x','\\u00').replace("\\'","'")
    data=json.loads(json.loads('"'+enc+'"'))
    return [{'id':x[0],'name':x[2],'mime':x[3],'path':path+[x[2]],'url':'https://drive.google.com/file/d/'+x[0]+'/view'} for x in data[0]]
def save_json(name,data): (ROOT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
def run():
    if (ROOT/'zhonghua_files.json').exists():
        files=json.loads((ROOT/'zhonghua_files.json').read_text(encoding='utf-8'))
        todo=[];logs=[]
    else:
        files=None
    top=listing(START,[])
    folders=[x for x in top if re.match(r'1(?:0[89]|1[0-5])',x['name'])]
    if files is None:todo=folders[:];files=[];logs=[]
    with ThreadPoolExecutor(max_workers=5) as ex:
        while todo:
            futs={ex.submit(listing,x['id'],x['path']):x for x in todo};todo=[]
            for f in as_completed(futs):
                parent=futs[f]
                try:
                    rows=f.result();logs.append({'path':parent['path'],'id':parent['id'],'status':'ok','items':len(rows)})
                    for x in rows:
                        if x['mime']=='application/vnd.google-apps.folder':todo.append(x)
                        else:files.append(x)
                except Exception as e:logs.append({'path':parent['path'],'status':'error','error':str(e)})
            save_json('zhonghua_files.json',files);save_json('zhonghua_folders.json',logs)
            print('folders',len(logs),'files',len(files),'pending',len(todo),flush=True)
    math=[x for x in files if '數' in x['name']]
    save_json('zhonghua_math.json',math)
    def download(x):
        ext=Path(x['name']).suffix.lower() or '.bin'
        target=RAW/(x['id']+ext)
        if target.exists():
            x.update(localPath=str(target.relative_to(ROOT.parent)).replace('\\','/'),downloadStatus='ok',sha256=hashlib.sha256(target.read_bytes()).hexdigest());return x
        try:
            r=requests.get('https://drive.google.com/uc?export=download&id='+x['id'],timeout=45)
            if not (r.content.startswith(b'%PDF') or r.content[:2]==b'PK' or r.content[:4]==bytes.fromhex('d0cf11e0')):
                r=requests.get('https://drive.usercontent.google.com/download?id='+x['id']+'&export=download&authuser=0&confirm=t',timeout=45)
            if r.content.startswith(b'%PDF') or r.content[:2]==b'PK' or r.content[:4]==bytes.fromhex('d0cf11e0'):
                target.write_bytes(r.content);x.update(localPath=str(target.relative_to(ROOT.parent)).replace('\\','/'),downloadStatus='ok',sha256=hashlib.sha256(r.content).hexdigest(),bytes=len(r.content))
            else:x.update(downloadStatus='not_pdf',httpStatus=r.status_code,contentType=r.headers.get('content-type'))
        except Exception as e:x.update(downloadStatus='error',error=str(e))
        return x
    out=[]
    with ThreadPoolExecutor(max_workers=5) as ex:
        for f in as_completed([ex.submit(download,x) for x in math]):
            out.append(f.result());save_json('zhonghua_math.json',out)
    print('math',len(out),'downloaded',sum(x.get('downloadStatus')=='ok' for x in out),flush=True)
if __name__=='__main__': run()
