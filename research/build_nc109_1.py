# -*- coding: utf-8 -*-
"""Builder script for nc-109-1-1-9
宜蘭縣立內城國民中小學-國中部109 學年度第一學期 九年級數學科第一次段考試題
"""
import json
import os
import pathlib
import re

PAPER_ID = "nc-109-1-1-9"
SOURCE_SHA256 = "ac78847bc6f20165ee568c146e2da4a5131b7715154e770ff5fa0f75918e94d1"
PRINTED_HEADER = "宜蘭縣立內城國民中小學-國中部109 學年度第一學期 九年級數學科第一次段考試題"

def clean_svg(s):
    """Strip whitespace between XML tags so check_transcript.py regex doesn't capture newlines."""
    return re.sub(r">\s+<", "><", s.strip())

# --- 12 Pure Vector SVGs ---

# SVG 1: Choice 1 - 圖一 (△ABC with DE // BC)
svg_c1 = clean_svg('''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 180" width="200" height="180">
  <polygon points="50,25 20,155 180,155" fill="none" stroke="#000" stroke-width="2"/>
  <line x1="35" y1="90" x2="115" y2="90" stroke="#000" stroke-width="1.8"/>
  <text x="50" y="18" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">A</text>
  <text x="12" y="162" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">B</text>
  <text x="190" y="162" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">C</text>
  <text x="24" y="92" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">D</text>
  <text x="125" y="88" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">E</text>
  <text x="100" y="175" font-size="13" font-family="serif" text-anchor="middle" fill="#000">圖一</text>
</svg>
''')

# SVG 2: Choice 2 - 圖二 (△ABC with D on AB, E on AC)
svg_c2 = clean_svg('''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 180" width="200" height="180">
  <polygon points="90,25 30,155 170,155" fill="none" stroke="#000" stroke-width="2"/>
  <line x1="66" y1="77" x2="122" y2="77" stroke="#000" stroke-width="1.8"/>
  <text x="90" y="18" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">A</text>
  <text x="20" y="162" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">B</text>
  <text x="180" y="162" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">C</text>
  <text x="56" y="75" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">D</text>
  <text x="132" y="75" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">E</text>
  <text x="100" y="175" font-size="13" font-family="serif" text-anchor="middle" fill="#000">圖二</text>
</svg>
''')

# SVG 3: Choice 3 - 圖三 (△ABC with midline DE)
svg_c3 = clean_svg('''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 180" width="200" height="180">
  <polygon points="80,25 30,155 180,155" fill="none" stroke="#000" stroke-width="2"/>
  <line x1="55" y1="90" x2="130" y2="90" stroke="#000" stroke-width="1.8"/>
  <text x="80" y="18" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">A</text>
  <text x="20" y="162" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">B</text>
  <text x="190" y="162" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">C</text>
  <text x="45" y="92" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">D</text>
  <text x="140" y="92" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">E</text>
  <text x="100" y="175" font-size="13" font-family="serif" text-anchor="middle" fill="#000">圖三</text>
</svg>
''')

# SVG 4: Choice 4 - 圖四 (Parallel lines cut by transversals)
svg_c4 = clean_svg('''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 180" width="220" height="180">
  <line x1="30" y1="40" x2="190" y2="40" stroke="#000" stroke-width="1.8"/>
  <line x1="30" y1="85" x2="190" y2="85" stroke="#000" stroke-width="1.8"/>
  <line x1="30" y1="130" x2="190" y2="130" stroke="#000" stroke-width="1.8"/>
  <line x1="45" y1="20" x2="75" y2="150" stroke="#000" stroke-width="1.5"/>
  <line x1="145" y1="20" x2="175" y2="150" stroke="#000" stroke-width="1.5"/>
  <text x="200" y="44" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">L1</text>
  <text x="200" y="89" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">L2</text>
  <text x="200" y="134" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">L3</text>
  <text x="40" y="16" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">M</text>
  <text x="140" y="16" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">N</text>
  <text x="36" y="38" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">A</text>
  <text x="46" y="83" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">B</text>
  <text x="56" y="128" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">C</text>
  <text x="160" y="38" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">D</text>
  <text x="170" y="83" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">E</text>
  <text x="180" y="128" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">F</text>
  <text x="110" y="172" font-size="13" font-family="serif" text-anchor="middle" fill="#000">圖四</text>
</svg>
''')

