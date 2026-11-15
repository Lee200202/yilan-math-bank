"""Fresh anonymous traversal of the two official entries, with complete link audit.
Does not rewrite prior catalogs or public data. Existing original downloads are hash-checked;
newly listed mathematical files are downloaded, with failures retained explicitly.
"""
import concurrent.futures,datetime,hashlib,json,pathlib,re,time,unicodedata
from urllib.parse import quote,unquote,urlsplit
import requests
from bs4 import BeautifulSoup
R=pathlib.Path(__file__).resolve().parent;ROOT=R.parent
PAGES=R/'full-official-crawl-pages';PAGES.mkdir(exist_ok=True)
RAW=R/'full-crawl-raw';RAW.mkdir(exist_ok=True)
ROOT_ID='0B-2YnWjsnzalMm84ck9yRUtPTG8';ROOT_KEY='0-Cc-rWuKRrhfzoTnh3M_BpA'
ROOT_URL=f'https://drive.google.com/drive/folders/{ROOT_ID}?resourcekey={ROOT_KEY}'
LD_URL='https://2blog.ilc.edu.tw/16771/category/c-12565/'
STARTED=datetime.datetime.now(datetime.timezone.utc).isoformat();HTTP=[]
existing={};catalogs=[]
for name in ['zhonghua_catalog.json','zhonghua-pre108-catalog.json','luodong-papers.json','luodong-pre108-papers.json']:
    catalogs+=json.loads((R/name).read_text(encoding='utf8'))
for row in catalogs:existing[row['id']]=row
public=json.loads((ROOT/'public/data/papers.json').read_text(encoding='utf8'))

def dump(name,data):(R/name).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
def http(url,key,attempts=2):
    for i in range(attempts):
        try:
            res=requests.get(quote(url,safe=':/?=&%'),timeout=45,headers={'User-Agent':'Mozilla/5.0 (public exam inventory)'})
            res.raise_for_status();res.encoding='utf8'
            path=PAGES/(key+'.html');path.write_bytes(res.content)
            evidence={'requestedUrl':url,'resolvedUrl':res.url,'httpStatus':res.status_code,'sha256':hashlib.sha256(res.content).hexdigest(),'bytes':len(res.content),'evidencePath':str(path.relative_to(ROOT)).replace('\\','/'),'retrievedAt':datetime.datetime.now(datetime.timezone.utc).isoformat()}
            HTTP.append(evidence);return res,evidence
        except Exception:
            if i==attempts-1:raise

def drive_list(fid,path):
    url=ROOT_URL if fid==ROOT_ID else f'https://drive.google.com/drive/folders/{fid}'
    res,evidence=http(url,'drive-'+fid)
    m=re.search(r"window\['_DRIVE_ivd'\] = '((?:\\.|[^'])*)';",res.text)
    if not m:raise ValueError('No anonymous folder listing in response')
    enc=m.group(1).replace('\\x','\\u00').replace("\\'","'")
    data=json.loads(json.loads('"'+enc+'"'))
    rows=[{'id':x[0],'name':x[2],'mime':x[3],'path':path+[x[2]],'url':('https://drive.google.com/drive/folders/' if x[3]=='application/vnd.google-apps.folder' else 'https://drive.google.com/file/d/')+x[0]+('' if x[3]=='application/vnd.google-apps.folder' else '/view')} for x in (data[0] or [])]
    return rows,{'id':fid,'path':path,'status':'empty-folder' if not rows else 'listed','itemCount':len(rows),'evidence':evidence,'children':[{'id':x['id'],'name':x['name'],'mime':x['mime']} for x in rows]}

