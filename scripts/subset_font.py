"""Build public/fonts/TW-Kai-subset.ttf from the full CNS 全字庫正楷體 (TW-Kai.ttf, 政府資料開放授權).

Keeps every character printed by the question bank (text/options/table/SVG text) plus ASCII,
common punctuation/symbols and all Big5 常用字 (level 1, 5,401 chars) so user-typed paper
titles still render. The build fails if any bank character is missing from the subset.
"""
import json
import pathlib
import re

from fontTools import subset
from fontTools.ttLib import TTFont

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / 'research/fonts/TW-Kai.ttf'
OUT = ROOT / 'public/fonts/TW-Kai-subset.ttf'


def bank_chars():
    chars = set()
    for q in json.loads((ROOT / 'public/data/questions.json').read_text(encoding='utf-8')):
        strings = []
        for b in q.get('blocks', []):
            strings += [b.get('text', '')] + b.get('items', []) + [c for r in b.get('rows', []) for c in r]
            if b.get('svg'):
                strings += re.findall(r'>([^<>]+)<', b['svg'])
        if q.get('diagramSvg'):
            strings += re.findall(r'>([^<>]+)<', q['diagramSvg'])
        for s in strings:
            chars |= set(re.sub(r'\$\$[\s\S]+?\$\$|\$[^$]+?\$', '', s))
    # Keep printable wide spaces (U+3000 is drawn as a glyph); drop only ASCII whitespace.
    return {c for c in chars if c not in ' \t\r\n'}


def big5_level1():
    out = set()
    for hi in range(0xA4, 0xC7):
        for lo in list(range(0x40, 0x7F)) + list(range(0xA1, 0xFF)):
            try:
                out.add(bytes([hi, lo]).decode('big5'))
            except UnicodeDecodeError:
                pass
    return out


def main():
    need = bank_chars()
    # Most later batches reuse the same Chinese glyphs. Avoid rebuilding a large
    # font when the existing, word-aligned subset already covers the entire bank.
    stamp_path = ROOT / 'public/fonts/subset-coverage.json'
    if OUT.exists() and OUT.with_suffix('.woff2').exists() and stamp_path.exists():
        cached = TTFont(OUT)
        if all(ord(c) in cached.getBestCmap() for c in need) and all(n % 2 == 0 for n in cached['loca'].locations):
            import hashlib
            stamp = json.loads(stamp_path.read_text(encoding='utf-8'))
            stamp.update(questionsSha256=hashlib.sha256((ROOT/'public/data/questions.json').read_bytes().replace(b'\r\n',b'\n')).hexdigest(),bankChars=len(need),ttfBytes=OUT.stat().st_size)
            stamp_path.write_text(json.dumps(stamp,ensure_ascii=False,indent=1),encoding='utf-8')
            print(json.dumps({'fontReused':True,**stamp}))
            return
    ui = set('　 八七九年級上下學期第一二三次段考練習選擇題填充非未寫計算過程不給分答＿（）、，。：；？！「」『』…—－＋×÷＝＜＞±√°％')
    keep = need | ui | big5_level1() | {chr(c) for c in range(0x20, 0x7F)} | set('²³¹⁰′″←→↑↓∠△□◇○◎☆★■▇█▓▲▼√∞≠≦≧≒≈∴∵∥⊥')
    font = TTFont(SRC)
    cmap = font.getBestCmap()
    keep = {c for c in keep if ord(c) in cmap}
    missing = sorted(c for c in need if ord(c) not in cmap)
    if missing:
        raise SystemExit(f'Bank characters missing from the source font: {missing}')
    opts = subset.Options()
    opts.layout_features = ['*']
    opts.name_IDs = ['*']
    opts.notdef_outline = True
    sub = subset.Subsetter(opts)
    sub.populate(unicodes=[ord(c) for c in keep])
    sub.subset(font)
    # fontkit chooses short loca offsets for small PDF subsets, dividing offsets
    # by two. Odd glyph lengths in the larger web font would be truncated there,
    # producing invisible native glyphs even though PDF text extraction succeeds.
    # Keep every source glyph word-aligned so both short and long subsets are valid.
    font['glyf'].padding = 2
    font.save(OUT)
    woff = TTFont(OUT)
    woff.flavor = 'woff2'
    woff.save(OUT.with_suffix('.woff2'))
    check = TTFont(OUT).getBestCmap()
    lost = sorted(c for c in need if ord(c) not in check)
    if lost:
        raise SystemExit(f'Subset lost bank characters: {lost}')
    import hashlib
    stamp = {'questionsSha256': hashlib.sha256((ROOT / 'public/data/questions.json').read_bytes().replace(b'\r\n', b'\n')).hexdigest(),
             'bankChars': len(need), 'glyphsKept': len(keep), 'ttfBytes': OUT.stat().st_size,
             'source': 'CNS 全字庫正楷體 TW-Kai.ttf（政府資料開放授權條款第1版），子集化保留題庫用字＋Big5常用字'}
    (ROOT / 'public/fonts/subset-coverage.json').write_text(json.dumps(stamp, ensure_ascii=False, indent=1), encoding='utf-8')
    print(json.dumps(stamp, ensure_ascii=False))


if __name__ == '__main__':
    main()
