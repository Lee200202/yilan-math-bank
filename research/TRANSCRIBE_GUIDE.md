# Whole-paper transcription guide (helpers)

Read `AI_HANDOFF.md` and `handoff/CLAIMS.json` before claiming a paper. One coordinator
owns rebuild and publication; assistants write only their claimed paper files.

**Figure-only options:** use `{ "type": "optionFigures", "svg": "<svg ...>...</svg>", "maxHeight": 100 }`
instead of a text-options block. The panel must faithfully contain all four option drawings
and one label each `(A)`–`(D)`. Do not append an `options` block containing only those labels.
That duplicates labels and can conceal entirely missing figures. The checker rejects
label-only text options and undrawn panels. Machine validation is not visual verification.

Goal: turn an original school math exam PDF into reviewed text questions that the site can
compose into new tests. One finished JSON file per paper. Quality over speed: every question
must read exactly like the original (numbers, signs, options, figures).

## Your files (touch nothing else)

- Read your target list: `research/targets/<group>.json` (ordered; work top to bottom).
- Write each finished paper to its `outFile` (`research/metro/transcribed/<paperId>.json` or
  `research/yilan/transcribed/<paperId>.json`). Skip a target whose outFile already exists.
- Page images go to `research/targets/render/<group>/` (ignored by git).
- Papers you cannot use go to `research/targets/<group>-skipped.json`, a JSON list of
  `{"paperId": ..., "reason": ...}` (create or extend it).
- Do NOT run `prepare_data.py`, `subset_font.py`, `build.mjs`, `npm test`, any `git` command, and do
  not edit any other repo file. The coordinator rebuilds, checks PDF output, and publishes.

## Steps per paper

1. Render: `python -I research/metro/render_pages.py <pdf> research/targets/render/<group>/<paperId> 2`
   → `<prefix>-p1.png …` and `<prefix>-text.txt` (text layer; may be empty for scans, and formulas in it
   are often garbled; always trust the image). Look at every page image with the Read tool; zoom by
   re-rendering at 3 if small print is unclear.
2. Confirm the printed header (school / 學年度 / 學期 / 年級 / 第幾次段考). `printedSlot` must equal the
   target's year/semester/grade/exam. If the printed header disagrees, or the file is an answer key,
   not math, not an exam paper, a duplicate, or unreadable → add it to the skipped list with the
   reason and move on. Never guess.
3. Transcribe every question unit of the whole paper (all pages) into the schema below.
4. Run `python scripts/check_transcript.py <outFile>`; fix every FAIL. Then re-read the page
   images once more against your file (numbers, signs, option order, figure labels).

## Schema

```json
{
 "paperId": "<target paperId>",
 "sourceSha256": "<sha256 of the PDF file: python -c \"import hashlib,sys;print(hashlib.sha256(open(sys.argv[1],'rb').read()).hexdigest())\" <pdf>>",
 "printedHeader": "臺中市立○○國中114學年度第一學期七年級數學科第二次段考",
 "printedSlot": {"year": 114, "semester": 1, "grade": 7, "exam": 2},
 "printedCounts": "選擇10題、填充16格、計算1題（3小題）。",
 "visualReviewComplete": true,
 "reviewNote": "two lines: what you checked, figures redrawn, anything excluded and why",
 "expectedTypes": {"choice": 10, "fill": 16, "written": 1},
 "questions": [
  {"type": "choice", "sourceNumber": "1", "page": 1, "difficulty": "easy",
   "primaryUnitId": "nanyi-7-1-1-1", "unitIds": ["nanyi-7-1-1-1"], "unitAssignmentBasis": "負數大小比較。",
   "blocks": [{"type": "text", "text": "比 $-5.68$ 小的整數中，最大的整數為下列何者？"},
              {"type": "options", "items": ["$-7$", "$-6$", "$-5$", "$-4$"]}]}
 ]
}
```

