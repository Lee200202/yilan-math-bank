# -*- coding: utf-8 -*-
"""Builder script for ld-107-1-3-9
宜蘭縣立羅東國中 107 學年度第一學期九年級數學科第三次段考試卷
"""
import json
import os
import pathlib
import re

PAPER_ID = "ld-107-1-3-9"
SOURCE_SHA256 = "a3cdffb947ef95fdb8caf8be746698232b3b2740c29182547da90eb5cb714dcf"
PRINTED_HEADER = "宜蘭縣立羅東國中 107 學年度第一學期九年級數學科第三次段考試卷"

def clean_svg(s):
    """Strip whitespace between XML tags so check_transcript.py regex doesn't capture newlines."""
    return re.sub(r">\s+<", "><", s.strip())

# --- 17 Pure Vector SVGs ---

# SVG 1: Q2 - 圖(一) (△ABC with circumcenter O)
svg_q2 = clean_svg('''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 180" width="220" height="180">
  <polygon points="100,30 25,120 175,120" fill="none" stroke="#000" stroke-width="2"/>
  <line x1="100" y1="30" x2="100" y2="150" stroke="#777" stroke-width="1.2" stroke-dasharray="4,3"/>
  <line x1="25" y1="120" x2="100" y2="150" stroke="#777" stroke-width="1.2" stroke-dasharray="4,3"/>
  <line x1="175" y1="120" x2="100" y2="150" stroke="#777" stroke-width="1.2" stroke-dasharray="4,3"/>
  <circle cx="100" cy="150" r="2.5" fill="#000"/>
  <text x="100" y="22" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">A</text>
  <text x="16" y="125" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">B</text>
  <text x="185" y="125" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">C</text>
  <text x="100" y="168" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">O</text>
  <text x="100" y="178" font-size="12" font-family="serif" text-anchor="middle" fill="#000">圖(一)</text>
</svg>
''')

# SVG 2: Q3 - 圖(二) (△PQR with medians PN and RM meeting at G)
svg_q3 = clean_svg('''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 180" width="220" height="180">
  <polygon points="25,45 195,45 110,145" fill="none" stroke="#000" stroke-width="2"/>
  <line x1="25" y1="45" x2="152.5" y2="95" stroke="#000" stroke-width="1.5"/>
  <line x1="195" y1="45" x2="67.5" y2="95" stroke="#000" stroke-width="1.5"/>
  <circle cx="110" cy="78.3" r="2.5" fill="#000"/>
  <text x="18" y="42" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">P</text>
  <text x="202" y="42" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">R</text>
  <text x="110" y="160" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">Q</text>
  <text x="56" y="98" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">M</text>
  <text x="164" y="98" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">N</text>
  <text x="118" y="75" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">G</text>
  <text x="110" y="175" font-size="12" font-family="serif" text-anchor="middle" fill="#000">圖(二)</text>
</svg>
''')

# SVG 3: Q4 - 圖(三) (△DEF with incenter I)
svg_q4 = clean_svg('''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 180" width="220" height="180">
  <polygon points="80,25 30,145 190,145" fill="none" stroke="#000" stroke-width="2"/>
  <line x1="80" y1="25" x2="105" y2="105" stroke="#000" stroke-width="1.5"/>
  <line x1="190" y1="145" x2="105" y2="105" stroke="#000" stroke-width="1.5"/>
  <circle cx="105" cy="105" r="2.5" fill="#000"/>
  <text x="80" y="18" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">D</text>
  <text x="20" y="152" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">E</text>
  <text x="200" y="152" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">F</text>
  <text x="116" y="108" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">I</text>
  <text x="110" y="172" font-size="12" font-family="serif" text-anchor="middle" fill="#000">圖(三)</text>
</svg>
''')

# SVG 4: Q5 - 圖(四) (Quadrilateral ABCD with midpoints E, F, G, H)
svg_q5 = clean_svg('''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 180" width="220" height="180">
  <polygon points="40,25 40,145 180,145 110,25" fill="none" stroke="#000" stroke-width="2"/>
  <line x1="40" y1="145" x2="110" y2="25" stroke="#777" stroke-width="1.2"/>
  <line x1="40" y1="25" x2="180" y2="145" stroke="#777" stroke-width="1.2"/>
  <polygon points="75,25 75,85 110,145 110,85" fill="none" stroke="#000" stroke-width="1.8"/>
  <text x="32" y="22" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">A</text>
  <text x="32" y="155" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">B</text>
  <text x="190" y="155" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">C</text>
  <text x="118" y="22" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">D</text>
  <text x="75" y="18" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">E</text>
  <text x="65" y="85" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">F</text>
  <text x="110" y="160" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">G</text>
  <text x="122" y="80" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">H</text>
  <text x="110" y="174" font-size="12" font-family="serif" text-anchor="middle" fill="#000">圖(四)</text>
</svg>
''')

