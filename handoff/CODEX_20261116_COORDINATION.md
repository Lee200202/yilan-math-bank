# Codex 協作訊息（2026-11-16）

使用者最新對齊：Antigravity 處理宜蘭八下、九上、九下；Claude 與 Codex 共同處理都會區，依八上、八下、九上、九下、最後七年級。Codex 代理僅寫各自認領的逐卷稿，不操作共用建置檔；同時發布由單一協調者執行。

Codex 此批認領：臺中大華114上八三 `metro-taichung-bb1ff929033d5f84`（已完成25題、格式檢查通過，圖形已比對；等待協調者核准）；新北新莊114上八二 `metro-new_taipei-a41eb729cd2bd83a`；桃園自強109上八一 `metro-taoyuan-b06156a26c8c7747`（後兩份進行中）。上述 ID 已寫入 CLAIMS；完成後依發布協調由單一人處理。

**可供協調者發行**：上述三卷均已完成並凍結，新莊 23/24（第6題條件疑義停用）、大華 25/25、自強 23/23。以目前檔案做 `python -X utf8 scripts/release_queue.py metro-taichung-bb1ff929033d5f84 metro-new_taipei-a41eb729cd2bd83a metro-taoyuan-b06156a26c8c7747`，再走建置與發布；尚未推送。下一批已認領臺中大華113上八三 `metro-taichung-8ffb22a69ae0874c`、新北福和113上八二 `metro-new_taipei-28b032a80273a72f-49d1c79a`、桃園自強109上八二 `metro-taoyuan-e829779527f94606`。

桃園自強 `metro-taoyuan-e829779527f94606` 已完成並凍結，22/22，亦可與前三卷一起納入。請發行協調者先確認目前 CLAIMS 與檔案 SHA，再核准；其餘兩卷仍在處理中。

新增可發布：臺中大華 `metro-taichung-8ffb22a69ae0874c` 25/25、新北福和 `metro-new_taipei-28b032a80273a72f-49d1c79a` 34/34，皆已由 Codex 再執行 checker；加上上列四份合計六份。以上六份仍須協調者核准與建置發布。新認領的臺中 `metro-taichung-f8f25ba3a7e8fabb`、桃園 `metro-taoyuan-2bb9a69db395f9d9` 在進行中。

桃園 `metro-taoyuan-2bb9a69db395f9d9` 亦已完成 25/25，checker 通過；累計七份待協調者發布。鷺江 `metro-new_taipei-74e31d9f211a21f6` 實為一頁答案卷，已登錄 source-issue、不當成試卷。

臺中大華 `metro-taichung-f8f25ba3a7e8fabb` 已完成 25/25，checker 通過，累計八份待集中發布。該卷非選第4題背景文章經轉寫者精簡，紀錄在其 reviewNote；請協調者保留此資訊。

新北新莊 `metro-new_taipei-b39aee3a53bde0be` 22/22 已完成並通過 checker，累計九份待發布；第13題原卷汙損已保留、不猜補，請保留原稿限制。各卷均有獨立 JSON、CLAIMS 狀態 text-ready，需協調者根據目前 SHA 核准。

桃園自強 `metro-taoyuan-576619c7f5a66954` 30/30 已完成，累計十份待集中發布。十份可用題數合計 254 題；其中新莊一題原題有歧義而停用，另新莊一題保留原卷污損。完成稿只是在共用資料夾，未宣稱已上站。

臺中大業 `metro-taichung-c54e88879c19ba0a-1f3c61ba` 21/21 已完成，累計十一份、275 題可用待集中發布。

桃園自強 `metro-taoyuan-00d7af668a7832fe` 25/25 已完成，累計十二份、300 題可用待集中發布。

中正 `metro-new_taipei-87b827bb0ab11204` 完成 28/28；原題 PDF 2 頁但頁尾標共3頁，代理另核對校方獨立答案 PDF `metro-new_taipei-497b4823d4481dca.pdf` 卷首為第3頁（SHA `1d2f06c1cbcf3288bf32ba907820fd9d1468c20259681927e02c802061ea1d88`），故題目兩頁完整。累計十三份、328 題可用待集中發布。

桃園自強 `metro-taoyuan-5e65a976e624a167` 26/26 已完成；累計十四份、354 題可用待集中發布。

臺中大華八下 `metro-taichung-33d2cfee46a4b4c1` 24/24 已完成；卷面非選說明誤印共5題、實際列1～4題，reviewNote 已記錄。累計十五份、378 題可用待集中發布。

新北中正 `metro-new_taipei-0601406e6e2d0bda` 25/25 完成，累計十六份、403 題可用待集中發布。

桃園自強 `metro-taoyuan-9a984a0914bdcfee` 36/36 完成，累計十七份、439 題可用待集中發布。

新北中正 `metro-new_taipei-b95574463fd45b8a` 25/25 完成，累計十八份、464 題可用待集中發布。

桃園自強 `metro-taoyuan-565e4b5610f5bbe5` 完成 24/25，第18填充題因原稿因式條件矛盾而停用；累計十九份、488 題可用待集中發布。

使用者最新指示 Codex 協助都會區八上，接續八下、九上、九下；Claude 的既有認領仍優先，Codex 只挑尚未認領 paperId，先寫 CLAIMS。首卷為 `metro-taichung-bb1ff929033d5f84`（大華114上八三），由 codex-metro_eight 處理。建置和發布仍由當前協調者執行，Codex 不覆蓋其他 AI 的成果。以下原「沒有另行認領」為較早狀態。

Codex 已讀取 OWNER.json 與 COORDINATION.md：Antigravity 負責宜蘭八下、九上、九下，Claude 負責八上及都會區後續。看到兩者均在執行，Codex 不改雙方轉寫、認領、建置產物或發行清單，也不推送，避免在共用工作目錄互相覆寫。Git HEAD 觀察到 fd25792，網站資料快照 8,124 題（v44），實際後續版本以 Git 與正式站為準。

本次 Codex 的三個 subagent 回報達使用額度上限並已停止；目前沒有另行認領試卷。兩位 AI 請繼續既有分工與單一建置發布順序，保留工作目錄中既有未追蹤稿件；不要將本訊息當作已完成轉寫。

可降低 token 的方式：先按 paperId 認領、以文字層或 Word 文字作草稿、僅檢視原卷題圖與辨識不清處；用獨立 JSON 分卷輸出，讓格式／SVG 檢查器集中跑，遇到缺圖或來源衝突標記停用及記錄，避免把機器檢查當成原卷正確性證明。批次固定後由一位協調者更新 SHA、建置、推送與確認部署。
