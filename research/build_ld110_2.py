# -*- coding: utf-8 -*-
"""
Builder for ld-110-1-2-9 (羅東國中 110-1 G9 E2)
22 items (20 fill items + 2 written)
All pure-vector SVGs conforming to strict standard.
"""
import json
import hashlib
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
paper_id = "ld-110-1-2-9"
pdf_path = ROOT / f"public/papers/{paper_id}.pdf"
pdf_sha256 = hashlib.sha256(pdf_path.read_bytes()).hexdigest()

font_attr = 'font-family="\'TW-Kai\', \'BiauKai\', \'DFKai-SB\', serif" font-size="14" font-style="italic"'
caption_font = 'font-family="\'TW-Kai\', \'BiauKai\', \'DFKai-SB\', serif" font-size="12"'

def clean_svg(svg: str) -> str:
    return ' '.join(svg.strip().split())

# 圖一: 相似三角形 ABC 與 A'B'C' 及其高
svg_fig1 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 140" width="260" height="130">
  <polygon points="50,25 20,105 85,105" fill="none" stroke="#222" stroke-width="2"/>
  <line x1="50" y1="25" x2="50" y2="105" stroke="#222" stroke-width="1.5"/>
  <rect x="42" y="97" width="8" height="8" fill="none" stroke="#222" stroke-width="1"/>
  <text x="46" y="20" {font_attr} fill="#222">A</text>
  <text x="8" y="112" {font_attr} fill="#222">B</text>
  <text x="90" y="112" {font_attr} fill="#222">C</text>
  <text x="46" y="120" {font_attr} fill="#222">D</text>

  <polygon points="190,15 140,115 250,115" fill="none" stroke="#222" stroke-width="2"/>
  <line x1="190" y1="15" x2="190" y2="115" stroke="#222" stroke-width="1.5"/>
  <rect x="180" y="105" width="10" height="10" fill="none" stroke="#222" stroke-width="1.2"/>
  <text x="185" y="10" {font_attr} fill="#222">A'</text>
  <text x="124" y="122" {font_attr} fill="#222">B'</text>
  <text x="255" y="122" {font_attr} fill="#222">C'</text>
  <text x="185" y="130" {font_attr} fill="#222">D'</text>
  <text x="135" y="136" {caption_font} text-anchor="middle" fill="#222">圖一</text>
</svg>''')

# 圖二: 同心圓與圓心角 50 度
svg_fig2 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="150" height="150">
  <circle cx="80" cy="80" r="60" fill="none" stroke="#222" stroke-width="2"/>
  <circle cx="80" cy="80" r="36" fill="none" stroke="#222" stroke-width="1.5"/>
  <line x1="80" y1="80" x2="140" y2="80" stroke="#222" stroke-width="1.5"/>
  <line x1="80" y1="80" x2="118.6" y2="34" stroke="#222" stroke-width="1.5"/>
  <circle cx="80" cy="80" r="2.5" fill="#222"/>
  <text x="68" y="85" {font_attr} fill="#222">O</text>
  <text x="144" y="84" {font_attr} fill="#222">B</text>
  <text x="114" y="84" {font_attr} fill="#222">D</text>
  <text x="122" y="32" {font_attr} fill="#222">A</text>
  <text x="100" y="48" {font_attr} fill="#222">C</text>
  <text x="80" y="152" {caption_font} text-anchor="middle" fill="#222">圖二</text>
</svg>''')

# 圖三: 梯子與地面 65 度
svg_fig3 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="150" height="150">
  <line x1="20" y1="135" x2="140" y2="135" stroke="#222" stroke-width="2"/>
  <line x1="125" y1="135" x2="125" y2="15" stroke="#222" stroke-width="2"/>
  <rect x="115" y="125" width="10" height="10" fill="none" stroke="#222" stroke-width="1.2"/>
  <!-- Ladder -->
  <line x1="60" y1="135" x2="125" y2="20" stroke="#8c5825" stroke-width="4"/>
  <text x="68" y="130" {caption_font} fill="#222">65°</text>
  <text x="80" y="152" {caption_font} text-anchor="middle" fill="#222">圖三</text>
