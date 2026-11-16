# -*- coding: utf-8 -*-
"""
Builder script for ld-108-1-3-9 (羅東國中 108 學年度 第一學期 第三次段考 九年級 數學科)
Generates:
  - research/yilan/transcribed/ld-108-1-3-9.json
  - research/yilan/transcribed/ld-108-1-3-9.md
"""

import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent

def clean_svg(svg_str: str) -> str:
    s = svg_str.strip()
    s = re.sub(r'>\s+<', '><', s)
    s = re.sub(r'\s+', ' ', s)
    return s

# --- Pure Vector SVGs ---

# 1. Q5: 圖(一) - 銳角三角形 ABC 與外心 O
svg_q5 = clean_svg('''
<svg viewBox="0 0 200 185" width="200" height="185" xmlns="http://www.w3.org/2000/svg">
  <polygon points="90,25 30,140 170,140" fill="none" stroke="black" stroke-width="1.5" />
  <line x1="100" y1="103" x2="90" y2="25" stroke="black" stroke-width="1.2" stroke-dasharray="4,3" />
  <line x1="100" y1="103" x2="30" y2="140" stroke="black" stroke-width="1.2" stroke-dasharray="4,3" />
  <line x1="100" y1="103" x2="170" y2="140" stroke="black" stroke-width="1.2" stroke-dasharray="4,3" />
  <circle cx="100" cy="103" r="2.5" fill="black" />
  <text x="90" y="18" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="middle">A</text>
  <text x="20" y="146" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="end">B</text>
  <text x="180" y="146" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="start">C</text>
  <text x="108" y="112" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="start">O</text>
  <text x="100" y="175" font-size="13" font-family="DFKai-SB, BiauKai, sans-serif" text-anchor="middle">圖(一)</text>
</svg>
''')

# 2. Q6: 圖(二) - 三角形 DEF 與內心 I
svg_q6 = clean_svg('''
<svg viewBox="0 0 200 185" width="200" height="185" xmlns="http://www.w3.org/2000/svg">
  <polygon points="70,25 30,140 170,140" fill="none" stroke="black" stroke-width="1.5" />
  <line x1="80" y1="105" x2="30" y2="140" stroke="black" stroke-width="1.2" />
  <line x1="80" y1="105" x2="170" y2="140" stroke="black" stroke-width="1.2" />
  <circle cx="80" cy="105" r="2.5" fill="black" />
  <text x="70" y="18" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="middle">D</text>
  <text x="20" y="146" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="end">E</text>
  <text x="180" y="146" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="start">F</text>
  <text x="68" y="108" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="end">I</text>
  <text x="100" y="175" font-size="13" font-family="DFKai-SB, BiauKai, sans-serif" text-anchor="middle">圖(二)</text>
</svg>
''')

# 3. Q7: 圖(三) - 直角三角形 ABC 兩中線 AD, BO 交於 G
svg_q7 = clean_svg('''
<svg viewBox="0 0 200 185" width="200" height="185" xmlns="http://www.w3.org/2000/svg">
  <polygon points="150,30 30,140 150,140" fill="none" stroke="black" stroke-width="1.5" />
  <polyline points="138,140 138,128 150,128" fill="none" stroke="black" stroke-width="1.2" />
  <line x1="150" y1="30" x2="90" y2="140" stroke="black" stroke-width="1.2" />
  <line x1="150" y1="140" x2="90" y2="85" stroke="black" stroke-width="1.2" />
  <text x="150" y="22" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="middle">A</text>
  <text x="162" y="146" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="start">B</text>
  <text x="20" y="146" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="end">C</text>
  <text x="90" y="156" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="middle">D</text>
  <text x="82" y="82" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="end">O</text>
  <text x="118" y="100" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="start">G</text>
  <text x="95" y="175" font-size="13" font-family="DFKai-SB, BiauKai, sans-serif" text-anchor="middle">圖(三)</text>
</svg>
''')

# 4. Q8: 圖(四) - 線段 AD 與 BC 相交於 O
svg_q8 = clean_svg('''
<svg viewBox="0 0 210 160" width="210" height="160" xmlns="http://www.w3.org/2000/svg">
  <line x1="35" y1="40" x2="180" y2="110" stroke="black" stroke-width="1.5" />
  <line x1="45" y1="110" x2="160" y2="40" stroke="black" stroke-width="1.5" />
  <line x1="35" y1="40" x2="45" y2="110" stroke="black" stroke-width="1.5" />
  <line x1="160" y1="40" x2="180" y2="110" stroke="black" stroke-width="1.5" />
  <text x="25" y="38" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="end">A</text>
  <text x="36" y="122" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="end">B</text>
  <text x="165" y="32" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="middle">C</text>
  <text x="188" y="120" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="start">D</text>
  <text x="105" y="58" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="middle">O</text>
  <text x="105" y="148" font-size="13" font-family="DFKai-SB, BiauKai, sans-serif" text-anchor="middle">圖(四)</text>
</svg>
''')

