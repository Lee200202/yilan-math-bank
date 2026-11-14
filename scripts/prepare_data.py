"""Reproducible source inventory and visually reviewed crop publication. Never infer reviews."""
import hashlib,json,pathlib,shutil
import pymupdf as fitz

ROOT=pathlib.Path(__file__).resolve().parents[1]
def read(path):return json.loads((ROOT/path).read_text(encoding='utf-8'))
def write(path,data):
    p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
def main():
    out=ROOT/'public';(out/'papers').mkdir(exist_ok=True);(out/'pages').mkdir(exist_ok=True)
    raw=read('research/luodong-papers.json')+read('research/neicheng-papers.json')+read('research/zhonghua_catalog.json')
    for extra in ['research/luodong-pre108-papers.json','research/zhonghua-pre108-catalog.json']:
        if (ROOT/extra).exists():raw+=read(extra)
    answers={}
    for p in raw:
        if p.get('kind')=='answer':answers[(p['school'],p['year'],p['semester'],p['grade'],p['exam'])]=p['url']
    papers=[];all_ids={}
    for p in raw:
        if p.get('kind','question')!='question':continue
        src=ROOT/p['localPath'].replace('\\','/')
        if not src.is_file():
            archived=out/'papers'/f'{p["id"]}{src.suffix.lower()}'
            if archived.is_file():src=archived
        if not src.is_file():continue
        sha=hashlib.sha256(src.read_bytes()).hexdigest()
        if sha!=p['sha256']:raise ValueError(f'Source hash changed: {p["id"]}')
        ext=src.suffix.lower();dest=out/'papers'/f'{p["id"]}{ext}'
        if src.resolve()!=dest.resolve():shutil.copyfile(src,dest)
        render_dest=None
        if p.get('renderPath'):
            render_src=ROOT/p['renderPath'].replace('\\','/')
            if not render_src.is_file():render_src=out/'papers'/f'{p["id"]}-rendered.pdf'
            if hashlib.sha256(render_src.read_bytes()).hexdigest()!=p['renderSha256']:raise ValueError(f'Render hash changed: {p["id"]}')
            render_dest=out/'papers'/f'{p["id"]}-rendered.pdf'
            if render_src.resolve()!=render_dest.resolve():shutil.copyfile(render_src,render_dest)
        warning=p.get('metadataWarning','')
        if p.get('metadataConflict'):warning='官方檔名／資料夾與卷首次別不一致，保留官方分類，待核對。'
        paper={'id':p['id'],'school':p['school'],'year':p['year'],'semester':p['semester'],'grade':p['grade'],'exam':p['exam'],'title':p.get('name',p.get('title',src.name)),'file':f'./papers/{dest.name}','format':ext[1:],'sha256':sha,'bytes':src.stat().st_size,'sourceUrl':p.get('sourceUrl',p.get('url')),'sourcePage':p['sourcePage'],'curriculum108':p['year']>=108+p['grade']-7,'track':p.get('track','regular'),'questionCount':0,'warning':warning,'answerUrl':answers.get((p['school'],p['year'],p['semester'],p['grade'],p['exam'])),'metadataBasis':p.get('metadataBasis','official-linked-source')}
        if render_dest:
            paper['originalFile']=paper['file'];paper['file']=f'./papers/{render_dest.name}';paper['renderSha256']=p['renderSha256'];paper['renderedFrom']=ext[1:]
        papers.append(paper);all_ids[paper['id']]=paper
    transcribed={};excluded=[]
    for name in ['transcribed-zhonghua-early.json','transcribed-zhonghua-late.json','transcribed-other-schools.json']:
        f=ROOT/'research'/name
        if not f.exists():continue
        for t in json.loads(f.read_text(encoding='utf-8')):
            if t['id'] in transcribed:raise ValueError(f'Duplicate transcription: {t["id"]}')
            transcribed[t['id']]=t
    questions=[];seen=set();review_files=[];source_reviewed=0;pending=0
    for f in sorted((ROOT/'research').glob('curated-*.json')):
        if f.stem.endswith('-review'):continue
        data=json.loads(f.read_text(encoding='utf-8'))
        if not isinstance(data,list):continue
        review_files.append(f.name)
        for q in data:
            if q.get('reviewed') is not True:continue
            if q['id'] in seen:raise ValueError(f'Duplicate question {q["id"]}')
            seen.add(q['id']);p=all_ids[q['paperId']]
            if q['sourceSha256']!=p['sha256']:raise ValueError(f'Review invalidated: {q["id"]}')
            if p['track']!='regular' or p['warning']:raise ValueError(f'Unresolved source: {q["id"]}')
            source_reviewed+=1;p['sourceQuestionCount']=p.get('sourceQuestionCount',0)+1
            t=transcribed.get(q['id'])
            if not t or t.get('verified') is not True:pending+=1;continue
            if t.get('usable') is False:
                excluded.append({'id':q['id'],'reason':t.get('sourceIssue','原題內容待釐清')});continue
            if t['sourceSha256']!=p['sha256']:raise ValueError(f'Transcription invalidated: {q["id"]}')
            if not t.get('blocks'):raise ValueError(f'Empty transcription: {q["id"]}')
            for block in t['blocks']:
                if block['type'] not in ['text','options','table','svg']:raise ValueError(f'Unknown text block: {q["id"]}')
                if block['type']=='svg' and any(s in block['svg'].lower() for s in ['<image','<script','<foreignobject','data:image']):raise ValueError(f'Non-vector diagram: {q["id"]}')
            if t.get('diagramSvg') and any(s in t['diagramSvg'].lower() for s in ['<image','<script','<foreignobject','data:image']):raise ValueError(f'Non-vector diagram: {q["id"]}')
            src=fitz.open(out/p['file'].removeprefix('./'));page=src[q['page']];r=fitz.Rect(q['rect'])
            if r.width<5 or r.height<5 or not page.rect.contains(r):raise ValueError(f'Invalid crop: {q["id"]}')
            row={**q,**{k:p[k] for k in ['school','year','semester','grade','exam','curriculum108']},'blocks':t['blocks'],'typesetVerified':True,'width':r.width,'height':r.height,'difficultyBasis':q.get('difficultyBasis','編輯教學估計，非官方答對率')}
            if t.get('diagramSvg'):row['diagramSvg']=t['diagramSvg']
            questions.append(row);p['questionCount']+=1;src.close()
    papers.sort(key=lambda p:(-p['year'],p['semester'],-p['exam'],p['school'],p['grade'],p['id']))
    inv=read('research/inventory_schools.json');schools=[]
    for s in inv['schools']:
        name=s['name'];matches=[p for p in papers if any(k in name and k in p['school'] for k in ['中華','羅東','內城'])]
        status=s['status'];note=s.get('note','')
        if matches:
            label='部分年度公開・已收錄';note='已下載公開原卷。並非所有年度／學期／年級／次別均齊全；部分原卷尚待拆題校對。'
        elif 'restricted' in status:label='限登入';note=s.get('note','官方入口需登入，未下載受限內容。')
        elif s.get('examEntrances'):label='已找到入口・待核查'
        elif s.get('httpStatus')!=200:label='連線受限・待複查'
        else:label='已查頁面未找到入口'
        schools.append({'id':s['id'],'name':name,'website':s.get('checkedUrl') or s['website'],'status':status,'statusLabel':label,'years':sorted(set(p['year'] for p in matches)),'paperCount':len(matches),'reviewedQuestionCount':sum(p['questionCount'] for p in matches),'note':note,'checkedPages':s.get('checkedPages',[]),'examEntrances':s.get('examEntrances',[])})
    coverage={'checkedAt':'2026-11-14','scope':'宜蘭縣中華、羅東、內城國中，105至115學年，僅公開來源；另保留全縣入口盤點','inventorySources':inv['sources'],'schools':schools,'filesDownloaded':sum((ROOT/p.get('localPath','')).is_file() for p in raw),'paperFiles':len(papers),'reviewedQuestions':len(questions),'sourceReviewedQuestions':source_reviewed,'pendingTranscriptions':pending,'excludedQuestionIssues':excluded,'reviewFiles':review_files,'limitation':'原卷下載、逐題辨識與文字重排分開計數；未完成文字核對的題目不參與組卷。'}
    write('public/data/papers.json',papers);write('public/data/questions.json',questions);write('public/data/coverage.json',coverage)
    print(json.dumps({'paperFiles':len(papers),'reviewedQuestions':len(questions),'years':sorted(set(p['year'] for p in papers)),'schools':sorted(set(p['school'] for p in papers))},ensure_ascii=False))
if __name__=='__main__':main()
