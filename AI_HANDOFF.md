> **最新入口：[skills/exam-bank-coordinator/SKILL.md](skills/exam-bank-coordinator/SKILL.md)** — 接手後先讀它（流程、指令、路徑、部署、坑、待決事項）。下方是較早的交接說明。

> 最新規則：先讀 [REVIEW_POLICY.md](handoff/REVIEW_POLICY.md)。完整AI文字直接沿用，圖形優先；不再等待全文或每頁PDF重審。

# Codex／Claude 共用交接入口

共用資料夾是本 Git 儲存庫，遠端為 <https://github.com/Lee200202/yilan-math-bank>。
這是可同步的檔案橋梁，並非兩個 AI 的即時通訊連線。雲端與本機必須先 fetch，再讀最新交接檔，不能只依先前聊天或本檔中的歷史數字接手。

同機實際路徑：`C:\Users\user\桌面\國中家教\yilan-math-bank`。可直接複製給其他AI的接手提示詞：[handoff/START_HERE_FOR_ANY_AI.md](handoff/START_HERE_FOR_ANY_AI.md)。外部聊天室的媒體工作包與MD回傳方式：[handoff/OTHER_CHAT_README.md](handoff/OTHER_CHAT_README.md)；全部待辦學校：[handoff/assignments/INDEX.md](handoff/assignments/INDEX.md)。

## 接手順序

1. `git status --short`、`git fetch origin`、`git log -5 --oneline`。若有未提交檔或分歧，先保留並核對；禁止 reset、強推或覆寫別人的半成品。
2. 執行 `python scripts/handoff.py`，讀 `handoff/STATUS.md`、`handoff/state.json`、`handoff/NEXT.md`。狀態是當時快照，命令會從目前資料重新計算。
3. 同時只由一位協調者編輯共用程式、重建資料及發布。接手者更新 `handoff/OWNER.json`；另一邊停止共用檔案修改。Git 中的 owner 是交接紀錄，不是分散式鎖。
4. 讀 `research/TRANSCRIBE_GUIDE.md`，從 `research/targets/<group>.json` 取尚未完成目標。助手只寫個別 paperId 的檔案；先在 `handoff/CLAIMS.json` 留認領，不與其他人處理同一卷。
5. 每卷逐頁確認原檔、卷首、所有題幹／子題／選項／必要圖形。文字與公式必須重排，圖形用忠實 SVG。按內容標難度與南一單元。**少量範例、下載原卷、檢查器通過均不等於全卷轉寫驗收完成。**
6. `python scripts/check_transcript.py <file>` → `python scripts/prepare_data.py` → `python scripts/subset_font.py` → `npm test` → `npm run build`。配合 `scripts/qa_metro.py --ids-file <清單>` 驗收新增／修改各卷，逐頁檢視輸出影像。檢查器無法判斷幾何條件是否畫對。
7. 記下程式／資料版本、每卷 PDF 結果及逐頁目視結果。只發布實際驗收完成的檔案；禁止把未驗收的同時到件檔順帶加入。明確 git add、commit、正常 push。
8. 正式站 <https://lee200202.github.io/yilan-math-bank/> 實測版本、可用題數、篩選、整卷預覽、單題替換、PDF 匯出及還原，再更新 `VERIFICATION.md`。
9. 停止前執行 `python scripts/handoff.py --write`，更新 NEXT／CLAIMS／OWNER，提交交接檔。未做 PDF 或目視驗收必須明列；不能用「完成」概括。

## 給另一邊的接手訊息

舊 `publish_batch.sh` 的廣泛自動暫存與推送已停用；不能把六份未做PDF檢查的同時到件卷一起上架。建置可用跨平台 `python scripts/merge_batch.py`；PDF驗收可用 `python scripts/qa_metro.py --ids-file <本批清單> --report-file <獨立報告>`，不要互相覆寫報告。整理逐頁檢視後，以 `python scripts/verify_release.py <本批acceptance.json>` 確認來源、build、PDF與所看頁面仍一致，再明確提交發布。QA的PDF／PNG屬忽略檔，交接保留報告與hash；換電腦時重製實際檔案，不假稱舊報告驗了新檔。

> 請同步 Lee200202/yilan-math-bank，先讀 AI_HANDOFF.md，執行 python scripts/handoff.py。保留未提交工作，依 handoff/NEXT.md 接續，更新認領後再開始。原卷不算已轉寫，未驗收不可發布；完成後更新交接快照與正式站驗收證據。

## 在另一台電腦／雲端取得原卷

Git 不包含忽略的 `research/metro/raw`、`research/fonts`。不可因本機路徑不存在便宣稱沒有原卷。
對清單中的 PDF 執行 `python scripts/fetch_paper.py PAPER_ID`，可從官方原檔／Drive／zip 指定成員補下載，寫到目標所需路徑，並驗證原有 SHA256；來源變更或權限頁會停止，禁止用新檔冒充舊校對證據。7z/rar 另依來源技能解壓，仍需驗 SHA。
字型完整原檔為官方 <https://data.cns11643.gov.tw/opendata/Fonts_Kai.zip> 中的 TW-Kai.ttf，放在 `research/fonts/TW-Kai.ttf`；授權與來源見 `public/fonts/`，不要複製 Windows 的標楷體字型。Python 需 `pymupdf fonttools brotli playwright`；本機瀏覽器測試使用 Chrome。

`handoff/pending-papers.json` 才是所有尚未全卷完成的清單；舊 targets 僅預排了一部分可直接處理的 PDF，不涵蓋所有 Word／其他格式。`state.json` 另列未排進 targets 的 ID 及各格式數量，後續仍須把這些原卷加入，不可把五份清單跑完當作全站完成。

`queues.remaining`是未認領且無來源衝突的PDF候選數；已預留給其他聊天室的六卷另見reservedOrClaimed與CLAIMS。這些卷仍算未完成，不能因預留而扣掉全站待辦。

## 原有需求（持續保留）

保留宜蘭中華／羅東／內城 105 學年度起公開原卷與 108 課綱開關；跨區來源依現有清單繼續。涵蓋七至九年級、上下學期、各考次，先補沒有可用整卷的範圍，再增加同範圍各校年度。不能為增加數量降低文字、選項或圖形完整度。

試卷使用統一楷體與原生文字，僅簡潔標題及題型章節；不顯示班級姓名、校名來源，不留大塊作答空白。非選擇題註「未寫計算過程不給分」。完整南一單元可選，比例與題數可調，庫存含 0 題需可見。選擇題同分，填充題由易至難，平均整數配分餘分優先難、中、易。舊 PDF 還原保留原 ID、順序及分數。