</svg>''')

# 圖四: 鏡子反射樹高
svg_fig4 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 160" width="220" height="146">
  <line x1="20" y1="135" x2="220" y2="135" stroke="#222" stroke-width="2"/>
  <!-- Boy at D(45, 135), Eye at E(45, 90) -->
  <circle cx="45" cy="85" r="4" fill="#333"/>
  <line x1="45" y1="89" x2="45" y2="135" stroke="#333" stroke-width="1.5"/>
  <!-- Mirror at C(85, 135) -->
  <rect x="80" y="134" width="10" height="3" fill="#0077b6"/>
  <!-- Tree at B(185, 135), Top at A(185, 30) -->
  <line x1="185" y1="30" x2="185" y2="135" stroke="#222" stroke-width="2"/>
  <circle cx="185" cy="45" r="18" fill="#588157"/>
  <!-- Light rays -->
  <line x1="45" y1="90" x2="85" y2="135" stroke="#e63946" stroke-width="1.5" stroke-dasharray="3,2"/>
  <line x1="85" y1="135" x2="185" y2="30" stroke="#e63946" stroke-width="1.5" stroke-dasharray="3,2"/>
  <text x="42" y="148" {font_attr} fill="#222">D</text>
  <text x="82" y="148" {font_attr} fill="#222">C</text>
  <text x="182" y="148" {font_attr} fill="#222">B</text>
  <text x="182" y="24" {font_attr} fill="#222">A</text>
  <text x="40" y="80" {font_attr} fill="#222">E</text>
  <text x="120" y="154" {caption_font} text-anchor="middle" fill="#222">圖四</text>
</svg>''')

# 圖五: 水桶等腰梯形剖面
svg_fig5 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 160" width="180" height="144">
  <polygon points="40,30 160,30 140,120 60,120" fill="none" stroke="#222" stroke-width="2"/>
  <!-- Water line at height 24 from bottom (h=90, 24/36*90 = 60 up -> y = 60) -->
  <line x1="47" y1="60" x2="153" y2="60" stroke="#0077b6" stroke-width="2" stroke-dasharray="4,2"/>
  <text x="36" y="65" {font_attr} fill="#222">A</text>
  <text x="156" y="65" {font_attr} fill="#222">B</text>
  <text x="96" y="24" {caption_font} fill="#222">36</text>
  <text x="96" y="132" {caption_font} fill="#222">24</text>
  <text x="162" y="95" {caption_font} fill="#222">24</text>
  <text x="15" y="80" {caption_font} fill="#222">36</text>
  <text x="100" y="152" {caption_font} text-anchor="middle" fill="#222">圖五</text>
</svg>''')

# 圖六: 圓 O 與切線 PA, PB
svg_fig6 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 160" width="200" height="145">
  <circle cx="80" cy="80" r="50" fill="none" stroke="#222" stroke-width="2"/>
  <circle cx="80" cy="80" r="2.5" fill="#222"/>
  <line x1="180" y1="80" x2="98" y2="34" stroke="#222" stroke-width="1.8"/>
  <line x1="180" y1="80" x2="98" y2="126" stroke="#222" stroke-width="1.8"/>
  <line x1="98" y1="34" x2="98" y2="126" stroke="#222" stroke-width="1.5"/>
  <line x1="30" y1="80" x2="180" y2="80" stroke="#222" stroke-width="1.5"/>
  <text x="70" y="75" {font_attr} fill="#222">O</text>
  <text x="96" y="26" {font_attr} fill="#222">A</text>
  <text x="96" y="140" {font_attr} fill="#222">B</text>
  <text x="185" y="84" {font_attr} fill="#222">P</text>
  <text x="104" y="75" {font_attr} fill="#222">M</text>
  <text x="110" y="154" {caption_font} text-anchor="middle" fill="#222">圖六</text>
</svg>''')

# 圖七: 圓直徑 AB 與垂線 OD
svg_fig7 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="150" height="150">
  <circle cx="80" cy="80" r="60" fill="none" stroke="#222" stroke-width="2"/>
  <line x1="20" y1="80" x2="140" y2="80" stroke="#222" stroke-width="2"/>
  <line x1="20" y1="80" x2="95" y2="23" stroke="#222" stroke-width="1.8"/>
  <line x1="80" y1="80" x2="57.5" y2="51.5" stroke="#222" stroke-width="1.5"/>
  <rect x="58" y="46" width="7" height="7" transform="rotate(37 58 46)" fill="none" stroke="#222" stroke-width="1"/>
  <circle cx="80" cy="80" r="2.5" fill="#222"/>
  <text x="8" y="84" {font_attr} fill="#222">B</text>
  <text x="144" y="84" {font_attr} fill="#222">A</text>
  <text x="96" y="18" {font_attr} fill="#222">C</text>
  <text x="76" y="96" {font_attr} fill="#222">O</text>
  <text x="46" y="48" {font_attr} fill="#222">D</text>
  <text x="80" y="154" {caption_font} text-anchor="middle" fill="#222">圖七</text>
