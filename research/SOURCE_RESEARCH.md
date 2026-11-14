# 羅東／內城公開數學段考查核

查核日期：2026-11-14（Asia/Taipei）。本次針對 108–115 學年度，實際可取得範圍如下；**不是全縣、全年度收齊**。

## 羅東國中

- 官方首頁 https://www.ltjh.ilc.edu.tw/ 仍直接連結「歷屆試題」至 https://2blog.ilc.edu.tw/16771/category/c-12565/ 。
- 按分類分頁實際列舉全部 108 學年度以後的數學下載連結，共 36 份：31 PDF、4 DOC、1 DOCX。全部已下載成功並記錄 SHA256。
- 已公開列出的學年度是 108、110、112；未找到 109、111、113、114、115 學年度公開卷，不能把查無當成未舉辦。
- 年級／學期／段次按發布頁標題及每一段「七／八／九年級」標頭擷取。110 下第二段頁面僅九年級有數學連結，沒有替七八年級補造資料。
- PDF 其中 30 份為掃描影像，沒有可用文字層；112 上二段七年級可抽字。下載成功不代表題目已完成逐題校對。
- 原始清單：`luodong-papers.json`；爬過頁面：`luodong-pages.json`；重跑：`python research/collect_luodong_neicheng.py`。

## 內城國民中小學

- 官方首頁 https://www.ryjh.ilc.edu.tw/ 直接連結「歷屆段考試題」至 https://drive.google.com/drive/folders/1k1_c5hebr8RsSehpDlyWQCRSD92Vz3RU?usp=sharing 。
- 公開資料夾只有 109 上、110 上。遞迴列舉 150 個資料夾／檔案項目，其中數學 PDF 15 份，全部成功下載。
- 109 上 7 份；110 上 8 份。110 八年級另有 3 份「抽班」試卷，以 `track=pullout` 標示，不應預設與普通班混合。
- 109 上二段七年級：資料夾與檔名為二段，PDF 頁首卻寫「第一次段考」，範圍為1-4至2-2。保留 `exam=2` 並註記原卷標頭衝突。
- 全 15 PDF 可抽取文字，但公式、向量圖與內嵌方程式不保證能按文字順序重建，組卷應保留視覺原件並核對。
- 原始清單：`neicheng-papers.json`；Drive 遞迴清單：`neicheng-drive.json`；重跑下載：`python research/download_neicheng.py`。

## 課綱與檔案身分

- 108 課綱從 108 學年度七年級逐年實施，初步按 `year - (grade - 7) >= 108` 標示 cohort；108 學年度八九年級及109學年度九年級不應宣稱是108課綱試卷。
- 來源是校方公開頁／校方直接連出的 Drive，公開可讀不等於已聲明重新散布授權；來源頁未明列授權時留 `rightsStatus=not-stated`，不要補寫開放授權。
- 原始卷在 `raw/`，並保留來源 URL、下載狀態、檔案大小、SHA256；原件不覆寫。
- `pdf-text-audit.json` 只記錄頁數、文字層是否可用及答案字樣，不代表解答已校對。「答案卷」很多是空白作答卷，不能當成標準答案。

## 已逐題檢視的可組卷範圍

`curated-neicheng.json` 共 73 題，來源為內城110上八年級普通班三次段考，含52填充、18選擇、3非選。來源頁與精確裁切框逐題渲染檢視後才標 `reviewed=true`；結果見 `curated-neicheng-review.json` 與 `curated-review/sheet-*.png`。三段選擇第11題選項跨頁，暫時排除。難度是編輯判斷，非校方官方難度或答對率。