# SVG 5: Q8 - 圖(五) (Cyclic quadrilateral ABCD with circumcenter O)
svg_q8 = clean_svg('''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 180" width="200" height="180">
  <polygon points="80,25 40,85 60,150 160,105" fill="none" stroke="#000" stroke-width="2"/>
  <line x1="80" y1="25" x2="105" y2="85" stroke="#777" stroke-width="1.2"/>
  <line x1="60" y1="150" x2="105" y2="85" stroke="#777" stroke-width="1.2"/>
  <circle cx="105" cy="85" r="2.5" fill="#000"/>
  <text x="80" y="18" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">A</text>
  <text x="28" y="88" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">D</text>
  <text x="55" y="165" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">C</text>
  <text x="172" y="110" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">B</text>
  <text x="116" y="88" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">O</text>
  <text x="100" y="174" font-size="12" font-family="serif" text-anchor="middle" fill="#000">圖(五)</text>
</svg>
''')

# SVG 6: Q9 - 圖(六) (Square ABCD with E on CD, F on BC extension)
svg_q9 = clean_svg('''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 180" width="220" height="180">
  <rect x="65" y="30" width="100" height="100" fill="none" stroke="#000" stroke-width="2"/>
  <line x1="30" y1="130" x2="165" y2="130" stroke="#000" stroke-width="2"/>
  <line x1="65" y1="30" x2="165" y2="70" stroke="#000" stroke-width="1.8"/>
  <line x1="65" y1="30" x2="30" y2="130" stroke="#000" stroke-width="1.8"/>
  <line x1="30" y1="130" x2="165" y2="70" stroke="#000" stroke-width="1.5"/>
  <text x="65" y="22" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">A</text>
  <text x="65" y="145" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">B</text>
  <text x="175" y="145" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">C</text>
  <text x="175" y="25" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">D</text>
  <text x="175" y="75" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">E</text>
  <text x="22" y="145" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">F</text>
  <text x="110" y="168" font-size="12" font-family="serif" text-anchor="middle" fill="#000">圖(六)</text>
</svg>
''')

# SVG 7: Q10 - 圖(七) (Right triangle ABC with legs 8, 15)
svg_q10 = clean_svg('''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 160" width="200" height="160">
  <polygon points="160,35 160,125 35,125" fill="none" stroke="#000" stroke-width="2"/>
  <path d="M 152,125 L 152,117 L 160,117" fill="none" stroke="#000" stroke-width="1.2"/>
  <text x="170" y="38" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">B</text>
  <text x="170" y="132" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">A</text>
  <text x="25" y="132" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">C</text>
  <text x="100" y="152" font-size="12" font-family="serif" text-anchor="middle" fill="#000">圖(七)</text>
</svg>
''')

# SVG 8: Q11 - 圖(八) (Square ABCD with diagonals, E midpoint of BC, AE meets BD at G)
svg_q11 = clean_svg('''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 180" width="200" height="180">
  <rect x="35" y="25" width="110" height="110" fill="none" stroke="#000" stroke-width="2"/>
  <line x1="35" y1="25" x2="145" y2="135" stroke="#777" stroke-width="1.2"/>
  <line x1="35" y1="135" x2="145" y2="25" stroke="#777" stroke-width="1.2"/>
  <line x1="35" y1="25" x2="90" y2="135" stroke="#000" stroke-width="1.8"/>
  <circle cx="90" cy="80" r="2" fill="#000"/>
  <circle cx="71.7" cy="98.3" r="2.5" fill="#000"/>
  <text x="25" y="22" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">A</text>
  <text x="25" y="145" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">B</text>
  <text x="155" y="145" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">C</text>
  <text x="155" y="22" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">D</text>
  <text x="90" y="148" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">E</text>
  <text x="100" y="78" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">O</text>
  <text x="62" y="98" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">G</text>
  <text x="90" y="168" font-size="12" font-family="serif" text-anchor="middle" fill="#000">圖(八)</text>
</svg>
''')

