# -*- coding: utf-8 -*-
"""
Builder for ld-110-1-3-9 (羅東國中 110-1 G9 E3)
22 questions (20 fill + 2 written proofs)
All pure-vector SVGs conforming to strict standard.
"""
import json
import hashlib
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
paper_id = "ld-110-1-3-9"
pdf_path = ROOT / f"public/papers/{paper_id}.pdf"
pdf_sha256 = hashlib.sha256(pdf_path.read_bytes()).hexdigest()

font_attr = 'font-family="\'TW-Kai\', \'BiauKai\', \'DFKai-SB\', serif" font-size="14" font-style="italic"'
caption_font = 'font-family="\'TW-Kai\', \'BiauKai\', \'DFKai-SB\', serif" font-size="12"'

def clean_svg(svg: str) -> str:
    return ' '.join(svg.strip().split())

# 圖(一): 長方形 ABCD 與中點四邊形 EFGH (菱形)
svg_fig1 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 130" width="180" height="117">
  <rect x="30" y="25" width="140" height="75" fill="none" stroke="#222" stroke-width="2"/>
  <polygon points="100,25 170,62.5 100,100 30,62.5" fill="#fdf0ed" stroke="#222" stroke-width="1.8"/>
  <text x="20" y="22" {font_attr} fill="#222">A</text>
  <text x="96" y="20" {font_attr} fill="#222">E</text>
  <text x="174" y="22" {font_attr} fill="#222">D</text>
  <text x="176" y="66" {font_attr} fill="#222">H</text>
  <text x="174" y="112" {font_attr} fill="#222">C</text>
  <text x="96" y="114" {font_attr} fill="#222">G</text>
  <text x="20" y="112" {font_attr} fill="#222">B</text>
  <text x="16" y="66" {font_attr} fill="#222">F</text>
  <text x="100" y="125" {caption_font} text-anchor="middle" fill="#222">圖(一)</text>
</svg>''')

# 圖(二): 三角形 ABC 與外心 O
svg_fig2 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 140" width="150" height="131">
  <polygon points="80,20 25,105 135,105" fill="none" stroke="#222" stroke-width="2"/>
  <line x1="25" y1="105" x2="80" y2="75" stroke="#222" stroke-width="1.5"/>
  <line x1="135" y1="105" x2="80" y2="75" stroke="#222" stroke-width="1.5"/>
  <circle cx="80" cy="75" r="2.5" fill="#222"/>
  <text x="76" y="15" {font_attr} fill="#222">A</text>
  <text x="12" y="112" {font_attr} fill="#222">B</text>
  <text x="140" y="112" {font_attr} fill="#222">C</text>
  <text x="76" y="70" {font_attr} fill="#222">O</text>
  <text x="80" y="130" {caption_font} text-anchor="middle" fill="#222">圖(二)</text>
</svg>''')

# 圖(三): 三角形 ABC 與內心 I
svg_fig3 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 140" width="150" height="131">
  <polygon points="75,20 25,105 135,105" fill="none" stroke="#222" stroke-width="2"/>
  <line x1="25" y1="105" x2="75" y2="75" stroke="#222" stroke-width="1.5"/>
  <line x1="135" y1="105" x2="75" y2="75" stroke="#222" stroke-width="1.5"/>
  <circle cx="75" cy="75" r="2.5" fill="#222"/>
  <text x="72" y="15" {font_attr} fill="#222">A</text>
  <text x="12" y="112" {font_attr} fill="#222">B</text>
  <text x="140" y="112" {font_attr} fill="#222">C</text>
  <text x="72" y="70" {font_attr} fill="#222">I</text>
  <text x="80" y="130" {caption_font} text-anchor="middle" fill="#222">圖(三)</text>