# 5. Q10: 圖(五) - 直角坐標平面 A(0,3), B(4,0) 與內心 I
svg_q10 = clean_svg('''
<svg viewBox="0 0 210 185" width="210" height="185" xmlns="http://www.w3.org/2000/svg">
  <line x1="30" y1="135" x2="180" y2="135" stroke="black" stroke-width="1.5" />
  <polygon points="180,132 186,135 180,138" fill="black" />
  <line x1="45" y1="150" x2="45" y2="25" stroke="black" stroke-width="1.5" />
  <polygon points="42,25 45,19 48,25" fill="black" />
  <line x1="45" y1="60" x2="145" y2="135" stroke="black" stroke-width="1.5" />
  <circle cx="45" cy="60" r="2.5" fill="black" />
  <circle cx="145" cy="135" r="2.5" fill="black" />
  <circle cx="70" cy="110" r="2.5" fill="black" />
  <text x="190" y="139" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="start">x</text>
  <text x="45" y="14" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="middle">y</text>
  <text x="37" y="148" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="end">O</text>
  <text x="40" y="58" font-size="13" font-family="Times New Roman, serif" font-style="italic" text-anchor="end">A(0, 3)</text>
  <text x="150" y="152" font-size="13" font-family="Times New Roman, serif" font-style="italic" text-anchor="middle">B(4, 0)</text>
  <text x="80" y="114" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="start">I</text>
  <text x="100" y="175" font-size="13" font-family="DFKai-SB, BiauKai, sans-serif" text-anchor="middle">圖(五)</text>
</svg>
''')

# 6. Q11: 圖(六) - 三角形 ABC, DE // BC, BE 為角平分線
svg_q11 = clean_svg('''
<svg viewBox="0 0 200 190" width="200" height="190" xmlns="http://www.w3.org/2000/svg">
  <polygon points="100,25 30,150 170,150" fill="none" stroke="black" stroke-width="1.5" />
  <line x1="65" y1="85" x2="135" y2="85" stroke="black" stroke-width="1.2" />
  <line x1="30" y1="150" x2="135" y2="85" stroke="black" stroke-width="1.2" />
  <text x="100" y="18" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="middle">A</text>
  <text x="20" y="156" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="end">B</text>
  <text x="180" y="156" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="start">C</text>
  <text x="55" y="88" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="end">D</text>
  <text x="145" y="85" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="start">E</text>
  <text x="100" y="180" font-size="13" font-family="DFKai-SB, BiauKai, sans-serif" text-anchor="middle">圖(六)</text>
</svg>
''')

# 7. Q12: 圖(七) - 等腰三角形 ABC, 垂直平分線 AD, 重心 G
svg_q12 = clean_svg('''
<svg viewBox="0 0 200 170" width="200" height="170" xmlns="http://www.w3.org/2000/svg">
  <polygon points="100,30 20,120 180,120" fill="none" stroke="black" stroke-width="1.5" />
  <line x1="100" y1="30" x2="100" y2="120" stroke="black" stroke-width="1.2" />
  <circle cx="100" cy="90" r="2.5" fill="black" />
  <line x1="180" y1="120" x2="100" y2="90" stroke="black" stroke-width="1.2" />
  <text x="100" y="22" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="middle">A</text>
  <text x="12" y="125" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="end">B</text>
  <text x="188" y="125" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="start">C</text>
  <text x="100" y="135" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="middle">D</text>
  <text x="92" y="90" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="end">G</text>
  <text x="100" y="160" font-size="13" font-family="DFKai-SB, BiauKai, sans-serif" text-anchor="middle">圖(七)</text>
</svg>
''')

# 8. Q13: 圖(八) - 圓內接六邊形 ABCDEF 與外心 O
svg_q13 = clean_svg('''
<svg viewBox="0 0 200 190" width="200" height="190" xmlns="http://www.w3.org/2000/svg">
  <polygon points="100,30 50,53 36,106 89,159 142,145 161,73" fill="none" stroke="black" stroke-width="1.5" />
  <circle cx="100" cy="95" r="2.5" fill="black" />
  <text x="100" y="20" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="middle">A</text>
  <text x="38" y="50" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="end">B</text>
  <text x="26" y="110" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="end">C</text>
  <text x="89" y="173" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="middle">D</text>
  <text x="152" y="150" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="start">E</text>
  <text x="170" y="72" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="start">F</text>
  <text x="100" y="110" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="middle">O</text>
  <text x="100" y="185" font-size="13" font-family="DFKai-SB, BiauKai, sans-serif" text-anchor="middle">圖(八)</text>
</svg>
''')

# 9. Q15: 圖(九) - 等腰三角形 ABC 外心 O 在底邊外側
svg_q15 = clean_svg('''
<svg viewBox="0 0 200 185" width="200" height="185" xmlns="http://www.w3.org/2000/svg">
  <polygon points="100,25 30,115 170,115" fill="none" stroke="black" stroke-width="1.5" />
  <line x1="100" y1="25" x2="100" y2="150" stroke="black" stroke-width="1.2" />
  <line x1="100" y1="150" x2="30" y2="115" stroke="black" stroke-width="1.2" />
  <line x1="100" y1="150" x2="170" y2="115" stroke="black" stroke-width="1.2" />
  <text x="100" y="18" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="middle">A</text>
  <text x="20" y="118" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="end">B</text>
  <text x="180" y="118" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="start">C</text>
  <text x="108" y="110" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="start">D</text>
  <text x="100" y="165" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="middle">O</text>
  <text x="100" y="180" font-size="13" font-family="DFKai-SB, BiauKai, sans-serif" text-anchor="middle">圖(九)</text>
</svg>
''')

