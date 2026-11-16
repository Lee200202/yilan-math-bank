---
name: exam-bank-coordinator
description: Run the 蘭卷 junior-high math exam bank end to end — dispatch helpers to transcribe original exam PDFs into whole-paper text questions, check and build them, publish to GitHub Pages and verify the live site. Read this first when you take over the project from another AI or session.
---

# 蘭卷題庫：接手與協調流程

## 0. 一分鐘版

- 網站：<https://lee200202.github.io/yilan-math-bank/>（推到 `main` 就由 GitHub Actions `pages.yml` 自動部署，約 40 秒）。
- 本機資料夾：`C:\Users\user\桌面\國中家教\yilan-math-bank`（Windows，Git Bash／PowerShell 皆可）。儲存庫 `Lee200202/yilan-math-bank`，**同時推 `main` 與 `codex/initial-site`**：`git push origin HEAD:main HEAD:codex/initial-site`。
- 目標：把各縣市（宜蘭＋臺北／新北／桃園／臺中／高雄）學校的「原卷 PDF」轉成可組卷的全卷文字題（文字＋LaTeX＋手繪向量圖），讓網站能依年級、學期、段考次別、單元、難度組新卷。
- **使用者指定的優先順序（2026-11-16）：八上 → 八下 → 九上 → 九下 → 最後七年級。** 程式已內建（`research/make_waves.py` 的 `PRIORITY`）。
- 先跑 `python -X utf8 scripts/handoff.py` 看最新數字（可組卷題數、各狀態卷數、各佇列），再讀 `handoff/NEXT_BATCH_AND_DEPLOY.md`、`handoff/REVIEW_POLICY.md`、`handoff/OWNER.json`、`handoff/CLAIMS.json`、`AGENTS.md`。**聊天紀錄裡的數字會過期，以這些檔案與 git 為準。**

## 1. 角色分工

- **協調者**（一次只有一位）：建置、發布、改共用程式、改 `research/release-transcripts.json`。接手時把 `handoff/OWNER.json` 改成自己，另一位 AI 停止改共用檔。
- **助手（helper／subagent）**：每位只寫自己認領的 `research/{metro|yilan}/transcribed/<paperId>.json`，不碰 git、不重建資料。簡報在 `research/HELPER_PROMPT.md`，規格在 `research/TRANSCRIBE_GUIDE.md`（JSON 格式、LaTeX、SVG、optionFigures、難度、南一單元）。
- 另一位 AI 可能同時在同一資料夾工作：派工前一定先在 `handoff/CLAIMS.json` 認領（`make_waves.py` 會自動做），不要重做別人已認領／已完成的卷。

## 2. 主迴圈（每一波 ≈ 24 份卷）