def parse_slot(name,path):
    name=unicodedata.normalize('NFKC',name);joined='/'.join(unicodedata.normalize('NFKC',p) for p in path)
    ym=re.search(r'(10[5-9]|11[0-5])(?:學年度|學年)',joined)
    folder_year=int(ym[1]) if ym else None
    folder_sem=1 if re.search(r'上學期|第一學期|第1學期',joined) else 2 if re.search(r'下學期|第二學期|第2學期',joined) else None
    em=re.search(r'第([123一二三])次',joined);emap={'1':1,'2':2,'3':3,'一':1,'二':2,'三':3}
    folder_exam=emap[em[1]] if em else None
    folder_grade=None
    gm=re.search(r'([789七八九])年級',joined)
    if gm:folder_grade=int(gm[1]) if gm[1].isdigit() else {'七':7,'八':8,'九':9}[gm[1]]
    ny=re.match(r'(\d{3})',name);filename_year=int(ny[1]) if ny and 105<=int(ny[1])<=115 else None
    filename_sem=filename_exam=filename_grade=None
    m=re.match(r'\d{3}([上下])[-_ ]?([123])(?:次|段|[-_ ])+([123789七八九])',name)
    if m:
        filename_sem=1 if m[1]=='上' else 2;filename_exam=int(m[2]);filename_grade=int(m[3]) if m[3].isdigit() else {'七':7,'八':8,'九':9}[m[3]]
        if filename_grade in [1,2,3]:filename_grade+=6
    m2=re.match(r'\d{3}-([12])-([123])-([789])',name)
    if m2:filename_sem,filename_exam,filename_grade=map(int,m2.groups())
    if filename_grade is None:
        m=re.search(r'([789])數|([789])年級|數學[_ -]*([789])',name)
        if m:filename_grade=int(next(g for g in m.groups() if g))
    if filename_grade is None:
        m=re.search(r'([一二三七八九])年級',name)
        if m:filename_grade={'一':7,'二':8,'三':9,'七':7,'八':8,'九':9}[m[1]]
    if filename_grade is None:
        m=re.match(r'數([123])(?:\.|$)',name)
        if m:filename_grade=int(m[1])+6
    semester=filename_sem or folder_sem;exam=filename_exam or folder_exam;grade=filename_grade or folder_grade
    conflicts=[]
    for field,a,b in [('year',folder_year,filename_year),('semester',folder_sem,filename_sem),('exam',folder_exam,filename_exam),('grade',folder_grade,filename_grade)]:
        if a and b and a!=b:conflicts.append({'field':field,'folder':a,'fileName':b})
    return {'year':folder_year or filename_year,'semester':semester,'exam':exam,'grade':grade,'folderSlot':{'year':folder_year,'semester':folder_sem,'exam':folder_exam,'grade':folder_grade},'fileNameSlot':{'year':filename_year,'semester':filename_sem,'exam':filename_exam,'grade':filename_grade},'metadataConflicts':conflicts}

def kind(name,path):
    s='/'.join(path)
    if '答案卷' in s:return 'answer_sheet'
    if ('解答' in s or '答案' in s):return 'answer'
    return 'question'

def download(row):
    old=existing.get(row['id']);target=None
    if old and old.get('localPath'):
        path=ROOT/old['localPath'].replace('\\','/')
        if path.is_file():
            data=path.read_bytes();sha=hashlib.sha256(data).hexdigest()
            if old.get('sha256') and sha!=old['sha256']:
                row.update(downloadStatus='local-hash-mismatch',localPath=old['localPath']);return row
            row.update(downloadStatus='existing-original-verified',localPath=str(path.relative_to(ROOT)).replace('\\','/'),sha256=sha,bytes=len(data));return row
    try:
        ext=pathlib.Path(urlsplit(row['name']).path).suffix.lower() or '.bin';target=RAW/(row['id']+ext)
        urls=[row['sourceUrl']] if row['school']=='羅東國中' else [f'https://drive.google.com/uc?export=download&id={row["id"]}',f'https://drive.usercontent.google.com/download?id={row["id"]}&export=download&authuser=0&confirm=t']
        errors=[]
        for url in urls:
            try:
                res=requests.get(quote(url,safe=':/?=&%'),timeout=50);res.raise_for_status();b=res.content
                if not (b.startswith(b'%PDF') or b[:2]==b'PK' or b[:4]==bytes.fromhex('d0cf11e0')):raise ValueError('Response is not a PDF/Word original')
                target.write_bytes(b);row.update(downloadStatus='downloaded-now',localPath=str(target.relative_to(ROOT)).replace('\\','/'),sha256=hashlib.sha256(b).hexdigest(),bytes=len(b));return row
            except Exception as e:errors.append({'url':url,'error':str(e)})
        row.update(downloadStatus='download-failed',downloadErrors=errors)
    except Exception as e:row.update(downloadStatus='download-failed',error=str(e))
    return row