</svg>''')

# 圖八: 扇形 60度 與弓形灰色區域
svg_fig8 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="150" height="150">
  <path d="M 40,120 L 40,30 A 90,90 0 0,1 118,75 Z" fill="none" stroke="#222" stroke-width="1.5"/>
  <!-- Shaded circular segment: chord from (40, 30) to (118, 75) -->
  <path d="M 40,30 A 90,90 0 0,1 118,75 L 40,30 Z" fill="#b0c4de" stroke="#222" stroke-width="1.5"/>
  <line x1="40" y1="120" x2="40" y2="30" stroke="#222" stroke-width="2"/>
  <line x1="40" y1="120" x2="118" y2="75" stroke="#222" stroke-width="2"/>
  <text x="44" y="112" {caption_font} fill="#222">60°</text>
  <text x="75" y="110" {caption_font} fill="#222">10</text>
  <text x="80" y="154" {caption_font} text-anchor="middle" fill="#222">圖八</text>
</svg>''')

# 圖九: 同心弧 AB 與 CD
svg_fig9 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 180" width="160" height="160">
  <path d="M 30,50 A 100,100 0 0,1 150,50" fill="none" stroke="#222" stroke-width="2"/>
  <path d="M 50,85 A 60,60 0 0,1 130,85" fill="none" stroke="#222" stroke-width="2"/>
  <line x1="90" y1="145" x2="30" y2="50" stroke="#222" stroke-width="1.5"/>
  <line x1="90" y1="145" x2="150" y2="50" stroke="#222" stroke-width="1.5"/>
  <circle cx="90" cy="145" r="2.5" fill="#222"/>
  <text x="86" y="160" {font_attr} fill="#222">O</text>
  <text x="18" y="52" {font_attr} fill="#222">A</text>
  <text x="154" y="52" {font_attr} fill="#222">B</text>
  <text x="38" y="88" {font_attr} fill="#222">C</text>
  <text x="134" y="88" {font_attr} fill="#222">D</text>
  <text x="90" y="174" {caption_font} text-anchor="middle" fill="#222">圖九</text>
</svg>''')

# 圖十: 圓內接四邊形與外角割線交點 P
svg_fig10 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 160" width="180" height="144">
  <circle cx="70" cy="75" r="50" fill="none" stroke="#222" stroke-width="2"/>
  <polygon points="40,115 110,95 95,35 48,38" fill="none" stroke="#222" stroke-width="1.8"/>
  <line x1="40" y1="115" x2="175" y2="70" stroke="#222" stroke-width="1.5"/>
  <line x1="48" y1="38" x2="175" y2="70" stroke="#222" stroke-width="1.5"/>
  <text x="32" y="125" {font_attr} fill="#222">A</text>
  <text x="114" y="105" {font_attr} fill="#222">B</text>
  <text x="100" y="32" {font_attr} fill="#222">C</text>
  <text x="42" y="32" {font_attr} fill="#222">D</text>
  <text x="182" y="74" {font_attr} fill="#222">P</text>
  <text x="100" y="152" {caption_font} text-anchor="middle" fill="#222">圖十</text>
</svg>''')

# 圖十一: 兩圓交於 A, B 及割線 CBD
svg_fig11 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 160" width="220" height="146">
  <circle cx="75" cy="80" r="45" fill="none" stroke="#222" stroke-width="1.8"/>
  <circle cx="155" cy="80" r="55" fill="none" stroke="#222" stroke-width="1.8"/>
  <line x1="40" y1="115" x2="205" y2="75" stroke="#222" stroke-width="1.8"/>
  <line x1="110" y1="52" x2="40" y2="115" stroke="#222" stroke-width="1.5"/>
  <line x1="110" y1="52" x2="205" y2="75" stroke="#222" stroke-width="1.5"/>
  <line x1="110" y1="52" x2="110" y2="100" stroke="#222" stroke-width="1.5"/>
  <text x="106" y="44" {font_attr} fill="#222">A</text>
  <text x="112" y="112" {font_attr} fill="#222">B</text>
  <text x="28" y="125" {font_attr} fill="#222">C</text>
  <text x="210" y="78" {font_attr} fill="#222">D</text>
  <text x="120" y="154" {caption_font} text-anchor="middle" fill="#222">圖十一</text>
</svg>''')

# 圖十二: 三角形剪紙與平行四邊形 DEFG
svg_fig12 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 140" width="160" height="124">
  <polygon points="90,20 25,105 155,105" fill="none" stroke="#222" stroke-width="2"/>
  <line x1="57.5" y1="62.5" x2="122.5" y2="62.5" stroke="#222" stroke-width="1.5" stroke-dasharray="4,2"/>
  <line x1="57.5" y1="62.5" x2="42" y2="105" stroke="#222" stroke-width="1.5" stroke-dasharray="4,2"/>
  <line x1="122.5" y1="62.5" x2="90" y2="105" stroke="#222" stroke-width="1.5" stroke-dasharray="4,2"/>
  <text x="86" y="15" {font_attr} fill="#222">A</text>
  <text x="46" y="60" {font_attr} fill="#222">D</text>
  <text x="126" y="60" {font_attr} fill="#222">E</text>
  <text x="92" y="116" {font_attr} fill="#222">F</text>
  <text x="38" y="116" {font_attr} fill="#222">G</text>
  <text x="160" y="112" {font_attr} fill="#222">C</text>
  <text x="90" y="134" {caption_font} text-anchor="middle" fill="#222">圖十二</text>
</svg>''')