1. **挑卷並認領**：`python -X utf8 research/make_waves.py <wave> 6 4`（6 位助手、各 4 卷；產生 `research/targets/<wave>-<k>.json` 並寫入 CLAIMS）。每個「縣市×學年×年級×學期×次別」尚無全卷的缺口只挑一份最佳 PDF，依優先順序排序。
2. **派助手**（有 subagent 工具時，用較省的模型如 sonnet，`run_in_background`）：每位的提示只需一句——「你是 wave `<wave>` 第 `<k>` 位；先讀 `research/HELPER_PROMPT.md` 並照做；目標清單 `research/targets/<wave>-<k>.json`；草稿放 scratchpad 的 `<wave>-<k>\` 子資料夾；轉出頁面放 `research/targets/render/<wave>-<k>/`；略過清單 `research/targets/<wave>-<k>-skipped.json`」。沒有 subagent 工具就自己照簡報一卷一卷做。
3. **收件**：助手完成會回報（含不確定處與矛盾題）。把這些「原卷疑義」記進報告（見 §5）。
4. **一鍵檢查＋建置**：先開本機伺服器（`node scripts/server.mjs`，埠 4173；Claude 桌面版可用 `.claude/launch.json` 的 `yilan-math-bank`），再
   `python -X utf8 scripts/coordinate_wave.py <wave>`
   它會：內嵌 SVG 樣式 → 逐檔檢查 → `release_queue` 核准 → `merge_batch`（資料、字型、測試、靜態建置）→ 每卷 PDF 匯出檢查（`qa_metro.py`）→ 自動放寬被裁切的圖框。輸出在 `handoff/batches/<日期>-<wave>/`。
5. **目視抽查**：開 `qa/metro/<paperId>-p1.png`（挑圖多的幾卷）對照原卷頁面（`python -X utf8 research/metro/render_pages.py <pdf> <前綴> 1.4`）。依使用者政策（`REVIEW_POLICY.md`）**文字沿用、圖形優先**，不必全文重審。
6. **文件**：在 `handoff/batches/<批次>/SOURCE_ISSUES_REPORT.md` 寫停用題、原卷矛盾、待複核圖形（格式參考 `handoff/batches/20261116-v20/`）；`VERIFICATION.md` 加一小節；`CLAIMS.json` 把已發布卷標成 `published-text`（可用 `batch` 欄註記版本）。
7. **改版本字串並發布**：
   - `sed -i 's/20261116-metro-vNN/20261116-metro-vNN+1/g' public/app.mjs public/index.html public/units-ui.mjs public/workbench.css scripts/qa-requested-papers.mjs`（目前版本看 `grep -o "metro-v[0-9]*" public/index.html | head -1`）。
   - `python -X utf8 scripts/merge_batch.py`（再跑一次，確認 69+ 項測試通過）。
   - `python -X utf8 scripts/handoff.py --write`。
   - **只 `git add` 明確檔案**：`public scripts research/release-transcripts.json research/metro/slot-overrides.json handoff VERIFICATION.md tests`，再加本批核准的轉寫檔（清單可由 `release-transcripts.json` 對照 `git status` 取得，見 v20 的 commit-files.txt 做法）。**不要 `git add` 整個 transcribed 資料夾**（可能含別人的半成品），也不要加別人的一次性腳本（`scripts/build_*_xxxx.py`、`crop_*.py` 等，已在 `.gitignore`）。
   - `git commit`，然後 `git push origin HEAD:main HEAD:codex/initial-site`。
8. **正式站驗收**：等部署（`gh run list --repo Lee200202/yilan-math-bank --limit 1`，或輪詢首頁的 `metro-vNN`），再
   `python -X utf8 scripts/live_acceptance.py https://lee200202.github.io/yilan-math-bank handoff/batches/<批次>/live-acceptance.json <本批2–3個paperId>`
   （檢查版本、題數、地區分頁、原卷篩選、整卷預覽、單題替換、PDF 匯出再匯入、各年級隨機組卷、手機版溢出、主控台錯誤）。全過才算完成，並把報告 commit。
9. 回到步驟 1 開下一波。

## 3. 專案地圖

| 要找的 | 位置 |
|---|---|
| 網站原始碼 | `public/`（`index.html`、`app.mjs` 介面、`engine.mjs` 組卷、`typesetter.mjs` PDF 排版） |
| 發布資料（程式產生，勿手改） | `public/data/{questions,papers,coverage,paper-workflow,units}.json`、`public/papers/*.pdf` |
| 轉寫檔（真正的來源） | `research/metro/transcribed/`、`research/yilan/transcribed/`（一卷一檔） |
| 發行清單（哪些轉寫檔進網站） | `research/release-transcripts.json`（記每檔 SHA；檔案改了要重新 `release_queue.py`） |
| 學期次別更正 | `research/metro/slot-overrides.json`（卷首印字與資料夾不符時，附 SHA 與證據） |
| 原卷 | 宜蘭：`public/papers/<id>.pdf`；都會區：`research/metro/raw/<id>.pdf`（git 忽略；缺檔用 `python scripts/fetch_paper.py <paperId>`） |
| 清單 | `handoff/pending-papers.json`、`handoff/state.json`、`handoff/CLAIMS.json`、`handoff/source-issues/<paperId>.json`（不轉寫的卷，如答案卷） |
| 助手簡報／規格 | `research/HELPER_PROMPT.md`、`research/TRANSCRIBE_GUIDE.md`、`research/nanyi-units.json`（南一 60 單元） |
| 工具 | `research/make_waves.py`、`scripts/coordinate_wave.py`、`check_transcript.py`、`release_queue.py`、`merge_batch.py`、`qa_metro.py`、`fix_svg_viewbox.py`、`inline_svg_css.py`、`live_acceptance.py`、`sim_generate.mjs`、`sim_difficulty*.mjs` |
| 驗收紀錄 | `handoff/batches/<批次>/`（pdf-acceptance、live-acceptance、SOURCE_ISSUES_REPORT）、根目錄 `VERIFICATION.md` |
| 測試 | `npm test`（node --test，`tests/*.test.mjs`，目前 77 項）；建置 `node scripts/build.mjs` → `dist/` |