# SVG 9: Q13 - 圖(九) (E midpoint of BC, right triangles ABC and DBC)
svg_q13 = clean_svg('''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 180" width="220" height="180">
  <polygon points="50,45 25,135 175,135" fill="none" stroke="#000" stroke-width="2"/>
  <polygon points="160,45 25,135 175,135" fill="none" stroke="#000" stroke-width="2"/>
  <line x1="50" y1="45" x2="100" y2="135" stroke="#000" stroke-width="1.5"/>
  <line x1="160" y1="45" x2="100" y2="135" stroke="#000" stroke-width="1.5"/>
  <path d="M 44,52 L 52,58 L 57,50" fill="none" stroke="#000" stroke-width="1.2"/>
  <path d="M 153,50 L 158,58 L 166,52" fill="none" stroke="#000" stroke-width="1.2"/>
  <text x="42" y="38" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">A</text>
  <text x="18" y="142" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">B</text>
  <text x="182" y="142" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">C</text>
  <text x="168" y="38" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">D</text>
  <text x="100" y="152" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">E</text>
  <text x="100" y="172" font-size="12" font-family="serif" text-anchor="middle" fill="#000">圖(九)</text>
</svg>
''')

# SVG 10: Q14 - 圖(十) (Isosceles △ABC with altitudes BD and CE)
svg_q14 = clean_svg('''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
  <polygon points="120,20 60,110 120,175" fill="none" stroke="#000" stroke-width="2"/>
  <line x1="120" y1="20" x2="90" y2="142.5" stroke="#000" stroke-width="1.8"/>
  <line x1="120" y1="175" x2="90" y2="52.5" stroke="#000" stroke-width="1.8"/>
  <text x="125" y="16" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">B</text>
  <text x="48" y="115" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">A</text>
  <text x="125" y="190" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">C</text>
  <text x="82" y="48" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">E</text>
  <text x="82" y="152" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">D</text>
  <text x="108" y="105" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">F</text>
  <text x="90" y="195" font-size="12" font-family="serif" text-anchor="middle" fill="#000">圖(十)</text>
</svg>
''')

# SVG 11: Q15 - 圖(十一) (△ABC with incenter O, D on AB)
svg_q15 = clean_svg('''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 180" width="220" height="180">
  <polygon points="50,50 25,145 195,145" fill="none" stroke="#000" stroke-width="2"/>
  <line x1="50" y1="50" x2="60" y2="115" stroke="#000" stroke-width="1.5"/>
  <line x1="195" y1="145" x2="60" y2="115" stroke="#000" stroke-width="1.5"/>
  <line x1="60" y1="115" x2="81.7" y2="145" stroke="#000" stroke-width="1.5"/>
  <circle cx="60" cy="115" r="2.5" fill="#000"/>
  <text x="50" y="42" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">C</text>
  <text x="16" y="152" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">A</text>
  <text x="205" y="152" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">B</text>
  <text x="60" y="105" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">O</text>
  <text x="81.7" y="160" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">D</text>
  <text x="110" y="174" font-size="12" font-family="serif" text-anchor="middle" fill="#000">圖(十一)</text>
</svg>
''')

# SVG 12: Q16 - 圖(十二) (Isosceles △DEF with circumcenter O on DM extension)
svg_q12_geom = clean_svg('''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 180" width="200" height="180">
  <polygon points="100,30 30,110 170,110" fill="none" stroke="#000" stroke-width="2"/>
  <line x1="100" y1="30" x2="100" y2="150" stroke="#000" stroke-width="1.8"/>
  <path d="M 100,102 L 108,102 L 108,110" fill="none" stroke="#000" stroke-width="1.2"/>
  <circle cx="100" cy="150" r="2.5" fill="#000"/>
  <text x="100" y="22" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">D</text>
  <text x="20" y="115" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">E</text>
  <text x="180" y="115" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">F</text>
  <text x="88" y="105" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">M</text>
  <text x="112" y="155" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">O</text>
  <text x="100" y="174" font-size="12" font-family="serif" text-anchor="middle" fill="#000">圖(十二)</text>
</svg>
''')

# SVG 13: Q17 - 圖(十三) (△ABC with median AD, midpoints E, F, intersection G)
svg_q17 = clean_svg('''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 190" width="200" height="190">
  <polygon points="100,25 35,145 165,145" fill="none" stroke="#000" stroke-width="2"/>
  <line x1="100" y1="25" x2="100" y2="145" stroke="#000" stroke-width="1.8"/>
  <line x1="35" y1="145" x2="100" y2="85" stroke="#000" stroke-width="1.5"/>
  <line x1="165" y1="145" x2="67.5" y2="115" stroke="#000" stroke-width="1.5"/>
  <text x="100" y="18" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">A</text>
  <text x="25" y="152" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">B</text>
  <text x="175" y="152" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">C</text>
  <text x="100" y="160" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">D</text>
  <text x="110" y="85" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">E</text>
  <text x="58" y="115" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">F</text>
  <text x="110" y="112" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">G</text>
  <text x="100" y="180" font-size="12" font-family="serif" text-anchor="middle" fill="#000">圖(十三)</text>
</svg>
''')