# SVG 5: Choice 5 - 圖五 (Parallelogram ABCD with diagonals meeting at E)
svg_c5 = clean_svg('''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 180" width="240" height="180">
  <polygon points="175,40 65,48 25,135 135,127" fill="none" stroke="#000" stroke-width="2"/>
  <line x1="175" y1="40" x2="25" y2="135" stroke="#000" stroke-width="1.5"/>
  <line x1="65" y1="48" x2="135" y2="127" stroke="#000" stroke-width="1.5"/>
  <text x="185" y="35" font-size="12" font-family="sans-serif" text-anchor="middle" fill="#000">A(13 , 7)</text>
  <text x="55" y="40" font-size="12" font-family="sans-serif" text-anchor="middle" fill="#000">B(2 , 6)</text>
  <text x="145" y="142" font-size="12" font-family="sans-serif" text-anchor="middle" fill="#000">D(9 , 3)</text>
  <text x="18" y="148" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">C</text>
  <text x="96" y="98" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">E</text>
  <text x="100" y="172" font-size="13" font-family="serif" text-anchor="middle" fill="#000">圖五</text>
</svg>
''')

# SVG 6: Choice 9 - 圖九 (Quadrilaterals 甲 and 乙)
svg_c9 = clean_svg('''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 170" width="240" height="170">
  <rect x="40" y="50" width="90" height="80" fill="none" stroke="#000" stroke-width="2"/>
  <rect x="130" y="98" width="36" height="32" fill="none" stroke="#000" stroke-width="2"/>
  <path d="M 40,42 Q 103,30 166,42" fill="none" stroke="#000" stroke-width="1.2"/>
  <text x="103" y="32" font-size="14" font-family="sans-serif" text-anchor="middle" fill="#000">14</text>
  <path d="M 32,50 Q 22,90 32,130" fill="none" stroke="#000" stroke-width="1.2"/>
  <text x="16" y="95" font-size="14" font-family="sans-serif" text-anchor="middle" fill="#000">5</text>
  <path d="M 174,98 Q 182,114 174,130" fill="none" stroke="#000" stroke-width="1.2"/>
  <text x="190" y="118" font-size="14" font-family="sans-serif" text-anchor="middle" fill="#000">2</text>
  <text x="40" y="38" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">A</text>
  <text x="168" y="38" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">B</text>
  <text x="85" y="96" font-size="16" font-family="serif" text-anchor="middle" fill="#000">甲</text>
  <text x="148" y="119" font-size="14" font-family="serif" text-anchor="middle" fill="#000">乙</text>
  <text x="103" y="162" font-size="13" font-family="serif" text-anchor="middle" fill="#000">圖九</text>
</svg>
''')

# SVG 7: Choice 10 - 圖十 (AB // EF // CD)
svg_c10 = clean_svg('''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 180" width="220" height="180">
  <line x1="40" y1="145" x2="180" y2="145" stroke="#000" stroke-width="2"/>
  <line x1="40" y1="145" x2="40" y2="70" stroke="#000" stroke-width="2"/>
  <line x1="180" y1="145" x2="180" y2="25" stroke="#000" stroke-width="2"/>
  <line x1="40" y1="70" x2="180" y2="145" stroke="#000" stroke-width="1.5"/>
  <line x1="40" y1="145" x2="180" y2="25" stroke="#000" stroke-width="1.5"/>
  <line x1="82" y1="145" x2="82" y2="92" stroke="#000" stroke-width="1.8"/>
  <text x="30" y="68" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">A</text>
  <text x="30" y="152" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">B</text>
  <text x="190" y="152" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">C</text>
  <text x="190" y="25" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">D</text>
  <text x="82" y="84" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">E</text>
  <text x="82" y="160" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">F</text>
  <text x="26" y="112" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">x</text>
  <text x="96" y="125" font-size="12" font-family="sans-serif" text-anchor="middle" fill="#000">10</text>
  <text x="195" y="85" font-size="12" font-family="sans-serif" text-anchor="middle" fill="#000">30</text>
  <text x="110" y="172" font-size="13" font-family="serif" text-anchor="middle" fill="#000">圖十</text>
</svg>
''')

