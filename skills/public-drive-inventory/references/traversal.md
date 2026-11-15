# 路徑與下載驗收

典型樹為根目錄→學年度→上／下學期→考次→題目／答案。實際可能命名「第2次」「第二次段考」「107下3段素養導向題目」，依當次觀察解析，不能只匹配一種字串。

folder ledger：ID、parent ID、path、listedAt、listStatus、childFolders、files、paginationComplete、error。file ledger：ID、path、name、mime、kind、sourceUrl、downloadStatus、bytes、sha256、localPath、retryEvidence。

畫面載入中時先讀更新狀態，不能把暫時無項目當空目錄。UI確認入口／異常；大量清單可用當前connector或腳本。不要猜資料夾ID、跳過登入或擴大到私人檔案。

空回應記錄HTTP狀態、content-type、bytes；回原目錄點開確認可見性，另試官方下載入口。持續空檔標 empty-download-response，繼續獨立工作，不能存空PDF湊數。

交付區分發現檔案、下載原檔、驗證原檔、轉寫內容。宣告全量前比較 expected target IDs − archived target IDs，而非只看迴圈結束。