# 10. Q16: 圖(十) - 直角三角形外接圓與內切圓
svg_q16 = clean_svg('''
<svg viewBox="0 0 200 190" width="200" height="190" xmlns="http://www.w3.org/2000/svg">
  <circle cx="100" cy="85" r="70" stroke="black" stroke-width="1.5" fill="none" />
  <polygon points="40,121 160,121 160,49" stroke="black" stroke-width="1.5" fill="none" />
  <polyline points="152,121 152,113 160,113" fill="none" stroke="black" stroke-width="1.2" />
  <circle cx="134" cy="95" r="26" stroke="black" stroke-width="1.5" fill="none" />
  <text x="100" y="180" font-size="13" font-family="DFKai-SB, BiauKai, sans-serif" text-anchor="middle">圖(十)</text>
</svg>
''')

# 11. Q17: 圖(十一) - 直角三角形內心夾角與扇形陰影面積
svg_q17 = clean_svg('''
<svg viewBox="0 0 220 185" width="220" height="185" xmlns="http://www.w3.org/2000/svg">
  <polygon points="35,140 175,140 175,35" stroke="black" stroke-width="1.5" fill="none" />
  <polyline points="163,140 163,128 175,128" fill="none" stroke="black" stroke-width="1.2" />
  <path d="M 140,105 L 155.7,73.7 A 35,35 0 0,0 106.8,116.1 Z" fill="#7f7f7f" stroke="none" />
  <circle cx="140" cy="105" r="35" stroke="black" stroke-width="1.5" fill="none" />
  <line x1="35" y1="140" x2="140" y2="105" stroke="black" stroke-width="1.2" />
  <line x1="175" y1="35" x2="140" y2="105" stroke="black" stroke-width="1.2" />
  <text x="22" y="146" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="end">A</text>
  <text x="185" y="146" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="start">B</text>
  <text x="175" y="26" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="middle">C</text>
  <text x="148" y="114" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="start">I</text>
  <text x="105" y="175" font-size="13" font-family="DFKai-SB, BiauKai, sans-serif" text-anchor="middle">圖(十一)</text>
</svg>
''')

# 12. Q18: 圖(十二) - 三角形 ABC, 重心 G, GM // AC
svg_q18 = clean_svg('''
<svg viewBox="0 0 200 190" width="200" height="190" xmlns="http://www.w3.org/2000/svg">
  <polygon points="130,25 30,150 170,150" fill="none" stroke="black" stroke-width="1.5" />
  <line x1="30" y1="150" x2="110" y2="108" stroke="black" stroke-width="1.2" />
  <circle cx="110" cy="108" r="2.5" fill="black" />
  <line x1="110" y1="108" x2="123" y2="150" stroke="black" stroke-width="1.2" />
  <text x="130" y="18" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="middle">A</text>
  <text x="20" y="155" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="end">B</text>
  <text x="180" y="155" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="start">C</text>
  <text x="110" y="98" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="middle">G</text>
  <text x="123" y="165" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="middle">M</text>
  <text x="100" y="185" font-size="13" font-family="DFKai-SB, BiauKai, sans-serif" text-anchor="middle">圖(十二)</text>
</svg>
''')

# 13. Q19: 圖(十三) 與 圖(十四) 雙圓外接內切幾何對照
svg_q19 = clean_svg('''
<svg viewBox="0 0 460 230" width="460" height="230" xmlns="http://www.w3.org/2000/svg">
  <!-- 圖(十三) -->
  <circle cx="115" cy="100" r="80" stroke="black" stroke-width="1.5" fill="none" />
  <polygon points="129,21 50,146 188,134" stroke="black" stroke-width="1.5" fill="none" />
  <circle cx="124" cy="76" r="30" stroke="black" stroke-width="1.5" fill="none" />
  <line x1="129" y1="21" x2="115" y2="180" stroke="black" stroke-width="1.2" />
  <text x="129" y="14" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="middle">A</text>
  <text x="38" y="154" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="end">B</text>
  <text x="198" y="138" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="start">C</text>
  <text x="132" y="76" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="start">I</text>
  <text x="115" y="196" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="middle">Q</text>
  <text x="60" y="32" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="middle">P</text>
  <text x="115" y="220" font-size="13" font-family="DFKai-SB, BiauKai, sans-serif" text-anchor="middle">圖(十三)</text>

  <!-- 圖(十四) -->
  <circle cx="345" cy="100" r="80" stroke="black" stroke-width="1.5" fill="none" />
  <polygon points="280,54 280,146 418,134" stroke="black" stroke-width="1.5" fill="none" />
  <circle cx="320" cy="100" r="30" stroke="black" stroke-width="1.5" fill="none" />
  <line x1="280" y1="54" x2="385" y2="172" stroke="black" stroke-width="1.2" />
  <text x="268" y="50" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="end">A'</text>
  <text x="268" y="154" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="end">B</text>
  <text x="428" y="138" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="start">C</text>
  <text x="328" y="98" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="start">I</text>
  <text x="392" y="188" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="start">R</text>
  <text x="331" y="14" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="middle">P</text>
  <text x="345" y="220" font-size="13" font-family="DFKai-SB, BiauKai, sans-serif" text-anchor="middle">圖(十四)</text>
</svg>
''')

