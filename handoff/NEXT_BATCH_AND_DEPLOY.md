# 下一批與部署接續（快速流程）

## 最新接手（2026-11-16，Codex）

- 使用者指定先全部宜蘭八上、八下、九上、九下、七年級，再都會區相同順序；已修正 `research/make_waves.py` 對每一個原卷排隊，不再把同年、年級、考次只留一校一卷。詳讀 `AGENTS.md` 與 `skills/exam-bank-coordinator/SKILL.md` 最新說明。
- v25 已推 GitHub，commit `ba9011d`；本機建置 1,528 份原卷、6,946 可組卷題，77 項程式測試通過。GitHub Actions 與正式站是否完成須自行核對，勿將建置成功誤稱部署成功。上一批 v24 已部署。
- 宜蘭八上接續：中華 108上三 `1nMb5wIa9Ssd0PURUjncoC_25bZawOPud`、羅東 107上一 `ld-107-1-1-8` 完成待納入；內城 `nc-110-1-2-8-pullout`、`nc-110-1-3-8-pullout` 已完成稿但為抽班卷，暫存且未混入普通班。後者一題刻度矛盾已停用。其餘新稿以磁碟與 CLAIMS、實際代理狀態為準。
- 目前代理正在處理中華 107上三 `1ZbUCjCzbxUrS_P4G2d71I6cvV8rzd0Ma`、110上一 `1C8OHjkXiEXjJwe0tFeSHI_eIDbPVySAS`、109上一 `1ZASDtBiRnEoXShkcBvn-r9gbCo6txlYo`，羅東 106上三 `ld-106-1-3-8`；交接前先確認代理已停止，避免重複認領。Word/DOCX 等未能讀取者保留原卷、記缺口，不算完成。
- 下一批以 `python -X utf8 scripts/release_queue.py <完成ID...>` 鎖定，`python -X utf8 scripts/merge_batch.py` 建置，版本從 v25 增加、只加入核准 JSON 與必要 public 檔，再按下方 Git 指令推送。不要用全量 `git add` 收進其他 AI 的草稿。

共用位置：`C:\Users\user\桌面\國中家教\yilan-math-bank`；GitHub `Lee200202/yilan-math-bank`的main。接手先讀AI_HANDOFF.md、REVIEW_POLICY.md、OWNER與CLAIMS，保留未提交工作。

## 現在先做什麼

1. 沿用其他AI完整文字稿，只比對圖形；不再重做全文／逐頁PDF驗收。
2. 收齊正在修圖的完整卷，短暫freeze後更新發行清單；發布後立即讓助手續作。
3. 內城110上八第二次已完成29題填充文字、30填空與6幅SVG，已納入v16。
4. 興福106下七f2d...已依原卷卷首修正為第一次；自強a830...修正為八上第二次。來源SHA、卷首截圖與slot-overrides均保留。
5. 最新完整尚未全卷完成清單由`python scripts/handoff.py --write`及`python scripts/handoff_exchange.py inventory`產生；另看CLAIMS及本批source-extra報告，避免重複派工。

## 如何發布到GitHub／網站

在儲存庫根目錄依序執行（協調者操作，助手不推送）：

```powershell
git status --short
git fetch origin
python -X utf8 scripts/release_queue.py paperId1 paperId2
python -X utf8 scripts/merge_batch.py
```

release_queue只接納完整結構、來源與槽位正確的卷，記錄發行SHA；未完成／衝突卷保留，不假稱成功。release-transcripts是發行清單，其他助手在磁碟上的半成品不會意外加入建置。

更新public/index.html、app.mjs、units-ui.mjs、workbench.css及qa-requested-papers版本字串，下一次用v17、v18依序遞增；不要改完資料仍沿用快取版本。確認新增原卷已由prepare_data複製到public/papers。

```powershell
git add -- public scripts research/release-transcripts.json research/metro/slot-overrides.json handoff README.md VERIFICATION.md
# 再逐一加入這次核准的research/metro/transcribed或research/yilan/transcribed完整卷檔；不要git add整個未完成資料夾。
git diff --cached --check
git diff --cached --stat
git commit -m "Add completed math transcriptions and corrected vector figures"
git push origin HEAD:main HEAD:codex/initial-site
gh run list --repo Lee200202/yilan-math-bank --limit 1
```

