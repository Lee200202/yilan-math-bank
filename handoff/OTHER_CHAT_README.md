# 把工作交給另一個聊天室

最容易的方式：把「學校工作包.zip」附到另一個AI聊天室，再貼 [EXTERNAL_AI_PROMPT.md](EXTERNAL_AI_PROMPT.md) 全文。每個聊天室分1–2份完整原卷，別把相同paperId同時派給兩邊。

工作包已附原卷、每頁PNG、來源SHA256、宣告範圍、原文字層、完整南一單元表、轉寫規格及MD回傳範本。對方應直接看包內媒體，無須重新爬校網；Codex也保有同一份原卷供校對。PNG僅供看原題，不能成為正式題目的圖片。

首批3包也已放進共用Git：`handoff/workpacks/yilan-zhonghua-01.zip`、`yilan-luodong-01.zip`、`yilan-neicheng-01.zip`。同機AI直接讀取，雲端AI同步儲存庫後亦可讀到，或由使用者下載後附到聊天室。如果對方不能讀ZIP，解壓後提供該卷original PDF、全部pages與AI_PROMPT即可。

## 回傳給Codex／Claude

1. 請對方產生 `<paperId>.md` 可下載附件，或把多個MD放ZIP。必須含全卷可讀題文與唯一完整JSON資料區塊；圖形用內嵌SVG。
2. 下載到電腦，直接將MD／ZIP拖進這個聊天室或新的Codex聊天室，說「請依AI_HANDOFF.md匯入這批轉寫MD並驗收」。也可提供完整本機檔案路徑。無法上傳時，完整貼MD正文亦可；大型媒體仍需檔案附件。
3. 新的Codex／Claude先同步GitHub，讀AI_HANDOFF.md。收到檔案後執行：

```powershell
python scripts/handoff_exchange.py intake "C:/Users/user/Downloads/AI回傳.zip"
```

工具驗證paperId、原檔SHA、卷首範圍、題型／題數、難度／單元、公式格式與選項完整性，再放進 `research/incoming-external/<paperId>/` 待審。**不覆寫既有全卷、不直接改網站、不自動發布**。一般自由格式MD也可交給協調者閱讀，但缺少結構JSON時不能一鍵匯入。

協調者實看原卷與題圖後，才把核對的JSON放到research/yilan/transcribed或research/metro/transcribed，依既有流程重建、PDF逐頁驗收及正式站驗證。其他AI說「完成」不是驗收證據。

## 完整待辦與後續分派

- [19校摘要與各校明細](assignments/INDEX.md)
- [全部1,453份未全卷完成資料](assignments/all-targets.json)：含1,415未轉寫與38部分；844 PDF、320 DOCX、148 DOC、141 ODT。Word／ODT也要處理，不能只完成PDF便結案。
- `python scripts/handoff_exchange.py inventory` 可重算各校待辦。
- 產新工作包範例：

```powershell
python scripts/handoff_exchange.py pack --school "中華國中" --limit 2 --out "output/external-ai/中華下一批"
```

包裝工具優先從已定位PDF清單挑未完成普通班卷；抽班卷、來源衝突或Word格式需另明確分派，不會偷偷當一般PDF。現有包代表這一批任務，不能當整校完成。

## API選項

雲端聊天室通常無法存取本機 `127.0.0.1`，所以跨聊天室以ZIP／MD傳遞為主。以下本機API供能執行本機程式的AI或協調者使用；本站GitHub Pages沒有公開寫入API。

```powershell
python scripts/handoff_exchange.py serve --port 8787
```

詳見 [API.md](API.md) 與 [OpenAPI規格](api/openapi.json)。只綁本機、不開跨站CORS；匯入只進待審區。不要為了讓雲端聊天室連進來而公開電腦連接埠或交出GitHub金鑰。