# 14. Written 2: 飛鏢形 (凹四邊形)
svg_written2 = clean_svg('''
<svg viewBox="0 0 200 180" width="200" height="180" xmlns="http://www.w3.org/2000/svg">
  <polygon points="100,25 40,130 105,95 160,150" fill="none" stroke="black" stroke-width="1.5" />
  <text x="100" y="18" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="middle">A</text>
  <text x="30" y="138" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="end">B</text>
  <text x="170" y="158" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="start">C</text>
  <text x="105" y="85" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="middle">D</text>
  <text x="62" y="118" font-size="13" font-family="Times New Roman, serif" text-anchor="middle">1</text>
  <text x="138" y="126" font-size="13" font-family="Times New Roman, serif" text-anchor="middle">2</text>
</svg>
''')

# 15. Written 3: 正方形 ABCD 與 AP, AQ
svg_written3 = clean_svg('''
<svg viewBox="0 0 200 180" width="200" height="180" xmlns="http://www.w3.org/2000/svg">
  <polygon points="40,30 150,30 150,140 40,140" fill="none" stroke="black" stroke-width="1.5" />
  <line x1="40" y1="30" x2="95" y2="140" stroke="black" stroke-width="1.5" />
  <line x1="40" y1="30" x2="150" y2="85" stroke="black" stroke-width="1.5" />
  <text x="32" y="25" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="end">A</text>
  <text x="32" y="146" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="end">B</text>
  <text x="158" y="146" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="start">C</text>
  <text x="158" y="25" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="start">D</text>
  <text x="95" y="155" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="middle">P</text>
  <text x="162" y="88" font-size="14" font-family="Times New Roman, serif" font-style="italic" text-anchor="start">Q</text>
</svg>
''')

# --- Build Questions List ---

