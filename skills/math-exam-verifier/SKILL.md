---
name: math-exam-verifier
description: 國中數學段考試卷「全卷文字化＋純向量幾何 SVG 重繪」專用驗收與複核技能。提供與原卷逐頁逐題對照、KaTeX 數學式、純向量幾何 SVG 品質審查、自動化雙重檢驗工具執行與立案標準。
---

# 國中數學段考試卷全卷轉寫與向量驗收技能指南

本技能專為審查、驗收或接手轉寫臺灣各國中（宜蘭縣及都會區臺北市、新北市、桃園市、臺中市、高雄市）數學段考試卷的 AI 代理人設計。
確保題庫從「紙本掃描點陣圖」轉換為「高品質結構化資料（KaTeX 數學式＋純向量幾何 SVG）」的過程中，與原始試卷保持 100% 忠實對齊，達到免重新組卷、直接可作答與出版之標準。

---

## 一、 核心存放目錄與檔案架構

接手或驗收任何試卷時，請依下列路徑讀取與校對檔案：

```
yilan-math-bank/
├── public/data/papers.json          # 全庫試卷元資料（年度、學期、年級、考次、學校）
├── output/external-ai/
│   └── <學校名稱>_第1包/
│       └── <paperId>/
│           ├── original/<paperId>.pdf    # 原始 PDF 試題卷
│           ├── pages/page-01.png...      # 高解析逐頁渲染圖（視覺驗收對照基準）
│           ├── text-layer.txt            # 原 PDF 提取之文字層參考（不可直接盲信）
│           ├── manifest.json             # 該卷之 SHA-256、頁數、宣告槽位
│           └── <paperId>.md              # 交付 Markdown 檔（含唯一 complete JSON 區塊）
├── research/
│   ├── metro/transcribed/<paperId>.json  # 都會區試卷轉寫標準 JSON
│   ├── yilan/transcribed/<paperId>.json  # 宜蘭區試卷轉寫標準 JSON
│   └── incoming-external/<paperId>/      # 通過 intake 檢驗之暫存驗收區
│       ├── intake.md                     # 驗收入庫之 Markdown 副本
│       └── receipt.json                  # 驗收證明（記錄 usableQuestions、SHA256 等）
└── handoff/
    ├── CLAIMS.json                       # 派工認領狀態表
    └── source-issues/                    # 原卷爭議與版本衝突存證紀錄
```

---

## 二、 轉寫標準規範（Authoring Standards）

轉寫試卷時，必須遵循下列嚴格規範：

### 1. 結構化題型與 JSON 綱要
每個試卷 JSON 主體包含：
- `paperId`: 試卷唯一識別碼。
- `year`, `semester`, `grade`, `exam`: 經卷首核對之真實考期。
- `school`: 學校全稱（如「新北市立中正國民中學」）。
- `questions`: 題幹物件陣列。
  - `type`: `"choice"`（選擇題）、`"fill"`（填充題／選填題）、`"written"`（綜合非選／計算／證明題）。
  - `sourceNumber`: 原卷題號（如 `"1"`, `"2"`, `"一、1"`, `"計算1"`）。
  - `page`: 所在原卷頁碼（整數，從 1 起算）。
  - `difficulty`: `"easy"`, `"medium"`, `"hard"`。
  - `primaryUnitId`: 108 課綱南一單元 ID（如 `"nanyi-8-1-1-2"`）。
  - `unitIds`: 相關單元 ID 陣列。
  - `blocks`: 內容區塊陣列（依序排列）。

### 2. 文字與 KaTeX 數學式規範
- **文字區塊**：`{"type": "text", "text": "..."}`。
- **數學式標記**：所有變數、數值運算、未知數（如 $x$）、分數（如 $\dfrac{a}{b}$）、根號（如 $\sqrt{3}$）、幾何符號（如 $\triangle ABC$、$\overline{AB}$、$\angle A$、$\angle 1$、$\parallel$、$\perp$）一律使用 KaTeX 格式並以單錢號 `$...$` 包裹。
- **禁止裸露換行**：字串內部嚴禁直接出現 ASCII 0x0A (`\n`) 裸露換行字元，若需分段或換行，必須拆分為多個連續的 `text` 區塊。
- **字型限制**：文字字元必須在 `TW-Kai.ttf` 字型支援範圍內（ASCII 0x20..0x7E 及常用正體中文全形字）。

### 3. 純向量幾何 SVG 重繪規範（最關鍵標準）
- **一律純向量重繪**：幾何圖形、函數圖形、統計圖表必須以純向量 SVG 繪製：`{"type": "svg", "svg": "<svg ...>...</svg>"}`。
- **嚴格禁止**：
  - ❌ 禁止使用點陣圖截圖、Base64 編碼。
  - ❌ 禁止使用 `<image>` 標籤。
  - ❌ 禁止使用 `<tspan>` 標籤。