</svg>''')

# 圖(四): 三角形 ABC 與重心 G 及中線 AD
svg_fig4 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 140" width="150" height="131">
  <polygon points="80,20 25,105 135,105" fill="none" stroke="#222" stroke-width="2"/>
  <line x1="80" y1="20" x2="80" y2="105" stroke="#222" stroke-width="1.5"/>
  <circle cx="80" cy="76" r="2.5" fill="#222"/>
  <text x="76" y="15" {font_attr} fill="#222">A</text>
  <text x="12" y="112" {font_attr} fill="#222">B</text>
  <text x="140" y="112" {font_attr} fill="#222">C</text>
  <text x="76" y="118" {font_attr} fill="#222">D</text>
  <text x="86" y="78" {font_attr} fill="#222">G</text>
  <text x="80" y="132" {caption_font} text-anchor="middle" fill="#222">圖(四)</text>
</svg>''')

# 圖(五): 三角形 ABC 三中線與重心 G
svg_fig5 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 170 145" width="160" height="136">
  <polygon points="85,20 25,105 145,105" fill="none" stroke="#222" stroke-width="2"/>
  <line x1="85" y1="20" x2="85" y2="105" stroke="#222" stroke-width="1.5"/>
  <line x1="25" y1="105" x2="115" y2="62" stroke="#222" stroke-width="1.5"/>
  <line x1="145" y1="105" x2="55" y2="62" stroke="#222" stroke-width="1.5"/>
  <circle cx="85" cy="77" r="2.5" fill="#222"/>
  <text x="82" y="15" {font_attr} fill="#222">A</text>
  <text x="12" y="112" {font_attr} fill="#222">B</text>
  <text x="150" y="112" {font_attr} fill="#222">C</text>
  <text x="82" y="118" {font_attr} fill="#222">D</text>
  <text x="120" y="62" {font_attr} fill="#222">E</text>
  <text x="40" y="62" {font_attr} fill="#222">F</text>
  <text x="88" y="75" {font_attr} fill="#222">G</text>
  <text x="85" y="134" {caption_font} text-anchor="middle" fill="#222">圖(五)</text>
</svg>''')

# 圖(六): 直角三角形 ABC 與內心 I
svg_fig6 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="150" height="150">
  <polygon points="120,25 120,125 35,125" fill="none" stroke="#222" stroke-width="2"/>
  <line x1="120" y1="25" x2="90" y2="95" stroke="#222" stroke-width="1.5"/>
  <line x1="120" y1="125" x2="90" y2="95" stroke="#222" stroke-width="1.5"/>
  <line x1="35" y1="125" x2="90" y2="95" stroke="#222" stroke-width="1.5"/>
  <rect x="110" y="115" width="10" height="10" fill="none" stroke="#222" stroke-width="1.2"/>
  <circle cx="90" cy="95" r="2.5" fill="#222"/>
  <text x="120" y="18" {font_attr} fill="#222">B</text>
  <text x="125" y="132" {font_attr} fill="#222">A</text>
  <text x="22" y="132" {font_attr} fill="#222">C</text>
  <text x="82" y="96" {font_attr} fill="#222">I</text>
  <text x="80" y="148" {caption_font} text-anchor="middle" fill="#222">圖(六)</text>
</svg>''')

# 圖(七): 正方形 ABCD 與外接截線垂足 E, F
svg_fig7 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 160" width="160" height="142">
  <line x1="20" y1="125" x2="160" y2="125" stroke="#222" stroke-width="1.5"/>
  <polygon points="90,125 145,85 105,30 50,70" fill="#f5f0fa" stroke="#222" stroke-width="2"/>
  <line x1="50" y1="70" x2="50" y2="125" stroke="#222" stroke-width="1.5"/>
  <line x1="145" y1="85" x2="145" y2="125" stroke="#222" stroke-width="1.5"/>
  <rect x="50" y="115" width="10" height="10" fill="none" stroke="#222" stroke-width="1.2"/>
  <rect x="135" y="115" width="10" height="10" fill="none" stroke="#222" stroke-width="1.2"/>
  <text x="86" y="140" {font_attr} fill="#222">A</text>
  <text x="150" y="85" {font_attr} fill="#222">B</text>
  <text x="103" y="24" {font_attr} fill="#222">C</text>
  <text x="36" y="70" {font_attr} fill="#222">D</text>
  <text x="36" y="140" {font_attr} fill="#222">F</text>
  <text x="145" y="140" {font_attr} fill="#222">E</text>
  <text x="90" y="154" {caption_font} text-anchor="middle" fill="#222">圖(七)</text>