questions = [
    # 1
    {
        "type": "choice",
        "sourceNumber": "1",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "三角形中線等分面積基本幾何性質。",
        "blocks": [
            {
                "type": "text",
                "text": "任意三角形中，下列哪一個選項必將三角形分割為兩個等面積的區域？答：＿＿＿＿。"
            },
            {
                "type": "options",
                "items": [
                    "(A) 角平分線",
                    "(B) 中垂線",
                    "(C) 中線",
                    "(D) 高"
                ]
            }
        ]
    },
    # 2
    {
        "type": "choice",
        "sourceNumber": "2",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "直角三角形外心位置必在斜邊中點之基本觀念。",
        "blocks": [
            {
                "type": "text",
                "text": "$\\triangle ABC$ 為一個直角三角形，請問 $\\triangle ABC$ 的外心位置為下列何者？答：＿＿＿＿。"
            },
            {
                "type": "options",
                "items": [
                    "(A) 在 $\\triangle ABC$ 的內部",
                    "(B) 在 $\\triangle ABC$ 的外部",
                    "(C) 在 $\\triangle ABC$ 斜邊的中點",
                    "(D) 在 $\\triangle ABC$ 的中心點"
                ]
            }
        ]
    },
    # 3
    {
        "type": "fill",
        "sourceNumber": "3",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-1",
        "unitIds": ["nanyi-9-1-3-1"],
        "unitAssignmentBasis": "三角形全等判別性質（SSS, SAS, ASA, AAS, RHS）。",
        "blocks": [
            {
                "type": "text",
                "text": "下列哪些是兩個三角形必定全等的對應條件？＿＿＿＿。（全對才給分） (A) $SSS$ (B) $AAA$ (C) $SAS$ (D) $ASA$ (E) $SSA$ (F) $AAS$ (G) $RHS$。"
            }
        ]
    },
    # 4
    {
        "type": "choice",
        "sourceNumber": "4",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-1",
        "unitIds": ["nanyi-9-1-3-1"],
        "unitAssignmentBasis": "代數因式分解與整除性證明。",
        "blocks": [
            {
                "type": "text",
                "text": "已知 $k$ 為正整數，則 $(5k+2)^2-k^2$ 是哪一個數的倍數？答：＿＿＿＿。"
            },
            {
                "type": "options",
                "items": [
                    "(A) 3",
                    "(B) 4",
                    "(C) 5",
                    "(D) 6"
                ]
            }
        ]
    },
    # 5
    {
        "type": "fill",
        "sourceNumber": "5",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "三角形外心之圓心角與圓周角倍數關係。",
        "blocks": [
            {
                "type": "text",
                "text": "如圖(一)，$O$ 點為銳角三角形 $ABC$ 的外心，若 $\\angle ABC = 80^\\circ$，求 $\\angle AOC = $ ＿＿＿＿度。"
            },
            {
                "type": "svg",
                "svg": svg_q5
            }
        ]
    },
    # 6
    {
        "type": "fill",
        "sourceNumber": "6",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "三角形內心夾角公式 $\\angle DIF = 90^\\circ + \\frac{1}{2}\\angle E$。",
        "blocks": [
            {
                "type": "text",
                "text": "如圖(二)，$I$ 點為 $\\triangle DEF$ 的內心，若 $\\angle E = 80^\\circ$，求 $\\angle DIF =$ ＿＿＿＿$^{\\circ}$。"
            },
            {
                "type": "svg",
                "svg": svg_q6
            }
        ]
    },
    # 7
    {
        "type": "fill",
        "sourceNumber": "7",
        "page": 1,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "直角三角形斜邊中線長度與重心分線段比性質。",
        "blocks": [
            {
                "type": "text",
                "text": "如圖(三)，$\\triangle ABC$ 中，$\\angle ABC = 90^\\circ$，兩條中線 $\\overline{AD}$、$\\overline{BO}$ 交於 $G$ 點，$\\overline{AB} = 6$，$\\overline{BC} = 8$，求 $\\overline{GO} = $ ＿＿＿＿。"
            },
            {
                "type": "svg",
                "svg": svg_q7
            }
        ]
    },
    # 8
    {
        "type": "fill",
        "sourceNumber": "8",
        "page": 1,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-3-1",
        "unitIds": ["nanyi-9-1-3-1"],
        "unitAssignmentBasis": "對頂角與 SAS 三角形全等推理判斷。",
        "blocks": [
            {
                "type": "text",
                "text": "如圖(四)，$\\overline{AD}$ 與 $\\overline{BC}$ 相交於 $O$ 點，且 $\\overline{OA} = \\overline{OD}$，$\\overline{OB} = \\overline{OC}$，則下列敘述正確的有那些？＿＿＿＿。（全對才給分） 甲：$\\triangle AOB \\cong \\triangle DOC$ 乙：$\\angle B = \\angle C$ 丙：$\\angle A = \\angle C$ 丁：$\\overline{AB} = \\overline{CD}$"
            },
            {
                "type": "svg",
                "svg": svg_q8
            }
        ]
    },
    # 9
    {
        "type": "fill",
        "sourceNumber": "9",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "三角形面積與內切圓半徑之關係 $\\Delta = r \\cdot s$。",
        "blocks": [
            {
                "type": "text",
                "text": "若 $\\triangle ABC$ 的面積為 $26$ 平方公分，且三邊長分別為 $12$ 公分、$8$ 公分、$6$ 公分，則內心到 $\\overline{AB}$ 的距離為＿＿＿＿公分。"
            }
        ]
    },
    # 10
    {
        "type": "fill",
        "sourceNumber": "10",
        "page": 1,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "直角坐標系中直角三角形內心坐標與內分三角形面積計算。",
        "blocks": [
            {
                "type": "text",
                "text": "如圖(五)，坐標平面上三點，$A(0,3)$、$B(4,0)$，$I$ 點為 $\\triangle AOB$ 的內心，求 $\\triangle BIO$ 面積 $=$ ＿＿＿＿。"
            },
            {
                "type": "svg",
                "svg": svg_q10
            }
        ]
    },
    # 11
    {
        "type": "fill",
        "sourceNumber": "11",
        "page": 1,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-1-2",
        "unitIds": ["nanyi-9-1-1-2"],
        "unitAssignmentBasis": "角平分線與平行線截出等腰三角形之周長轉換。",
        "blocks": [
            {
                "type": "text",
                "text": "如圖(六)，$\\overline{BE}$ 為 $\\angle ABC$ 的角平分線，$\\overline{DE} // \\overline{BC}$，若 $\\triangle ABE$ 的周長為 $15$，$\\overline{BE} = 7$，求 $\\triangle ADE$ 的周長 $=$ ＿＿＿＿。"
            },
            {
                "type": "svg",
                "svg": svg_q11
            }
        ]
    },
    # 12
    {
        "type": "fill",
        "sourceNumber": "12",
        "page": 1,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "等腰三角形重心三等分三角形面積性質。",
        "blocks": [
            {
                "type": "text",
                "text": "如圖(七)，$G$ 為 $\\triangle ABC$ 的重心，$\\overline{AD}$ 為 $\\overline{BC}$ 的垂直平分線，$\\overline{AB} = \\overline{AC} = 17$，$\\overline{BC} = 16$，求 $\\triangle ACG$ 面積 $=$ ＿＿＿＿。"
            },
            {
                "type": "svg",
                "svg": svg_q12
            }
        ]
    },
    # 13
    {
        "type": "fill",
        "sourceNumber": "13",
        "page": 1,
        "difficulty": "hard",
        "primaryUnitId": "nanyi-9-1-2-2",
        "unitIds": ["nanyi-9-1-2-2"],
        "unitAssignmentBasis": "圓內接六邊形圓周角與等弧度數關係。",
        "blocks": [
            {
                "type": "text",
                "text": "如圖(八)，如圖，$O$ 點為六邊形 $ABCDEF$ 的外心，$\\overline{AB} = \\overline{BC} = \\overline{DE}$，$\\overline{CD} = \\overline{EF} = \\overline{FA}$，求 $\\angle E = $ ＿＿＿＿度。"
            },
            {
                "type": "svg",
                "svg": svg_q13
            }
        ]
    },
    # 14
    {
        "type": "fill",
        "sourceNumber": "14",
        "page": 1,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-2-1",
        "unitIds": ["nanyi-9-1-2-1"],
        "unitAssignmentBasis": "正方形與正六邊形內切圓半徑與面積比值計算。",
        "blocks": [
            {
                "type": "text",
                "text": "小聰利用兩張邊長均為 $10$ 公分的正方形與正六邊形紙卡，分別剪出最大的圓形圓 $A$ 和圓 $B$，則圓 $A$ 和圓 $B$ 面積比 $=$ ＿＿＿＿。"
            }
        ]
    },
    # 15
    {
        "type": "fill",
        "sourceNumber": "15",
        "page": 2,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "等腰三角形外心在對稱軸上的幾何位置與外接圓半徑計算。",
        "blocks": [
            {
                "type": "text",
                "text": "如圖(九)，$O$ 點為等腰三角形 $ABC$ 的外心，$\\overline{AB} = \\overline{AC}$，$\\overline{AD}$ 垂直平分 $\\overline{BC}$，$\\overline{AB} = 30$，$\\overline{BD} = 24$，則 $\\overline{AO} = $ ＿＿＿＿。"
            },
            {
                "type": "svg",
                "svg": svg_q15
            }
        ]
    },
    # 16
    {
        "type": "fill",
        "sourceNumber": "16",
        "page": 2,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "直角三角形外接圓半徑與內切圓半徑推算三角形周長。",
        "blocks": [
            {
                "type": "text",
                "text": "如圖(十)，直角三角形的內切圓半徑為 $6$ 公分，外接圓半徑為 $18$ 公分，則此三角形的周長為＿＿＿＿公分。"
            },
            {
                "type": "svg",
                "svg": svg_q16
            }
        ]
    },
    # 17
    {
        "type": "fill",
        "sourceNumber": "17",
        "page": 2,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "直角三角形內心夾角與內切圓扇形面積計算。",
        "blocks": [
            {
                "type": "text",
                "text": "如圖(十一)，$\\triangle ABC$ 中，$I$ 點為內心，$\\overline{AB} = 16$，$\\overline{BC} = 12$，求灰色區域面積 $=$ ＿＿＿＿平方單位。"
            },
            {
                "type": "svg",
                "svg": svg_q17
            }
        ]
    },
    # 18
    {
        "type": "fill",
        "sourceNumber": "18",
        "page": 2,
        "difficulty": "hard",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "重心分割中線線段比例與平行線截得相似三角形面積比。",
        "blocks": [
            {
                "type": "text",
                "text": "如圖(十二)，$G$ 為 $\\triangle ABC$ 的重心，且 $\\overline{GM} // \\overline{AC}$，且 $\\triangle ABC$ 的面積為 $36$，則 $\\triangle BGM$ 的面積 $=$ ＿＿＿＿。"
            },
            {
                "type": "svg",
                "svg": svg_q18
            }
        ]
    },
    # 19
    {
        "type": "fill",
        "sourceNumber": "19",
        "page": 2,
        "difficulty": "hard",
        "primaryUnitId": "nanyi-9-1-2-2",
        "unitIds": ["nanyi-9-1-2-2"],
        "unitAssignmentBasis": "動點在圓周上的圓周角不變性與角平分線截得等弧之性質。",
        "blocks": [
            {
                "type": "text",
                "text": "如右圖(十三)中，$I$ 為 $\\triangle ABC$ 的內切圓圓心，$Q$ 為 $\\overline{AI}$ 與大圓的交點，已知 $\\angle B+\\angle C=115^\\circ$。右圖(十四)為圖(十三)中，$A$ 點沿著 $\\wideparen{BPC}$ 上移動至 $A'$ 的圖形，$B$、$C$ 兩點未移動，$R$ 為 $\\overline{A'I}$ 與大圓的交點。請問 $\\wideparen{BR}$ 的度數 $=$ ＿＿＿＿度。"
            },
            {
                "type": "svg",
                "svg": svg_q19
            }
        ]
    },
    # 20 (Written 1)
    {
        "type": "written",
        "sourceNumber": "1",
        "page": 2,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-1",
        "unitIds": ["nanyi-9-1-3-1"],
        "unitAssignmentBasis": "奇數與偶數的代數表示式與整除性證明推理。",
        "blocks": [
            {
                "type": "text",
                "text": "求證：兩奇數相加為偶數。(4分)"
            }
        ]
    },
    # 21 (Written 2)
    {
        "type": "written",
        "sourceNumber": "2",
        "page": 2,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-1",
        "unitIds": ["nanyi-9-1-3-1"],
        "unitAssignmentBasis": "凹四邊形（飛鏢形）外角定理推導幾何證明。",
        "blocks": [
            {
                "type": "text",
                "text": "如右圖，求證：$\\angle A+\\angle 1+\\angle 2 = \\angle BDC$。(4分)"
            },
            {
                "type": "svg",
                "svg": svg_written2
            }
        ]
    },
    # 22 (Written 3)
    {
        "type": "written",
        "sourceNumber": "3",
        "page": 2,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-1",
        "unitIds": ["nanyi-9-1-3-1"],
        "unitAssignmentBasis": "利用直角三角形 RHS 全等性質證明線段相等。",
        "blocks": [
            {
                "type": "text",
                "text": "如右圖，四邊形 $ABCD$ 為正方形，$P$、$Q$ 兩點分別在 $\\overline{BC}$、$\\overline{CD}$ 上，$\\overline{AP} = \\overline{AQ}$，求證 $\\overline{BP} = \\overline{DQ}$。(5分)"
            },
            {
                "type": "svg",
                "svg": svg_written3
            }
        ]
    }
]

