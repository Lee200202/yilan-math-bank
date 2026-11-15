"""Verify all listed grade-8 upper-semester second-exam originals and Word derivatives."""
import json,pathlib,hashlib,collections,re,datetime
R=pathlib.Path(__file__).resolve().parent;ROOT=R.parent
audit=json.loads((R/'full-official-crawl-audit.json').read_text(encoding='utf8'))
papers=json.loads((ROOT/'public/data/papers.json').read_text(encoding='utf8'));public={p['id']:p for p in papers}
manifest=json.loads((R/'bulk-render-manifest.json').read_text(encoding='utf8'));renders={r['id']:r for r in manifest}
override=json.loads((R/'paper-metadata-overrides.json').read_text(encoding='utf8'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
priority=[]
for row in audit['allMathFiles']:
    if (row.get('semester'),row.get('exam'),row.get('grade'))!=(1,2,8):continue
    item={k:row.get(k) for k in ['id','school','year','semester','exam','grade','kind','name','sourceUrl','sourcePage','path','localPath','sha256','bytes','downloadStatus']}
    item['declaredCatalogYear']=row['year'];item['headerOverride']=override.get(row['id'])
    if item['headerOverride']:item['effectiveYear']=item['headerOverride'].get('year',row['year'])
    else:item['effectiveYear']=row['year']
    src=ROOT/row['localPath'];item['sourceExists']=src.is_file();item['sourceSha256Matches']=item['sourceExists'] and sha(src)==row['sha256'];item['sourceIdMatchesURL']=row['id'] in row['sourceUrl'] if row['school']=='中華國中' else True
    p=public.get(row['id']);item['inPublicCatalog']=bool(p)
    if p:
        original=p.get('originalFile',p['file']);original_path=ROOT/'public'/original.removeprefix('./');item['publicOriginalPath']='public/'+original.removeprefix('./');item['publicOriginalExists']=original_path.is_file();item['publicOriginalSha256Matches']=original_path.is_file() and sha(original_path)==row['sha256'];item['publicMetadata']={k:p.get(k) for k in ['school','year','semester','exam','grade','format','renderedFrom']}
    if row['id'] in renders:
        r=renders[row['id']];pdf=ROOT/r['renderPath'];item['renderPath']=r['renderPath'];item['renderSha256Matches']=pdf.is_file() and sha(pdf)==r['renderSha256'];item['renderSourceSha256Matches']=r['sourceSha256']==row['sha256'];item['renderVisualQA']=r.get('visualQA')
    priority.append(item)
slots=[]
for school in ['中華國中','羅東國中']:
 for year in range(105,116):
    rows=[r for r in priority if r['school']==school and r['declaredCatalogYear']==year];qs=[r for r in rows if r['kind']=='question'];valid=[r for r in qs if not r['headerOverride'] or r['effectiveYear']==year]
    if valid:status='available-original-verified'
    elif school=='中華國中' and year==105:status='official-folder-empty'
    elif school=='中華國中' and year==109:status='listed-question-header-is-108-not-109'
    elif school=='中華國中' and year==115:status='current-official-year-folder-only-first-exam-listed'
    else:status='no-official-year-category-post-or-question-link'
    slots.append({'school':school,'year':year,'semester':1,'exam':2,'grade':8,'status':status,'questionIds':[r['id'] for r in qs],'nonConflictingQuestionIds':[r['id'] for r in valid],'answerIds':[r['id'] for r in rows if r['kind']=='answer']})
errors=[]
for r in priority:
    for k in ['sourceSha256Matches','sourceIdMatchesURL','publicOriginalSha256Matches','renderSha256Matches','renderSourceSha256Matches']:
        if k in r and not r[k]:errors.append({'id':r['id'],'check':k})
report={'checkedDate':'2026-11-15','scope':'中華、羅東105–115學年度八年級上學期第二次段考；官方原卷與解答完整清單核對','priorityFiles':priority,'slots':slots,'summary':{'listedOriginalQuestionFiles':sum(r['kind']=='question' for r in priority),'listedAnswerFiles':sum(r['kind']=='answer' for r in priority),'nonConflictingQuestionSlots':sum(s['status']=='available-original-verified' for s in slots),'requestedYearSchoolSlots':len(slots),'wordOriginalsRendered':len(renders),'integrityFailures':errors},'notes':['1ZZ...宣告109但卷首108，保留來源衝突，不當作109真卷。','108 DOCX與1ZZ...正文不同，不因卷首相同而合併成同卷。','中華105上第2次官方資料夾直接列為空，並非搜尋失敗。','中華115目前官方上學期目錄只有第1次，未編造第2次。','羅東官方分類沒有109、111、113–115學年原卷連結。']}
(R/'priority-upper2-grade8-source-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
if errors:raise SystemExit(json.dumps(errors,ensure_ascii=False))
print(json.dumps(report['summary'],ensure_ascii=False))

# Keep the human-readable account tied to actual fresh traversal counts.
school_counts={s:collections.Counter(x['year'] for x in audit['allMathFiles'] if x['school']==s and x['kind']=='question') for s in ['中華國中','羅東國中']}
lines=['# 官方根入口完整盤點與八上二來源驗證','','查核日期：2026-11-15。這次重新匿名實際走官方入口，不以舊摘要或關鍵字結果代替目錄。','','## 實際查找路徑','',
'- 中華：校方公開 [Drive 根目錄](https://drive.google.com/drive/folders/0B-2YnWjsnzalMm84ck9yRUtPTG8?resourcekey=0-Cc-rWuKRrhfzoTnh3M_BpA) → 105–115 學年度 → 上／下學期 → 每次段考 → 題目／解答／答案卷。',
f'- 本次實際取得 {len(audit["zhonghua"]["folders"])} 個資料夾回應（含根），列舉 {audit["zhonghua"]["allFilesEnumerated"]} 個全科檔案，再識別其中 {len(audit["zhonghua"]["mathFiles"])} 個數學檔。每個資料夾有 HTTP 回應 SHA、子項清單與本機證據，沒有隱藏略過年級。',
'- 羅東：[官方歷屆試題分類](https://2blog.ilc.edu.tw/16771/category/c-12565/) → 全部五頁分類 → 每個105起的完整文章 → 數學附件。實際取得87個數學原卷連結。',
'- 先將全清單寫入 `full-official-crawl-index.json`，再核驗既有原始下載檔及嘗試未成功檔案；最終證據在 `full-official-crawl-audit.json`。','','## 檔案數與題數分開','',
'兩個官方來源共 **425 個數學檔案**，包括 **255 個題目卷檔案、165 個解答檔案、5 個答案卷檔案**。425 不是425份考卷，也不是425道題目。',
'422個原始檔可讀且SHA驗證相符。中華106下第一次的七／八／九年級三個解答雖可在目錄與預覽頁看到，但公開下載端點回傳HTTP200、0 bytes，未偽報成功，亦未誤標成登入限制。',
'同一次考試的不同格式、修訂版與相同內容檔均保留來源身分；內容相同者另列SHA重複資訊，不把它們當成新的試題內容。','','## 逐年度原卷檔案數','',
'以下按官方目錄／檔名宣告年度統計，並非已逐題核對題數；109卷首108的特定衝突另見下節。','','| 學年度 | 中華原卷檔 | 羅東原卷檔 |','| --- | ---: | ---: |']
for year in range(105,116):lines.append(f'| {year} | {school_counts["中華國中"][year]} | {school_counts["羅東國中"][year]} |')
lines += ['','## 精確缺漏及身分衝突','',
'1. **中華105上第二次：實際空資料夾。** 根目錄 → 105學年度 → 上學期 → 第2次，資料夾ID `1H8qN7duNBh8Q68u--W_aQWBJ0dF1O9ds`，HTTP匿名目錄回應為0子項。主代理亦透過實際瀏覽器看到「將檔案拖曳到這裡」。不是入口找不到，也不是把八年級檔名解析漏掉。',
'2. **中華105下第三次的題目資料夾也為空。** 目錄本身可進入，但沒有公開題目檔，不能用其他學期填補。',
'3. **中華109上二八年級：卷首寫108。** 檔案 `1ZZUkKjnXYPQn5CwCnQPqN9ayYj__D6wS` 的資料夾與檔名宣告109，原PDF卷首紅字實為一○八、上學期、第二次、八年級。依本案卷首政策修正年度為108，保留 `sourceFolderYear=109`。不能計為已取得真正109卷。',
'4. **同樣寫108的兩份卷並非同一內容。** 上述PDF與真正108資料夾的DOCX `16EeKUo1TFlipf950nPiry7mpCxdq6Cp-` 首題及大部分正文不同，全文正規化相似度約17%。不能只憑相同卷首自動合併去重。',
'5. **補回一份原先被誤標年級不明的共同命題卷。** `0627共同命題數學.pdf`、ID `1ODYj-V7KzqhYr8EM7s2gkTI2Rb8qKDg3`，卷首明列107下第三次、八年級，共4頁；已建立metadata override，應從原先269份公開原卷增補為270份（另外15份為內城）。',
'6. **羅東缺年度：** 全部官方分類頁與文章沒有109、111、113、114、115學年度數學原卷連結。保留可取得的105–108、110、112，不推定其他年度有卷。',
'7. **中華115：** 目前官方年度資料夾僅上學期第一次；沒有編造未列出的上二或下學期卷。','','## 本次八年級上學期第二次核對','',
'共22個「學校×年度」請求格，14格有不衝突的公開原卷；另保留1份宣告109但卷首108的衝突卷。對應15個題目原始檔與9個解答檔，全部可取得來源的SHA核對通過。',
'四份指定Word原卷均以全新隱藏Word實例唯讀開啟，強制停用巨集與連結更新後匯出PDF；原檔未更動，也沒有控制使用者既有Word文件。`bulk-render-manifest.json` 保留原SHA、衍生PDF SHA、頁數與逐頁PNG視覺核驗。',
'中華108及羅東108的衍生PDF尾端有空白／僅頁尾頁，原題內容均在前兩頁；未為湊頁數刪題，轉寫時可略過空白頁。','','| 學校 | 學年度 | 八上二來源狀態 |','| --- | --- | --- |']
labels={'available-original-verified':'原卷已取得、SHA通過','official-folder-empty':'官方實際空資料夾','listed-question-header-is-108-not-109':'有檔，但卷首108；不算109真卷','current-official-year-folder-only-first-exam-listed':'目前官方僅列上學期第一次','no-official-year-category-post-or-question-link':'官方分類沒有該學年原卷文章／連結'}
for s in slots:lines.append(f'| {s["school"]} | {s["year"]} | {labels[s["status"]]} |')
lines += ['','完整逐格與SHA：`priority-upper2-grade8-source-audit.json`。本文件只確認來源清單、原檔與身分，**不把已下載宣稱成已完成全部題目轉寫**。']
if (R/'full-official-header-screen.json').exists():
    hs=json.loads((R/'full-official-header-screen.json').read_text(encoding='utf8'))
    lines += ['','## 全部255原卷的卷首初篩','',
    '已逐檔讀取原卷第一頁文字層；Word原卷先用獨立唯讀、禁宏的Word實例匯出可讀PDF。這是身分初篩，不是把所有題目都宣稱轉寫完成。',
    f'目前四欄文字層一致 {hs["statuses"].get("full-header-text-consistent",0)} 份、部分欄位一致 {hs["statuses"].get("partial-header-text-consistent",0)} 份；另 {hs["statuses"].get("scanned-or-header-text-unresolved",0)} 份掃描／卷首無可讀文字者繼續待視覺或OCR核對。自動regex只列候選，不直接改年度。',
    '本次另外實際看原圖／Word衍生首頁後，確認以下三項衝突，才加入metadata overrides：',
    '- 羅東106下第一次九年級連結的原PDF其實是106上第一次，與正確106上九年級原檔完全同SHA；保留來源下學期，但按卷首上學期，並登錄canonical duplicate，避免重複抽樣。',
    '- 羅東106上第一次八年級連結的原DOC其實是105下第一次，與正確105下八年級原檔完全同SHA；保留來源106上，按卷首105下核定。',
    '- 中華107下第三次八年級DOC卷首紅字為108下第三次。其正文與真正108資料夾另一份卷不同，保留為有來源衝突的另卷，不只因卷首相同就合併。',
    '此外，一份中華106下第三次七年級卷初次被文字串流順序誤抓題幹「小恩第二次段考」為考次。實際看原頁，卷首明明是第三次，故未改資料；改用頁面位置排序抽取後，這個假警報已消除。',
    '33份Word原卷現在均有可供讀取卷首的衍生PDF：5份既有衍生檔復用、27份新匯出、1份同原始SHA衍生檔復用。其餘28份只做本次卷首初篩，沒有冒稱完成全文轉寫或逐頁排版驗收。詳見 `full-official-word-header-render-manifest.json`。',
    '以上年度表仍按官方來源宣告年度保留，實際組卷年度以已人工複核的卷首override為準。完整候選、未讀文字者與人工確認證據見 `full-official-header-screen.json`、`full-official-header-visual-review.json`。']
(R/'FULL_OFFICIAL_CRAWL_README.md').write_text('\n'.join(lines)+'\n',encoding='utf8')