</svg>''')

# 圖(八): 等腰三角形 ABC (120度) 與內心 I、外心 O
svg_fig8 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 160" width="180" height="144">
  <polygon points="100,30 25,85 175,85" fill="none" stroke="#222" stroke-width="2"/>
  <line x1="100" y1="30" x2="100" y2="125" stroke="#222" stroke-width="1.5"/>
  <line x1="25" y1="85" x2="100" y2="60" stroke="#222" stroke-width="1.5"/>
  <line x1="25" y1="85" x2="100" y2="125" stroke="#222" stroke-width="1.5"/>
  <circle cx="100" cy="60" r="2.5" fill="#222"/>
  <circle cx="100" cy="125" r="2.5" fill="#222"/>
  <text x="96" y="24" {font_attr} fill="#222">A</text>
  <text x="12" y="90" {font_attr} fill="#222">B</text>
  <text x="180" y="90" {font_attr} fill="#222">C</text>
  <text x="106" y="62" {font_attr} fill="#222">I</text>
  <text x="106" y="130" {font_attr} fill="#222">O</text>
  <text x="100" y="150" {caption_font} text-anchor="middle" fill="#222">圖(八)</text>
</svg>''')

# 圖(九): 平行四邊形 ABCD 中點與對角線交叉
svg_fig9 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 140" width="200" height="127">
  <polygon points="50,25 190,25 160,105 20,105" fill="none" stroke="#222" stroke-width="2"/>
  <line x1="20" y1="105" x2="190" y2="25" stroke="#222" stroke-width="1.5"/>
  <line x1="50" y1="25" x2="90" y2="105" stroke="#222" stroke-width="1.5"/>
  <line x1="50" y1="25" x2="175" y2="65" stroke="#222" stroke-width="1.5"/>
  <text x="42" y="20" {font_attr} fill="#222">A</text>
  <text x="195" y="24" {font_attr} fill="#222">D</text>
  <text x="165" y="112" {font_attr} fill="#222">C</text>
  <text x="10" y="112" {font_attr} fill="#222">B</text>
  <text x="86" y="118" {font_attr} fill="#222">E</text>
  <text x="180" y="70" {font_attr} fill="#222">F</text>
  <text x="46" y="78" {font_attr} fill="#222">G</text>
  <text x="110" y="52" {font_attr} fill="#222">H</text>
  <text x="110" y="132" {caption_font} text-anchor="middle" fill="#222">圖(九)</text>
</svg>''')

# 圖(十): 直線與坐標軸交點及重心 G
svg_fig10 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 160" width="180" height="144">
  <line x1="20" y1="120" x2="180" y2="120" stroke="#222" stroke-width="1.5"/>
  <line x1="50" y1="145" x2="50" y2="20" stroke="#222" stroke-width="1.5"/>
  <polygon points="180,120 172,116 172,124" fill="#222"/>
  <polygon points="50,20 46,28 54,28" fill="#222"/>
  <text x="175" y="112" {font_attr} fill="#222">x</text>
  <text x="40" y="24" {font_attr} fill="#222">y</text>
  <line x1="25" y1="42" x2="170" y2="135" stroke="#222" stroke-width="2"/>
  <circle cx="50" cy="56" r="2.5" fill="#222"/>
  <circle cx="145" cy="120" r="2.5" fill="#222"/>
  <circle cx="82" cy="99" r="2.5" fill="#222"/>
  <text x="36" y="133" {font_attr} fill="#222">O</text>
  <text x="36" y="58" {font_attr} fill="#222">A</text>
  <text x="145" y="135" {font_attr} fill="#222">B</text>
  <text x="88" y="98" {font_attr} fill="#222">G</text>
  <text x="22" y="38" {font_attr} fill="#222">L</text>
  <text x="100" y="152" {caption_font} text-anchor="middle" fill="#222">圖(十)</text>
</svg>''')