# SVG 14: Q18 - 圖(十四) (Rectangle ABCD with diagonal BD, centroid G, incenter I)
svg_q18 = clean_svg('''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 180" width="220" height="180">
  <rect x="40" y="30" width="140" height="105" fill="none" stroke="#000" stroke-width="2"/>
  <line x1="40" y1="135" x2="180" y2="30" stroke="#000" stroke-width="1.8"/>
  <circle cx="75" cy="55" r="2.5" fill="#000"/>
  <circle cx="145" cy="110" r="2.5" fill="#000"/>
  <text x="30" y="30" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">A</text>
  <text x="190" y="30" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">B</text>
  <text x="190" y="142" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">C</text>
  <text x="30" y="142" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">D</text>
  <text x="65" y="55" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">G</text>
  <text x="155" y="110" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">I</text>
  <text x="110" y="168" font-size="12" font-family="serif" text-anchor="middle" fill="#000">圖(十四)</text>
</svg>
''')

# SVG 15: Written 2 (Squares ABCD and DEFG)
svg_w2 = clean_svg('''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 170" width="220" height="170">
  <rect x="45" y="30" width="55" height="55" fill="none" stroke="#000" stroke-width="2"/>
  <rect x="100" y="30" width="85" height="85" fill="none" stroke="#000" stroke-width="2"/>
  <line x1="45" y1="30" x2="100" y2="115" stroke="#000" stroke-width="1.8"/>
  <line x1="100" y1="85" x2="185" y2="30" stroke="#000" stroke-width="1.8"/>
  <text x="40" y="24" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">A</text>
  <text x="35" y="88" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">B</text>
  <text x="112" y="82" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">C</text>
  <text x="100" y="24" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">D</text>
  <text x="100" y="130" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">E</text>
  <text x="190" y="130" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">F</text>
  <text x="190" y="24" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">G</text>
</svg>
''')

# SVG 16: Written 3 (Intersecting segments AB, CD, AC, BD meeting at O)
svg_w3 = clean_svg('''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 180" width="220" height="180">
  <polygon points="70,30 30,140 185,140 145,30" fill="none" stroke="#000" stroke-width="2"/>
  <line x1="70" y1="30" x2="185" y2="140" stroke="#000" stroke-width="1.8"/>
  <line x1="145" y1="30" x2="30" y2="140" stroke="#000" stroke-width="1.8"/>
  <circle cx="107.5" cy="85" r="2.5" fill="#000"/>
  <text x="70" y="22" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">A</text>
  <text x="20" y="148" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">B</text>
  <text x="195" y="148" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">C</text>
  <text x="145" y="22" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">D</text>
  <text x="107.5" y="102" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">O</text>
</svg>
''')

# SVG 17: Written 4 (△ABC with incenter I, ID // AB, IE // AC)
svg_w4 = clean_svg('''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 180" width="200" height="180">
  <polygon points="135,25 40,145 160,145" fill="none" stroke="#000" stroke-width="2"/>
  <line x1="120" y1="95" x2="80" y2="145" stroke="#000" stroke-width="1.8"/>
  <line x1="120" y1="95" x2="130" y2="145" stroke="#000" stroke-width="1.8"/>
  <circle cx="120" cy="95" r="2.5" fill="#000"/>
  <text x="135" y="18" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">A</text>
  <text x="30" y="152" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">B</text>
  <text x="170" y="152" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">C</text>
  <text x="80" y="160" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">D</text>
  <text x="130" y="160" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">E</text>
  <text x="120" y="85" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">I</text>
</svg>
''')


