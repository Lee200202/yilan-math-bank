# 宜蘭專案定位

專案 yilan-math-bank，GitHub Lee200202/yilan-math-bank。先檢查當前目錄／remote，勿依本檔猜路徑或覆蓋其他專案。範圍仍依使用者當次指示；本次三校為中華、羅東、內城，105學年度起。

官方入口：

- 中華： https://drive.google.com/drive/u/1/folders/0B-2YnWjsnzalMm84ck9yRUtPTG8?resourcekey=0-Cc-rWuKRrhfzoTnh3M_BpA
- 羅東： https://2blog.ilc.edu.tw/16771/category/c-12565/ ，沿「較舊的文章」及各公告進年級數學附件。
- 內城：從既有來源ledger確認官方連結，不猜根目錄。

資料管線：research/full-official-crawl.py 是中華／羅東全目錄重查，使用前讀參數及下載行為。full-official-crawl-audit.json保留結果。paper-metadata-overrides.json必須有視覺核定、原SHA與原資料夾身分，不憑regex改年度。

curated-*.json為原題對照，transcribed-*.json為文字／向量內容，proof-bulk-*或completeness-bulk-*為全卷證明。新檔模式需接入scripts/prepare_data.py，避免寫了檔案卻未入站。

執行 python scripts/prepare_data.py → npm test → npm run build。驗收public/data/paper-workflow.json、official-source-audit.json及coverage.json，不能只看總題數。八上二曾只有29題，因此要驗跨三校所有公開年度該範圍，不用幾道新示例代替。

既有查核線索仍需後續重查：105中華上二官方資料夾為空；109資料夾某八上二原卷實印108；0627共同命題數學.pdf檔名未寫年級，卷首明列107下三八年級。不能一律說「搜尋不到」。