# 圖十三: 平行四邊形 ABCD 與對角延伸相交
svg_fig13 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 150" width="220" height="137">
  <!-- ABCD: A(65,30), D(185,30), C(165,110), B(45,110) -->
  <polygon points="65,30 185,30 165,110 45,110" fill="none" stroke="#222" stroke-width="2"/>
  <!-- Line GH through BC extended -->
  <line x1="15" y1="110" x2="225" y2="110" stroke="#222" stroke-width="1.8"/>
  <!-- Lines DG and AH meeting at O -->
  <line x1="185" y1="30" x2="20" y2="110" stroke="#222" stroke-width="1.8"/>
  <line x1="65" y1="30" x2="205" y2="110" stroke="#222" stroke-width="1.8"/>
  <text x="56" y="24" {font_attr} fill="#222">A</text>
  <text x="188" y="24" {font_attr} fill="#222">D</text>
  <text x="35" y="122" {font_attr} fill="#222">B</text>
  <text x="165" y="122" {font_attr} fill="#222">C</text>
  <text x="10" y="122" {font_attr} fill="#222">G</text>
  <text x="210" y="122" {font_attr} fill="#222">H</text>
  <text x="122" y="60" {font_attr} fill="#222">O</text>
  <text x="38" y="72" {font_attr} fill="#222">E</text>
  <text x="180" y="72" {font_attr} fill="#222">F</text>
  <text x="120" y="142" {caption_font} text-anchor="middle" fill="#222">圖十三</text>
</svg>''')

# 圖十四: 直角三角形與扇形相切內接矩形灰色區域
svg_fig14 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 180" width="160" height="160">
  <polygon points="35,145 155,145 35,25" fill="none" stroke="#222" stroke-width="2"/>
  <rect x="35" y="135" width="10" height="10" fill="none" stroke="#222" stroke-width="1.2"/>
  <!-- Quarter circle from B(35,145) with r=72 (tangent to AC) -->
  <path d="M 35,73 A 72,72 0 0,1 107,145 L 35,145 Z" fill="#b0c4de" stroke="#222" stroke-width="1.5"/>
  <rect x="35" y="99" width="43" height="46" fill="#fff" stroke="#222" stroke-width="1.5"/>
  <text x="24" y="25" {font_attr} fill="#222">C</text>
  <text x="24" y="152" {font_attr} fill="#222">B</text>
  <text x="160" y="152" {font_attr} fill="#222">A</text>
  <text x="24" y="75" {font_attr} fill="#222">E</text>
  <text x="108" y="152" {font_attr} fill="#222">F</text>
  <text x="82" y="95" {font_attr} fill="#222">D</text>
  <text x="24" y="102" {font_attr} fill="#222">G</text>
  <text x="76" y="152" {font_attr} fill="#222">H</text>
  <text x="90" y="172" {caption_font} text-anchor="middle" fill="#222">圖十四</text>
</svg>''')

# 圖十五: 坐標系切線與圓心 R(4,3)
svg_fig15 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 180" width="180" height="162">
  <line x1="20" y1="140" x2="185" y2="140" stroke="#222" stroke-width="1.5"/>
  <line x1="45" y1="160" x2="45" y2="20" stroke="#222" stroke-width="1.5"/>
  <polygon points="185,140 177,136 177,144" fill="#222"/>
  <polygon points="45,20 41,28 49,28" fill="#222"/>
  <!-- R=(125, 65) [x=4, y=3], r=45 -->
  <circle cx="125" cy="65" r="45" fill="none" stroke="#222" stroke-width="1.8"/>
  <circle cx="125" cy="65" r="2.5" fill="#222"/>
  <!-- Tangent PB from B(125, 140) to circle -->
  <line x1="45" y1="140" x2="125" y2="65" stroke="#222" stroke-width="1.5"/>
  <line x1="125" y1="65" x2="125" y2="140" stroke="#222" stroke-width="1.5"/>
  <line x1="125" y1="140" x2="95" y2="92" stroke="#222" stroke-width="1.8"/>
  <text x="32" y="148" {font_attr} fill="#222">O</text>
  <text x="132" y="65" {font_attr} fill="#222">R</text>
  <text x="128" y="152" {font_attr} fill="#222">B</text>
  <text x="84" y="92" {font_attr} fill="#222">P</text>
  <text x="128" y="115" {font_attr} fill="#222">A</text>
  <text x="100" y="174" {caption_font} text-anchor="middle" fill="#222">圖十五</text>