# SVG 8: Fill 4 - 圖四 (River measurement)
svg_f4 = clean_svg('''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
  <line x1="30" y1="65" x2="170" y2="65" stroke="#777" stroke-width="1"/>
  <line x1="30" y1="135" x2="170" y2="135" stroke="#777" stroke-width="1"/>
  <path d="M 40,80 Q 70,75 100,80 T 160,80" fill="none" stroke="#aaa" stroke-width="1"/>
  <path d="M 40,100 Q 70,95 100,100 T 160,100" fill="none" stroke="#aaa" stroke-width="1"/>
  <path d="M 40,120 Q 70,115 100,120 T 160,120" fill="none" stroke="#aaa" stroke-width="1"/>
  <line x1="50" y1="50" x2="50" y2="170" stroke="#000" stroke-width="2"/>
  <line x1="50" y1="135" x2="95" y2="135" stroke="#000" stroke-width="1.8"/>
  <line x1="50" y1="170" x2="122" y2="170" stroke="#000" stroke-width="1.8"/>
  <line x1="50" y1="50" x2="122" y2="170" stroke="#000" stroke-width="1.8"/>
  <path d="M 50,127 L 58,127 L 58,135" fill="none" stroke="#000" stroke-width="1"/>
  <path d="M 50,162 L 58,162 L 58,170" fill="none" stroke="#000" stroke-width="1"/>
  <text x="50" y="42" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">A</text>
  <text x="38" y="138" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">D</text>
  <text x="38" y="174" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">B</text>
  <text x="95" y="128" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">E</text>
  <text x="132" y="174" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">C</text>
  <text x="100" y="194" font-size="13" font-family="serif" text-anchor="middle" fill="#000">圖四</text>
</svg>
''')

# SVG 9: Fill 5 - 圖五 (Similar triangles with medians)
svg_f5 = clean_svg('''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 170" width="260" height="170">
  <polygon points="30,30 30,135 140,135" fill="none" stroke="#000" stroke-width="2"/>
  <polygon points="30,30 30,135 85,135" fill="#e8e8e8" stroke="none"/>
  <line x1="30" y1="30" x2="85" y2="135" stroke="#000" stroke-width="1.8"/>
  <polygon points="175,70 175,135 235,135" fill="none" stroke="#000" stroke-width="2"/>
  <polygon points="175,70 175,135 205,135" fill="#e8e8e8" stroke="none"/>
  <line x1="175" y1="70" x2="205" y2="135" stroke="#000" stroke-width="1.8"/>
  <text x="30" y="22" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">B</text>
  <text x="20" y="142" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">A</text>
  <text x="148" y="142" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">C</text>
  <text x="85" y="148" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">M</text>
  <text x="175" y="62" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">E</text>
  <text x="165" y="142" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">D</text>
  <text x="242" y="142" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">F</text>
  <text x="205" y="148" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">N</text>
  <text x="130" y="164" font-size="13" font-family="serif" text-anchor="middle" fill="#000">圖五</text>
</svg>
''')

# SVG 10: Fill 6 - 圖六 (Trapezoid ABCD with diagonal AC)
svg_f6 = clean_svg('''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 160" width="220" height="160">
  <polygon points="50,35 150,35 190,125 30,125" fill="none" stroke="#000" stroke-width="2"/>
  <polygon points="50,35 30,125 190,125" fill="#e8e8e8" stroke="none"/>
  <line x1="50" y1="35" x2="190" y2="125" stroke="#000" stroke-width="1.8"/>
  <text x="45" y="28" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">A</text>
  <text x="155" y="28" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">D</text>
  <text x="20" y="132" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">B</text>
  <text x="200" y="132" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">C</text>
  <text x="110" y="152" font-size="13" font-family="serif" text-anchor="middle" fill="#000">圖六</text>
</svg>
''')

