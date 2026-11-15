# Codex／Claude 接力

以使用者既有GitHub儲存庫作可同步的共用資料夾。沒有Claude連接器時不能宣稱已建立即時AI通訊。若專案有AI_HANDOFF.md，先讀入口，fetch並比較HEAD及未提交工作，記錄單一協調者，助手只處理認領paperId的個別檔案。不得重設、強推、整批覆寫或把別人的未驗收檔順帶發布。

交接至少有：版本與commit、資料實際題數、原卷／部分／全卷／來源疑義狀態、完整待辦而不只PDF捷徑、認領檔、來源SHA、下一批目標、執行命令與結果、PDF每頁目視與hash、正式站實測證據。停止或換平台時更新快照，另一邊重新計算而不照搬聊天數字。

原卷與字型可能被.gitignore排除，須附官方下載與同SHA復原方法。PDF示例、targets清單與幾份成功卷都不能當作全量。遇來源卷首衝突記證據，停用衝突目標並接續其他卷，不從章節猜學期。

機器驗收題數、題號、無raster、單字型、公式錯誤、SVG邊界、嵌入字型輪廓可解碼、PDF還原ID/順序/分數；人或AI逐頁實看所有輸出頁才能補足圖形條件、遮字、缺字與不必要留白。記錄所看頁面雜湊，修改相關資料後重驗，不准只抽兩頁而稱整批通過。

分派外部聊天室時，附每卷原檔、所有頁PNG、SHA manifest、單元表、AI提示詞與MD範本，讓對方直接用已備媒體。回傳MD須有全卷可讀題文與唯一JSON區塊、SVG內嵌，不把普通圖片當正式題目。先驗證並存incoming待審，再由協調者原卷／圖形／PDF驗收；草稿與部分交付不能標完成。雲端聊天室不能直接讀本機路徑或localhost API，應提供GitHub共用檔或ZIP／MD附件。蘭卷現有入口：handoff/START_HERE_FOR_ANY_AI.md、OTHER_CHAT_README.md；工具scripts/handoff_exchange.py的inventory／pack／intake／serve，不自動發布。
