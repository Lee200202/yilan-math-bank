"""Only the findings actually opened and read visually are applied as overrides."""
import json,pathlib,hashlib
R=pathlib.Path(__file__).resolve().parent;ROOT=R.parent
sp=R/'full-official-header-screen.json'
initial=R/'full-official-header-screen-initial.json'
if not initial.exists():initial.write_bytes(sp.read_bytes())
audit=json.loads((R/'full-official-crawl-audit.json').read_text(encoding='utf8'));byid={x['id']:x for x in audit['allMathFiles']}
op=R/'paper-metadata-overrides.json';over=json.loads(op.read_text(encoding='utf8'))
findings=[
 {'id':'ld-106-2-1-9','year':106,'semester':1,'exam':1,'grade':9,'sourceFolderYear':106,'sourceFolderSemester':2,'contentDuplicateOf':'ld-106-1-1-9','metadataBasis':'已實際開啟原始掃描PDF首頁，卷首清楚為106學年度第一學期九年級數學科第一次段考。官網106下第一次文章誤連到同一原PDF；原始SHA與ld-106-1-1-9完全相同。按卷首核定上學期，保留來源文章下學期供追溯。','metadataEvidence':'research/ld-106-2-1-9-full-header-check.png'},
 {'id':'ld-106-1-1-8','year':105,'semester':2,'exam':1,'grade':8,'sourceFolderYear':106,'sourceFolderSemester':1,'contentDuplicateOf':'ld-105-2-1-8','metadataBasis':'已將原DOC以全新獨立Word唯讀禁宏轉PDF並實際看首頁；卷首清楚為105學年度第二學期八年級第一次段考。原始DOC與ld-105-2-1-8完全同SHA。官網106上第一次文章誤連舊卷，按原卷首核定105下，保留來源106上供追溯。','metadataEvidence':'research/full-official-conflict-ld-106-1-1-8.png'},
 {'id':'1AhIbjzAwUEmFrWisDMwTc-OzZhFUpm91','year':108,'semester':2,'exam':3,'grade':8,'sourceFolderYear':107,'sourceFolderSemester':2,'metadataBasis':'已將原DOC以全新獨立Word唯讀禁宏轉PDF並實際看首頁；卷首紅字清楚為一○八學年度第二學期第三次段考、八年級。資料夾/檔名宣告107，按卷首核定108並保留來源年度107。與108下第三次正確資料夾的161r...原卷正文不同，不以相同卷首直接合併。','metadataEvidence':'research/full-official-conflict-1AhIbjzAwUEmFrWisDMwTc-OzZhFUpm91.png'}]
for item in findings:
    item['sourceSha256']=byid[item['id']]['sha256'];over[item['id']]={**over.get(item['id'],{}),**{k:v for k,v in item.items() if k!='id'}}
op.write_text(json.dumps(over,ensure_ascii=False,indent=2),encoding='utf8')
report={'checkedDate':'2026-11-15','visualConfirmedOverrides':findings,'falsePositiveResolved':{'id':'1UMI7X448uFG4u-xZh7bBZSj2jsO2Phsh','result':'No metadata correction. Actual displayed Word/PDF header is106學年度第二學期第三次段考、一年級(7). The initial text-stream order placed a question about小恩第二次段考 before the floating header and falsely suggested exam2. Source first page was opened visually; position-sorted extraction is now used.','metadataEvidence':'research/full-official-conflict-1UMI7X448uFG4u-xZh7bBZSj2jsO2Phsh.png'},'additionalSameHeaderDistinctPaper':{'misfiledId':'1AhIbjzAwUEmFrWisDMwTc-OzZhFUpm91','actual108FolderId':'161rWGzcQYllb6Vl0DXXV1sjxuPMFzpDP','normalizedCjkSimilarity':0.2474074074074074,'result':'Both headers show108下三八年級, but first questions and most content differ. Do not merge solely on header. Only the two Luodong byte-identical files are canonical duplicates.'},'scannedOriginalsNotReadByRegex':'All unresolved scanned/textless headers remain pending; this report does not infer their identity from a regex.'}
(R/'full-official-header-visual-review.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print('3 newly visually confirmed metadata overrides; one parser false positive retained without changes')