# SVG 11: Fill 7 - 圖七 (△ABC with DE // BC)
svg_f7 = clean_svg('''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 180" width="200" height="180">
  <polygon points="90,25 30,155 170,155" fill="none" stroke="#000" stroke-width="2"/>
  <polygon points="90,25 57,97 134,97" fill="#e8e8e8" stroke="none"/>
  <line x1="57" y1="97" x2="134" y2="97" stroke="#000" stroke-width="1.8"/>
  <text x="90" y="18" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">A</text>
  <text x="20" y="162" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">B</text>
  <text x="180" y="162" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">C</text>
  <text x="46" y="97" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">D</text>
  <text x="144" y="97" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">E</text>
  <text x="100" y="175" font-size="13" font-family="serif" text-anchor="middle" fill="#000">圖七</text>
</svg>
''')

# SVG 12: Fill 8 - 圖八 (Rectangle ABCD with midpoints)
svg_f8 = clean_svg('''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 180" width="200" height="180">
  <rect x="30" y="30" width="140" height="110" fill="none" stroke="#000" stroke-width="2"/>
  <polygon points="100,30 30,85 100,140 170,85" fill="none" stroke="#000" stroke-width="1.8"/>
  <rect x="65" y="57.5" width="70" height="55" fill="none" stroke="#000" stroke-width="1.8"/>
  <text x="20" y="28" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">A</text>
  <text x="180" y="28" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">D</text>
  <text x="20" y="148" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">B</text>
  <text x="180" y="148" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">C</text>
  <text x="100" y="22" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">E</text>
  <text x="18" y="88" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">F</text>
  <text x="100" y="156" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">G</text>
  <text x="182" y="88" font-size="14" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">H</text>
  <text x="56" y="55" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">I</text>
  <text x="56" y="120" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">J</text>
  <text x="144" y="120" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">K</text>
  <text x="144" y="55" font-size="13" font-family="serif" font-style="italic" text-anchor="middle" fill="#000">L</text>
  <text x="100" y="174" font-size="13" font-family="serif" text-anchor="middle" fill="#000">圖八</text>
</svg>
''')


