# 貼給其他聊天室 AI 的完整提示詞

請協助蘭卷數學題庫「全卷轉寫」。我會附工作包ZIP或其中一個paperId資料夾。你只處理分派給你的paperId，不更動網站、不提交Git、不發布。目標是讓Codex／Claude直接讀你回傳的MD整合，無須重新下載原卷。

1. 先讀工作包的TARGET.md、manifest.json、nanyi-units.json與TRANSCRIBE_GUIDE.md。原始考卷在original/，每一頁PNG在pages/；text-layer.txt僅供查找，公式常有亂碼，不能把文字擷取當校對。
2. 逐頁實際查看原卷及PNG，先核對校名、卷首學年、學期、年級、考次。與declaredSlot不符就回報衝突及頁碼，不能由題目主題猜學期或改成另一卷。
3. 完整轉寫全卷：所有題幹、共同條件、子題、選項、所有填答格與必要表圖。答案欄和解答不混入題幹；一頁兼有題目和答案格時，仍須保留該頁題目。不能只做幾題範例。
4. 題目是原生繁體中文與LaTeX公式，不能放原卷截圖、base64圖片、PNG/JPG、SVG內嵌image或把整段題文畫成路徑。必要幾何圖、統計圖、作圖步驟及圖形選項忠實SVG重繪，保留點名、角度、虛線、陰影、尺寸。SVG可以放在MD的JSON字串中，不需另外上傳圖片。
5. 按內容標easy／medium／hard（簡單／中等／困難），並寫difficultyBasis；選南一單元primaryUnitId、unitIds與unitAssignmentBasis，不能按考次猜標籤。完整單元在nanyi-units.json。
6. 填充題保留所有空格「＿＿＿＿」，多格仍屬同一題時不任意拆散。原卷題號重複時以原大題前綴區分sourceNumber，例如「基礎7」「填充7」。選擇題文字選項不含(A)等前綴；純圖選項用optionFigures SVG，內含全部選項圖與一次(A)–(D)，不能只回傳四個標籤。
7. 分類type為choice／fill／written；是非題用fill並寫清填○或×。完整題組保留必要共同條件，獨立題須可單獨抽出。sourceNumber與page必須能反查原卷。
8. 原卷本身缺條件、多解或圖文矛盾，保留全文，usable:false並具體寫sourceIssue。若只是你未能看清、未完成圖形或用量不足，寫deliveryStatus:partial，列出未完成題號；不能假裝是原稿錯誤或全卷完成。
9. 完成後再次把每一頁原卷與所有轉寫題對照：數字、正負號、分母根號、選項順序、圖形條件、題數及子題均核對。visualReviewComplete只有在原卷全文確實重看完成後才可設true；這不代表Codex已完成PDF輸出驗收。

## 請回傳的檔案

每一份原卷交付一個 `<paperId>.md`，使用工作包RETURN_TEMPLATE.md的格式。檔名保留paperId，不合併不同原卷、不把相同題號誤當同題。多份MD可以放同一ZIP回傳。

MD應含：卷首原文、逐題可讀全文、每題難度／單元／來源頁、原卷大題與題數盤點、來源SHA256、圖形核對與疑義、尚未完成項目；以及**恰好一個完整的 `json` fenced block**，內容為TRANSCRIBE_GUIDE的whole-paper schema。此JSON是匯入依據，MD可讀題文必須與它一致。不可使用省略號、TODO或「其餘同原卷」代替題目。

JSON必須是標準JSON：LaTeX反斜線需跳脫成雙反斜線；SVG字串的引號正確跳脫。sourceSha256只能用manifest提供、且與原始檔核對的值。若執行環境可用，請檢查JSON與SVG解析；若沒有工具，就如實寫未跑檢查，不假造測試結果。

完成MD請作為可下載附件回傳；若不能產檔，直接完整貼出MD正文，使用外層四個反引號包住，避免裡面的JSON fenced block被截斷。不要只給雲端暫存連結，也不要只回覆「完成」。

## 你不需要做的事

不要自行配分、添加姓名班級、重新設計網站或產生正式考卷PDF。Codex／Claude協調者會做整合、輸出排版、每頁目視、換題／配分／PDF還原與正式站驗收。你的MD是待審資料，不會直接自動發布。