- **幾何要素完整度**：
  - 頂點字母標籤（$A, B, C, D \dots$）位置必須與圖形頂點精確對齊。
  - 垂直直角記號（正方形摺角）、平行箭頭、等長記號、同位角／內錯角弧線必須真實重現。
  - 輔助虛線（如立體圖內部隱藏稜線、高線、對角線）必須以 `stroke-dasharray="4,4"` 標繪。
  - 幾何比例、坐標系刻度與標註長度數值必須符合題意。
- **四選項圖形**：若選擇題的 (A)(B)(C)(D) 各自為一幅圖形，採用 `optionFigures` 結構化屬性呈現。

---

## 三、 驗收與複核執行流程（Verification Workflow）

接手審查或驗收試卷時，請依下列三階段嚴格執行：

### 階段一：自動化工具語法與綱要檢核

在終端機進入 `yilan-math-bank` 目錄：

1. **執行單卷 JSON 格式檢驗**：
   ```bash
   python scripts/check_transcript.py research/metro/transcribed/<paperId>.json
   ```
   **合格標準**：輸出開頭為 `OK`，顯示 `usable X/X`，無任何字型報錯、無缺題、無無效標籤。

2. **執行 Markdown 交付檔 intake 暫存入庫**：
   ```bash
   python scripts/handoff_exchange.py intake "output/external-ai/<學校資料夾>/<paperId>/<paperId>.md"
   ```
   **合格標準**：輸出狀態為 `"status": "staged-for-coordinator-review"`，並在 `research/incoming-external/<paperId>/` 產生 `receipt.json`。

3. **庫存狀態盤點**：
   ```bash
   python scripts/handoff.py --write
   ```
   *注意：絕不可執行 `git push` 或將成果發布至 live 網站。*

---

### 階段二：逐頁人工／視覺側向對照（Side-by-Side Review）

開啟 `output/external-ai/<學校資料夾>/<paperId>/pages/page-*.png` 與轉錄結果逐頁核對：

1. **卷首資訊核對**：
   - 學校全稱、學年度、學期、年級、段考次數是否與卷首印刷完全一致？
   - 若原卷印刷與資料庫清單衝突，必須依照「四、來源衝突處置規範」立案，不可擅自修改或偽造。
2. **題數與題型配分對照**：
   - 原卷大題（選擇題、填充題、計算題）之題數是否無一漏採？
   - 選填題／多格填充題是否完整記錄每格子題與代號？
   - 若原卷明載「試題在答案卷上」且未附答案卷，題號必須保留，並標記 `usable: false, sourceIssue: "..."`。
3. **題幹與公式逐字檢核**：
   - 題幹敘述文字無錯漏字。
   - 所有數學符號是否均正確包覆於 `$...$` 中，無打成純文字。
4. **SVG 圖形精準度驗收**：
   - 圖形幾何拓撲是否正確？（如三角形邊長比例、直角三角形斜邊位置、摺疊角方向）。
   - 頂點與線段標籤是否清晰易讀、未被線段遮蔽？
   - 統計圖表（如長條圖、盒狀圖、圓形圖）之數值與百分比是否與原卷圖形精準吻合？

---

## 四、 原卷爭議與衝突處置規範（Source Conflict Protocol）

若原卷掃描檔存在以下情況：
1. **考期衝突**：卷首明印的年度、學期、年級、段考次數與 `papers.json` 不符。
2. **缺頁或模糊**：原 PDF 缺頁、頁碼倒置或圖形模糊無法判讀。
3. **題目錯印**：原題題目本身存在印刷錯誤或無法作答。

**處置流程**：
1. **嚴禁擅改**：不得自行改動資料庫或偽造卷首。
2. **存證截圖**：截取卷首或爭議頁面存於 `handoff/source-issues/<paperId>-header.png`。
3. **建立存證 JSON**：建立 `handoff/source-issues/<paperId>.json`，記載 `printedHeader`, `declaredSlot`, `printedSlot`, `visualEvidence` 與推論。
4. **回報管理者**：在交付 Markdown 中將 `deliveryStatus` 標為 `"partial"`，保留 pending，待管理者明確決策後方可調整。

---

## 五、 驗收完成回報範本

完成驗收後，請輸出結構化報告，格式如下：

```markdown
### 【<學校全稱> <考期代號> 驗收完成報告】
- **試卷 ID**：`<paperId>`
- **卷首比對**：卷首「<原卷卷首印刷全文>」與申報考期完全相符。
- **題數盤點**：共 XX 題（選擇 XX 題、填充 XX 格、非選 XX 題），可用度 XX/XX。
- **難易度分布**：easy: X, medium: Y, hard: Z。
- **純向量 SVG 數量**：共 XX 組純向量 SVG（逐題列舉圖形主題），全無點陣圖或違規標籤。
- **自動驗證結果**：
  - check_transcript.py: OK
  - handoff_exchange.py intake: staged-for-coordinator-review
- **檔案路徑**：
  - JSON: `research/metro/transcribed/<paperId>.json`
  - Markdown: `output/external-ai/<學校資料夾>/<paperId>/<paperId>.md`
  - Staging: `research/incoming-external/<paperId>/`
```
