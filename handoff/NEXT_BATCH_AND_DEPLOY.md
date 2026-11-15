# 下一批與部署接續（快速流程）

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
