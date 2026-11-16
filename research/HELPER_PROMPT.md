# Transcription helper brief (read fully; your wave id and number are in your launch message)

You convert original school math exam PDFs into reviewed text questions for a Taiwanese junior-high math exam bank.
Repo: C:\Users\user\桌面\國中家教\yilan-math-bank (Windows; Bash = Git Bash). Always run python with `-X utf8` and WITHOUT `-I`.

Target list: research/targets/<wave>-<k>.json (papers already claimed for you in handoff/CLAIMS.json). Each entry: paperId,
school/year/semester/grade/exam, pdf (original), outFile (where to write your JSON). If a target's outFile already exists, skip it.

FIRST read research/TRANSCRIBE_GUIDE.md fully and follow it exactly (schema, LaTeX rules, SVG figure rules, optionFigures, difficulty,
南一 units in research/nanyi-units.json). Match style of finished examples such as research/metro/transcribed/metro-taichung-4df3addf545236f6-270006bc.json
and research/yilan/transcribed/183TRa0vOg4H9S12jauOZXQNBl8SvJoPp.json.

Per paper:
1. `python -X utf8 research/metro/render_pages.py <pdf> research/targets/render/<wave>-<k>/<paperId> 1.6` → page PNGs + `<prefix>-text.txt`
   (PDF text layer: exact digits/words, but fractions/roots/superscripts may be garbled and two-column pages interleave). Use the text layer
   for exact numbers/wording and the page images (Read tool) for structure, math layout and figures. Scanned PDFs have no text layer: read
   images only (zoom to 2.5 if small). View EVERY page. Trailing answer-key / answer-sheet pages are not questions: do not transcribe them
   (use them only to sanity-check).
2. Confirm the printed header matches the target slot (year/semester/grade/exam). If it does not, or the file is only an answer key / not math /
   unreadable, do NOT guess: add {"paperId","reason"} to research/targets/<wave>-<k>-skipped.json and go on. A blank grade field is fine if the answer
   sheet or exam range clearly shows the grade.
3. Transcribe the WHOLE paper: every question and sub-question, with type, difficulty (easy/medium/hard judged from content) and 南一 unit.
   Figures are redrawn as vector SVG with plain attributes ONLY (no <style>, no class=, no style=, no height="auto"/width="100%" on the root).
   Figure-only options use optionFigures. If the original contradicts itself or a figure cannot be redrawn faithfully, keep the question with
   usable:false and a sourceIssue instead of guessing.
4. Write the JSON with the Write tool or a small Python script using json.dump (never shell heredocs/echo for LaTeX: they mangle backslashes).
   Keep scratch scripts in your OWN folder scratchpad\<wave>-<k>\ under the session scratchpad directory (helpers share the parent and overwrite each other).
   sourceSha256 = sha256 of the PDF (must equal papers.json for that paperId). visualReviewComplete true only after comparing your file with every page image.
5. `python -X utf8 scripts/check_transcript.py <outFile>` until OK; then reread your file against the pages once more (numbers, signs, options, figure labels).

Touch only your outFiles, research/targets/<wave>-<k>-skipped.json and research/targets/render/<wave>-<k>/. No git, no prepare_data/build/npm test/qa scripts,
no CLAIMS edits. Other helpers work in parallel. Work through ALL papers in order; do not stop early.
Final reply (short): per paper → paperId, usable/total, type counts, difficulty counts, number of SVG figures, anything uncertain (contradictions,
approximate figures, judgment calls); plus skipped papers with reasons.
