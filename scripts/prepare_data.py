"""Reproducible source inventory and visually reviewed crop publication. Never infer reviews."""
import hashlib,json,pathlib,shutil,collections
import pymupdf as fitz
import sys
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
import prepare_metro

ROOT=pathlib.Path(__file__).resolve().parents[1]
def read(path):return json.loads((ROOT/path).read_text(encoding='utf-8'))
def write(path,data):
    p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
def main():
    out=ROOT/'public';(out/'papers').mkdir(exist_ok=True);(out/'pages').mkdir(exist_ok=True)
    raw=read('research/luodong-papers.json')+read('research/neicheng-papers.json')+read('research/zhonghua_catalog.json')
    for extra in ['research/luodong-pre108-papers.json','research/zhonghua-pre108-catalog.json']:
        if (ROOT/extra).exists():raw+=read(extra)
    render_manifest=ROOT/'research/bulk-render-manifest.json'
    renders={p['id']:p for p in read('research/bulk-render-manifest.json') if p.get('status')=='rendered'} if render_manifest.exists() else {}
    for p in raw:
        if p['id'] in renders:
            render=renders[p['id']]
            if render['sourceSha256']!=p['sha256']:raise ValueError(f'Render source changed: {p["id"]}')
            p.update({k:render[k] for k in ['renderPath','renderSha256']})
    overrides=read('research/paper-metadata-overrides.json') if (ROOT/'research/paper-metadata-overrides.json').exists() else {}
    for p in raw:
        if p['id'] in overrides:
            override=overrides[p['id']]
            if override['sourceSha256']!=p['sha256']:raise ValueError(f'Metadata evidence invalidated: {p["id"]}')
            p.update(override);p['metadataConflict']=False
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
        if not src.is_file():raise FileNotFoundError(f'Question source missing from archive: {p["id"]}: {src}')
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
        paper={'id':p['id'],'region':'yilan','school':p['school'],'year':p['year'],'semester':p['semester'],'grade':p['grade'],'exam':p['exam'],'title':p.get('name',p.get('title',src.name)),'file':f'./papers/{dest.name}','format':ext[1:],'sha256':sha,'bytes':src.stat().st_size,'sourceUrl':p.get('sourceUrl',p.get('url')),'sourcePage':p['sourcePage'],'curriculum108':p['year']>=108+p['grade']-7,'track':p.get('track','regular'),'questionCount':0,'warning':warning,'answerUrl':answers.get((p['school'],p['year'],p['semester'],p['grade'],p['exam'])),'metadataBasis':p.get('metadataBasis','official-linked-source')}
        if render_dest:
            paper['originalFile']=paper['file'];paper['file']=f'./papers/{render_dest.name}';paper['renderSha256']=p['renderSha256'];paper['renderedFrom']=ext[1:]
        if p.get('sourceFolderYear'):
            paper['sourceFolderYear']=p['sourceFolderYear'];paper['metadataEvidence']=p.get('metadataEvidence')
        if p.get('sourceNote'):paper['sourceNote']=p['sourceNote']
        papers.append(paper);all_ids[paper['id']]=paper
    transcribed={};excluded=[]
    transcript_names=['transcribed-zhonghua-early.json','transcribed-zhonghua-late.json','transcribed-other-schools.json']
    transcript_names += [f.name for f in sorted((ROOT/'research').glob('transcribed-requested-*.json')) if f.stem.rsplit('-',1)[-1].isdigit()]
    transcript_names += [f.name for f in sorted((ROOT/'research').glob('transcribed-bulk-*.json'))]
    for name in transcript_names:
        f=ROOT/'research'/name
        if not f.exists():continue
        for t in json.loads(f.read_text(encoding='utf-8')):
            if t['id'] in transcribed:raise ValueError(f'Duplicate transcription: {t["id"]}')
            transcribed[t['id']]=t
    questions=[];seen=set();review_files=[];source_reviewed=0;pending=0;review_ids={}
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
            review_ids.setdefault(p['id'],[]).append(q['id'])
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
            row={**q,**{k:p[k] for k in ['region','school','year','semester','grade','exam','curriculum108']},'blocks':t['blocks'],'typesetVerified':True,'width':r.width,'height':r.height,'difficultyBasis':q.get('difficultyBasis','編輯教學估計，非官方答對率')}
            if t.get('diagramSvg'):row['diagramSvg']=t['diagramSvg']
            questions.append(row);p['questionCount']+=1;src.close()
    split_path=ROOT/'research/independent-question-splits.json'
    if split_path.exists():
        by_id={q['id']:q for q in questions}
        for plan in json.loads(split_path.read_text(encoding='utf-8')):
            parent=by_id[plan['parentId']]
            if len(plan['children'])<2:raise ValueError('A split needs at least two independent questions')
            parent['selectionHidden']=True;parent['splitInto']=[]
            for child in plan['children']:
                child_id=parent['id']+'::'+str(child['suffix'])
                if child_id in by_id:raise ValueError(f'Duplicate split child {child_id}')
                if child['difficulty'] not in ['easy','medium','hard']:raise ValueError('Invalid child difficulty')
                if not child['blocks'] or any(b['type']!='text' for b in child['blocks']):raise ValueError('Independent splits must use reviewed text blocks')
                row={**parent,'id':child_id,'number':child['sourceNumber'],'blocks':child['blocks'],'difficulty':child['difficulty'],'sourceParentId':parent['id'],'selectionHidden':False}
                row.pop('splitInto',None);row.pop('diagramSvg',None);questions.append(row);by_id[child_id]=row;parent['splitInto'].append(child_id)
    for p in papers:p['questionCount']=sum(q['paperId']==p['id'] and not q.get('selectionHidden') for q in questions)
    completeness_path=ROOT/'research/paper-completeness.json'
    if completeness_path.exists():
        for pid,proof in json.loads(completeness_path.read_text(encoding='utf-8')).items():
            p=all_ids[pid];active=[q for q in questions if q['paperId']==pid and not q.get('selectionHidden')]
            if len(active)!=proof['expectedQuestions']:raise ValueError(f'Incomplete requested paper: {pid}')
            if {t:sum(q['type']==t for q in active) for t in ['choice','fill','written']}!=proof['types']:raise ValueError(f'Wrong paper question types: {pid}')
            p['transcriptionStatus']='complete';p['completionEvidence']=proof['evidence']
    # A downloaded paper is not a completed question bank. Completion requires
    # a whole-paper proof and exact mapping of every source question unit.
    for proof_file in sorted((ROOT/'research').glob('*-bulk-*.json')):
        if not proof_file.name.startswith(('proof-bulk-','completeness-bulk-')):continue
        proof=json.loads(proof_file.read_text(encoding='utf-8'))
        if not isinstance(proof,dict) or 'paperId' not in proof:continue
        pid=proof['paperId'];p=all_ids[pid]
        if proof.get('sourceSha256')!=p['sha256']:raise ValueError(f'Completion proof invalidated: {pid}')
        if proof.get('sourcePrintedYear',p['year'])!=p['year']:raise ValueError(f'Unresolved printed year: {pid}')
        source_ids=set(review_ids.get(pid,[]))
        verified=[transcribed[i] for i in source_ids if i in transcribed and transcribed[i].get('verified')]
        if len(verified)!=proof['expectedQuestions']:raise ValueError(f'Incomplete whole-paper mapping: {pid}: {len(verified)}/{proof["expectedQuestions"]}')
        usable=[q for q in questions if q['paperId']==pid and not q.get('selectionHidden')]
        if len(usable)!=sum(t.get('usable') is not False for t in verified):raise ValueError(f'Incomplete usable mapping: {pid}')
        expected_types=proof.get('expectedTypes',proof.get('types',{}))
        # Excluded source defects still count as reviewed source units.
        curated=json.loads((ROOT/'research'/f'curated-bulk-{pid}.json').read_text(encoding='utf-8'))
        actual_types={kind:sum(q['type']==kind for q in curated) for kind in ['choice','fill','written']}
        if any(actual_types[kind]!=expected_types.get(kind,0) for kind in actual_types):raise ValueError(f'Wrong whole-paper types: {pid}')
        p['transcriptionStatus']=('complete' if len(usable)==len(verified) else 'complete-with-source-issues') if proof.get('visualReviewComplete') is True else 'partial'
        p['sourceUnitCount']=len(verified);p['excludedUnitCount']=len(verified)-len(usable);p['completionEvidence']=proof_file.name
    for p in papers:
        p.setdefault('transcriptionStatus','partial' if p['questionCount'] else 'pending')
    units_path=ROOT/'research/nanyi-units.json';tags_path=ROOT/'research/question-unit-tags.json'
    if units_path.exists():
        units=json.loads(units_path.read_text(encoding='utf-8'));unit_ids={u['id'] for u in units};write('public/data/units.json',units)
        if tags_path.exists():
            tags={t['id']:t for t in json.loads(tags_path.read_text(encoding='utf-8'))}
            for q in questions:
                if q.get('selectionHidden'):continue
                tag=tags.get(q['id'])
                if not tag:raise ValueError(f'Question lacks unit review: {q["id"]}')
                if tag.get('reviewed') is not True:raise ValueError(f'Unit classification not reviewed: {q["id"]}')
                content=json.dumps({'blocks':q.get('blocks',[]),'diagramSvg':q.get('diagramSvg')},ensure_ascii=False,separators=(',',':'))
                if hashlib.sha256(content.encode('utf-8')).hexdigest()!=tag['contentSha256']:raise ValueError(f'Unit review invalidated: {q["id"]}')
                if tag['status']=='assigned':
                    if tag['primaryUnitId'] not in unit_ids or any(u not in unit_ids for u in tag['unitIds']):raise ValueError(f'Unknown curriculum unit: {q["id"]}')
                    if tag['primaryUnitId'] not in tag['unitIds']:raise ValueError(f'Primary unit absent from unit list: {q["id"]}')
                    q.update(primaryUnitId=tag['primaryUnitId'],unitIds=tag['unitIds'],unitAssignmentBasis=tag['assignmentBasis'])
                else:q.update(primaryUnitId='unknown',unitIds=[])
    yilan_paper_count=len(papers)
    unit_ids_all={u['id'] for u in json.loads(units_path.read_text(encoding='utf-8'))}
    metro_papers,metro_questions,metro_summary=prepare_metro.build(ROOT,unit_ids_all)
    ids=set(all_ids)
    for mp in metro_papers:
        if mp['id'] in ids:raise ValueError(f'Duplicate paper id {mp["id"]}')
    qids={q['id'] for q in questions}
    for mq in metro_questions:
        if mq['id'] in qids:raise ValueError(f'Duplicate question id {mq["id"]}')
    papers+=metro_papers;questions+=metro_questions
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
    active_count=sum(not q.get('selectionHidden') for q in questions)
    workflow=[{k:p.get(k) for k in ['id','region','school','year','semester','grade','exam','title','sourceUrl','sourcePage','sha256','questionCount','sourceUnitCount','excludedUnitCount','transcriptionStatus','completionEvidence','warning']} for p in papers]
    write('public/data/paper-workflow.json',workflow)
    coverage={'checkedAt':'2026-11-15','scope':'宜蘭縣中華、羅東、內城國中，105至115學年，僅公開來源；另保留全縣入口盤點。都會區（臺北、新北、桃園、臺中、高雄）各以公開題庫入口全量列舉。','metro':metro_summary,'inventorySources':inv['sources'],'schools':schools,'filesDownloaded':sum((ROOT/p.get('localPath','')).is_file() for p in raw),'paperFiles':len(papers),'yilanPaperFiles':yilan_paper_count,'metroPaperFiles':len(metro_papers),'metroQuestions':len(metro_questions),'reviewedQuestions':active_count,'legacyQuestionGroups':len(questions)-active_count,'sourceReviewedQuestions':source_reviewed,'pendingTranscriptions':pending,'excludedQuestionIssues':excluded,'reviewFiles':review_files,'limitation':'原卷下載、逐題辨識與文字重排分開計數；未完成文字核對的題目不參與組卷。'}
    coverage['paperWorkflow']={status:sum(p['transcriptionStatus']==status for p in papers) for status in ['complete','complete-with-source-issues','partial','pending']}
    coverage['pendingWholePaperTranscriptions']=sum(p['transcriptionStatus'] in ['partial','pending'] for p in papers)
    coverage['unitClassification']={'publisher':'南一','catalogEdition':'112學年度教材簡介本（108課綱）','assigned':sum(q.get('primaryUnitId') not in [None,'unknown'] for q in questions if not q.get('selectionHidden')),'unknown':sum(q.get('primaryUnitId')=='unknown' for q in questions if not q.get('selectionHidden')),'basis':'依題幹、公式與必要圖逐題核對；每題以主要單元計配比，另保留跨單元標籤。'}
    audit_path=ROOT/'research/full-official-crawl-audit.json'
    if audit_path.exists():
        audit=json.loads(audit_path.read_text(encoding='utf-8'))
        source_files=[{**p,**overrides.get(p['id'],{})} for p in audit['allMathFiles']]
        source_questions=[p for p in source_files if p.get('kind')=='question']
        missing=[p['id'] for p in source_questions if p['id'] not in all_ids]
        if missing:raise ValueError(f'Official question files omitted from publication: {missing}')
        for source in source_questions:
            source['declaredMetadata']={k:source.get(k) for k in ['year','semester','grade','exam']}
            source.update({k:all_ids[source['id']][k] for k in ['year','semester','grade','exam']})
        audit_summary={'checkedAt':audit['checkedDate'],'rootUrls':[audit[s]['rootUrl'] for s in ['zhonghua','luodong']],'driveFoldersInspected':len(audit['zhonghua']['folders']),'driveFilesEnumerated':audit['zhonghua']['allFilesEnumerated'],'categoryPagesInspected':len(audit['luodong']['categoryPages']),'examPostsInspected':len(audit['luodong']['inScopePosts']),'mathFilesIncludingAnswers':len(source_files),'questionFilesArchived':len(source_questions),'missingQuestionDownloads':missing,'downloadStatuses':dict(collections.Counter(p['downloadStatus'] for p in source_files)),'criticalFindings':audit['criticalFindings'],'missingLuodongYearsInOfficialIndex':audit['luodong']['missingYearsFromOfficialCategory'],'limitations':audit['limitations'],'coverage':audit['coverage'],'files':[{k:p.get(k) for k in ['id','school','year','semester','grade','exam','name','kind','sourceUrl','sourcePage','path','sha256','bytes','downloadStatus','sourceFolderYear']} for p in source_files]}
        audit_summary['coverageBasis']='status與原列舉ID保留官方目錄原分類；archivedCanonicalQuestionIds依卷首修正後的實際發布分類。'
        for slot in audit_summary['coverage']:
            slot['archivedCanonicalQuestionIds']=[p['id'] for p in source_questions if all(p.get(k)==slot.get(k) for k in ['school','year','semester','grade','exam'])]
        for row,source in zip(audit_summary['files'],source_files):
            if source.get('declaredMetadata'):row['declaredMetadata']=source['declaredMetadata']
        write('public/data/official-source-audit.json',audit_summary)
        coverage['officialSourceAudit']={k:audit_summary[k] for k in ['checkedAt','driveFoldersInspected','categoryPagesInspected','examPostsInspected','mathFilesIncludingAnswers','questionFilesArchived','missingQuestionDownloads']}
    write('public/data/papers.json',papers);write('public/data/questions.json',questions);write('public/data/coverage.json',coverage)
    print(json.dumps({'paperFiles':len(papers),'reviewedQuestions':active_count,'legacyQuestionGroups':len(questions)-active_count,'years':sorted(set(p['year'] for p in papers)),'schools':sorted(set(p['school'] for p in papers))},ensure_ascii=False))
if __name__=='__main__':main()