</svg>''')

# 圖十六: 圓 O 與直徑 AE 及垂線 AD
svg_fig16 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 180" width="160" height="160">
  <circle cx="90" cy="90" r="65" fill="none" stroke="#222" stroke-width="2"/>
  <line x1="90" y1="25" x2="90" y2="155" stroke="#222" stroke-width="2"/>
  <polygon points="90,25 35,115 145,85" fill="none" stroke="#222" stroke-width="1.8"/>
  <line x1="90" y1="25" x2="115" y2="93" stroke="#222" stroke-width="1.5"/>
  <rect x="111" y="87" width="8" height="8" transform="rotate(-15 111 87)" fill="none" stroke="#222" stroke-width="1"/>
  <circle cx="90" cy="90" r="2.5" fill="#222"/>
  <text x="86" y="18" {font_attr} fill="#222">A</text>
  <text x="86" y="170" {font_attr} fill="#222">E</text>
  <text x="22" y="122" {font_attr} fill="#222">B</text>
  <text x="152" y="88" {font_attr} fill="#222">C</text>
  <text x="96" y="92" {font_attr} fill="#222">O</text>
  <text x="116" y="108" {font_attr} fill="#222">D</text>
  <text x="90" y="175" {caption_font} text-anchor="middle" fill="#222">圖十六</text>
</svg>''')

# 計算題 1 圖: 圓內接四邊形與外角交點 P, Q
svg_written1 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 180" width="200" height="164">
  <circle cx="90" cy="95" r="50" fill="none" stroke="#222" stroke-width="2"/>
  <polygon points="45,95 110,55 125,110 95,138" fill="none" stroke="#222" stroke-width="1.8"/>
  <line x1="45" y1="95" x2="190" y2="35" stroke="#222" stroke-width="1.5"/>
  <line x1="95" y1="138" x2="190" y2="35" stroke="#222" stroke-width="1.5"/>
  <line x1="45" y1="95" x2="135" y2="165" stroke="#222" stroke-width="1.5"/>
  <line x1="110" y1="55" x2="135" y2="165" stroke="#222" stroke-width="1.5"/>
  <text x="32" y="98" {font_attr} fill="#222">A</text>
  <text x="106" y="48" {font_attr} fill="#222">D</text>
  <text x="130" y="112" {font_attr} fill="#222">C</text>
  <text x="85" y="146" {font_attr} fill="#222">B</text>
  <text x="195" y="38" {font_attr} fill="#222">P</text>
  <text x="136" y="176" {font_attr} fill="#222">Q</text>
</svg>''')

# 計算題 2 圖: 圓 O 外一點 P 作切線尺規作圖
svg_written2 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 160" width="180" height="144">
  <circle cx="130" cy="90" r="45" fill="none" stroke="#222" stroke-width="2"/>
  <circle cx="130" cy="90" r="2.5" fill="#222"/>
  <circle cx="45" cy="90" r="2.5" fill="#222"/>
  <text x="136" y="94" {font_attr} fill="#222">O</text>
  <text x="32" y="94" {font_attr} fill="#222">P</text>
</svg>''')

