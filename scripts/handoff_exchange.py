"""External-chat work packs, structured Markdown intake and a localhost staging API.

Commands: inventory; pack --school SCHOOL --limit 2; intake FILE.md|FILE.zip;
          serve --port 8787. No command publishes or overwrites completed transcripts.
"""
import argparse
import collections
import hashlib
import io
import json
import pathlib
import re
import shutil
import sys
import zipfile
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, unquote, urlsplit

ROOT = pathlib.Path(__file__).resolve().parents[1]
REGIONS = {'yilan':'宜蘭縣','taipei':'臺北市','new_taipei':'新北市','taoyuan':'桃園市','taichung':'臺中市','kaohsiung':'高雄市'}


def read(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8-sig'))


def write(path, value):
    path = pathlib.Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def papers():
    return {p['id']:p for p in read('public/data/papers.json')}


def raw_rows():
    inv=read('research/metro/metro-inventory.json')
    return {f['id']:f for s in inv['sources'].values() for f in s['files'] if 'id' in f}


def queue():
    blocked={p.stem for p in (ROOT/'handoff/source-issues').glob('*.json')}
    claims={c['paperId']:c for c in read('handoff/CLAIMS.json').get('claims',[]) if c.get('status') in ('claimed','transcribing','repairing-figures','assigned-external','reserved-for-external-dispatch','staged-for-coordinator-review')}
    rows=raw_rows()
    result=[]
    for p in papers().values():
        if p['transcriptionStatus'].startswith('complete'):
            continue
        row={k:p.get(k) for k in ['id','region','school','year','semester','grade','exam','format','track','questionCount','transcriptionStatus','sha256','sourceUrl','sourcePage']}
        row['originalUrl']='https://lee200202.github.io/yilan-math-bank/'+p['file'].removeprefix('./') if p.get('file') else p['sourceUrl']
        row['archiveMember']=rows.get(p['id'],{}).get('archiveMember')
        row['blocked']=p['id'] in blocked
        row['claim']=claims.get(p['id'])
        result.append(row)
    return result


def label(p):
    return f"{p['year']}{'上' if p['semester']==1 else '下'}・{p['grade']}年級・第{p['exam']}次"


def inventory():
    rows=queue(); folder=ROOT/'handoff/assignments';folder.mkdir(exist_ok=True)
    write(folder/'all-targets.json',rows)
    out=['# 可分派給其他聊天室的完整待辦','','原卷列舉不是轉寫完成。下表包括尚未全卷完成的所有PDF、DOCX、DOC、ODT，不能只跑PDF清單就結案。','', '| 地區 | 學校 | 未轉寫 | 部分轉寫 | 待處理合計 | 清單 |','| --- | --- | ---: | ---: | ---: | --- |']
    for region in REGIONS:
        for school in sorted({r['school'] for r in rows if r['region']==region}):
            mine=[r for r in rows if r['region']==region and r['school']==school]
            slug=f'{region}-{school}'
            pending=sum(r['transcriptionStatus']=='pending' for r in mine); partial=len(mine)-pending
            out.append(f'| {REGIONS[region]} | {school} | {pending} | {partial} | {len(mine)} | [{school}]({slug}.md) |')
            lines=[f'# {REGIONS[region]} {school} 待完成清單','',f'未轉寫 {pending} 份，部分轉寫 {partial} 份。每卷一個paperId，整卷處理；卷首與清單衝突時回報，不猜分類。','', '| 範圍 | 狀態 | 格式 | paperId | 原檔／官方包 | SHA256 |','| --- | --- | --- | --- | --- | --- |']
            for r in sorted(mine,key=lambda r:(-r['year'],r['grade'],r['semester'],r['exam'],r['id'])):
                status='來源衝突，暫勿認領' if r['blocked'] else '已預留外部AI，勿重派' if r.get('claim') else '部分轉寫' if r['transcriptionStatus']=='partial' else '未轉寫'
                suffix=f"；ZIP成員：{r['archiveMember']}" if r['archiveMember'] else ''
                lines.append(f"| {label(r)} | {status} | {r['format']} | `{r['id']}` | [原檔/來源](<{r['originalUrl']}>) {suffix} | `{r['sha256']}` |")
            (folder/f'{slug}.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    formats=collections.Counter(r['format'] for r in rows)
    out+=['',f'合計 {len(rows)} 份尚未全卷完成：{dict(formats)}。', '', '先讀 [完整AI提示詞](../EXTERNAL_AI_PROMPT.md)。建議每個聊天室分派1–2份全卷，避免重複認領；回傳MD或MD ZIP交給Codex／Claude匯入待審區。']
    (folder/'INDEX.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
    print(f'Wrote {len(rows)} targets across {len({r["school"] for r in rows})} schools')


def original(pid):
    p=papers()[pid]
    candidates=[]
    if p.get('file'):candidates.append(ROOT/'public'/p['file'].removeprefix('./'))
    row=raw_rows().get(pid,{})
    if row.get('localPath'):candidates.append(ROOT/row['localPath'])
    for path in candidates:
        if path.is_file() and sha(path.read_bytes())==p['sha256']:
            return path
    from fetch_paper import fetch
    path=fetch(pid)
    if sha(path.read_bytes())!=p['sha256']:raise ValueError('Source checksum mismatch')
    return path


def template(p):
    obj={'deliveryStatus':'draft','paperId':p['id'],'sourceSha256':p['sha256'],'printedHeader':'請實看卷首後填寫','printedSlot':{k:p[k] for k in ['year','semester','grade','exam']},'printedCounts':'請逐頁盤點題型、題號與子題','visualReviewComplete':False,'reviewNote':'請記錄看過的原卷頁、圖形、原稿疑義與未完成項目','expectedTypes':{'choice':0,'fill':0,'written':0},'questions':[]}
    return f"# {p['school']} {label(p)}\n\npaperId: `{p['id']}`\n\n## 卷首與來源核對\n\n請核對manifest，填寫原卷全部頁碼；不得把預填declaredSlot當作實際卷首證據。\n\n## 逐題全文\n\n此處逐題列出可讀文字、公式、所有選項／填答格、難度、南一單元與來源頁。SVG完整放入下方JSON，不使用截圖代替。\n\n## 原題盤點與未完成項目\n\n請列原大題→題數、所有子題及原稿疑義。完成後將deliveryStatus改complete；未完成則partial並明列缺漏。\n\n## 匯入資料（恰好一個JSON區塊）\n\n```json\n{json.dumps(obj,ensure_ascii=False,indent=2)}\n```\n"


def pack(school, limit, out):
    allp=papers(); blocked={r['id'] for r in queue() if r['blocked']}
    claims=read('handoff/CLAIMS.json').get('claims',[])
    blocked.update(c['paperId'] for c in claims if c.get('status') in ('claimed','transcribing','repairing-figures','assigned-external','reserved-for-external-dispatch','staged-for-coordinator-review'))
    if (ROOT/'research/incoming-external').exists():
        blocked.update(p.name for p in (ROOT/'research/incoming-external').iterdir() if p.is_dir())
    ordered=[t['paperId'] for path in sorted((ROOT/'research/targets').glob('*.json')) for t in read(path.relative_to(ROOT)) if isinstance(t,dict) and 'paperId' in t]
    candidates=[allp[pid] for pid in dict.fromkeys(ordered) if pid in allp and allp[pid]['school']==school and not allp[pid]['transcriptionStatus'].startswith('complete') and allp[pid].get('track','regular')=='regular' and pid not in blocked]
    if len(candidates)<limit:raise ValueError(f'Only {len(candidates)} ready regular PDF targets for {school}; do not invent more')
    dest=pathlib.Path(out).resolve();dest.mkdir(parents=True,exist_ok=True)
    import pymupdf as fitz
    selected=[]
    for p in candidates[:limit]:
        pid=p['id'];folder=dest/pid
        if folder.exists():raise ValueError(f'Pack already exists: {folder}')
        source=original(pid)
        if not source.read_bytes().startswith(b'%PDF'):raise ValueError(f'This pack command expects a PDF, not a renamed Word file: {pid}')
        (folder/'original').mkdir(parents=True);(folder/'pages').mkdir()
        orig=folder/'original'/f'{pid}.pdf';shutil.copyfile(source,orig)
        doc=fitz.open(source);pages=[];texts=[]
        for i,page in enumerate(doc,1):
            target=folder/'pages'/f'page-{i:02}.png';page.get_pixmap(matrix=fitz.Matrix(2,2)).save(target)
            pages.append({'page':i,'file':target.relative_to(folder).as_posix(),'sha256':sha(target.read_bytes())})
            texts.append(f'===== page {i} =====\n'+page.get_text())
        (folder/'text-layer.txt').write_text('\n'.join(texts),encoding='utf-8')
        manifest={**p,'declaredSlot':{k:p[k] for k in ['year','semester','grade','exam']},'originalFile':orig.relative_to(folder).as_posix(),'pageCount':len(doc),'pages':pages,'scope':'one entire original exam, every question and necessary figure; not a sample'}
        write(folder/'manifest.json',manifest)
        (folder/'RETURN_TEMPLATE.md').write_text(template(p),encoding='utf-8')
        (folder/'TARGET.md').write_text(f"# 任務：{p['school']} {label(p)}\n\n只認領 `{pid}`。請先讀本資料夾manifest與根目錄AI_PROMPT.md，再看original與全部pages。\n\n回傳 `{pid}.md`，不能只回傳此空範本；必須包含全卷文字與唯一完整JSON區塊。\n",encoding='utf-8')
        selected.append({'paperId':pid,'school':school,'scope':label(p),'pages':len(doc),'status':'ready-for-external-chat'})
    for name,src in [('AI_PROMPT.md','handoff/EXTERNAL_AI_PROMPT.md'),('TRANSCRIBE_GUIDE.md','research/TRANSCRIBE_GUIDE.md'),('nanyi-units.json','research/nanyi-units.json')]:shutil.copyfile(ROOT/src,dest/name)
    write(dest/'ASSIGNMENTS.json',selected)
    zip_path=pathlib.Path(str(dest)+'.zip')
    with zipfile.ZipFile(zip_path,'w',compression=zipfile.ZIP_DEFLATED) as z:
        for path in dest.rglob('*'):
            if path.is_file():z.write(path,path.relative_to(dest))
    print(f'{zip_path}: {len(selected)} papers, {sum(x["pages"] for x in selected)} pages, {zip_path.stat().st_size} bytes')
    return zip_path


def parse_md(text):
    text=text.replace('\r\n','\n')
    blocks=re.findall(r'^```json[ \t]*\n(.*?)^```[ \t]*$',text,re.M|re.S)
    if len(blocks)!=1:raise ValueError('MD must contain exactly one complete ```json block')
    value=json.loads(blocks[0])
    if not isinstance(value,dict):raise ValueError('Expected one whole-paper object')
    return value


def stage(markdown, filename):
    t=parse_md(markdown);pid=t.get('paperId');allp=papers()
    if pid not in allp:raise ValueError('Unknown paperId')
    if t.get('deliveryStatus') in ('draft','partial') or not t.get('visualReviewComplete') or not t.get('questions'):raise ValueError('Draft/partial delivery: keep it as working material; it cannot enter the completed queue')
    p=allp[pid]
    if p['transcriptionStatus'].startswith('complete'):raise ValueError('Paper already fully transcribed; coordinator must review any correction separately')
    from prepare_metro import rows_from_transcript
    usable=rows_from_transcript(t,dict(p),{u['id'] for u in read('research/nanyi-units.json')},filename)
    if not usable:raise ValueError('No usable questions')
    folder=ROOT/'research/incoming-external'/pid
    if folder.exists():raise ValueError('Existing incoming delivery; no overwrite')
    try:folder.mkdir(parents=True)
    except FileExistsError as e:raise ValueError('Existing incoming delivery; no overwrite') from e
    (folder/f'{pid}.md').write_text(markdown,encoding='utf-8')
    write(folder/f'{pid}.json',t)
    receipt={'paperId':pid,'school':p['school'],'usableQuestions':len(usable),'sourceUnits':len(t['questions']),'sourceSha256':p['sha256'],'inputName':pathlib.Path(filename).name,'status':'staged-for-coordinator-review','published':False,'warning':'External AI claims are untrusted data; original/diagram review, PDF QA and publication remain pending.'}
    write(folder/'receipt.json',receipt)
    return receipt


def intake(path):
    path=pathlib.Path(path);results=[]
    if path.suffix.lower()=='.zip':
        with zipfile.ZipFile(path) as z:
            members=[i for i in z.infolist() if not i.is_dir() and i.filename.lower().endswith('.md')]
            if not members:raise ValueError('No Markdown deliveries in ZIP')
            if len(members)>100 or sum(i.file_size for i in members)>50_000_000:raise ValueError('Delivery ZIP too large')
            for member in members:
                # No extraction, no execution, no paths supplied by the sender are used.
                try:results.append(stage(z.read(member).decode('utf-8-sig'),member.filename))
                except (ValueError,KeyError,TypeError) as e:results.append({'inputName':member.filename,'error':str(e),'published':False})
    else:results.append(stage(path.read_text(encoding='utf-8-sig'),path.name))
    print(json.dumps(results,ensure_ascii=False,indent=2))
    return results


def serve(port):
    class Handler(BaseHTTPRequestHandler):
        def respond(self,status,value,kind='application/json; charset=utf-8'):
            body=value if isinstance(value,bytes) else json.dumps(value,ensure_ascii=False).encode('utf-8')
            self.send_response(status);self.send_header('Content-Type',kind);self.send_header('Content-Length',str(len(body)));self.send_header('Cache-Control','no-store');self.end_headers();self.wfile.write(body)
        def allowed(self):
            origin=self.headers.get('Origin')
            return self.headers.get('Host') in (f'127.0.0.1:{port}',f'localhost:{port}') and (not origin or origin in (f'http://127.0.0.1:{port}',f'http://localhost:{port}'))
        def do_GET(self):
            if not self.allowed():return self.respond(403,{'error':'Localhost only'})
            route=urlsplit(self.path);parts=route.path.strip('/').split('/');query=parse_qs(route.query)
            try:
                if parts==['api','targets']:
                    rows=queue()
                    for key in ('school','region','year','semester','grade','exam','format'):
                        if key in query:rows=[r for r in rows if str(r.get(key))==query[key][0]]
                    return self.respond(200,{'count':len(rows),'targets':rows})
                if parts==['api','units']:return self.respond(200,read('research/nanyi-units.json'))
                if len(parts)>=3 and parts[:2]==['api','papers']:
                    pid=unquote(parts[2]);p=papers()[pid]
                    if len(parts)==3:return self.respond(200,p)
                    if parts[3:]==['source']:
                        path=original(pid);return self.respond(200,path.read_bytes(),'application/pdf' if path.read_bytes().startswith(b'%PDF') else 'application/octet-stream')
                    if len(parts)==5 and parts[3]=='pages':
                        import pymupdf as fitz
                        path=original(pid)
                        if not path.read_bytes().startswith(b'%PDF'):return self.respond(409,{'error':'Original is Word/ODT; convert and verify before rendering'})
                        doc=fitz.open(path);number=int(parts[4].removesuffix('.png'))
                        if not 1<=number<=len(doc):return self.respond(404,{'error':'Page not found'})
                        return self.respond(200,doc[number-1].get_pixmap(matrix=fitz.Matrix(2,2)).tobytes('png'),'image/png')
                return self.respond(404,{'error':'Unknown endpoint'})
            except (ValueError,KeyError,IndexError) as e:return self.respond(400,{'error':str(e)})
        def do_POST(self):
            if not self.allowed():return self.respond(403,{'error':'Localhost only'})
            if self.path!='/api/import':return self.respond(404,{'error':'Only /api/import is supported'})
            if self.headers.get('Content-Type','').split(';')[0]!='application/json':return self.respond(415,{'error':'application/json required'})
            try:size=int(self.headers.get('Content-Length','0'))
            except ValueError:return self.respond(400,{'error':'Invalid Content-Length'})
            if not 0<size<=10_000_000:return self.respond(413,{'error':'Expected 1–10000000 bytes'})
            try:
                data=json.loads(self.rfile.read(size));return self.respond(202,stage(data['markdown'],data.get('filename','delivery.md')))
            except (ValueError,KeyError,TypeError) as e:return self.respond(400,{'error':str(e),'published':False})
    print(f'Local staging API http://127.0.0.1:{port}/api/targets; cloud chats cannot reach this address.',flush=True)
    ThreadingHTTPServer(('127.0.0.1',port),Handler).serve_forever()


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);commands=parser.add_subparsers(dest='command',required=True)
    commands.add_parser('inventory')
    sub=commands.add_parser('pack');sub.add_argument('--school',required=True);sub.add_argument('--limit',type=int,default=2);sub.add_argument('--out',required=True)
    sub=commands.add_parser('intake');sub.add_argument('file')
    sub=commands.add_parser('serve');sub.add_argument('--port',type=int,default=8787)
    args=parser.parse_args()
    if args.command=='inventory':inventory()
    elif args.command=='pack':pack(args.school,args.limit,args.out)
    elif args.command=='intake':intake(args.file)
    elif args.command=='serve':serve(args.port)
