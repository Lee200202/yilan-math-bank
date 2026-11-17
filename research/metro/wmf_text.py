"""Dump the text records of a WMF picture (MathType equation pictures render as overlapping glyphs in PNG;
the WMF text records give the characters with x/y positions, which is easier to read reliably).

Usage: python -X utf8 research/metro/wmf_text.py <file.wmf> [more.wmf ...]
Prints one line per text record: T/t x y bytes, and font records. Characters of the Symbol font appear as raw bytes
(0xB1 = ±, 0xB4 = ×, 0xB8 = ÷, 0xD6 = √ ...). Read left-to-right, small y offsets = sub/superscripts; check against the answer key.
Idea and first version: wave o1-6 helper.
"""
import struct
import sys

for path in sys.argv[1:]:
    d = open(path, 'rb').read()
    off = 22 if d[:4] == b'\xd7\xcd\xc6\x9a' else 0
    p = off + 18
    print(path)
    while p < len(d):
        size, fn = struct.unpack('<IH', d[p:p + 6])
        if size < 3:
            break
        body = d[p + 6:p + size * 2]
        if fn == 0x0A32:
            y, x, cnt, opt = struct.unpack('<hhhH', body[:8])
            print(' T', x, y, body[8:8 + cnt])
        elif fn == 0x0521:
            cnt = struct.unpack('<h', body[:2])[0]
            pad = (cnt + 1) // 2 * 2
            y, x = struct.unpack('<hh', body[2 + pad:6 + pad])
            print(' t', x, y, body[2:2 + cnt])
        elif fn == 0x02FB:
            lf = struct.unpack('<hhhhhBBBBBBBB', body[:18]) if len(body) >= 18 else ()
            print(' font h', lf[0] if lf else None, body[18:].split(b'\0')[0])
        p += size * 2
