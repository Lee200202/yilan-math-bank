# Word → DOCX 自動轉檔（2026-11-17，已驗證可用）

這台電腦的 Word（Office 16）可以無人值守把舊版 `.doc` 轉成 `.docx`，約 8–11 秒／份，不會卡住。**不要用 Word 轉 PDF（ExportAsFixedFormat）**，那一步先前會卡住；轉 docx 沒有問題。

- 單檔：`python -X utf8 scripts/word_convert.py <in.doc> <out.docx> [逾時秒數]`（子行程＋逾時＋逐步紀錄 `%TEMP%\wordconv_*.log`；逾時只關掉本次啟動的 Word，不碰使用者自己開的 Word）。
- 批次：`python -X utf8 scripts/word_convert_batch.py <輸出資料夾>`（所有尚未完成的 `.doc` 卷，含宜蘭；輸出 `<paperId>.docx` 與 `_report.json`；已轉過的略過）。共用資料夾的輸出在 `research/metro/converted/`（不進 git，可重做）。
- 轉出的 docx 以 `python -X utf8 research/metro/office_extract.py <docx> <輸出資料夾>` 抽文字／LaTeX 公式／圖片（見 `research/HELPER_OFFICE.md`）。舊版 Equation Editor 公式會被 Word 轉成真的公式，比 antiword 純文字好很多。轉寫稿的 `sourceSha256` 仍用**原始 .doc** 的 SHA。
- 認領與派工：`python -X utf8 research/make_office_waves.py <wave> <helpers> <per-helper>`（docx / odt / 已轉換的 doc）。
- 羅東 108 上九第二次（`research/word-reference/`）等先前因舊 doc 卡住的卷，現在可先轉成 docx 再抽取。
