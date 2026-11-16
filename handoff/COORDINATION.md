# 兩位 AI 同時作業的分工與發布規則（2026-11-16，Claude 與 Antigravity 共用同一資料夾）

兩位 AI 共用同一個工作目錄與同一個 GitHub 儲存庫。為避免重複轉寫與互相覆蓋，照下列分工：

| 負責人 | 範圍（轉寫＋認領） |
|---|---|
| **Antigravity** | **宜蘭縣**（中華、羅東、內城）：八下 → 九上 → 九下。 |
| **Claude（及 Codex）** | **都會區（臺北／新北／桃園／臺中／高雄）**：八上 → 八下 → 九上 → 九下 → 最後七年級。（宜蘭八上已由 Claude 完成 w4，之後不再碰宜蘭。） |

- 認領一律先寫 `handoff/CLAIMS.json`（`research/make_waves.py` 會自動排除已被認領或已有轉寫檔的卷）。看到 `agent` 欄不是自己的卷就不要碰。
- 想換範圍時，先改這個檔並推送，再開始做；不要靜默跨進對方的範圍。
- 兩邊都可以發布，但**一次只有一位在建置／推送**：開始前看 `git log origin/main -1` 與 `git status`；建置（`merge_batch.py`）與推送之間不要讓出時間；推送前先 `git fetch`，若 `origin/main` 前進了，先 `git pull --rebase`，衝突只會出現在程式產生的檔案（`public/data/*.json`、`research/release-transcripts.json`、`handoff/*.json`）——`release-transcripts.json` 取兩邊「papers」的聯集，其餘產生檔取任一邊後重跑 `python -X utf8 scripts/merge_batch.py`。
- 版本字串（`20261116-metro-vNN`）永遠取目前最大值再加一（兩人不要同時改成同一個數字）。
- 只 `git add` 自己核准的檔案；不要把對方進行中、尚未核准的轉寫檔或一次性腳本加進 commit。
- 對方的卷已進 `release-transcripts.json` 就是已發布／待發布，不要重做。
- 省 token 的方法見 `skills/exam-bank-coordinator/SKILL.md` §8。

## 使用者 2026-11-16 最新指示

各 AI 只寫自己範圍的轉寫檔，**不碰共用建置檔**（`public/data/*`、`research/release-transcripts.json`、版本字串）；全部或一段完成後，由使用者指定的一位集中檢查格式與圖形，再銜接發布。因此 Claude 從現在起只產出都會區轉寫檔，不自行建置、不推送，除非使用者要求發布。