- `type`: `choice` (has an `options` block, items WITHOUT (A)(B) labels), `fill` (blank written as
  `＿＿＿＿`), `written` (計算/應用/證明; sub-parts as separate text blocks "(1) …", "(2) …").
- `sourceNumber`: the printed number within its section (choice 1.., fill 1.., written 1..). Must be
  unique per type. If a fill item has several blanks, keep it one question with several `＿＿＿＿`.
  If the paper numbers fills by blank letters (A, B, …) inside numbered items, number by the item.
- True/false items → `fill`: "判斷對錯（填○或✕）：…＿＿＿＿".
- A group of questions sharing one stem (題組): repeat the needed stem in each question so each
  question stands alone.
- `expectedTypes` counts ALL questions in the file (including `usable:false`).
- `page`: 1-based page where the question starts.
- `difficulty`: `easy` (one direct step / definition), `medium` (2–3 steps or one concept applied),
  `hard` (multi-step, combined concepts, unusual reasoning). Judge each question honestly.
- Units: pick from `research/nanyi-units.json` (南一 108 units, ids `nanyi-<grade>-<sem>-<ch>-<sec>`).
  `primaryUnitId` is the main skill; `unitIds` includes it plus secondary ones. Usually within the
  paper's grade/semester (or earlier, for review questions). `unitAssignmentBasis`: one short sentence.
- Unusable question (original contradictory, figure missing, text cut off, cannot be read): keep it
  with `"usable": false, "sourceIssue": "reason"` — it still counts in expectedTypes.
- Leave out score notes, school unit codes such as (1-2), "會考題" tags, and answer-sheet instructions.

## Text and math

- Math in `$…$` (MathJax): `\dfrac{a}{b}`, `\times`, `\div`, `\sqrt{}`, `^{}`, `\overline{AB}`,
  `\angle`, `\triangle`, `\pm`, `\ne`, `\le`, `\ge`, `\approx`, `\perp`, `\sim`, `\cdots`, `\circ`.
- In the JSON file every backslash is doubled: `"$\\dfrac{1}{2}$"`.
- Keep each `$…$` short (≈ 25 characters of output max). Split long chains into segments separated by
  a space: `$=(-24)-6\\times(-1)$ $=-18$`. The PDF column is narrow and a too-wide formula fails.
- Avoid tables whose cells hold long formulas; use one text line per item instead.
- Tables: `{"type": "table", "header": true, "rows": [["x", "1", "2"], ["y", "3", "4"]]}` (short cells).
- Chinese text outside `$…$`; full-width punctuation（，。：？）as in the original.
- Write files with the Write tool (never shell heredocs/echo: this machine mangles backslashes).

## Figures (must be redrawn as vector SVG — no images)

`{"type": "svg", "maxHeight": 120, "svg": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 300 160\">…</svg>"}`

- Only `path/line/polyline/polygon/circle/ellipse/rect/text/g`. No `<image>`, `<tspan>`, `<foreignObject>`,
  scripts or embedded data. Stroke `#111`, width 1.2–1.6, `fill="none"` for outlines.
- `<text>` is printed in Kai at a fixed size: use plain Unicode (², ³, √, π, °, −), no super/subscript
  markup. Italic letters for points/variables (`font-style="italic"`), font-size 14–18 in viewBox units.
- Reproduce what the question needs: shape, labels, given lengths/angles, right-angle marks, tick
  marks, parallel arrows, number-line positions, coordinate axes/grid. Keep proportions close.
- `maxHeight` 50–180 (points). Keep labels clear of lines.
- Charts/graphs: redraw axes, ticks, values. If a figure is too complex to redraw faithfully (photo,
  dense map), mark that question `usable:false` with the reason instead of a wrong drawing.

## Report

When you stop, reply with: finished files (paperId, school, slot, usable/total), skipped papers with
reasons, and anything the coordinator should double-check. Only leave fully finished, checked files.