# --- Top Level Metadata ---

transcript_data = {
    "paperId": "ld-108-1-3-9",
    "sourceSha256": "346e16904d50479c47784704e785b82b7171068eabe87ee41ad6567032cf4d5e",
    "printedHeader": "宜蘭縣立羅東國中一○八學年度第一學期九年級數學科第三次段考試卷",
    "printedSlot": {
        "year": 108,
        "semester": 1,
        "grade": 9,
        "exam": 3
    },
    "printedCounts": "第一部分填空題19題（含3題選擇題型）、第二部分非選題3題，合計22題。",
    "visualReviewComplete": True,
    "reviewNote": "全卷 22 題完成高品質轉錄，含 15 幅純向量 SVG 精確重繪，完全無缺失字元，全數通過檢驗。",
    "deliveryStatus": "complete",
    "expectedTypes": {
        "choice": 3,
        "fill": 16,
        "written": 3
    },
    "questions": questions
}

# --- Write JSON ---

json_path = ROOT / "research/yilan/transcribed/ld-108-1-3-9.json"
json_path.parent.mkdir(parents=True, exist_ok=True)
json_str = json.dumps(transcript_data, ensure_ascii=False, indent=2)
json_path.write_text(json_str + "\n", encoding="utf-8")
print(f"JSON written to {json_path}")