## 4. 已知的坑（都踩過）

- **Bash heredoc 會吞反斜線**：寫含 LaTeX 的 JSON／Python 用 Write 工具，或在 Python 內用 `json.dump`；不要 `cat <<EOF` 寫 `\times`、`\n`。
- `python -I` 會讓 `pymupdf` 找不到，一律用 `python -X utf8 …`（不加 `-I`）。
- 目標清單 JSON 可能帶 BOM（PowerShell 寫的），讀檔用 `utf-8-sig`。
- SVG 規則（`check_transcript.py` 會擋）：不可有 `<style>`／`class=`／`style=`（PDF 排版器只讀屬性，會印成黑塊；`scripts/inline_svg_css.py --write` 可自動修）、不可有重複屬性（非法 XML）、根元素不可 `height="auto"`、不可有 `<image>`／`<tspan>`／`<foreignObject>`。`<text>` 以固定楷體尺寸印出，上標下標用 Unicode。
- 公式太寬 PDF 會報「公式超過欄寬」→ 把 `$…$` 拆成幾段、避免塞滿公式的寬表格。
- 測試夾具若重複用同一句話當不同題目，會被「內容相同只算一題」去重；夾具文字要各不相同。
- 不要 `Stop-Process -Force WINWORD`（會被權限擋，也可能關掉使用者的文件）。
- Word 轉 PDF（`scripts/render_office_source.ps1`）在這台電腦會卡住無回應；只有 Word／ODT 原卷的缺口（約 164 個，多在高雄、桃園）要等使用者確認 Word 可無人值守開啟，或改用別的轉檔法。
- 助手共用同一個 scratchpad 父資料夾，會互相覆寫檔案；各用自己的 `<wave>-<k>\` 子資料夾。
- 同一個時段若唯一的檔是 1 頁答案卷（鷺江 113上七第三次、113上八第一次），在 `handoff/source-issues/` 登記，不轉寫、不要重複派工。
- 九年級三角比在 `nanyi-units.json` 沒有對應單元，暫歸 `nanyi-8-1-2-3`（畢氏定理）並在 reviewNote 註明。

## 5. 組卷程式（已修，勿退回）

- 同題的小題（`1-1`／`1-2`、`6(1)`／`6(3)`、同開頭 50 字）屬同一「家族」，組卷與換題只在範圍內沒有別的題可換時才併用（`familyKeys`、`diversify`）；內容（文字＋選項＋表格＋圖形）完全相同者只算一題。
- 難度比例要分到**每個題型**（選擇、填充、非選各自照比例），整卷題數配額仍優先（`typeLevelPlan`）。
- 改 `engine.mjs` 後必跑：`npm test`、`node scripts/sim_generate.mjs 2500`（重複題應為 0）、`node scripts/sim_difficulty.mjs`。

## 6. 預算與交棒（約 5 小時為一段）

- 剩約 1 小時時：不再派新一波；把已完成的卷走完 §2 步驟 4–8 發布；再更新 `handoff/NEXT_BATCH_AND_DEPLOY.md`（最後版本、題數、已發布與未驗收卷、進行中的認領、阻塞原因）、`python scripts/handoff.py --write`、提交推送。
- 助手中途被中斷時沒寫完的檔案不會有半成品（寫檔是一次完成）；CLAIMS 裡仍是 `in-progress` 的卷，確認助手已停止後把該認領刪掉或改回，再重新派。
- 不要把「下載了原卷」「檢查器通過」說成「逐字／逐頁驗收完成」。報告裡要寫清楚哪些做了、哪些沒做。

## 7. 還在等使用者決定的事

1. Word／ODT 原卷（約 164 個缺口）如何轉 PDF（見 §4）。
2. 兩個只有答案卷的時段需要找到真正的試題卷（鷺江）。
3. `metro-kaohsiung-af064db20548ddb6` 卷首印「民族國中」但收在美濃——學校歸屬是否更正。
4. 中正 113上八第三次 填充 10（圓餅與折線資料互相矛盾）要不要停用。
5. 使用者先前要求的「逐卷與原卷全面比對報告」只對 v17–v22 的卷做了抽查與疑義整理，完整逐題比對未做。
6. 九年級三角比單元是否要補進 `nanyi-units.json`。