GitHub Actions的pages.yml會執行測試與靜態build，成功後更新 <https://lee200202.github.io/yilan-math-bank/>。至少確認版本／可用題數與已加入卷的「查看全卷文字題」按鈕確實出現；依使用者最新要求，不再做冗長全文／全部PDF視覺驗收。

## 交接前更新

寫下最後commit與部署版本、剛新增卷ID與題數、圖形已修／待修、來源衝突、下一批認領及部署結果。不要把仍在原卷狀態的學校說成已有全卷文字，也不要把文字直接沿用說成逐字校對完成。

## v16 本批狀態

目前發布批次 v16：1,528 份原卷、3,866 題可組卷；新增 53 份全卷文字（較v15增加 1,249 題）。全卷狀態 128 份；部分轉寫 37 份、尚未轉寫 1,363 份。依使用者要求直接沿用其他AI文字，圖形比對持續修正；這批不宣稱全文或全部PDF逐頁複核。部署完成與否另見本批release-summary.json。

圖形尚待比對：1Kqjgn-K3nvvgGfntroSOtnScJ0rhsOuf, 1nxHnyR47GQM4EgbVPJ3iBvZPFEqKCPxH, ld-110-2-1-7, ld-112-1-1-7, metro-taipei-f2d726b55ed00db9, nc-110-1-1-9, nc-110-1-3-9。完成即可單獨修正發布，不阻擋現有完整文字稿。

## v17 本批狀態（Claude 接手協調，2026-11-16）

- 正式站 v17：1,528 份原卷、4,760 題可組卷；全卷 163 份（complete 146＋含來源疑義 17），部分 37、未轉寫 1,328。已用 `scripts/live_acceptance.py` 在正式站實測：版本、題數、地區分頁、原卷篩選、整卷預覽、單題替換、PDF 匯出再匯入、各年級隨機組卷、手機版無橫向溢出（見 handoff/batches/20261116-v17/live-acceptance.json）。唯一待修：部分 SVG 根元素帶 height="auto"，瀏覽器主控台報錯但不影響顯示；`inline_svg_css.py` 已能一併清除，下一批建置會帶入。
- 協調流程（協調者操作）：`python scripts/release_queue.py <ids>` → `python scripts/inline_svg_css.py --write <檔>`（SVG 含 CSS／class 會印成黑塊，check_transcript 會擋）→ `python scripts/merge_batch.py` → `python scripts/qa_metro.py --ids-file <本批> --report-file <報告>`（圖形超出畫框時用 `scripts/fix_svg_viewbox.py <paperId>`）→ 逐頁抽查含圖頁 → 提交推送 → `python scripts/live_acceptance.py <站址> <報告> <paperId…>`。
- 下一批派工：`python research/make_waves.py <wave> <helpers> <每人篇數> [region…]`，每個「地區×學年×年級×學期×次別」尚無全卷的缺口挑一份最佳 PDF，寫入 research/targets/<wave>-<k>.json 並在 CLAIMS 認領。w1 六組各 4 卷已派工；缺口共 618 個，其中 164 個只有 Word/ODT 原卷（高雄 84、桃園 41、新北 21、臺北 13、宜蘭 5）。
- Word 轉 PDF（scripts/render_office_source.ps1）在本機 2026-11-16 實測 120 秒無回應（隱藏對話框），已清掉遺留的隱藏 Word 程序；Word/ODT 缺口需使用者先確認 Word 可無人值守開啟，或改用其他轉檔方式。

## v20–v22（Claude，2026-11-16）

- v20：6,277 題、全卷 231 份（wave 2 尾卷＋wave 3）。v21–v22：組卷修正——①同題小題家族／同內容不並抽（`familyKeys`、內容去重、去重換題）；②難度比例分到每個題型（`typeLevelPlan`）。正式站實測：UI 連按「生成」40 次，各題型都是簡單50／中等50（選擇 5/5、填充 3/3、非選 2/2），重複題 0；`scripts/live_acceptance.py` 全過（handoff/batches/20261116-v22/live-acceptance.json）。
- 下一批：`python research/make_waves.py w4 6 4`，helpers 讀 `research/HELPER_PROMPT.md`；其餘流程見上方 v17 段。原卷疑義報告在各 batch 目錄的 SOURCE_ISSUES_REPORT.md。