def crawl_zhonghua():
    top,rootlog=drive_list(ROOT_ID,[]);folders=[rootlog];todo=[];files=[];errors=[]
    for x in top:
        ym=re.match(r'(\d{3})',x['name'])
        if x['mime']=='application/vnd.google-apps.folder' and ym and 105<=int(ym[1])<=115:todo.append(x)
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
        while todo:
            pending={ex.submit(drive_list,x['id'],x['path']):x for x in todo};todo=[]
            for fut in concurrent.futures.as_completed(pending):
                parent=pending[fut]
                try:
                    rows,log=fut.result();folders.append(log)
                    for x in rows:
                        if x['mime']=='application/vnd.google-apps.folder':todo.append(x)
                        else:files.append(x)
                except Exception as e:errors.append({'id':parent['id'],'path':parent['path'],'error':str(e)})
            dump('full-official-drive-progress.json',{'folders':folders,'allFiles':files,'errors':errors,'pendingFolders':todo})
            print('fresh drive folders',len(folders),'files',len(files),'pending',len(todo),flush=True)
    math=[]
    for x in files:
        if '數' not in '/'.join(x['path']):continue
        row={**x,**parse_slot(x['name'],x['path']),'school':'中華國中','kind':kind(x['name'],x['path']),'sourceUrl':x['url'],'sourcePage':'https://www.chjh.ilc.edu.tw/','metadataBasis':'fresh official-linked public Drive folder listing; filename/folder identity retained separately'}
        if x['id'] in existing:
            old=existing[x['id']];row['priorCatalogMetadata']={k:old.get(k) for k in ['year','semester','exam','grade','kind','metadataBasis','metadataWarning','sourceNote'] if old.get(k) is not None}
        if row['id']=='1ZZUkKjnXYPQn5CwCnQPqN9ayYj__D6wS':
            row['confirmedHeaderSlot']={'year':108,'semester':1,'exam':2,'grade':8};row['headerVerification']='First source PDF page reopened and visually checked: 宜蘭縣中華國民中學一○八學年度第一學期第二次段考數學科試卷 八年級';row['identityStatus']='confirmed-header-conflict';row['metadataConflicts'].append({'field':'year','declared':109,'confirmedHeader':108,'evidencePath':'research/full-official-year-conflict-1ZZ.png'});row['eligibleAsDeclaredYearQuestion']=False
        math.append(row)
    return {'rootUrl':ROOT_URL,'rootEntries':top,'folders':folders,'mathFiles':math,'allFilesEnumerated':len(files),'folderErrors':errors,'emptyFolders':[x for x in folders if x['status']=='empty-folder']}

def ldslot(title):
    ym=re.search(r'(\d{3})學年度',title);year=int(ym[1]) if ym else None
    semester=1 if '第一學期' in title else 2 if '第二學期' in title else None
    em=re.search(r'第([一二三123])次',title);exam={'一':1,'二':2,'三':3,'1':1,'2':2,'3':3}.get(em[1]) if em else None
    return year,semester,exam
