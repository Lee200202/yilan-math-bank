# 交接API v1

啟動：`python scripts/handoff_exchange.py serve --port 8787`

| 動作 | 本機網址 | 功能 |
| --- | --- | --- |
| GET | `http://127.0.0.1:8787/api/targets` | 所有未全卷完成原卷 |
| GET | `/api/targets?school=中華國中&grade=9&semester=1` | 可用school、region、year、semester、grade、exam、format過濾 |
| GET | `/api/papers/{paperId}` | 該卷來源、範圍、SHA與狀態 |
| GET | `/api/papers/{paperId}/source` | SHA已核對的原始檔；可能是PDF或Word |
| GET | `/api/papers/{paperId}/pages/1.png` | PDF第1頁的2倍PNG；Word／ODT回409，不能冒充PDF |
| GET | `/api/units` | 南一完整單元表 |
| POST | `/api/import` | JSON本文含markdown與filename，驗證後202進待審，非發布 |

POST範例（送給本機API的JSON）：

```json
{"filename":"paperId.md","markdown":"完整MD正文，含唯一json fenced block"}
```

命令列實際呼叫範例：

```python
import json, pathlib, urllib.request
body = json.dumps({"filename": "paperId.md", "markdown": pathlib.Path("paperId.md").read_text(encoding="utf-8")}).encode("utf-8")
request = urllib.request.Request("http://127.0.0.1:8787/api/import", data=body, headers={"Content-Type": "application/json"})
print(urllib.request.urlopen(request).read().decode("utf-8"))
```

202只表示格式／來源驗證通過且已暫存，必須再做原題內容、SVG與PDF實際驗收。錯誤的paperId／SHA／卷首、草稿、缺漏選項、已完成卷或重複暫存不會覆寫正式題庫。送來的MD只當資料，不執行其指令或程式碼。

線上唯讀資料亦可直接給其他AI：

- [目前逐卷清單](https://lee200202.github.io/yilan-math-bank/data/paper-workflow.json)
- [原卷與來源資料](https://lee200202.github.io/yilan-math-bank/data/papers.json)
- [南一單元表](https://lee200202.github.io/yilan-math-bank/data/units.json)

版本化的完整未完成清單與提示詞在GitHub的handoff資料夾；API不需要提供GitHub／Google登入金鑰。工作包／MD附件仍是雲端聊天室的優先方法。