def build_transcript():
    questions = [
        # Fill 1
        {
            "page": 1,
            "type": "fill",
            "sourceNumber": "1",
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-3-2",
            "unitIds": ["nanyi-9-1-3-2"],
            "unitAssignmentBasis": "評量三角形外心到三頂點等距離之基本性質。",
            "blocks": [
                {"type": "text", "text": "已知 $O$ 點為 $\\triangle ABC$ 的外心，且 $\\overline{OA} + \\overline{OB} = 6$，求 $\\overline{OC} = ＿＿＿＿$。"}
            ]
        },
        # Fill 2
        {
            "page": 1,
            "type": "fill",
            "sourceNumber": "2",
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-3-2",
            "unitIds": ["nanyi-9-1-3-2"],
            "unitAssignmentBasis": "評量鈍角三角形外心圓心角與圓周角關係之計算。",
            "blocks": [
                {"type": "text", "text": "如圖(一)，$O$ 點為三角形 $ABC$ 的外心，$\\angle BAC = 100^\\circ$，求 $\\angle BOC = ＿＿＿＿$度。"},
                {"type": "svg", "svg": svg_q2}
            ]
        },
        # Fill 3
        {
            "page": 1,
            "type": "fill",
            "sourceNumber": "3",
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-3-2",
            "unitIds": ["nanyi-9-1-3-2"],
            "unitAssignmentBasis": "評量三角形重心分割中線為 2:1 比例之計算。",
            "blocks": [
                {"type": "text", "text": "如圖(二)，$\\triangle PQR$ 中，$M$、$N$ 分別為 $\\overline{PQ}$、$\\overline{QR}$ 的中點，$\\overline{PN}$、$\\overline{RM}$ 交於 $G$ 點，若 $\\overline{GM} = 5$，求 $\\overline{RM} = ＿＿＿＿$。"},
                {"type": "svg", "svg": svg_q3}
            ]
        },
        # Fill 4
        {
            "page": 1,
            "type": "fill",
            "sourceNumber": "4",
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-3-2",
            "unitIds": ["nanyi-9-1-3-2"],
            "unitAssignmentBasis": "評量三角形內心頂角與兩內角平分線夾角公式計算。",
            "blocks": [
                {"type": "text", "text": "如圖(三)，$I$ 點為 $\\triangle DEF$ 的內心，$\\angle EFD = 40^\\circ$，$\\angle E = 80^\\circ$，求 $\\angle DIF = ＿＿＿＿$度。"},
                {"type": "svg", "svg": svg_q4}
            ]
        },
        # Fill 5
        {
            "page": 1,
            "type": "fill",
            "sourceNumber": "5",
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-2",
            "unitIds": ["nanyi-9-1-1-2"],
            "unitAssignmentBasis": "評量三角形中點連線段性質與四邊形周長計算。",
            "blocks": [
                {"type": "text", "text": "如圖(四)，四邊形 $ABCD$ 中，$E$、$F$、$G$、$H$ 分別為 $\\overline{AD}$、$\\overline{BD}$、$\\overline{BC}$、$\\overline{AC}$ 的中點，若 $\\overline{AB} = 30$，$\\overline{CD} = 36$，求四邊形 $EFGH$ 的周長為＿＿＿＿。"},
                {"type": "svg", "svg": svg_q5}
            ]
        },
        # Fill 6
        {
            "page": 1,
            "type": "fill",
            "sourceNumber": "6",
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-3-2",
            "unitIds": ["nanyi-9-1-3-2"],
            "unitAssignmentBasis": "評量三角形內心到三邊垂直距離相等之基本性質。",
            "blocks": [
                {"type": "text", "text": "在 $\\triangle ABC$ 中，$I$ 為內心，且 $\\overline{ID} \\perp \\overline{AB}$ 於 $D$ 點，$\\overline{IE} \\perp \\overline{BC}$ 於 $E$ 點，$\\overline{IF} \\perp \\overline{AC}$ 於 $F$ 點，則 $\\overline{ID} : \\overline{IE} : \\overline{IF} = ＿＿＿＿$。"}
            ]
        },
        # Fill 7
        {
            "page": 1,
            "type": "fill",
            "sourceNumber": "7",
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-3-2",
            "unitIds": ["nanyi-9-1-3-2"],
            "unitAssignmentBasis": "評量利用三角形面積與內切圓半徑求周長之公式運算。",
            "blocks": [
                {"type": "text", "text": "已知 $\\triangle ABC$ 的面積為 $24$，內切圓半徑為 $2$，求 $\\triangle ABC$ 的周長＝＿＿＿＿。"}
            ]
        },
        # Fill 8
        {
            "page": 1,
            "type": "fill",
            "sourceNumber": "8",
            "difficulty": "medium",
            "primaryUnitId": "nanyi-9-1-2-2",
            "unitIds": ["nanyi-9-1-2-2", "nanyi-9-1-3-2"],
            "unitAssignmentBasis": "評量圓內接四邊形對角互補與外心圓心角之關係計算。",
            "blocks": [
                {"type": "text", "text": "如圖(五)，$O$ 點為四邊形 $ABCD$ 的外心，$\\angle ADC = 115^\\circ$，則 $\\angle AOC = ＿＿＿＿$度。"},
                {"type": "svg", "svg": svg_q8}
            ]
        },
        # Fill 9
        {
            "page": 1,
            "type": "fill",
            "sourceNumber": "9",
            "difficulty": "medium",
            "primaryUnitId": "nanyi-9-1-3-1",
            "unitIds": ["nanyi-9-1-3-1"],
            "unitAssignmentBasis": "評量正方形全等旋轉性質與等腰直角三角形角度計算。",
            "blocks": [
                {"type": "text", "text": "如圖(六)，正方形 $ABCD$ 中，$E$ 點在 $\\overline{CD}$ 上，$F$ 點在 $\\overline{BC}$ 的延長線上，若 $\\overline{AE} \\perp \\overline{AF}$，$\\angle DAE = 20^\\circ$，求 $\\angle EFC = ＿＿＿＿$度。"},
                {"type": "svg", "svg": svg_q9}
            ]
        },
        # Fill 10
        {
            "page": 1,
            "type": "fill",
            "sourceNumber": "10",
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-3-2",
            "unitIds": ["nanyi-9-1-3-2"],
            "unitAssignmentBasis": "評量直角三角形兩股與斜邊求內切圓半徑之公式應用。",
            "blocks": [
                {"type": "text", "text": "如圖(七)，$\\triangle ABC$ 中，$\\angle A = 90^\\circ$，$\\overline{AB} = 8$，$\\overline{AC} = 15$，求 $\\triangle ABC$ 的內切圓半徑為＿＿＿＿。"},
                {"type": "svg", "svg": svg_q10}
            ]
        },
        # Fill 11
        {
            "page": 1,
            "type": "fill",
            "sourceNumber": "11",
            "difficulty": "medium",
            "primaryUnitId": "nanyi-9-1-3-2",
            "unitIds": ["nanyi-9-1-3-2"],
            "unitAssignmentBasis": "評量正方形對角線交點與中線交會之重心性質求線段長度。",
            "blocks": [
                {"type": "text", "text": "如圖(八)，正方形 $ABCD$ 中，$O$ 為對角線的交點，$E$ 為 $\\overline{BC}$ 中點，且 $\\overline{AE}$、$\\overline{BD}$ 交於 $G$ 點，若 $\\overline{AB} = 6$，求 $\\overline{GD}$ 為＿＿＿＿。"},
                {"type": "svg", "svg": svg_q11}
            ]
        },
        # Fill 12
        {
            "page": 1,
            "type": "fill",
            "sourceNumber": "12",
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-3-2",
            "unitIds": ["nanyi-9-1-3-2"],
            "unitAssignmentBasis": "評量正三角形重心即內心外心，求內切圓半徑與面積。",
            "blocks": [
                {"type": "text", "text": "正三角形 $ABC$ 中，$G$ 點為重心，$\\overline{AG} = 8$，求 $\\triangle ABC$ 內切圓的面積為＿＿＿＿。"}
            ]
        },
        # Fill 13
        {
            "page": 1,
            "type": "fill",
            "sourceNumber": "13",
            "difficulty": "medium",
            "primaryUnitId": "nanyi-9-1-3-2",
            "unitIds": ["nanyi-9-1-3-2"],
            "unitAssignmentBasis": "評量直角三角形斜邊中點到三頂點等距之性質與角度計算。",
            "blocks": [
                {"type": "text", "text": "如圖(九)，$E$ 為 $\\overline{BC}$ 中點，且 $\\overline{AC} \\perp \\overline{AB}$，$\\overline{BD} \\perp \\overline{CD}$，$\\angle ABE = 70^\\circ$，$\\angle DCE = 75^\\circ$，則 $\\angle AED = ＿＿＿＿$度。"},
                {"type": "svg", "svg": svg_q13}
            ]
        },
        # Fill 14
        {
            "page": 1,
            "type": "fill",
            "sourceNumber": "14",
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-3-1",
            "unitIds": ["nanyi-9-1-3-1"],
            "unitAssignmentBasis": "評量等腰三角形高線性質與畢氏定理求線段長度。",
            "blocks": [
                {"type": "text", "text": "如圖(十)，$\\overline{AB} = \\overline{AC}$，$\\overline{CE} \\perp \\overline{AB}$，$\\overline{BD} \\perp \\overline{AC}$，$\\overline{BD}$ 與 $\\overline{CE}$ 交於 $F$ 點，若 $\\overline{AB} = 13$，$\\overline{BD} = 12$，則 $\\overline{BE}$ 為＿＿＿＿。"},
                {"type": "svg", "svg": svg_q14}
            ]
        },
        # Fill 15
        {
            "page": 1,
            "type": "fill",
            "sourceNumber": "15",
            "difficulty": "medium",
            "primaryUnitId": "nanyi-9-1-3-2",
            "unitIds": ["nanyi-9-1-3-2"],
            "unitAssignmentBasis": "評量內心分割三角形面積比例與底邊線段比之綜合計算。",
            "blocks": [
                {"type": "text", "text": "如圖(十一)，$\\overline{AB} = 12$，$\\overline{BC} = 10$，$\\overline{AC} = 6$，且 $\\overline{BO}$、$\\overline{AO}$ 為 $\\triangle ABC$ 的兩內角平分線。若 $2\\overline{AD} = \\overline{BD}$，則 $\\triangle ADO$ 與 $\\triangle ABC$ 的面積比為＿＿＿＿。"},
                {"type": "svg", "svg": svg_q15}
            ]
        },
        # Fill 16
        {
            "page": 2,
            "type": "fill",
            "sourceNumber": "16",
            "difficulty": "medium",
            "primaryUnitId": "nanyi-9-1-3-2",
            "unitIds": ["nanyi-9-1-3-2"],
            "unitAssignmentBasis": "評量等腰三角形中垂線上外心半徑之直角三角形勾股定理運算。",
            "blocks": [
                {"type": "text", "text": "如圖(十二)，$O$ 點為等腰三角形 $DEF$ 的外心，$\\overline{DE} = \\overline{DF} = 10$，$\\overline{EM} = 8$，$\\overline{DM}$ 垂直平分 $\\overline{EF}$，$O$ 點在 $\\overline{DM}$ 的延長線上，求 $\\triangle DEF$ 的外接圓半徑為＿＿＿＿。"},
                {"type": "svg", "svg": svg_q12_geom}
            ]
        },
        # Fill 17
        {
            "page": 2,
            "type": "fill",
            "sourceNumber": "17",
            "difficulty": "hard",
            "primaryUnitId": "nanyi-9-1-3-2",
            "unitIds": ["nanyi-9-1-3-2", "nanyi-9-1-1-2"],
            "unitAssignmentBasis": "評量中線比例、孟氏定理或中線倍長分割三角形面積之進階推理。",
            "blocks": [
                {"type": "text", "text": "如圖(十三)，在 $\\triangle ABC$ 中，$\\overline{AD}$ 為中線，$E$ 為 $\\overline{AD}$ 的中點，$F$ 為 $\\overline{BE}$ 的中點。若 $\\overline{AD}$ 與 $\\overline{CF}$ 相交於 $G$ 點，則 $\\triangle EFG$ 的面積：$\\triangle ABC$ 的面積＝＿＿＿＿。"},
                {"type": "svg", "svg": svg_q17}
            ]
        },
        # Fill 18
        {
            "page": 2,
            "type": "fill",
            "sourceNumber": "18",
            "difficulty": "hard",
            "primaryUnitId": "nanyi-9-1-3-2",
            "unitIds": ["nanyi-9-1-3-2"],
            "unitAssignmentBasis": "評量直角坐標系中三角形重心與內心坐標之兩點距離計算。",
            "blocks": [
                {"type": "text", "text": "如圖(十四)，長方形 $ABCD$ 中，$\\overline{AB} = 12$，$\\overline{BC} = 9$，其中 $G$ 為 $\\triangle ABD$ 的重心，且 $I$ 為 $\\triangle BCD$ 的內心，則 $\\overline{GI} = ＿＿＿＿$。"},
                {"type": "svg", "svg": svg_q18}
            ]
        },
        # Written 1
        {
            "page": 2,
            "type": "written",
            "sourceNumber": "1",
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-3-1",
            "unitIds": ["nanyi-9-1-3-1"],
            "unitAssignmentBasis": "評量代數展開、因式分解與整除性之推理證明。",
            "blocks": [
                {"type": "text", "text": "已知：$a$、$b$ 為正整數，且 $a + 36 = (6b + 12)^2$，求證：$a$ 是 $36$ 的倍數。"}
            ]
        },
        # Written 2
        {
            "page": 2,
            "type": "written",
            "sourceNumber": "2",
            "difficulty": "medium",
            "primaryUnitId": "nanyi-9-1-3-1",
            "unitIds": ["nanyi-9-1-3-1"],
            "unitAssignmentBasis": "評量共頂點兩正方形邊角關係與 SAS 三角形全等證明。",
            "blocks": [
                {"type": "text", "text": "如圖，四邊形 $ABCD$、$DEFG$ 均為正方形。求證：$\\overline{AE} = \\overline{CG}$。"},
                {"type": "svg", "svg": svg_w2}
            ]
        },
        # Written 3
        {
            "page": 2,
            "type": "written",
            "sourceNumber": "3",
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-3-1",
            "unitIds": ["nanyi-9-1-3-1"],
            "unitAssignmentBasis": "評量 SSS 三角形全等性質與等腰三角形對稱證明。",
            "blocks": [
                {"type": "text", "text": "如圖，$\\overline{AB} = \\overline{CD}$，$\\overline{AC} = \\overline{BD}$。求證：$\\overline{AO} = \\overline{DO}$。"},
                {"type": "svg", "svg": svg_w3}
            ]
        },
        # Written 4
        {
            "page": 2,
            "type": "written",
            "sourceNumber": "4",
            "difficulty": "medium",
            "primaryUnitId": "nanyi-9-1-3-2",
            "unitIds": ["nanyi-9-1-3-2"],
            "unitAssignmentBasis": "評量內心角平分線與平行線所夾等腰三角形性質求周長。",
            "blocks": [
                {"type": "text", "text": "如圖，$I$ 為 $\\triangle ABC$ 的內心，$\\overline{ID} \\parallel \\overline{AB}$，$\\overline{IE} \\parallel \\overline{AC}$。若 $\\overline{AB} = 10$，$\\overline{BC} = 9$，$\\overline{AC} = 8$，求 $\\triangle IDE$ 的周長為多少？"},
                {"type": "svg", "svg": svg_w4}
            ]
        }
    ]

    transcript = {
        "paperId": PAPER_ID,
        "sourceSha256": SOURCE_SHA256,
        "printedHeader": PRINTED_HEADER,
        "printedSlot": {
            "year": 107,
            "semester": 1,
            "grade": 9,
            "exam": 3
        },
        "printedCounts": "填充題18題、計算證明題4題，合計22題。",
        "expectedTypes": {
            "choice": 0,
            "fill": 18,
            "written": 4
        },
        "questions": questions
    }
    return transcript


