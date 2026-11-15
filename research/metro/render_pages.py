"""Render each page of a metro PDF to PNG for visual transcription, and dump the text layer.
Usage: python -I render_pages.py <pdf> <out_prefix> [zoom]"""
import sys
import pathlib
import pymupdf as fitz

pdf, prefix = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
zoom = float(sys.argv[3]) if len(sys.argv) > 3 else 1.6
prefix.parent.mkdir(parents=True, exist_ok=True)
doc = fitz.open(pdf)
texts = []
for i, page in enumerate(doc):
    page.get_pixmap(matrix=fitz.Matrix(zoom, zoom)).save(f"{prefix}-p{i + 1}.png")
    texts.append(f"===== page {i + 1} ({page.rect.width:.0f}x{page.rect.height:.0f}) =====\n" + page.get_text("text"))
pathlib.Path(f"{prefix}-text.txt").write_text("\n".join(texts), encoding="utf-8")
print(len(doc), "pages")