# 圖(十一): 直角三角形內切圓切點四邊形 IDCE
svg_fig11 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 150" width="160" height="133">
  <polygon points="40,25 40,115 150,115" fill="none" stroke="#222" stroke-width="2"/>
  <rect x="40" y="105" width="10" height="10" fill="none" stroke="#222" stroke-width="1.2"/>
  <circle cx="68" cy="87" r="28" fill="#f0f7f4" stroke="#222" stroke-width="1.5"/>
  <line x1="68" y1="87" x2="40" y2="87" stroke="#222" stroke-width="1.5"/>
  <line x1="68" y1="87" x2="68" y2="115" stroke="#222" stroke-width="1.5"/>
  <line x1="68" y1="87" x2="40" y2="25" stroke="#666" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="68" y1="87" x2="150" y2="115" stroke="#666" stroke-width="1" stroke-dasharray="3,2"/>
  <circle cx="68" cy="87" r="2" fill="#222"/>
  <text x="28" y="24" {font_attr} fill="#222">A</text>
  <text x="26" y="122" {font_attr} fill="#222">C</text>
  <text x="155" y="120" {font_attr} fill="#222">B</text>
  <text x="26" y="88" {font_attr} fill="#222">E</text>
  <text x="66" y="128" {font_attr} fill="#222">D</text>
  <text x="74" y="85" {font_attr} fill="#222">I</text>
  <text x="95" y="142" {caption_font} text-anchor="middle" fill="#222">圖(十一)</text>
</svg>''')

# 圖(十二): 直角三角形與角平分線垂直垂足
svg_fig12 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 150" width="160" height="133">
  <polygon points="35,25 35,115 155,115" fill="none" stroke="#222" stroke-width="2"/>
  <rect x="35" y="105" width="10" height="10" fill="none" stroke="#222" stroke-width="1.2"/>
  <line x1="35" y1="25" x2="80" y2="115" stroke="#222" stroke-width="1.5"/>
  <line x1="80" y1="115" x2="110" y2="81" stroke="#222" stroke-width="1.5"/>
  <rect x="80" y="105" width="8" height="8" transform="rotate(-35 80 105)" fill="none" stroke="#222" stroke-width="1.2"/>
  <text x="24" y="24" {font_attr} fill="#222">A</text>
  <text x="22" y="122" {font_attr} fill="#222">B</text>
  <text x="160" y="120" {font_attr} fill="#222">C</text>
  <text x="76" y="128" {font_attr} fill="#222">D</text>
  <text x="114" y="80" {font_attr} fill="#222">E</text>
  <text x="95" y="142" {caption_font} text-anchor="middle" fill="#222">圖(十二)</text>
</svg>''')

# 證明題 1: 正方形內部點 E 與連線 DE, BE
svg_proof1 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="150" height="150">
  <rect x="30" y="30" width="100" height="100" fill="none" stroke="#222" stroke-width="2"/>
  <line x1="30" y1="30" x2="95" y2="60" stroke="#222" stroke-width="1.8"/>
  <line x1="130" y1="130" x2="95" y2="60" stroke="#222" stroke-width="1.8"/>
  <circle cx="95" cy="60" r="2.5" fill="#222"/>
  <text x="18" y="30" {font_attr} fill="#222">D</text>
  <text x="135" y="30" {font_attr} fill="#222">C</text>
  <text x="18" y="135" {font_attr} fill="#222">A</text>
  <text x="135" y="135" {font_attr} fill="#222">B</text>
  <text x="98" y="56" {font_attr} fill="#222">E</text>