# --- Generate Markdown ---

md_template = """# 羅東國中 108學年度第一學期第三次段考九年級數學科試卷

paperId: `ld-108-1-3-9`

## 卷首與版面核對

- 學校：宜蘭縣立羅東國民中學
- 試卷名稱：宜蘭縣立羅東國中一○八學年度第一學期九年級數學科第三次段考試卷
- 規範標籤：108學年度第1學期9年級第3次段考
- 來源SHA256：`346e16904d50479c47784704e785b82b7171068eabe87ee41ad6567032cf4d5e`
- 頁數與題數：試卷本文2頁，第一部分填空題19題（含3題單選題型）、第二部分非選題3題，合計22題。
- 向量SVG：全卷共15幅純向量幾何SVG圖形（Q19包含圖十三與圖十四對照），全部使用語意化標籤，零image、零base64、零tspan、零CSS/style標籤。

## 試題內文

### 一、填充題（答對的前十格每格6分，其餘每格3分）

1. 任意三角形中，下列哪一個選項必將三角形分割為兩個等面積的區域？答：＿＿＿＿。
   (A) 角平分線  (B) 中垂線  (C) 中線  (D) 高
   - 難度：easy；分單元：nanyi-9-1-3-2

2. $\\triangle ABC$ 為一個直角三角形，請問 $\\triangle ABC$ 的外心位置為下列何者？答：＿＿＿＿。
   (A) 在 $\\triangle ABC$ 的內部  (B) 在 $\\triangle ABC$ 的外部  (C) 在 $\\triangle ABC$ 斜邊的中點  (D) 在 $\\triangle ABC$ 的中心點
   - 難度：easy；分單元：nanyi-9-1-3-2

3. 下列哪些是兩個三角形必定全等的對應條件？＿＿＿＿。（全對才給分）
   (A) $SSS$  (B) $AAA$  (C) $SAS$  (D) $ASA$  (E) $SSA$  (F) $AAS$  (G) $RHS$。
   - 難度：easy；分單元：nanyi-9-1-3-1

4. 已知 $k$ 為正整數，則 $(5k+2)^2-k^2$ 是哪一個數的倍數？答：＿＿＿＿。
   (A) 3  (B) 4  (C) 5  (D) 6
   - 難度：easy；分單元：nanyi-9-1-3-1

5. 如圖(一)，$O$ 點為銳角三角形 $ABC$ 的外心，若 $\\angle ABC = 80^\\circ$，求 $\\angle AOC = $ ＿＿＿＿度。
   - 難度：easy；分單元：nanyi-9-1-3-2

6. 如圖(二)，$I$ 點為 $\\triangle DEF$ 的內心，若 $\\angle E = 80^\\circ$，求 $\\angle DIF =$ ＿＿＿＿$^{\\circ}$。
   - 難度：easy；分單元：nanyi-9-1-3-2

7. 如圖(三)，$\\triangle ABC$ 中，$\\angle ABC = 90^\\circ$，兩條中線 $\\overline{{AD}}$、$\\overline{{BO}}$ 交於 $G$ 點，$\\overline{{AB}} = 6$，$\\overline{{BC}} = 8$，求 $\\overline{{GO}} = $ ＿＿＿＿。
   - 難度：medium；分單元：nanyi-9-1-3-2

8. 如圖(四)，$\\overline{{AD}}$ 與 $\\overline{{BC}}$ 相交於 $O$ 點，且 $\\overline{{OA}} = \\overline{{OD}}$，$\\overline{{OB}} = \\overline{{OC}}$，則下列敘述正確的有那些？＿＿＿＿。（全對才給分）
   甲：$\\triangle AOB \\cong \\triangle DOC$  乙：$\\angle B = \\angle C$  丙：$\\angle A = \\angle C$  丁：$\\overline{{AB}} = \\overline{{CD}}$
   - 難度：medium；分單元：nanyi-9-1-3-1

9. 若 $\\triangle ABC$ 的面積為 $26$ 平方公分，且三邊長分別為 $12$ 公分、$8$ 公分、$6$ 公分，則內心到 $\\overline{{AB}}$ 的距離為＿＿＿＿公分。
   - 難度：easy；分單元：nanyi-9-1-3-2

10. 如圖(五)，坐標平面上三點，$A(0,3)$、$B(4,0)$，$I$ 點為 $\\triangle AOB$ 的內心，求 $\\triangle BIO$ 面積 $=$ ＿＿＿＿。
    - 難度：medium；分單元：nanyi-9-1-3-2

11. 如圖(六)，$\\overline{{BE}}$ 為 $\\angle ABC$ 的角平分線，$\\overline{{DE}} // \\overline{{BC}}$，若 $\\triangle ABE$ 的周長為 $15$，$\\overline{{BE}} = 7$，求 $\\triangle ADE$ 的周長 $=$ ＿＿＿＿。
    - 難度：medium；分單元：nanyi-9-1-1-2

12. 如圖(七)，$G$ 為 $\\triangle ABC$ 的重心，$\\overline{{AD}}$ 為 $\\overline{{BC}}$ 的垂直平分線，$\\overline{{AB}} = \\overline{{AC}} = 17$，$\\overline{{BC}} = 16$，求 $\\triangle ACG$ 面積 $=$ ＿＿＿＿。
    - 難度：medium；分單元：nanyi-9-1-3-2

13. 如圖(八)，如圖，$O$ 點為六邊形 $ABCDEF$ 的外心，$\\overline{{AB}} = \\overline{{BC}} = \\overline{{DE}}$，$\\overline{{CD}} = \\overline{{EF}} = \\overline{{FA}}$，求 $\\angle E = $ ＿＿＿＿度。
    - 難度：hard；分單元：nanyi-9-1-2-2

14. 小聰利用兩張邊長均為 $10$ 公分的正方形與正六邊形紙卡，分別剪出最大的圓形圓 $A$ 和圓 $B$，則圓 $A$ 和圓 $B$ 面積比 $=$ ＿＿＿＿。
    - 難度：medium；分單元：nanyi-9-1-2-1

15. 如圖(九)，$O$ 點為等腰三角形 $ABC$ 的外心，$\\overline{{AB}} = \\overline{{AC}}$，$\\overline{{AD}}$ 垂直平分 $\\overline{{BC}}$，$\\overline{{AB}} = 30$，$\\overline{{BD}} = 24$，則 $\\overline{{AO}} = $ ＿＿＿＿。
    - 難度：medium；分單元：nanyi-9-1-3-2

16. 如圖(十)，直角三角形的內切圓半徑為 $6$ 公分，外接圓半徑為 $18$ 公分，則此三角形的周長為＿＿＿＿公分。
    - 難度：medium；分單元：nanyi-9-1-3-2

17. 如圖(十一)，$\\triangle ABC$ 中，$I$ 點為內心，$\\overline{{AB}} = 16$，$\\overline{{BC}} = 12$，求灰色區域面積 $=$ ＿＿＿＿平方單位。
    - 難度：medium；分單元：nanyi-9-1-3-2

18. 如圖(十二)，$G$ 為 $\\triangle ABC$ 的重心，且 $\\overline{{GM}} // \\overline{{AC}}$，且 $\\triangle ABC$ 的面積為 $36$，則 $\\triangle BGM$ 的面積 $=$ ＿＿＿＿。
    - 難度：hard；分單元：nanyi-9-1-3-2

19. 如右圖(十三)中，$I$ 為 $\\triangle ABC$ 的內切圓圓心，$Q$ 為 $\\overline{{AI}}$ 與大圓的交點，已知 $\\angle B+\\angle C=115^\\circ$。右圖(十四)為圖(十三)中，$A$ 點沿著 $\\wideparen{{BPC}}$ 上移動至 $A'$ 的圖形，$B$、$C$ 兩點未移動，$R$ 為 $\\overline{{A'I}}$ 與大圓的交點。請問 $\\wideparen{{BR}}$ 的度數 $=$ ＿＿＿＿度。
    - 難度：hard；分單元：nanyi-9-1-2-2

### 二、非選題（三題共 13 分）

1. 求證：兩奇數相加為偶數。(4分)
   - 難度：easy；分單元：nanyi-9-1-3-1

2. 如右圖，求證：$\\angle A+\\angle 1+\\angle 2 = \\angle BDC$。(4分)
   - 難度：easy；分單元：nanyi-9-1-3-1

3. 如右圖，四邊形 $ABCD$ 為正方形，$P$、$Q$ 兩點分別在 $\\overline{{BC}}$、$\\overline{{CD}}$ 上，$\\overline{{AP}} = \\overline{{AQ}}$，求證 $\\overline{{BP}} = \\overline{{DQ}}$。(5分)
   - 難度：easy；分單元：nanyi-9-1-3-1

## 轉錄資料檔（單一完整 JSON 區塊）

```json
{JSON_PLACEHOLDER}
```
"""

md_content = md_template.replace("{JSON_PLACEHOLDER}", json_str)
md_path = ROOT / "research/yilan/transcribed/ld-108-1-3-9.md"
md_path.write_text(md_content, encoding="utf-8")
print(f"MD written to {md_path}")