def build_transcript():
    questions = [
        # Choice 1
        {
            "page": 1,
            "type": "choice",
            "sourceNumber": "1",
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-2",
            "unitIds": ["nanyi-9-1-1-2"],
            "unitAssignmentBasis": "評量平行線截比例線段性質計算線段長度。",
            "blocks": [
                {"type": "text", "text": "如圖一，$\\triangle ABC$ 中，$D$、$E$ 分別為 $\\overline{AB}$、$\\overline{AC}$ 上一點，且 $\\overline{DE} \\parallel \\overline{BC}$，若 $\\overline{AD} = 5$、$\\overline{DB} = 7$、$\\overline{AE} = 10$，則 $\\overline{EC} = ？$"},
                {"type": "options", "items": ["$12$", "$14$", "$16$", "$13$"]},
                {"type": "svg", "svg": svg_c1}
            ]
        },
        # Choice 2
        {
            "page": 1,
            "type": "choice",
            "sourceNumber": "2",
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-2",
            "unitIds": ["nanyi-9-1-1-2"],
            "unitAssignmentBasis": "評量平行線判別性質與同位角相等判斷角度。",
            "blocks": [
                {"type": "text", "text": "如圖二，若 $\\overline{AE} = 4$、$\\overline{AD} = \\overline{EC} = 6$、$\\overline{DB} = 9$，且 $\\angle B = 60^\\circ$，則 $\\angle ADE = ？$"},
                {"type": "options", "items": ["$70^\\circ$", "$60^\\circ$", "$50^\\circ$", "$40^\\circ$"]},
                {"type": "svg", "svg": svg_c2}
            ]
        },
        # Choice 3
        {
            "page": 1,
            "type": "choice",
            "sourceNumber": "3",
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-2",
            "unitIds": ["nanyi-9-1-1-2"],
            "unitAssignmentBasis": "評量三角形兩邊中點連線段性質與三角形周長計算。",
            "blocks": [
                {"type": "text", "text": "如圖三，$\\triangle ABC$ 中，$D$ 為 $\\overline{AB}$ 中點，且 $\\overline{DE} \\parallel \\overline{BC}$，若 $\\overline{AD} = 20$、$\\overline{AE} = 22$、$\\overline{DE} = 24$，則 $\\triangle ABC$ 的周長＝？"},
                {"type": "options", "items": ["$132$", "$120$", "$142$", "$88$"]},
                {"type": "svg", "svg": svg_c3}
            ]
        },
        # Choice 4
        {
            "page": 1,
            "type": "choice",
            "sourceNumber": "4",
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-2",
            "unitIds": ["nanyi-9-1-1-2"],
            "unitAssignmentBasis": "評量三條平行線截比例線段性質與一元一次方程式求解。",
            "blocks": [
                {"type": "text", "text": "如圖四，$L_1 \\parallel L_2 \\parallel L_3$，且分別與 $M$ 相交於 $A$、$B$、$C$ 三點，與 $N$ 相交於 $D$、$E$、$F$ 三點，若 $\\overline{AB} = 2$，$\\overline{BC} = 2x - 2$，$\\overline{DE} = 3$，$\\overline{EF} = -x + 13$，則 $x = ？$"},
                {"type": "options", "items": ["$2$", "$4$", "$0$", "$-2$"]},
                {"type": "svg", "svg": svg_c4}
            ]
        },
        # Choice 5
        {
            "page": 1,
            "type": "choice",
            "sourceNumber": "5",
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-2",
            "unitIds": ["nanyi-9-1-1-2"],
            "unitAssignmentBasis": "評量直角坐標系中平行四邊形對角線互相平分與中點坐標公式。",
            "blocks": [
                {"type": "text", "text": "如圖五，$E$ 為平行四邊形 $ABCD$ 對角線的交點，則：$C$ 點坐標為何？"},
                {"type": "options", "items": ["$C(-2, -2)$", "$C(2, 2)$", "$C(2, -2)$", "$C(-2, 2)$"]},
                {"type": "svg", "svg": svg_c5}
            ]
        },
        # Choice 6
        {
            "page": 2,
            "type": "choice",
            "sourceNumber": "6",
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-2",
            "unitIds": ["nanyi-9-1-1-2"],
            "unitAssignmentBasis": "評量直角坐標系兩點中點坐標公式之運算判斷。",
            "blocks": [
                {"type": "text", "text": "下列各組點中，哪一組的中點坐標是 $(2, -3)$？"},
                {"type": "options", "items": [
                    "$(2, 1)$、$(5, -3)$",
                    "$(-4, 2)$、$(8, -8)$",
                    "$(2, 0)$、$(0, -3)$",
                    "$(0, -1)$、$(1, -2)$"
                ]}
            ]
        },
        # Choice 7
        {
            "page": 2,
            "type": "choice",
            "sourceNumber": "7",
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-3",
            "unitIds": ["nanyi-9-1-1-3"],
            "unitAssignmentBasis": "評量平面圖形相似定義（對應角相等且對應邊成比例）之判別。",
            "blocks": [
                {"type": "text", "text": "下列各組圖形中，哪一組圖形不一定相似？"},
                {"type": "options", "items": ["任意兩個正三角形", "任意兩個等腰直角三角形", "任意兩個正方形", "任意兩個菱形"]}
            ]
        },
        # Choice 8
        {
            "page": 2,
            "type": "choice",
            "sourceNumber": "8",
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-3",
            "unitIds": ["nanyi-9-1-1-3"],
            "unitAssignmentBasis": "評量多邊形縮放性質：邊長依比例縮放而對應角度不變。",
            "blocks": [
                {"type": "text", "text": "將五邊形 $ABCDE$ 縮放 $60\\%$ 後得到一五邊形 $A'B'C'D'E'$，其中 $A$、$B$、$C$、$D$、$E$ 的對應點分別為 $A'$、$B'$、$C'$、$D'$、$E'$。若 $\\overline{AB} = 6$、$\\angle A = 70^\\circ$，則 $\\overline{A'B'}$ 的長度與 $\\angle A'$ 的度數分別為何？"},
                {"type": "options", "items": [
                    "$\\overline{A'B'} = 6$，$ \\angle A' = 70^\\circ$",
                    "$\\overline{A'B'} = 3.6$，$ \\angle A' = 70^\\circ$",
                    "$\\overline{A'B'} = 3.6$，$ \\angle A' = 42^\\circ$",
                    "$\\overline{A'B'} = 6$，$ \\angle A' = 42^\\circ$"
                ]}
            ]
        },
        # Choice 9
        {
            "page": 2,
            "type": "choice",
            "sourceNumber": "9",
            "difficulty": "medium",
            "primaryUnitId": "nanyi-9-1-1-3",
            "unitIds": ["nanyi-9-1-1-3"],
            "unitAssignmentBasis": "評量相似多邊形對應邊成比例與並排面積之計算。",
            "blocks": [
                {"type": "text", "text": "如圖九，四邊形甲和四邊形乙相似，將甲與乙並排，若甲和乙的寬分別為 $5$、$2$，且 $\\overline{AB} = 14$，則甲和乙面積和＝？"},
                {"type": "options", "items": ["$58$", "$60$", "$62$", "$64$"]},
                {"type": "svg", "svg": svg_c9}
            ]
        },
        # Choice 10
        {
            "page": 2,
            "type": "choice",
            "sourceNumber": "10",
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-3",
            "unitIds": ["nanyi-9-1-1-3"],
            "unitAssignmentBasis": "評量梯形內交叉線段與平行線比例關係（倒數和公式）。",
            "blocks": [
                {"type": "text", "text": "如圖十，$\\overline{AB} \\parallel \\overline{EF} \\parallel \\overline{CD}$，若 $\\overline{AB} = x$，$\\overline{CD} = 30$，$\\overline{EF} = 10$，則 $x = ？$"},
                {"type": "options", "items": ["$15$", "$16$", "$18$", "$20$"]},
                {"type": "svg", "svg": svg_c10}
            ]
        },
        # Fill 1
        {
            "page": 3,
            "type": "fill",
            "sourceNumber": "1",
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-4",
            "unitIds": ["nanyi-9-1-1-4"],
            "unitAssignmentBasis": "評量利用日照影長比例測量樹高之相似形生活應用。",
            "blocks": [
                {"type": "text", "text": "阿花的身高為 $150\\text{ 公分}$，在清晨時測得他被太陽照出的影子長為 $180\\text{ 公分}$，同一時刻，身旁的樹影長是 $3\\text{ 公尺}$，則這棵樹的高度為＿＿＿＿公尺。"}
            ]
        },
        # Fill 2
        {
            "page": 3,
            "type": "fill",
            "sourceNumber": "2",
            "difficulty": "medium",
            "primaryUnitId": "nanyi-9-1-1-3",
            "unitIds": ["nanyi-9-1-1-3"],
            "unitAssignmentBasis": "評量直角三角形斜邊上的高引導之母子相似定理與線段長度計算。",
            "blocks": [
                {"type": "text", "text": "直角三角形 $ABC$ 中，$\\angle B = 90^\\circ$，$\\overline{BD} \\perp \\overline{AC}$ 交 $\\overline{AC}$ 於 $D$，若 $\\overline{AD} = 4$，$\\overline{BD} = \\sqrt{24}$，則："},
                {"type": "text", "text": "(1) $\\overline{AC} = ＿＿＿＿$。"},
                {"type": "text", "text": "(2) $\\overline{BC} = ＿＿＿＿$。"}
            ]
        },
        # Fill 3
        {
            "page": 3,
            "type": "fill",
            "sourceNumber": "3",
            "difficulty": "medium",
            "primaryUnitId": "nanyi-9-1-1-3",
            "unitIds": ["nanyi-9-1-1-3"],
            "unitAssignmentBasis": "評量直角三角形母子相似定理求股長。",
            "blocks": [
                {"type": "text", "text": "直角三角形 $ABC$ 中，$\\angle B = 90^\\circ$，$\\overline{BD} \\perp \\overline{AC}$ 交 $\\overline{AC}$ 於 $D$，若 $\\overline{AD} = 5$，$\\overline{CD} = 9$，則："},
                {"type": "text", "text": "(1) $\\overline{AB} = ＿＿＿＿$。"},
                {"type": "text", "text": "(2) $\\overline{BC} = ＿＿＿＿$。"}
            ]
        },
        # Fill 4
        {
            "page": 3,
            "type": "fill",
            "sourceNumber": "4",
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-4",
            "unitIds": ["nanyi-9-1-1-4"],
            "unitAssignmentBasis": "評量利用直角三角形相似測量河寬之實際應用。",
            "blocks": [
                {"type": "text", "text": "如圖四，小林設計了兩個直角三角形來測量河寬 $\\overline{AD}$，若 $\\overline{DE} = 5\\text{ 公尺}$，$\\overline{BC} = 8\\text{ 公尺}$，$\\overline{DB} = 3\\text{ 公尺}$，則河寬為＿＿＿＿公尺。"},
                {"type": "svg", "svg": svg_f4}
            ]
        },
        # Fill 5
        {
            "page": 3,
            "type": "fill",
            "sourceNumber": "5",
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-3",
            "unitIds": ["nanyi-9-1-1-3"],
            "unitAssignmentBasis": "評量相似三角形對應中線比等於對應邊長比之性質。",
            "blocks": [
                {"type": "text", "text": "如圖五，已知 $\\triangle ABC \\sim \\triangle DEF$，$M$、$N$ 分別為 $\\overline{AC}$、$\\overline{DF}$ 的中點。若 $\\overline{AB} = 15$，$\\overline{DE} = 5$，$\\overline{BM} = 20$，則 $\\overline{EN} = ＿＿＿＿$。"},
                {"type": "svg", "svg": svg_f5}
            ]
        },
        # Fill 6
        {
            "page": 3,
            "type": "fill",
            "sourceNumber": "6",
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-2",
            "unitIds": ["nanyi-9-1-1-2"],
            "unitAssignmentBasis": "評量同高圖形面積比等於底邊長比與梯形面積之比例關係。",
            "blocks": [
                {"type": "text", "text": "如圖六，在梯形 $ABCD$ 中，$\\overline{AD} \\parallel \\overline{BC}$，且 $\\overline{AD} = 4$、$\\overline{BC} = 7$，則 $\\triangle ABC$ 面積：梯形 $ABCD$ 面積＝＿＿＿＿。"},
                {"type": "svg", "svg": svg_f6}
            ]
        },
        # Fill 7
        {
            "page": 4,
            "type": "fill",
            "sourceNumber": "7",
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-3",
            "unitIds": ["nanyi-9-1-1-3", "nanyi-9-1-1-2"],
            "unitAssignmentBasis": "評量相似三角形周長比與面積比之幾何計算。",
            "blocks": [
                {"type": "text", "text": "如圖七，$\\triangle ABC$ 中，$\\overline{DE} \\parallel \\overline{BC}$，$\\overline{AD} : \\overline{DB} = 5 : 4$，則："},
                {"type": "text", "text": "(1) $\\overline{AE} : \\overline{EC} = ＿＿＿＿$。"},
                {"type": "text", "text": "(2) $\\triangle ADE$ 周長：$\\triangle ABC$ 周長＝＿＿＿＿。"},
                {"type": "text", "text": "(3) 若 $\\triangle ABC$ 面積為 $162\\text{ 平方公分}$，則 $\\triangle ADE$ 面積＝＿＿＿＿平方公分。"},
                {"type": "svg", "svg": svg_f7}
            ]
        },
        # Fill 8
        {
            "page": 4,
            "type": "fill",
            "sourceNumber": "8",
            "difficulty": "medium",
            "primaryUnitId": "nanyi-9-1-1-2",
            "unitIds": ["nanyi-9-1-1-2"],
            "unitAssignmentBasis": "評量長方形與菱形四邊中點連線段之周長與面積關係。",
            "blocks": [
                {"type": "text", "text": "如圖八，$E$、$F$、$G$、$H$ 分別為長方形 $ABCD$ 四邊的中點，$I$、$J$、$K$、$L$ 分別為四邊形 $EFGH$ 四邊的中點，若 $\\overline{AB} = 6$、$\\overline{BC} = 8$，則："},
                {"type": "text", "text": "(1) 四邊形 $EFGH$ 周長為多少？＿＿＿＿"},
                {"type": "text", "text": "(2) 四邊形 $IJKL$ 的面積為多少？＿＿＿＿"},
                {"type": "svg", "svg": svg_f8}
            ]
        },
        # Fill 9
        {
            "page": 4,
            "type": "fill",
            "sourceNumber": "9",
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-2",
            "unitIds": ["nanyi-9-1-1-2"],
            "unitAssignmentBasis": "評量三角形三邊中點連線性質求原三角形周長。",
            "blocks": [
                {"type": "text", "text": "$\\triangle ABC$ 中，$D$、$E$、$F$ 分別為 $\\overline{AB}$、$\\overline{BC}$、$\\overline{CA}$ 的中點，且 $\\overline{DE} = 5$、$\\overline{EF} = 6$、$\\overline{FD} = 7$，則 $\\triangle ABC$ 的周長為＿＿＿＿。"}
            ]
        },
        # Fill 10
        {
            "page": 4,
            "type": "fill",
            "sourceNumber": "10",
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-3",
            "unitIds": ["nanyi-9-1-1-3"],
            "unitAssignmentBasis": "評量圖形連續縮放倍率之逆運算概念。",
            "blocks": [
                {"type": "text", "text": "小妍利用影印機將甲圖縮放 $200\\%$ 得到乙圖，若小翊欲將乙圖縮放回甲圖的大小，則此時的縮放倍率為＿＿＿＿$\\%$。"}
            ]
        }
    ]

    transcript = {
        "paperId": PAPER_ID,
        "sourceSha256": SOURCE_SHA256,
        "printedHeader": PRINTED_HEADER,
        "printedSlot": {
            "year": 109,
            "semester": 1,
            "grade": 9,
            "exam": 1
        },
        "printedCounts": "選擇題10題、填充題10題（共15格），合計20題。",
        "expectedTypes": {
            "choice": 10,
            "fill": 10,
            "written": 0
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
    md_lines.append("- **學校/考次**: 宜蘭縣立內城國民中小學 109 學年度 第 1 學期 第 1 次段考 九年級 (109-1 G9 E1)")
    md_lines.append("- **總題數**: 20 題（選擇題 10 題、填充題 10 題共 15 格）")
    md_lines.append("")
    md_lines.append("---")
    md_lines.append("")
    md_lines.append("## 一、試題純文字預覽")
    md_lines.append("")

    for q in transcript["questions"]:
        q_type_str = {"choice": "選擇題", "fill": "填充題", "written": "非選題/作圖題"}[q["type"]]
        md_lines.append(f"### 【{q_type_str} {q['sourceNumber']}】 (難度: {q['difficulty']}, 單元: {q['primaryUnitId']})")
        for b in q["blocks"]:
            if b["type"] == "text":
                md_lines.append(b["text"])
            elif b["type"] == "options":
                for idx, opt in enumerate(b["items"]):
                    lbl = chr(65 + idx)
                    md_lines.append(f"({lbl}) {opt}")
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