</svg>''')

questions = [
    {
        "type": "fill",
        "sourceNumber": "一-1",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-1",
        "unitIds": ["nanyi-9-1-3-1"],
        "unitAssignmentBasis": "奇數與偶數的代數定義推理判斷。",
        "blocks": [
            {"type": "text", "text": "假設 $a$、$b$ 為整數，則 $2a + 4b + 5$ 為______數。（填入奇或偶）"}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-2",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "三角形三內角平分線交點定義為內心。",
        "blocks": [
            {"type": "text", "text": "三角形三內角的角平分線交點稱為三角形的______心。"}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-3",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "外心到三頂點等距之性質求外心線段長。",
        "blocks": [
            {"type": "text", "text": "已知 $O$ 為 $\\triangle ABC$ 的外心，若 $\\overline{OA} + \\overline{OB} + \\overline{OC} = 30$，則 $\\overline{OA} =$ ______。"}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-4",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "直角三角形斜邊中點即外心與外接圓半徑計算。",
        "blocks": [
            {"type": "text", "text": "直角三角形 $ABC$ 中，$\\angle B = 90^\\circ$，若 $\\overline{AB} = 16$，$\\overline{BC} = 30$，則 $\\triangle ABC$ 的外接圓半徑 $=$ ______。"}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-5",
        "page": 1,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-3-1",
        "unitIds": ["nanyi-9-1-3-1"],
        "unitAssignmentBasis": "長方形各邊中點連線為菱形之角度推算。",
        "blocks": [
            {"type": "text", "text": "如圖(一)，長方形 $ABCD$ 中，$E$、$F$、$G$、$H$ 分別為各邊中點，若 $\\angle AEF = 40^\\circ$，則 $\\angle EFG =$ ______度。"},
            {"type": "svg", "svg": svg_fig1}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-6",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "外心圓心角等於同弧圓周角兩倍之角度性質。",
        "blocks": [
            {"type": "text", "text": "如圖(二)，$\\triangle ABC$ 中，$\\angle A = 50^\\circ$，$O$ 為 $\\triangle ABC$ 的外心，則 $\\angle BOC =$ ______度。"},
            {"type": "svg", "svg": svg_fig2}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-7",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "內心頂角與底角交角之角度公式 90度 + 頂角一半。",
        "blocks": [
            {"type": "text", "text": "如圖(三)，$\\triangle ABC$ 中，$\\angle A = 70^\\circ$，$I$ 為 $\\triangle ABC$ 的內心，則 $\\angle BIC =$ ______度。"},
            {"type": "svg", "svg": svg_fig3}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-8",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "重心分中線段為 2 比 1 之性質求中線全長。",
        "blocks": [
            {"type": "text", "text": "如圖(四)，$G$ 為 $\\triangle ABC$ 的重心，$\\overline{AD}$ 為 $\\overline{BC}$ 邊上的中線，若 $\\overline{AG} = 10$，則 $\\overline{AD} =$ ______。"},
            {"type": "svg", "svg": svg_fig4}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-9",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "三中線六等分三角形面積性質求全體面積。",
        "blocks": [
            {"type": "text", "text": "如圖(五)，$\\triangle ABC$ 的三中線 $\\overline{AD}$、$\\overline{BE}$、$\\overline{CF}$ 交於一點 $G$，若 $\\triangle BGD$ 的面積為 $10$，則 $\\triangle ABC$ 的面積 $=$ ______。"},
            {"type": "svg", "svg": svg_fig5}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-10",
        "page": 1,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "內心分割面積比等於三角形三邊長比。",
        "blocks": [
            {"type": "text", "text": "如圖(六)，$I$ 為 $\\triangle ABC$ 的內心，且 $\\angle A = 90^\\circ$，$\\angle B = 30^\\circ$，則 $\\triangle IAB$ 面積 : $\\triangle IBC$ 面積 : $\\triangle ICA$ 面積 $=$ ______。"},
            {"type": "svg", "svg": svg_fig6}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-11",
        "page": 1,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-3-1",
        "unitIds": ["nanyi-9-1-3-1"],
        "unitAssignmentBasis": "正方形頂點垂線全等直角三角形與面積計算。",
        "blocks": [
            {"type": "text", "text": "如圖(七)，四邊形 $ABCD$ 為正方形，$A$ 在 $\\overline{EF}$ 上，$\\angle BEA = \\angle DFA = 90^\\circ$，若 $\\overline{BE} = 12$，$\\overline{DF} = 8$，則四邊形 $ABCD$ 的面積 $=$ ______。"},
            {"type": "svg", "svg": svg_fig7}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-12",
        "page": 1,
        "difficulty": "hard",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "鈍角等腰三角形外心在形外與內心角度綜合計算。",
        "blocks": [
            {"type": "text", "text": "如圖(八)，$\\triangle ABC$ 為一等腰三角形，$I$ 為其內心，$O$ 為其外心，已知頂角 $\\angle BAC = 120^\\circ$，則 $\\angle IBO =$ ______度。"},
            {"type": "svg", "svg": svg_fig8}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-13",
        "page": 2,
        "difficulty": "hard",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "鈍角等腰三角形外接圓半徑之畢氏定理或面積公式計算。",
        "blocks": [
            {"type": "text", "text": "鈍角 $\\triangle ABC$ 中，$\\overline{AB} = \\overline{AC} = 15$，$\\overline{BC} = 24$，則 $\\triangle ABC$ 的外接圓半徑 $=$ ______。"}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-14",
        "page": 2,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "直角三角形內切圓半徑公式計算。",
        "blocks": [
            {"type": "text", "text": "$\\triangle ABC$ 中，$\\overline{AB} = 12$、$\\overline{BC} = 9$、$\\overline{AC} = 15$，則 $\\triangle ABC$ 的內切圓半徑 $=$ ______。"}
        ]
    },
    {
        "type": "choice",
        "sourceNumber": "一-15",
        "page": 2,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-3-1",
        "unitIds": ["nanyi-9-1-3-1"],
        "unitAssignmentBasis": "二次式因式分解與奇數偶數倍數性質代數推理。",
        "blocks": [
            {"type": "text", "text": "已知 $a$ 是正整數，$A = (2a+1)^2 - 4(2a+1) - 21$，則 $A$ 必為下列哪一個數的倍數？"},
            {"type": "options", "items": ["$3$", "$4$", "$5$", "$6$"]}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-16",
        "page": 2,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "正三角形外接圓與內切圓面積比公式計算。",
        "blocks": [
            {"type": "text", "text": "若一正三角形的面積為 $A$，外接圓面積為 $B$，內切圓面積為 $C$，則 $A : B : C =$ ______。"}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-17",
        "page": 2,
        "difficulty": "hard",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "平行四邊形中點連線與重心性質分割求面積。",
        "blocks": [
            {"type": "text", "text": "如圖(九)，$ABCD$ 為平行四邊形，$E$、$F$ 分別為 $\\overline{BC}$、$\\overline{CD}$ 的中點，$\\overline{BD}$ 交 $\\overline{AE}$、$\\overline{AF}$ 於 $G$、$H$，若 $\\triangle ABG$ 的面積為 $12$，則 $\\triangle AEF$ 的面積 $=$ ______。"},
            {"type": "svg", "svg": svg_fig9}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-18",
        "page": 2,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "直線兩軸截距與直角三角形重心坐標公式計算。",
        "blocks": [
            {"type": "text", "text": "如圖(十)，直線 $L : 8x + 15y = 120$ 交兩軸於 $A$、$B$ 兩點，則其重心 $G$ 的坐標為 ______。"},
            {"type": "svg", "svg": svg_fig10}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-19",
        "page": 2,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "直角三角形內切圓切點所成正方形之面積計算。",
        "blocks": [
            {"type": "text", "text": "如圖(十一)，$\\triangle ABC$ 為一直角三角形，$\\angle C = 90^\\circ$，$I$ 為其內心，若 $\\overline{AC} = 18$，$\\overline{BC} = 24$，則四邊形 $IDCE$ 的面積 $=$ ______。"},
            {"type": "svg", "svg": svg_fig11}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "一-20",
        "page": 2,
        "difficulty": "hard",
        "primaryUnitId": "nanyi-9-1-3-1",
        "unitIds": ["nanyi-9-1-3-1"],
        "unitAssignmentBasis": "角平分線垂直截線三角比與線段比之綜合幾何推理。",
        "blocks": [
            {"type": "text", "text": "如圖(十二)，直角 $\\triangle ABC$ 中，$\\angle B = 90^\\circ$，$\\angle BAC$ 的角平分線交 $\\overline{BC}$ 於 $D$，$\\overline{AD} \\perp \\overline{DE}$，$E$ 在 $\\overline{AC}$ 上，若 $\\overline{AB} = 9$，$\\overline{AE} = 13$，則 $\\overline{CD} : \\overline{CE} =$ ______。"},
            {"type": "svg", "svg": svg_fig12}
        ]
    },
    {
        "type": "written",
        "sourceNumber": "二-1",
        "page": 2,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-3-1",
        "unitIds": ["nanyi-9-1-3-1"],
        "unitAssignmentBasis": "正方形對稱性與三角形 SSS 全等幾何證明。",
        "blocks": [
            {"type": "text", "text": "【已知】如右圖，$E$ 點在正方形 $ABCD$ 內部，$\\overline{DE} = \\overline{BE}$。\n【求證】$\\angle CDE = \\angle CBE$\n【證明】連接 $\\overline{CE}$。在 $\\triangle CDE$ 與 $\\triangle CBE$ 中，因為四邊形 $ABCD$ 為正方形，所以 $\\overline{CD} = \\overline{CB}$。又 $\\overline{DE} = \\overline{BE}$（已知），$\\overline{CE} = \\overline{CE}$（公用邊），故 $\\triangle CDE \\cong \\triangle CBE$（SSS 全等性質）。因此 $\\angle CDE = \\angle CBE$（對應角相等）。"},
            {"type": "svg", "svg": svg_proof1}
        ]
    },
    {
        "type": "written",
        "sourceNumber": "二-2",
        "page": 2,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-1",
        "unitIds": ["nanyi-9-1-3-1"],
        "unitAssignmentBasis": "奇數乘以偶數必為偶數之代數嚴格證明。",
        "blocks": [
            {"type": "text", "text": "【已知】$a$ 是奇數，$b$ 是偶數。\n【求證】$a \\times b$ 是偶數\n【證明】設 $a = 2k + 1$，$b = 2m$（其中 $k, m$ 為整數）。則 $a \\times b = (2k + 1) \\times 2m = 2(2km + m)$。因為 $k, m$ 為整數，所以 $2km + m$ 亦為整數。因此 $a \\times b$ 為 2 的倍數，即 $a \\times b$ 是偶數。"}
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
    "printedHeader": "宜蘭縣立羅東國中 110 學年度第一學期九年級數學科第三次段考試卷",
    "printedSlot": {
        "year": 110,
        "semester": 1,
        "grade": 9,
        "exam": 3
    },
    "printedCounts": "填充題 20 題、證明題 2 題，合計 22 題。",
    "visualReviewComplete": True,
    "reviewNote": "全卷22題（填充20題、證明2題），涵蓋外心、內心、重心、幾何全等推理與代數證明。純向量幾何SVG全數重繪。",
    "expectedTypes": {
        "choice": 1,
        "fill": 19,
        "written": 2
    },
    "questions": questions
}

out_path = ROOT / f"research/yilan/transcribed/{paper_id}.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(doc_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Successfully written {out_path} with {len(questions)} questions")