questions = [
    {
        "type": "fill",
        "sourceNumber": "一-1(1)",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-1-3",
        "unitIds": ["nanyi-9-1-1-3"],
        "unitAssignmentBasis": "相似三角形對應高之比等於對應邊長之比。",
        "blocks": [
            {"type": "text", "text": "如圖一，$\\triangle ABC \\sim \\triangle A'B'C'$，$A$、$B$、$C$ 的對應點分別是 $A'$、$B'$、$C'$，$\\overline{AD} \\perp \\overline{BC}$ 於 $D$ 點，$\\overline{A'D'} \\perp \\overline{B'C'}$ 於 $D'$ 點，若 $\\overline{AD} : \\overline{A'D'} = 3 : 5$，求(1) $\\overline{AB} : \\overline{A'B'} =$ ______。"},
            {"type": "svg", "svg": svg_fig1}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-1(2)",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-1-3",
        "unitIds": ["nanyi-9-1-1-3"],
        "unitAssignmentBasis": "相似三角形面積比等於對應邊長平方比。",
        "blocks": [
            {"type": "text", "text": "如圖一，$\\triangle ABC \\sim \\triangle A'B'C'$，$A$、$B$、$C$ 的對應點分別是 $A'$、$B'$、$C'$，$\\overline{AD} \\perp \\overline{BC}$ 於 $D$ 點，$\\overline{A'D'} \\perp \\overline{B'C'}$ 於 $D'$ 點，若 $\\overline{AD} : \\overline{A'D'} = 3 : 5$，求(2) $\\triangle ABC : \\triangle A'B'C' =$ ______。（面積比）"},
            {"type": "svg", "svg": svg_fig1}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-2",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-2-1",
        "unitIds": ["nanyi-9-1-2-1"],
        "unitAssignmentBasis": "點與圓心距離小於半徑判斷點在圓內。",
        "blocks": [
            {"type": "text", "text": "已知圓 $O$ 的半徑為 $6$，$D$ 點與此圓心 $O$ 的距離為 $5$，判別 $D$ 點與圓 $O$ 的位置關係______。（填入圓內、圓上或圓外）"}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-3",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-2-1",
        "unitIds": ["nanyi-9-1-2-1"],
        "unitAssignmentBasis": "直線到圓心距離等於半徑為切線。",
        "blocks": [
            {"type": "text", "text": "已知圓 $O$ 的直徑為 $10$，圓心 $O$ 到三條直線 $L_1$、$L_2$、$L_3$ 的距離分別為 $3$、$5$、$7$，試問這三條直線中，切線為何？______。"}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-4",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-2-2",
        "unitIds": ["nanyi-9-1-2-2"],
        "unitAssignmentBasis": "同圓心角所對同心弧度數相同。",
        "blocks": [
            {"type": "text", "text": "如圖二，兩同心圓中，大圓的半徑為 $5$，小圓的半徑為 $3$，$\\angle AOB = 50^\\circ$，求 $\\widehat{AB}$ 的度數 : $\\widehat{CD}$ 的度數 $=$ ______。"},
            {"type": "svg", "svg": svg_fig2}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-5",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-1-4",
        "unitIds": ["nanyi-9-1-1-4"],
        "unitAssignmentBasis": "直角三角形銳角正切值定義計算。",
        "blocks": [
            {"type": "text", "text": "直角 $\\triangle ABC$ 中，若 $\\overline{AB} = 13$、$\\overline{BC} = 5$、$\\overline{AC} = 12$，試問 $\\tan A =$ ______。"}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-6",
        "page": 1,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-1-4",
        "unitIds": ["nanyi-9-1-1-4"],
        "unitAssignmentBasis": "三角比餘弦值實際應用測量距離。",
        "blocks": [
            {"type": "text", "text": "如圖三，一座梯子長度為 $2$ 公尺，工人在施工時將梯子靠著牆面置放。若梯子與地面的夾角為 $65^\\circ$，求梯子底部與牆面的距離 $=$ ______。（$\\sin 65^\\circ \\fallingdotseq 0.91, \\cos 65^\\circ \\fallingdotseq 0.42, \\tan 65^\\circ \\fallingdotseq 2.14$）"},
            {"type": "svg", "svg": svg_fig3}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-7",
        "page": 1,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-1-4",
        "unitIds": ["nanyi-9-1-1-4"],
        "unitAssignmentBasis": "光線反射相似三角形測量樹高。",
        "blocks": [
            {"type": "text", "text": "如圖四，小懿在地上放了一面鏡子，透過鏡子的反射（入射角等於反射角），他可以看見樹梢。已知小懿與鏡子的距離是 $1.4$ 公尺，鏡子與樹的距離是 $5$ 公尺，小懿眼睛離地面的高度是 $1.6$ 公尺，求樹高 $=$ ______。"},
            {"type": "svg", "svg": svg_fig4}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-8",
        "page": 1,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-1-2",
        "unitIds": ["nanyi-9-1-1-2"],
        "unitAssignmentBasis": "梯形截比例線段求水面寬度。",
        "blocks": [
            {"type": "text", "text": "如圖五，有一個水桶，其剖面為等腰梯形，下底為 $24$ 公分，上底為 $36$ 公分，水桶高為 $36$ 公分，打掃時，威利在水桶內裝了 $24$ 公分高的水，此時水面的寬為______公分。"},
            {"type": "svg", "svg": svg_fig5}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-9",
        "page": 1,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-2-1",
        "unitIds": ["nanyi-9-1-2-1"],
        "unitAssignmentBasis": "圓外切線長與直角三角形斜邊高計算弦長。",
        "blocks": [
            {"type": "text", "text": "如圖六，$\\overline{PA}$、$\\overline{PB}$ 切圓 $O$ 於 $A$、$B$ 兩點，$\\overline{OP}$ 與 $\\overline{AB}$ 交於 $M$ 點，若圓 $O$ 半徑為 $10$，$\\overline{OP} = 26$，求 $\\overline{AB} =$ ______。"},
            {"type": "svg", "svg": svg_fig6}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-10",
        "page": 1,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-2-1",
        "unitIds": ["nanyi-9-1-2-1"],
        "unitAssignmentBasis": "弦心距平分弦與畢氏定理求三角形面積。",
        "blocks": [
            {"type": "text", "text": "如圖七，$\\overline{AB}$ 為圓 $O$ 的直徑，$\\overline{BC}$ 為圓 $O$ 的一弦，自 $O$ 點作 $\\overline{BC}$ 的垂線，交 $\\overline{BC}$ 於 $D$ 點。若 $\\overline{AB} = 20$，$\\overline{BC} = 18$，求 $\\triangle OBD$ 的面積 $=$ ______。"},
            {"type": "svg", "svg": svg_fig7}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-11",
        "page": 1,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-2-2",
        "unitIds": ["nanyi-9-1-2-2"],
        "unitAssignmentBasis": "扇形面積減正三角形面積計算弓形面積。",
        "blocks": [
            {"type": "text", "text": "如圖八，已知扇形的半徑為 $10$ 公分，圓心角為 $60^\\circ$，則斜線區域面積為______平方公分。"},
            {"type": "svg", "svg": svg_fig8}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-12",
        "page": 1,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-2-2",
        "unitIds": ["nanyi-9-1-2-2"],
        "unitAssignmentBasis": "圓心角相同之同心弧長與半徑成正比關係。",
        "blocks": [
            {"type": "text", "text": "如圖九，已知 $\\widehat{AB}$ 和 $\\widehat{CD}$ 是以 $O$ 點為圓心，不同半徑所畫出的兩個弧，且 $\\widehat{AB} = 12$，$\\widehat{CD} = 8$，$\\overline{OA} = 8$，求 $\\overline{OC} =$ ______。"},
            {"type": "svg", "svg": svg_fig9}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-13",
        "page": 2,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-2-2",
        "unitIds": ["nanyi-9-1-2-2"],
        "unitAssignmentBasis": "圓內接四邊形外角等於內對角性質。",
        "blocks": [
            {"type": "text", "text": "如圖十，四邊形 $ABCD$ 為圓內接四邊形，$\\overline{AB}$、$\\overline{CD}$ 交於 $P$ 點，若 $\\angle P = 50^\\circ$，$\\angle ABC = 110^\\circ$，求 $\\angle A =$ ______度。"},
            {"type": "svg", "svg": svg_fig10}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-14",
        "page": 2,
        "difficulty": "hard",
        "primaryUnitId": "nanyi-9-1-2-2",
        "unitIds": ["nanyi-9-1-2-2"],
        "unitAssignmentBasis": "兩圓相交割線共線之圓周角與弧度數綜合推算。",
        "blocks": [
            {"type": "text", "text": "如圖十一，兩圓交於 $A$、$B$ 兩點。若 $C$、$B$、$D$ 三點共線，且 $\\widehat{BC} = 90^\\circ$，$\\angle C = 30^\\circ$，求 $\\widehat{ABD}$ 的度數 $=$ ______度。"},
            {"type": "svg", "svg": svg_fig11}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-15",
        "page": 2,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-1-3",
        "unitIds": ["nanyi-9-1-1-3"],
        "unitAssignmentBasis": "三角形截平行線相似三角形與平行四邊形面積比例。",
        "blocks": [
            {"type": "text", "text": "如圖十二，將一張面積為 $30$ 的大三角形紙片沿著虛線剪成三張小三角形紙片與一張平行四邊形紙片。已知 $\\overline{DE} = 6$，$\\overline{BC} = 12$，求平行四邊形 $DEFG$ 的面積 $=$ ______。"},
            {"type": "svg", "svg": svg_fig12}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-16",
        "page": 2,
        "difficulty": "hard",
        "primaryUnitId": "nanyi-9-1-1-3",
        "unitIds": ["nanyi-9-1-1-3"],
        "unitAssignmentBasis": "平行四邊形邊分比截線相似三角形面積比綜合計算。",
        "blocks": [
            {"type": "text", "text": "如圖十三，$ABCD$ 為平行四邊形，且 $\\overline{AE} : \\overline{EB} = \\overline{DF} : \\overline{FC} = 2 : 1$，求平行四邊形 $ABCD : \\triangle OGH =$ ______。（面積比）"},
            {"type": "svg", "svg": svg_fig13}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-17",
        "page": 2,
        "difficulty": "hard",
        "primaryUnitId": "nanyi-9-1-2-1",
        "unitIds": ["nanyi-9-1-2-1"],
        "unitAssignmentBasis": "扇形切斜邊與內接矩形互補區域周長計算。",
        "blocks": [
            {"type": "text", "text": "如圖十四，$\\triangle ABC$ 中，$\\angle B = 90^\\circ$，以 $B$ 為圓心，$\\overline{BE}$ 為半徑畫弧，切 $\\overline{AC}$ 於 $D$ 點，交 $\\overline{BC}$ 於 $F$ 點，$\\overline{DG}$ 平行 $\\overline{BC}$，$\\overline{DH}$ 平行 $\\overline{AB}$，若 $\\overline{AB} = 6$，$\\overline{BC} = 8$，求灰色區域的周長 $=$ ______。"},
            {"type": "svg", "svg": svg_fig14}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-18",
        "page": 2,
        "difficulty": "hard",
        "primaryUnitId": "nanyi-9-1-2-1",
        "unitIds": ["nanyi-9-1-2-1"],
        "unitAssignmentBasis": "平面坐標圓切線長度與相似直角三角形半徑求值。",
        "blocks": [
            {"type": "text", "text": "如圖十五，若 $R$ 點座標為 $(4, 3)$，$B$ 點在 $X$ 軸上，$\\overline{PB}$ 為切線，$\\overline{RB} \\perp X$ 軸，$R$ 為圓心，$P$ 為切點，$R$、$P$、$O$ 三點共線，連接 $R$ 點及 $A$ 點交 $X$ 軸於 $B$，求 $\\overline{AB} =$ ______。"},
            {"type": "svg", "svg": svg_fig15}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-19",
        "page": 2,
        "difficulty": "hard",
        "primaryUnitId": "nanyi-9-1-2-2",
        "unitIds": ["nanyi-9-1-2-2"],
        "unitAssignmentBasis": "圓外接三角形直徑直角圓周角與直角三角形正弦比求外接圓半徑。",
        "blocks": [
            {"type": "text", "text": "如圖十六，$\\triangle ABC$ 三頂點均在圓 $O$ 上，$\\overline{AE}$ 為直徑，若 $\\overline{AD} \\perp \\overline{CD}$，$\\overline{CD} : \\overline{AD} = 1 : 3$，且 $\\overline{AB} = 15$，求此圓半徑 $=$ ______。"},
            {"type": "svg", "svg": svg_fig16}
        ]
    },
    {
        "type": "written",
        "sourceNumber": "二-1",
        "page": 2,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-2-2",
        "unitIds": ["nanyi-9-1-2-2"],
        "unitAssignmentBasis": "圓內接四邊形對角互補與延長線交角計算。",
        "blocks": [
            {"type": "text", "text": "如圖，四邊形 $ABCD$ 為圓內接四邊形，若 $\\angle A = 65^\\circ$，$\\angle P = 30^\\circ$，求 $\\angle Q$。（5 分）\n【解】在 $\\triangle PAD$ 中，$\\angle PDA = 180^\\circ - 65^\\circ - 30^\\circ = 85^\\circ$。因為四邊形 $ABCD$ 為圓內接四邊形，所以對角互補，$\\angle B = 180^\\circ - 85^\\circ = 95^\\circ$，故外角 $\\angle QBC = 180^\\circ - 95^\\circ = 85^\\circ$。又外角 $\\angle QCD = \\angle A = 65^\\circ$。在 $\\triangle QBC$ 中，$\\angle Q = 180^\\circ - \\angle QBC - \\angle QCD = 180^\\circ - 85^\\circ - 65^\\circ = 30^\\circ$。答：$\\angle Q = 30^\\circ$。"},
            {"type": "svg", "svg": svg_written1}
        ]
    },
    {
        "type": "written",
        "sourceNumber": "二-2",
        "page": 2,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-2-1",
        "unitIds": ["nanyi-9-1-2-1"],
        "unitAssignmentBasis": "過圓外一點作圓切線之尺規作圖。",
        "blocks": [
            {"type": "text", "text": "如圖，$P$ 為圓 $O$ 外的一點，利用尺規作圖，畫出通過 $P$ 點且與圓 $O$ 相切的直線。（不用寫作法）（5 分）\n【作法說明】1. 連接 $\\overline{OP}$，作 $\\overline{OP}$ 的垂直平分線交 $\\overline{OP}$ 於 $M$ 點。2. 以 $M$ 為圓心，$\\overline{OM}$ 為半徑畫圓，交圓 $O$ 於 $A$、$B$ 兩點。3. 連接直線 $PA$ 或 $PB$ 即為所求之切線。"},
            {"type": "svg", "svg": svg_written2}
        ]
    }
]

# Ensure no newlines in text
for q in questions:
    for b in q['blocks']:
        if 'text' in b:
            b['text'] = b['text'].replace('\n', ' ')

doc_data = {
    "paperId": paper_id,
    "sourceSha256": pdf_sha256,
    "printedHeader": "宜蘭縣立羅東國中 110 學年度第 1 學期九年級數學科第二次段考試卷",
    "printedSlot": {
        "year": 110,
        "semester": 1,
        "grade": 9,
        "exam": 2
    },
    "printedCounts": "填充題 20 題（含第1題2小題）、計算作圖題 2 題，合計 22 題。",
    "visualReviewComplete": True,
    "reviewNote": "全卷22題（填充20小題、計算作圖2題），涵蓋相似形、圓心角弦切角、切線性質、扇形面積、弓形面積與尺規切線作圖。純向量幾何SVG全數重繪。",
    "expectedTypes": {
        "choice": 0,
        "fill": 20,
        "written": 2
    },
    "questions": questions
}

out_path = ROOT / f"research/yilan/transcribed/{paper_id}.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(doc_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Successfully written {out_path} with {len(questions)} questions")