def crawl_luodong():
    url=LD_URL;seen=set();pages=[];posts={}
    while url and url not in seen:
        seen.add(url);res,evidence=http(url,'luodong-category-'+str(len(pages)+1));s=BeautifulSoup(res.text,'html.parser');entries=[]
        for art in s.select('article'):
            h=art.select_one('.entry-title a')
            if not h:continue
            entries.append({'title':h.get_text(' ',strip=True),'url':h['href']});posts[h['href']]={'title':h.get_text(' ',strip=True),'html':str(art.select_one('.entry-content') or art),'sourceUrl':h['href']}
        nxt=next((a['href'] for a in s.select('a[href]') if '較舊的文章' in a.get_text()),None)
        pages.append({'evidence':evidence,'posts':entries,'nextPage':nxt});url=nxt
    rows=[];math_links=[]
    for post in posts.values():
        year,semester,exam=ldslot(post['title'])
        if not year or not 105<=year<=115:continue
        # Fetch every in-scope post itself, rather than trusting only category excerpts.
        res,evidence=http(post['sourceUrl'],'luodong-post-'+hashlib.sha256(post['sourceUrl'].encode()).hexdigest()[:16]);s=BeautifulSoup(res.text,'html.parser');art=s.select_one('.entry-content') or s
        links=[]
        for a in art.select('a[href]'):
            name=a.get_text(' ',strip=True);href=a['href']
            if not ('數學' in name or '數學' in unquote(href)):continue
            context=re.sub(r'\s','',a.parent.get_text());gm=re.search(r'([七八九])年級',context);grade={'七':7,'八':8,'九':9}.get(gm[1]) if gm else None
            identity=f'ld-{year}-{semester}-{exam}-{grade}';file_name=pathlib.Path(unquote(urlsplit(href).path)).name
            role=kind(name+' '+file_name,[name,file_name]);row={'id':identity,'name':file_name,'school':'羅東國中','year':year,'semester':semester,'exam':exam,'grade':grade,'kind':role,'path':[post['title'],context[:160],name],'sourceUrl':href,'sourcePage':post['sourceUrl'],'metadataBasis':'fresh official category pagination and each full official post; grade from linked paragraph','evidence':evidence,'linkLabel':name,'linkContext':context}
            if identity in existing:
                old=existing[identity]
                row['priorCatalogMetadata']={k:old.get(k) for k in ['year','semester','exam','grade','metadataConflict','contentDuplicateOf','metadataBasis'] if old.get(k) is not None}
            rows.append(row);links.append({'id':identity,'label':name,'url':href,'grade':grade})
        math_links.append({'title':post['title'],'year':year,'semester':semester,'exam':exam,'sourceUrl':post['sourceUrl'],'mathLinks':links,'evidence':evidence})
    return {'rootUrl':LD_URL,'categoryPages':pages,'inScopePosts':math_links,'mathFiles':rows,'missingYearsFromOfficialCategory':[y for y in range(105,116) if y not in {x['year'] for x in rows}]}

