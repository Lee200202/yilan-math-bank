"""Enrich the completed fresh crawl with independently checked header findings.
The original HTTP evidence remains unchanged. Does not modify the source catalogs/public bank.
"""
import json,pathlib,re,hashlib,importlib.util,collections,datetime
import pymupdf as fitz
R=pathlib.Path(__file__).resolve().parent;ROOT=R.parent
spec=importlib.util.spec_from_file_location('fresh_inventory',R/'full-official-crawl.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
p=R/'full-official-crawl-audit.json';audit=json.loads(p.read_text(encoding='utf8'));rows=audit['allMathFiles']
for row in rows:
    if row['school']=='中華國中':
        parsed=mod.parse_slot(row['name'],row['path'])
        for key,val in parsed.items():row[key]=val
    if row['id']=='1ZZUkKjnXYPQn5CwCnQPqN9ayYj__D6wS':
        row['metadataConflicts'].append({'field':'year','declared':109,'confirmedHeader':108,'evidencePath':'research/full-official-year-conflict-1ZZ.png'})
    if row.get('localPath') and row['localPath'].lower().endswith('.pdf'):
        try:
            d=fitz.open(ROOT/row['localPath']);header=d[0].get_text()[:450];row['headerTextCandidate']=header
            d.close()
        except Exception as e:row['headerReadError']=str(e)
    if row['downloadStatus']=='download-failed':
        row['downloadFailureDetail']={'classification':'empty-download-response','httpStatus':200,'contentType':'application/octet-stream','bytes':0,'checkedAtUTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'evidencePath':f'research/full-official-failed-download-{row["id"]}.bin','previewPageEvidence':f'research/full-official-failed-view-{row["id"]}.html','description':'The official listing and /view page exist, but the tested public download endpoint returned a zero-byte response. Not classified as a login restriction.'}
joint=next(x for x in rows if x['id']=='1ODYj-V7KzqhYr8EM7s2gkTI2Rb8qKDg3')
joint.update(year=107,semester=2,exam=3,grade=8,kind='question',confirmedHeaderSlot={'year':107,'semester':2,'exam':3,'grade':8},identityStatus='confirmed-header-reviewed',headerVerification='Original PDF reopened: 宜蘭縣107學年度第二學期第三次段考共同命題／八年級數學科試題',metadataBasis='Fresh official Drive folder listing plus actual PDF header visual check',metadataEvidence='research/full-official-unclassified-supplement.png')
byid={x['id']:x for x in rows}
audit['zhonghua']['mathFiles']=[byid[x['id']] for x in audit['zhonghua']['mathFiles']]
audit['luodong']['mathFiles']=[byid[x['id']] for x in audit['luodong']['mathFiles']]
audit['coverage']=mod.coverage('中華國中',audit['zhonghua']['mathFiles'],audit['zhonghua']['folders'])+mod.coverage('羅東國中',audit['luodong']['mathFiles'])
empty=next(x for x in audit['zhonghua']['folders'] if x['id']=='1H8qN7duNBh8Q68u--W_aQWBJ0dF1O9ds');assert empty['itemCount']==0 and empty['status']=='empty-folder'
audit['criticalFindings']['zhonghua105UpperSecond']['httpEvidence']=empty['evidence']
audit['criticalFindings']['zhonghua105UpperSecond']['itemCount']=0
audit['criticalFindings']['zhonghua107LowerThirdGrade8']={'fileId':joint['id'],'name':joint['name'],'year':107,'semester':2,'exam':3,'grade':8,'status':'newly-identified-paper-previously-excluded-as-unclassified','evidencePath':joint['metadataEvidence'],'meaning':'The original is 4 PDF pages and explicitly identifies grade 8 in its header. Previous grade parser failed because the filename has no grade; add to the 269-file public snapshot rather than leaving it unclassified.'}
comparison=json.loads((R/'full-official-108-109-duplicate-comparison.json').read_text(encoding='utf8'));comparison['visualComparisonResult']='Distinct papers, not duplicate copies. Both headers show 108 upper-semester second exam, but their first question and most subsequent questions differ. Keep the source-folder conflict explicit; do not merge by matching header alone.';comparison['firstQuestionDeclared109']='計算 √(35/12)÷√(7/3)';comparison['firstQuestion108Docx']='下列何者正確？ four radical equality statements'
(R/'full-official-108-109-duplicate-comparison.json').write_text(json.dumps(comparison,ensure_ascii=False,indent=2),encoding='utf8');audit['criticalFindings']['zhonghua108AndMisfiled109Comparison']={k:v for k,v in comparison.items() if not k.endswith('Text')}
audit['reconciliation']['unparsedMetadata']=[{'id':x['id'],'name':x['name'],'path':x['path']} for x in rows if any(x.get(k) is None for k in ['year','semester','exam','grade'])]
audit['reconciliation']['mathRoles']=dict(collections.Counter(x['kind'] for x in rows))
audit['reconciliation']['allGradeSlotsResolved']=not audit['reconciliation']['unparsedMetadata']
audit['reconciliation']['publicOriginalSnapshotNote']='Reconciliation is against the 269 public paper files read at the beginning of this fresh run; the root agent may since have integrated new metadata.'
audit['finishedMetadataReviewAtUTC']=datetime.datetime.now(datetime.timezone.utc).isoformat()
p.write_text(json.dumps(audit,ensure_ascii=False,indent=2),encoding='utf8')
op=R/'paper-metadata-overrides.json';over=json.loads(op.read_text(encoding='utf8')) if op.exists() else {}
over[joint['id']]={'year':107,'semester':2,'exam':3,'grade':8,'kind':'question','sourceFolderYear':107,'metadataBasis':'原檔名0627共同命題數學.pdf未寫年級；已實際開啟原PDF卷首，明列宜蘭縣107學年度第二學期第三次段考共同命題、八年級數學科試題。','metadataEvidence':joint['metadataEvidence'],'sourceSha256':joint['sha256'],'sourceNote':'中華國中官方公開目錄所列的宜蘭縣共同命題卷，非自行假定適用年級。'}
op.write_text(json.dumps(over,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'mathFiles':len(rows),'questionFiles':sum(x['kind']=='question' for x in rows),'unparsedMetadata':audit['reconciliation']['unparsedMetadata'],'newlyResolvedGrade8Paper':joint['id'],'empty105UpperSecondFolder':empty['itemCount']},ensure_ascii=False))