def generate_markdown(transcript):
    """Generate delivery markdown following RETURN_TEMPLATE.md."""
    md_lines = []
    md_lines.append(f"# 試卷轉錄交付：{PRINTED_HEADER}")
    md_lines.append("")
    md_lines.append(f"- **Paper ID**: `{PAPER_ID}`")
    md_lines.append(f"- **來源 SHA256**: `{SOURCE_SHA256}`")
    md_lines.append("- **學校/考次**: 宜蘭縣立羅東國民中學 107 學年度 第 1 學期 第 3 次段考 九年級 (107-1 G9 E3)")
    md_lines.append("- **總題數**: 22 題（填充題 18 題、計算證明題 4 題）")
    md_lines.append("")
    md_lines.append("---")
    md_lines.append("")
    md_lines.append("## 一、試題純文字預覽")
    md_lines.append("")

    for q in transcript["questions"]:
        q_type_str = {"choice": "選擇題", "fill": "填充題", "written": "計算證明題"}[q["type"]]
        md_lines.append(f"### 【{q_type_str} {q['sourceNumber']}】 (難度: {q['difficulty']}, 單元: {q['primaryUnitId']})")
        for b in q["blocks"]:
            if b["type"] == "text":
                md_lines.append(b["text"])
            elif b["type"] == "svg":
                md_lines.append("*(幾何圖形純向量 SVG)*")
        md_lines.append("")

    md_lines.append("---")
    md_lines.append("")
    md_lines.append("## 二、完整轉錄 JSON 封裝")
    md_lines.append("")

    handoff_dict = dict(transcript)
    handoff_dict["deliveryStatus"] = "complete"
    handoff_dict["visualReviewComplete"] = True
    handoff_dict["reviewNote"] = "全卷22題忠實轉錄，重繪17幅純向量幾何SVG，完成108課綱單元標註與難度評定。"

    json_str = json.dumps(handoff_dict, ensure_ascii=False, indent=2)
    md_lines.append("```json")
    md_lines.append(json_str)
    md_lines.append("```")
    md_lines.append("")

    return "\n".join(md_lines)


def main():
    transcript = build_transcript()
    out_dir = pathlib.Path("research/yilan/transcribed")
    out_dir.mkdir(parents=True, exist_ok=True)

    json_path = out_dir / f"{PAPER_ID}.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(transcript, f, ensure_ascii=False, indent=2)
    print(f"Generated {json_path.resolve()} with {len(transcript['questions'])} questions.")

    md_path = out_dir / f"{PAPER_ID}.md"
    md_content = generate_markdown(transcript)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Generated {md_path.resolve()}")


if __name__ == "__main__":
    main()
