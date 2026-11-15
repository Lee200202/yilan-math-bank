# 都會區（臺北／新北／桃園／臺中／高雄）來源與流程

查核 2026-11-15。外部AI指南給的網址先逐一重驗（`research/metro/probe_seeds.py` → `probe-seeds.json`）：石牌 Pastexam 空頁、新莊／三和列表為 JS 空殼、濱江無 REST 列表、弘道只有零散 PDF 無目錄，這些不採用。**一定要實際開官網、點進「歷屆試題／段考題庫」連結**，很多學校把卷放在 Google Drive 或整包 zip。

| 地區 | 學校 | 官方入口 | 結構 | 試題卷 |
| --- | --- | --- | --- | --- |
| 臺北 | 興福國中 | 教學組「段考題庫」頁 | 38 個 Drive 資料夾；104–105 為全科 rar/zip | 105–108 |
| 新北 | 中正國中 | RPage「段考考古題專區」403-1000-114(-n) | 列表→每次段考公告→附件（PDF） | 106–114 |
| 新北 | 溪崑國中 | RPage「歷屆試題-數學科」 | 每學期一篇，附件全為 docx/odt | 105–114 |
| 桃園 | 自強國中 | 首頁「歷屆段考試題」→Drive | 學年/學期/次別/年級/數學 多層資料夾，docx＋pdf 並存 | 106–114 |
| 臺中 | 向上國中 | 專題網頁「歷屆試題」→各學期 Drive | 每年級一個**全科 zip**，須解壓取數學 | 110–115 |
| 高雄 | 美濃國中 | 靜態 exam-section.htm | 新檔名 `115-1-1-8數學`；舊檔在路徑 `/exam/1122/1/二數學.doc` | 108–115 |
| 高雄 | 大灣國中 | view/index.php 分頁「下一頁」 | 依頁走到底 | 105–114 |
| 臺北 | 誠正國中 | NSS「段考歷屆試題」 | 項目是 JS 開關（href=`#`），須在瀏覽器點開才出現每年級**全科 zip**；只取「題目」zip | 113–115 |
| 新北 | 三和、鷺江、新莊 | RPage 列表→公告→附件 | 通用 `rpage_archive`；新莊每學年一個列表頁 | 112–115 |
| 新北 | 福和 | RPage 列表→公告 | 每年級一個 **7z**（本環境無 7z 解壓器、安裝套件被權限擋下）→ 只列入、不上架 | — |
| 新北 | 五峰 | RPage 列表→公告 | 每次段考一個全科 zip | — |
| 新北 | 永和 | 段考試題頁→Drive | Drive 資料夾 | — |
| 臺中 | 大華、大業 | 檔案下載頁／Google Sites → Drive | Drive 資料夾 | — |

JS 渲染頁先用 `research/metro/probe_rendered.py`（無頭瀏覽器）列連結，再決定爬法。

## 操作

1. `python research/metro/crawl_metro.py [來源鍵]`：全量列舉、下載、SHA256、zip 解壓（Big5 檔名以 cp437→cp950 還原）；`--reslot` 只重算年度／學期／次別／年級。原檔在 `research/metro/raw/`（忽略，不入庫）。
2. 檔名解析需涵蓋：`8G數學`、`七上`、`108年8年級`、`(8)`、`二年級`、`第2學期`、`114-1-1-8`；「作答卷」是答案卷不是試題。解析不出完整時段的檔案保留在清單、不上架，不猜。
3. 只轉寫**官方即為 PDF** 的卷；本機 Word COM 轉檔會卡住（隱藏對話框），Word 原卷只列原檔連結。
4. 轉寫檔 `research/metro/transcribed/<paperId>.json`：`printedHeader/printedSlot` 必須與卷首一致；每題 `blocks`、難度、南一主要單元；原稿矛盾題 `usable:false`＋`sourceIssue`。校方的單元代號、「會考題」、配分說明不屬題文。
5. **不要用 bash heredoc 寫含 `\\` 的 LaTeX**（會把 `\times` 變成 TAB＋imes）；用檔案寫入。`prepare_metro.py` 會拒收控制字元。
6. `npm run prepare:data`（含字型子集化）→ `npm test` → `python scripts/qa_metro.py <網址>`：逐卷 PDF 題數、零點陣、單一字型、各地區按鈕題數與手機寬度。PDF 引擎遇到超寬公式會報錯，把長式拆成多段 `$…$ $…$`。

## 目前進度

16 校、1,261 份都會區試題卷已列入「歷屆考卷」（連官方原檔）；14 份全卷轉寫（八上第一次、第二次為主），共 372 題可組卷。各校表格由 `python scripts/readme_metro.py` 依 coverage.json 重產到 README。其餘須逐卷轉寫，不能以這些代表全部。
