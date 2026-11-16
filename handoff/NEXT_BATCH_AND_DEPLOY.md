# Next Batch and Deployment Record

## v48 交接（2026-11-16，Codex 接手）

使用者指示先收尾都會區已完成工作，再接續 Antigravity：宜蘭九上→九下→七年級，其後都會區。v48 本機建置納入發行清單中較 v47 新增的 127 份稿件，資料為 1,528 份原卷、11,684 題可組卷、全卷狀態 463 份、部分 11、待轉寫 1,054；77 項測試通過。推送與部署是否成功以 Git 與 Actions 實際狀態為準。

這批文字依使用者要求沿用其他 AI 已完成稿件，沒有進行全部全文或全部 PDF 逐頁重審。部分 Claude 交棒稿的圖形尚待後續集中對照：永和114上一／上二、向上110上二／上三、鷺江113上三（fda4…）、福和112上一；不要將建置成功說成這些圖已確認無誤。持續按原卷核對圖形，待釐清題不能猜測。

宜蘭九上正在處理 `1tQDE7sJrJX2xBbkfVok8vwdiOz-pipuF`、`ld-107-1-1-9`、`ld-106-1-3-9`；`ld-107-1-2-9` 已在這批核准清單。依 CLAIMS 檢查實際狀態，接續前確認代理是否仍在執行。下方 v40、v41 等均為歷史記錄。

## Milestone v40 (Current Deployment)
- **Scope**: Completed and approved 5 Yilan Grade 8 Semester 2 exam papers:
  1. `1b94poZdz6s5sgBAkXf--VMoKS2fpoyce`: 中華國中 107-2 E2 (31 usable questions, 16 pure-vector SVGs)
  2. `1ODYj-V7KzqhYr8EM7s2gkTI2Rb8qKDg3`: 中華國中 107-2 E3 (3 usable questions, 3 pure-vector SVGs)
  3. `1Oyz6Mhe7vxl1LjqAFdEtFWXeWuNk0Trn`: 中華國中 106-2 E1 (25 usable questions, 8 pure-vector SVGs)
  4. `192AO5odd7tQJrJpT4HAJVRWx5UQCA-vC`: 中華國中 106-2 E2 (26 usable questions, 17 pure-vector SVGs)
  5. `1nj1GNW5mcPe7cPhk8aaArk1cLOqmrjHO`: 中華國中 106-2 E3 (28 usable questions, 18 pure-vector SVGs)
- **Total usable questions**: Reached **7,683** (113 newly added in this milestone).
- **Test suite**: 77/77 tests passing.
- **Pure-vector standard**: 100% semantic `<line>`, `<polygon>`, `<path>`, `<circle>`, `<text>`. Zero raster images, zero base64, zero `<tspan>`.

## Milestone v41 (Immediate Next Batch)
- **Target**: Remaining 5 Yilan Grade 8 Semester 2 PDF papers:
  1. `1VyvQlXHgH65wE5NCKFyAUW29K0ENrofT`: 中華國中 105-2 E1 (二年級數學.pdf)
  2. `18klCcvdduoHtgoXIo17wK_btxr7U1nrS`: 中華國中 105-2 E2 (二年級數學.pdf)
  3. `ld-105-2-2-8`: 羅東國中 105-2 E2 (105學年度第二學期第二次段考)
  4. `ld-106-2-1-8`: 羅東國中 106-2 E1 (106學年度第二學期第一次段考)
  5. `ld-105-2-3-8`: 羅東國中 105-2 E3 (105學年度第二學期第三次段考)
- **Goal**: Clear all remaining Yilan 八下 PDF papers (pending PDF count $\rightarrow$ 0) and advance to Priority 1 next semester: Yilan 九上 (Grade 9 Semester 1).

## Claude 交棒筆記（2026-11-16，都會區轉寫）

- 分工見 `handoff/COORDINATION.md`：Antigravity＝宜蘭八下→九上→九下；Claude／Codex＝都會區八上→八下→九上→九下→七年級。**只寫轉寫檔，不碰共用建置檔；集中檢查後才發布。**
- 已寫好但**尚未核准／建置／發布**的都會區轉寫檔（在 `research/metro/transcribed/`）：wave 5（14 卷，清單 `handoff/batches/20261116-w5/targets.txt`）、wave 6（15 卷，`20261116-w6/targets.txt`）；wave 7（`20261116-w7/targets.txt`）、wave 8、wave 9（`20261116-w8/`、`20261116-w9/targets.txt`，八下）。發布時：`python -X utf8 scripts/release_queue.py $(cat <清單>)` → `python -X utf8 scripts/merge_batch.py` → `python -X utf8 scripts/qa_metro.py --ids-file <清單> --report-file <報告>`（需本機伺服器 `node scripts/server.mjs`）→ 抽查含圖頁 → 版本字串加一 → commit → push 兩個分支 → `scripts/live_acceptance.py`。也可一次用 `scripts/coordinate_wave.py w5 w6 w7`。
- 圖形待集中比對（助手沒能實際看到渲染結果）：wave 5 永和 114上一／114上二、wave 6 向上 110上二、鷺江 113上三（fda4…）、福和 112上一、向上 110上三。
- 已登記的答案卷（不轉寫）：`handoff/source-issues/` 內鷺江 113上七第三次、113上八第一次／第三次（2e34…）、114上八第一次／第三次，中正 112上八第三次。這些時段需要找到真正試題卷。
- 剩餘都會區 PDF 缺口：`python -X utf8 research/make_waves.py <新波名> 4 4` 會列出下一批（八上已接近完成，之後八下、九上、九下、七年級）。