def coverage(school,rows,folders=None):
    result=[]
    for year in range(105,116):
      for semester in [1,2]:
       for exam in [1,2,3]:
        for grade in [7,8,9]:
            cell=[x for x in rows if (x.get('year'),x.get('semester'),x.get('exam'),x.get('grade'))==(year,semester,exam,grade)]
            questions=[x for x in cell if x['kind']=='question'];usable=[x for x in questions if x.get('eligibleAsDeclaredYearQuestion',True)]
            state='files-listed' if cell else 'no-math-file-listed'
            if year==105 and semester==1 and exam==2 and school=='中華國中':state='empty-folder'
            if year==115 and semester==2 and not cell:state='not-current-semester'
            if questions and not usable:state='listed-question-header-conflict'
            result.append({'school':school,'year':year,'semester':semester,'exam':exam,'grade':grade,'status':state,'questionFileIds':[x['id'] for x in questions],'nonConflictingDeclaredQuestionIds':[x['id'] for x in usable],'answerFileIds':[x['id'] for x in cell if x['kind']=='answer'],'answerSheetFileIds':[x['id'] for x in cell if x['kind']=='answer_sheet']})
    return result

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        fz=ex.submit(crawl_zhonghua);fl=ex.submit(crawl_luodong);zh=fz.result();ld=fl.result()
    allrows=zh['mathFiles']+ld['mathFiles']
    # The entire index is persisted before downloading any newly discovered file.
    dump('full-official-crawl-index.json',{'checkedDate':'2026-11-15','zhonghua':zh,'luodong':ld,'allMathFiles':allrows})
    print('FULL INDEX SAVED',len(allrows),'math files',flush=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:allrows=list(ex.map(download,allrows))
    byid={x['id']:x for x in allrows}
    zh['mathFiles']=[byid[x['id']] for x in zh['mathFiles']];ld['mathFiles']=[byid[x['id']] for x in ld['mathFiles']]
    public_two=[x for x in public if x['school'] in ['中華國中','羅東國中']];pubids={x['id'] for x in public_two};freshquestions=[x for x in allrows if x['kind']=='question'];freshids={x['id'] for x in freshquestions}
    seen_hash={};duplicates=[]
    for row in allrows:
        if not row.get('sha256'):continue
        key=(row['school'],row['sha256'])
        if key in seen_hash:duplicates.append({'id':row['id'],'sameContentAs':seen_hash[key],'school':row['school']})
        else:seen_hash[key]=row['id']
    report={'checkedDate':'2026-11-15','startedAtUTC':STARTED,'finishedAtUTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':{'years':list(range(105,116)),'schools':['中華國中','羅東國中'],'subject':'數學','sequence':'Fresh full official index saved first; existing original files hash-verified and missing downloads attempted afterwards.'},'zhonghua':zh,'luodong':ld,'allMathFiles':allrows,'coverage':coverage('中華國中',zh['mathFiles'],zh['folders'])+coverage('羅東國中',ld['mathFiles']),'reconciliation':{'existingPublicPaperFilesAllSchools':len(public),'existingPublicFilesTheseTwoSchools':len(public_two),'freshOfficialMathFilesIncludingAnswerSheetsAndAnswers':len(allrows),'freshOfficialQuestionFiles':len(freshquestions),'questionIdsNotInPublic':sorted(freshids-pubids),'publicIdsNotInFreshQuestionListing':sorted(pubids-freshids),'newSourceFileIdsNotInPriorCatalogs':sorted({r['id'] for r in allrows}-set(existing)),'unparsedMetadata':[{'id':x['id'],'name':x['name'],'path':x['path']} for x in allrows if any(x.get(k) is None for k in ['year','semester','exam','grade'])],'downloadStatuses':dict(__import__('collections').Counter(x['downloadStatus'] for x in allrows)),'identicalContentFiles':duplicates},'criticalFindings':{'zhonghua105UpperSecond':{'status':'empty-folder','folderId':'1H8qN7duNBh8Q68u--W_aQWBJ0dF1O9ds','folderUrl':'https://drive.google.com/drive/folders/1H8qN7duNBh8Q68u--W_aQWBJ0dF1O9ds','meaning':'The actual official 105 upper-semester second-exam folder is empty; not a keyword-search or metadata-parser failure. Root agent also opened this path in the browser and observed the empty-folder UI.'},'zhonghua109UpperSecondGrade8':{'fileId':'1ZZUkKjnXYPQn5CwCnQPqN9ayYj__D6wS','status':'confirmed-header-conflict','folderAndFilenameYear':109,'actualHeaderYear':108,'actualHeaderSemester':1,'actualHeaderExam':2,'actualHeaderGrade':8,'evidencePath':'research/full-official-year-conflict-1ZZ.png','meaning':'Cannot count this upload as a genuine 109 academic-year question paper.'}},'httpEvidence':HTTP,'limitations':['A public folder listing is not proof that every expected exam was held or every paper was published.','Question/answer identity uses official paths and labels; most PDF headers still require individual review. Confirmed mismatches are retained explicitly.','Source originals already on disk are retained with verified SHA256 rather than silently redownloaded/overwritten.','No login gate was bypassed and no missing paper was replaced by another year.']}
    dump('full-official-crawl-audit.json',report)
    print(json.dumps(report['reconciliation'],ensure_ascii=False),flush=True)
if __name__=='__main__':main()
