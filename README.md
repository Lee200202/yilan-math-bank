# 蘭卷｜宜蘭國中數學題庫

依年度、上下學期、年級、學校與段考次別抽題，製作可換題、改分及再次匯入的練習卷。支援桌機、手機及 A4 PDF。

## 列印版

標題預設為「八年級上學期第一次段考練習」等實際範圍。其下只有題型標題、題目、配分與選項，沒有班級、姓名、座號、來源註記、宣傳頁尾或額外作答空白。本文統一 11.5 pt；題幹重新轉寫為原生 PDF 文字，分數、根號與次方統一重排，必要題圖以純向量重繪。沒有原卷裁圖或點陣圖片。短選項排為二／四欄，題幹與圖表盡量同頁。

每題可改分，亦可按目標總分重新整數配分。指定換題只替換同範圍、同題型、同難度且未使用的題目，其餘題目與配分不變。題型不足會停止並提示；難度不足會明示補足情形。

PDF 的隱藏 Subject 保存 `LANJUAN1:` 組卷紀錄，匯入同一份本站 PDF 可繼續修改；另可備份 JSON。外部軟體若轉存並移除中繼資料，請用 JSON 還原。本機自動儲存不需登入或學生個資。

## 官方原卷範圍

查核日期：2026-11-14。依使用者指定，自 105 學年度起收集三校公開試卷，找不到則記錄後略過。

| 學校 | 找到的年度 | 官方來源 |
| --- | --- | --- |
| 中華國中 | 105–115；115 目前僅上學期第一次 | [校方所連 Drive](https://drive.google.com/drive/folders/0B-2YnWjsnzalMm84ck9yRUtPTG8?resourcekey=0-Cc-rWuKRrhfzoTnh3M_BpA) |
| 羅東國中 | 105、106、107、108、110、112 | [校方歷屆試題](https://2blog.ilc.edu.tw/16771/category/c-12565/) |
| 內城國民中小學 | 109、110 部分上學期 | [官網所連 Drive](https://drive.google.com/drive/folders/1k1_c5hebr8RsSehpDlyWQCRSD92Vz3RU) |

已下載 **269 份原卷檔案**，含同一考試的不同格式、修訂版及抽班卷。只有完成文字核對的普通班題目可組卷。未轉寫的原卷仍可查閱，不當成已完成的文字題。最新題數及逐年進度在 `public/data/coverage.json`。

原卷、解答、空白答案卷分開辨識。已知矛盾、缺字題保留研究紀錄並排除組卷，不自行補造。羅東缺漏年度查核分類五頁、公開文章／附件索引及關鍵字；內城105–108未找到合格公開卷。證據在 `research/luodong-source-audit.json`、`luodong-api-audit.json`、`neicheng-pre108-search.json`。全縣29校／國中部入口盤點亦保留，未找到入口不代表沒有公開卷。

108課綱按入學年實施：七年級108、八年級109、九年級110起。可勾「僅使用108課綱」排除較早梯次。難度為教學估計，非學校答對率。

## 執行與發布

需要 Node.js 22以上；執行、測試及建置不必安裝套件。

```text
npm run dev
npm test
npm run build
```

開啟 `http://127.0.0.1:4173`。`dist/` 可部署至 GitHub Pages。推送至 `main` 會由 `.github/workflows/pages.yml` 測試、建置及發布，儲存庫 Pages 建置來源須設定為 GitHub Actions。

字型、MathJax與PDF引擎隨專案提供，不依賴外部CDN或後端API。PDF本文為原生文字，公式及圖形為向量。完整嵌入 Noto Sans TC 避免中文字型子集缺字，PDF約4.3MB起，主要為字型大小。

## 新增題目

1. 從官方來源下載，登錄學校、年度、學期、年級、次別、網址及SHA256。原檔不改；Word轉檔或掃描旋轉另存衍生PDF及雜湊。
2. `research/curated-*.json` 登錄題目ID、頁序、座標、全部子題邊界，實際檢視後標記 `reviewed:true`。
3. `research/transcribed-*.json` 逐題轉寫，使用 `text/options/table/svg` 區塊，公式以 `$LaTeX$` 表達。完整保留已知量、選項、共同題幹及必要圖表，移除原題號、配分、獨立答案及來源頁尾。
4. 核對數字、根號範圍、分子分母、上下標及題圖才標 `verified:true`。原題瑕疵標 `usable:false`、`sourceIssue`。
5. 安裝Python `pymupdf` 後執行 `npm run prepare:data`，再測試、建置、視覺驗收。來源雜湊、唯一ID及文字核對狀態均須通過。

## 驗收

`npm test` 驗證篩選、舊課綱開關、題型／難度／不重複抽題、整數配分、單題替換、匯入及公式曲線。

安裝Playwright與Chrome後，`npm run qa` 實際組卷、換題、改分、下載PDF及重新匯入，確認題目與配分完全還原，並檢查手機寬度、來源篩選與29校表。

`node scripts/qa-typeset.mjs` 將全部可組題分批輸出PDF，檢查溢出及無裁圖預覽。`python scripts/verify_typeset_pdfs.py` 檢查全頁零點陣圖、題數、統一字級及多餘欄位，並渲染全部頁面供實際視覺核驗。驗收產物在忽略的 `qa/`。

程式碼採MIT。原卷權利屬原作者及學校；套件、字型授權見 `public/THIRD-PARTY.md`。
