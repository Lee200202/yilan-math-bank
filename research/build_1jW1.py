"""Build transcription JSON and Markdown for paper 1jW1spNUDS2CHvsrFo7o3XKWSnpcTkN9M
宜蘭縣中華國民中學一○九學年度第一學期第三次段考數學科試卷 九年級
"""
import hashlib
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent

paper_id = "1jW1spNUDS2CHvsrFo7o3XKWSnpcTkN9M"
pdf_path = ROOT / f"public/papers/{paper_id}.pdf"
pdf_sha256 = hashlib.sha256(pdf_path.read_bytes()).hexdigest()

def clean_svg(s: str) -> str:
    s = re.sub(r'<!--.*?-->', '', s, flags=re.DOTALL)
    s = re.sub(r'>\s+<', '><', s)
    return s.strip()

font_italic = 'font-family="\'TW-Kai\', \'BiauKai\', \'DFKai-SB\', serif" font-size="14" font-style="italic"'
font_roman = 'font-family="\'TW-Kai\', \'BiauKai\', \'DFKai-SB\', serif" font-size="13"'
font_small = 'font-family="\'TW-Kai\', \'BiauKai\', \'DFKai-SB\', serif" font-size="11"'

# 1. Q3 SVG: Parallelogram AC and BD crossing at M with shaded AMD and BMC
svg_q3 = clean_svg(f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 135" width="160" height="135">
  <polygon points="55,20 135,20 80,65" fill="#e0e0e0" stroke="none" />
  <polygon points="25,110 105,110 80,65" fill="#e0e0e0" stroke="none" />
  <polygon points="55,20 135,20 105,110 25,110" fill="none" stroke="#111" stroke-width="1.5" />
  <line x1="55" y1="20" x2="105" y2="110" stroke="#111" stroke-width="1.3" />
  <line x1="25" y1="110" x2="135" y2="20" stroke="#111" stroke-width="1.3" />
  <g {font_italic} fill="#111">
    <text x="50" y="16">A</text>
    <text x="140" y="18">D</text>
    <text x="14" y="115">B</text>
    <text x="110" y="118">C</text>
    <text x="83" y="60">M</text>
  </g>
</svg>""")

# 2. Q4 SVG: Square ABCD with perpendiculars to line L at E and F
svg_q4 = clean_svg(f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 205 150" width="205" height="150">
  <polygon points="30,120 75,120 30,60" fill="#e0e0e0" stroke="none" />
  <polygon points="75,120 135,120 135,75" fill="#e0e0e0" stroke="none" />
  <line x1="15" y1="120" x2="185" y2="120" stroke="#111" stroke-width="1.3" />
  <polygon points="75,120 135,75 90,15 30,60" fill="none" stroke="#111" stroke-width="1.5" />
  <line x1="30" y1="60" x2="30" y2="120" stroke="#111" stroke-width="1.4" />
  <line x1="135" y1="75" x2="135" y2="120" stroke="#111" stroke-width="1.4" />
  <polyline points="30,112 38,112 38,120" fill="none" stroke="#111" stroke-width="1.2" />
  <polyline points="127,120 127,112 135,112" fill="none" stroke="#111" stroke-width="1.2" />
  <polyline points="69,112 77,106 83,114" fill="none" stroke="#111" stroke-width="1.2" />
  <g {font_italic} fill="#111">
    <text x="15" y="62">D</text>
    <text x="90" y="10" text-anchor="middle">C</text>
    <text x="142" y="75">B</text>
    <text x="75" y="136" text-anchor="middle">A</text>
    <text x="30" y="136" text-anchor="middle">E</text>
    <text x="135" y="136" text-anchor="middle">F</text>
    <text x="190" y="124">L</text>
  </g>
  <g {font_roman} fill="#111">
    <text x="34" y="75">1</text>
    <text x="42" y="115">5</text>
    <text x="60" y="115">2</text>
    <text x="75" y="100" text-anchor="middle">7</text>
    <text x="89" y="115">3</text>
    <text x="122" y="115">6</text>
    <text x="126" y="85">4</text>
  </g>
</svg>""")

# 3. Q6 SVG: AD and BC crossing at E, horizontal AB and CD
svg_q6 = clean_svg(f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 145 130" width="145" height="130">
  <line x1="25" y1="20" x2="70" y2="20" stroke="#111" stroke-width="1.5" />
  <line x1="70" y1="110" x2="115" y2="110" stroke="#111" stroke-width="1.5" />
  <line x1="70" y1="20" x2="70" y2="110" stroke="#111" stroke-width="1.5" />
  <line x1="25" y1="20" x2="115" y2="110" stroke="#111" stroke-width="1.5" />
  <g {font_italic} fill="#111">
    <text x="12" y="24">B</text>
    <text x="74" y="24">A</text>
    <text x="56" y="68">E</text>
    <text x="56" y="114">D</text>
    <text x="120" y="114">C</text>
  </g>
</svg>""")

# 4. Q7 SVG: Rectangle ABCD with point P above AD
svg_q7 = clean_svg(f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 150 140" width="150" height="140">
  <rect x="30" y="55" width="80" height="60" fill="none" stroke="#111" stroke-width="1.5" />
  <line x1="70" y1="20" x2="30" y2="55" stroke="#111" stroke-width="1.4" />
  <line x1="70" y1="20" x2="110" y2="55" stroke="#111" stroke-width="1.4" />
  <line x1="70" y1="20" x2="30" y2="115" stroke="#111" stroke-width="1.3" />
  <line x1="70" y1="20" x2="110" y2="115" stroke="#111" stroke-width="1.3" />
  <g {font_italic} fill="#111">
    <text x="70" y="14" text-anchor="middle">P</text>
    <text x="18" y="58">A</text>
    <text x="116" y="58">D</text>
    <text x="18" y="120">B</text>
    <text x="116" y="120">C</text>
  </g>
</svg>""")

# 5. Q10 SVG: Isosceles triangle ABC with circumcenter O on altitude AD, gray filled
svg_q10 = clean_svg(f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 155 150" width="155" height="150">
  <polygon points="75,20 20,120 130,120" fill="#e0e0e0" stroke="#111" stroke-width="1.5" />
  <line x1="75" y1="20" x2="75" y2="120" stroke="#111" stroke-width="1.4" />
  <circle cx="75" cy="98" r="3" fill="#111" />
  <g {font_italic} fill="#111">
    <text x="75" y="14" text-anchor="middle">A</text>
    <text x="10" y="125">B</text>
    <text x="135" y="125">C</text>
    <text x="75" y="136" text-anchor="middle">D</text>
    <text x="81" y="96">O</text>
  </g>
</svg>""")

# 6. Q13 SVG: Trapezoid ABCD with diagonal midpoints E, F connected
svg_q13 = clean_svg(f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 155 130" width="155" height="130">
  <polygon points="45,25 105,25 130,105 20,105" fill="none" stroke="#111" stroke-width="1.5" />
  <line x1="45" y1="25" x2="130" y2="105" stroke="#111" stroke-width="1.2" />
  <line x1="105" y1="25" x2="20" y2="105" stroke="#111" stroke-width="1.2" />
  <line x1="62.5" y1="65" x2="87.5" y2="65" stroke="#111" stroke-width="1.5" />
  <g {font_italic} fill="#111">
    <text x="36" y="24">A</text>
    <text x="110" y="24">D</text>
    <text x="10" y="112">B</text>
    <text x="135" y="112">C</text>
    <text x="50" y="65">E</text>
    <text x="92" y="65">F</text>
  </g>
</svg>""")

# 7. Q14 SVG: Triangle ABC with medians AD and BE intersecting at P
svg_q14 = clean_svg(f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 155 135" width="155" height="135">
  <polygon points="70,20 20,110 135,110" fill="none" stroke="#111" stroke-width="1.5" />
  <line x1="70" y1="20" x2="77.5" y2="110" stroke="#111" stroke-width="1.3" />
  <line x1="20" y1="110" x2="102.5" y2="65" stroke="#111" stroke-width="1.3" />
  <g {font_italic} fill="#111">
    <text x="70" y="14" text-anchor="middle">A</text>
    <text x="8" y="115">B</text>
    <text x="140" y="115">C</text>
    <text x="77" y="125" text-anchor="middle">D</text>
    <text x="108" y="63">E</text>
    <text x="80" y="86">P</text>
  </g>
</svg>""")

# 8. Q15 SVG: Triangle ABC with bisectors AD and BI meeting at I, gray filled
svg_q15 = clean_svg(f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 165 110" width="165" height="110">
  <polygon points="58,25 15,85 150,85" fill="#e0e0e0" stroke="#111" stroke-width="1.5" />
  <line x1="58" y1="25" x2="60" y2="85" stroke="#111" stroke-width="1.3" />
  <line x1="15" y1="85" x2="59" y2="58" stroke="#111" stroke-width="1.3" />
  <g {font_italic} fill="#111">
    <text x="58" y="18" text-anchor="middle">A</text>
    <text x="5" y="90">B</text>
    <text x="154" y="90">C</text>
    <text x="60" y="98" text-anchor="middle">D</text>
    <text x="65" y="62">I</text>
  </g>
</svg>""")

# 9. Q16 SVG: Isosceles triangle ABC with incenter I and centroid G on AD, gray filled
svg_q16 = clean_svg(f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 145 135" width="145" height="135">
  <polygon points="70,20 15,105 125,105" fill="#e0e0e0" stroke="#111" stroke-width="1.5" />
  <line x1="70" y1="20" x2="70" y2="105" stroke="#111" stroke-width="1.4" />
  <circle cx="70" cy="68" r="3" fill="#111" />
  <circle cx="70" cy="77" r="3" fill="#111" />
  <g {font_italic} fill="#111">
    <text x="70" y="14" text-anchor="middle">A</text>
    <text x="5" y="110">B</text>
    <text x="130" y="110">C</text>
    <text x="70" y="120" text-anchor="middle">D</text>
    <text x="75" y="70">I</text>
    <text x="56" y="80">G</text>
  </g>
</svg>""")

# 10. Q17 SVG: Square ABCD with incircle, circumcircle, center O, tangent point E
svg_q17 = clean_svg(f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 155 155" width="155" height="155">
  <circle cx="75" cy="75" r="49.5" fill="none" stroke="#111" stroke-width="1.4" />
  <rect x="40" y="40" width="70" height="70" fill="none" stroke="#111" stroke-width="1.5" />
  <circle cx="75" cy="75" r="35" fill="none" stroke="#111" stroke-width="1.4" />
  <circle cx="75" cy="75" r="2.5" fill="#111" />
  <g {font_italic} fill="#111">
    <text x="28" y="38">A</text>
    <text x="114" y="38">D</text>
    <text x="28" y="118">B</text>
    <text x="114" y="118">C</text>
    <text x="75" y="34" text-anchor="middle">E</text>
    <text x="81" y="68">O</text>
  </g>
</svg>""")

# 11. Q19 SVG: Triangle ABC with altitudes BE, CD and midpoint F forming DEF
svg_q19 = clean_svg(f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 155 140" width="155" height="140">
  <polygon points="75,20 20,115 135,105" fill="none" stroke="#111" stroke-width="1.5" />
  <line x1="20" y1="115" x2="90" y2="41" stroke="#111" stroke-width="1.2" />
  <line x1="135" y1="105" x2="58" y2="49" stroke="#111" stroke-width="1.2" />
  <polygon points="58,49 90,41 77.5,110" fill="none" stroke="#111" stroke-width="1.5" />
  <g {font_italic} fill="#111">
    <text x="75" y="14" text-anchor="middle">A</text>
    <text x="44" y="52">D</text>
    <text x="96" y="43">E</text>
    <text x="10" y="122">B</text>
    <text x="140" y="110">C</text>
    <text x="76" y="126" text-anchor="middle">F</text>
  </g>
</svg>""")

# 12. Q20 SVG: Collinear A-E-C, perpendicular BE, triangles forming quadrilateral ABCD
svg_q20 = clean_svg(f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 170 145" width="170" height="145">
  <polygon points="20,75 55,25 150,75 45,115" fill="none" stroke="#111" stroke-width="1.5" />
  <line x1="20" y1="75" x2="150" y2="75" stroke="#111" stroke-width="1.4" />
  <line x1="55" y1="25" x2="55" y2="75" stroke="#111" stroke-width="1.4" />
  <g {font_italic} fill="#111">
    <text x="10" y="78">A</text>
    <text x="55" y="18" text-anchor="middle">B</text>
    <text x="155" y="78">C</text>
    <text x="40" y="128">D</text>
    <text x="55" y="92" text-anchor="middle">E</text>
  </g>
</svg>""")

# 13. Q21 SVG: Triangles ABC and DAC on line BCD with incenters E and F
svg_q21 = clean_svg(f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 185 135" width="185" height="135">
  <polygon points="20,105 65,30 165,105" fill="none" stroke="#111" stroke-width="1.5" />
  <line x1="65" y1="30" x2="65" y2="105" stroke="#111" stroke-width="1.4" />
  <circle cx="50" cy="80" r="2.5" fill="#111" />
  <circle cx="90" cy="78" r="2.5" fill="#111" />
  <g {font_italic} fill="#111">
    <text x="65" y="22" text-anchor="middle">A</text>
    <text x="10" y="110">B</text>
    <text x="63" y="122" text-anchor="middle">C</text>
    <text x="170" y="110">D</text>
    <text x="55" y="84">E</text>
    <text x="95" y="82">F</text>
  </g>
</svg>""")

# 14. Comprehensive 1 SVG: Equilateral triangle ABC with altitude AD, DE perpendicular to AC, EF parallel to BC
svg_p3_q1 = clean_svg(f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 155 135" width="155" height="135">
  <polygon points="75,20 25,110 125,110" fill="none" stroke="#111" stroke-width="1.5" />
  <line x1="75" y1="20" x2="75" y2="110" stroke="#111" stroke-width="1.4" />
  <line x1="75" y1="110" x2="112.5" y2="87.5" stroke="#111" stroke-width="1.4" />
  <line x1="37.5" y1="87.5" x2="112.5" y2="87.5" stroke="#111" stroke-width="1.4" />
  <polyline points="108,85 111,80 115,83" fill="none" stroke="#111" stroke-width="1.2" />
  <g {font_italic} fill="#111">
    <text x="75" y="14" text-anchor="middle">A</text>
    <text x="14" y="115">B</text>
    <text x="130" y="115">C</text>
    <text x="75" y="124" text-anchor="middle">D</text>
    <text x="26" y="88">F</text>
    <text x="117" y="88">E</text>
  </g>
</svg>""")

# 15. Comprehensive 2 SVG: Triangle ABC with centroid G, perpendiculars BD, GH, AE, CF to line L
svg_p3_q2 = clean_svg(f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 195 155" width="195" height="155">
  <line x1="15" y1="125" x2="175" y2="125" stroke="#111" stroke-width="1.4" />
  <polygon points="30,105 120,30 150,85" fill="none" stroke="#111" stroke-width="1.5" />
  <line x1="30" y1="105" x2="30" y2="125" stroke="#111" stroke-width="1.3" />
  <line x1="100" y1="73.3" x2="100" y2="125" stroke="#111" stroke-width="1.3" />
  <line x1="120" y1="30" x2="120" y2="125" stroke="#111" stroke-width="1.3" />
  <line x1="150" y1="85" x2="150" y2="125" stroke="#111" stroke-width="1.3" />
  <circle cx="100" cy="73.3" r="2.5" fill="#111" />
  <rect x="30" y="119" width="6" height="6" fill="none" stroke="#111" stroke-width="1.1" />
  <rect x="100" y="119" width="6" height="6" fill="none" stroke="#111" stroke-width="1.1" />
  <rect x="120" y="119" width="6" height="6" fill="none" stroke="#111" stroke-width="1.1" />
  <rect x="150" y="119" width="6" height="6" fill="none" stroke="#111" stroke-width="1.1" />
  <g {font_italic} fill="#111">
    <text x="18" y="108">B</text>
    <text x="120" y="22" text-anchor="middle">A</text>
    <text x="155" y="87">C</text>
    <text x="88" y="76">G</text>
    <text x="30" y="138" text-anchor="middle">D</text>
    <text x="100" y="138" text-anchor="middle">H</text>
    <text x="120" y="138" text-anchor="middle">E</text>
    <text x="150" y="138" text-anchor="middle">F</text>
    <text x="180" y="128">L</text>
  </g>
</svg>""")

data = {
  "paperId": paper_id,
  "sourceSha256": pdf_sha256,
  "printedHeader": "宜蘭縣中華國民中學一○九學年度第一學期第三次段考數學科試卷 九年級",
  "printedSlot": {
    "year": 109,
    "semester": 1,
    "grade": 9,
    "exam": 3
  },
  "printedCounts": "第一部分選擇與填空題22格、第二部分綜合題3題，合計25題（24計分項目）。",
  "visualReviewComplete": True,
  "reviewNote": "已逐題嚴格對照原始試卷3頁影像及官方教師手寫解答卷，全卷共15幅純向量幾何SVG圖形，純標籤語意化繪製，零image、零base64、零tspan、零CSS。",
  "deliveryStatus": "complete",
  "expectedTypes": {
    "choice": 6,
    "fill": 16,
    "written": 3
  },
  "questions": [
    # Q1
    {
      "type": "choice",
      "sourceNumber": "一-1",
      "page": 1,
      "difficulty": "easy",
      "primaryUnitId": "nanyi-9-1-3-2",
      "unitIds": ["nanyi-9-1-3-2"],
      "unitAssignmentBasis": "外心的定義（三角形三邊垂直平分線的交點）。",
      "blocks": [
        {
          "type": "text",
          "text": "下列哪一個是外心？"
        },
        {
          "type": "options",
          "items": [
            "三角形三高的交點",
            "三角形三內角平分線的交點",
            "三角形三邊垂直平分線的交點",
            "三角形三中線的交點"
          ]
        }
      ]
    },
    # Q2
    {
      "type": "choice",
      "sourceNumber": "一-2",
      "page": 1,
      "difficulty": "easy",
      "primaryUnitId": "nanyi-9-1-3-1",
      "unitIds": ["nanyi-9-1-3-1"],
      "unitAssignmentBasis": "整數性質、偶數乘積與不等式的推理證明判斷。",
      "blocks": [
        {
          "type": "text",
          "text": "下列敘述何者正確？"
        },
        {
          "type": "options",
          "items": [
            "若 $a \\cdot b$ 為偶數，則 $a$ 和 $b$ 皆為偶數",
            "若 $a \\cdot b$ 為正數，則 $a$ 或 $b$ 只有一個為正數",
            "若 $n$ 為偶數，則 $n^3$ 為奇數",
            "若 $n$ 為任意數，則 $(n+1)^2 \\ge 2n+1$"
          ]
        }
      ]
    },
    # Q3
    {
      "type": "choice",
      "sourceNumber": "一-3",
      "page": 1,
      "difficulty": "easy",
      "primaryUnitId": "nanyi-9-1-3-1",
      "unitIds": ["nanyi-9-1-3-1"],
      "unitAssignmentBasis": "全等性質的判斷與證明步驟推理（SAS 全等）。",
      "blocks": [
        {
          "type": "text",
          "text": "如圖，$\\overline{AC}$ 與 $\\overline{BD}$ 交於 $M$ 點，且 $\\overline{BM} = \\overline{DM}$，$\\overline{AM} = \\overline{CM}$。試問下列證明 $\\overline{BC} = \\overline{AD}$ 的過程中，哪一個選項是錯誤的？"
        },
        {
          "type": "svg",
          "maxHeight": 135,
          "svg": svg_q3
        },
        {
          "type": "options",
          "items": [
            "$\\because \\overline{BM} = \\overline{DM}$，$\\overline{CM} = \\overline{AM}$",
            "且 $\\angle BMC = \\angle DMA$ (對頂角相等)",
            "$\\therefore \\triangle BMC \\cong \\triangle DMA$ ( SSS 全等性質 )",
            "故 $\\overline{BC} = \\overline{AD}$"
          ]
        }
      ]
    },
    # Q4
    {
      "type": "choice",
      "sourceNumber": "一-4",
      "page": 1,
      "difficulty": "medium",
      "primaryUnitId": "nanyi-9-1-3-1",
      "unitIds": ["nanyi-9-1-3-1"],
      "unitAssignmentBasis": "正方形與直角三角形全等幾何證明的步驟推理（AAS 全等）。",
      "blocks": [
        {
          "type": "text",
          "text": "如附圖，已知 $ABCD$ 是正方形，$A$ 在 $L$ 上，$\\overline{DE} \\perp L$，$\\overline{BF} \\perp L$，垂足分別為 $E$、$F$ ( $\\overline{AE} \\neq \\overline{AF}$ )。"
        },
        {
          "type": "text",
          "text": "求證：$\\triangle ADE \\cong \\triangle BAF$。"
        },
        {
          "type": "text",
          "text": "證明："
        },
        {
          "type": "text",
          "text": "(1) $\\because ABCD$ 是正方形 $\\therefore \\overline{AB} = \\overline{AD}$，$\\angle 7 = 90^\\circ$"
        },
        {
          "type": "text",
          "text": "(2) 又 $\\because \\overline{DE} \\perp L$，$\\overline{BF} \\perp L$ $\\therefore \\angle 5 = \\angle 6 = 90^\\circ$"
        },
        {
          "type": "text",
          "text": "(3) ＿＿＿＿(甲)＿＿＿＿"
        },
        {
          "type": "text",
          "text": "(4) $\\therefore \\triangle ADE \\cong \\triangle BAF$"
        },
        {
          "type": "text",
          "text": "從下列選項中，選出可填入 (甲) 中的正確證明過程。"
        },
        {
          "type": "svg",
          "maxHeight": 150,
          "svg": svg_q4
        },
        {
          "type": "options",
          "items": [
            "$\\because \\overline{DE} \\perp L$，$\\overline{BF} \\perp L$，$\\angle 7 = 90^\\circ$ $\\therefore \\overline{DE} = \\overline{BF}$",
            "$\\because \\overline{DE} \\perp L$，$\\overline{BF} \\perp L$，$\\angle 7 = 90^\\circ$ $\\therefore \\angle 1 = \\angle 4$",
            "$\\because \\angle 7 = 90^\\circ$，$\\angle 5 = \\angle 6 = 90^\\circ$ $\\therefore \\angle 2 = \\angle 3$",
            "$\\because \\angle 7 = \\angle 5 = 90^\\circ$ $\\therefore \\angle 1 + \\angle 2 = \\angle 2 + \\angle 3$ $\\therefore \\angle 1 = \\angle 3$"
          ]
        }
      ]
    },
    # Q5
    {
      "type": "choice",
      "sourceNumber": "一-5",
      "page": 1,
      "difficulty": "easy",
      "primaryUnitId": "nanyi-9-1-3-2",
      "unitIds": ["nanyi-9-1-3-2"],
      "unitAssignmentBasis": "多邊形外心、內心與對稱性質的定義與概念判斷。",
      "blocks": [
        {
          "type": "text",
          "text": "下列敘述何者錯誤？"
        },
        {
          "type": "options",
          "items": [
            "正多邊形一定有外接圓與內切圓，且它們有同心圓",
            "正多邊形為線對稱圖形",
            "若多邊形各內角平分線交於一點 $G$，則 $G$ 點為此多邊形的內心",
            "多邊形的外心一定存在，且外心到各頂點等距離"
          ]
        }
      ]
    },
    # Q6
    {
      "type": "choice",
      "sourceNumber": "一-6",
      "page": 1,
      "difficulty": "easy",
      "primaryUnitId": "nanyi-9-1-3-1",
      "unitIds": ["nanyi-9-1-3-1"],
      "unitAssignmentBasis": "三角形全等條件的判別（AAA 只能證明相似不能證明全等）。",
      "blocks": [
        {
          "type": "text",
          "text": "如圖，$\\overline{AD}$、$\\overline{BC}$ 交於 $E$ 點，根據下列何者不能證明 $\\triangle ABE \\cong \\triangle DCE$？"
        },
        {
          "type": "svg",
          "maxHeight": 130,
          "svg": svg_q6
        },
        {
          "type": "options",
          "items": [
            "$E$ 是 $\\overline{BC}$ 中點，且 $\\angle B = \\angle C$",
            "$\\overline{AB} // \\overline{CD}$",
            "$\\overline{AD}$、$\\overline{BC}$ 互相平分",
            "$\\overline{AB} \\perp \\overline{AD}$，$\\overline{AD} \\perp \\overline{CD}$，$\\overline{BE} = \\overline{CE}$"
          ]
        }
      ]
    },
    # Q7
    {
      "type": "fill",
      "sourceNumber": "一-7",
      "page": 1,
      "difficulty": "easy",
      "primaryUnitId": "nanyi-9-1-3-1",
      "unitIds": ["nanyi-9-1-3-1"],
      "unitAssignmentBasis": "矩形性質與三角形全等條件的應用。",
      "blocks": [
        {
          "type": "text",
          "text": "如圖，$P$ 為矩形 $ABCD$ 外一點。若 $\\overline{PB} = \\overline{PC}$，則利用＿＿＿＿全等性質可得知 $\\triangle PAB \\cong \\triangle PDC$。"
        },
        {
          "type": "svg",
          "maxHeight": 140,
          "svg": svg_q7
        }
      ]
    },
    # Q8
    {
      "type": "fill",
      "sourceNumber": "一-8",
      "page": 1,
      "difficulty": "easy",
      "primaryUnitId": "nanyi-9-1-3-2",
      "unitIds": ["nanyi-9-1-3-2"],
      "unitAssignmentBasis": "外心到三頂點等距離的性質與一元一次方程式。",
      "blocks": [
        {
          "type": "text",
          "text": "若 $O$ 點為 $\\triangle ABC$ 的外心，$\\overline{OA} = 5x-3$，$\\overline{OC} = -2x+11$，則 $\\overline{OB} = $＿＿＿＿。"
        }
      ]
    },
    # Q9
    {
      "type": "fill",
      "sourceNumber": "一-9",
      "page": 1,
      "difficulty": "easy",
      "primaryUnitId": "nanyi-9-1-3-2",
      "unitIds": ["nanyi-9-1-3-2"],
      "unitAssignmentBasis": "利用內切圓半徑與周長求三角形面積。",
      "blocks": [
        {
          "type": "text",
          "text": "$\\triangle ABC$ 中，$\\overline{AB} = 8$，$\\overline{BC} = 12$，$\\overline{AC} = 9$，若 $\\triangle ABC$ 的內切圓半徑為 $3$，則 $\\triangle ABC$ 的面積＝＿＿＿＿。"
        }
      ]
    },
    # Q10
    {
      "type": "fill",
      "sourceNumber": "一-10",
      "page": 1,
      "difficulty": "medium",
      "primaryUnitId": "nanyi-9-1-3-2",
      "unitIds": ["nanyi-9-1-3-2"],
      "unitAssignmentBasis": "等腰三角形外心與外接圓半徑的幾何計算（勾股定理）。",
      "blocks": [
        {
          "type": "text",
          "text": "如圖，已知 $O$ 點為銳角 $\\triangle ABC$ 的外心，$\\overline{AB} = \\overline{AC} = 10$，$\\overline{BC} = 12$，且 $\\overleftrightarrow{AO}$ 交 $\\overline{BC}$ 於 $D$ 點，求 $\\triangle ABC$ 的外接圓半徑＝＿＿＿＿。"
        },
        {
          "type": "svg",
          "maxHeight": 150,
          "svg": svg_q10
        }
      ]
    },
    # Q11
    {
      "type": "fill",
      "sourceNumber": "一-11",
      "page": 2,
      "difficulty": "medium",
      "primaryUnitId": "nanyi-9-1-3-2",
      "unitIds": ["nanyi-9-1-3-2", "nanyi-9-1-2-2"],
      "unitAssignmentBasis": "鈍角三角形外心圓心角與頂角的度數關係。",
      "blocks": [
        {
          "type": "text",
          "text": "在鈍角 $\\triangle ABC$ 中，$O$ 點為外心，若 $\\angle BAC = 150^\\circ$，則 $\\angle BOC$ 的度數＝＿＿＿＿度。"
        }
      ]
    },
    # Q12
    {
      "type": "fill",
      "sourceNumber": "一-12",
      "page": 2,
      "difficulty": "easy",
      "primaryUnitId": "nanyi-9-1-3-1",
      "unitIds": ["nanyi-9-1-3-1"],
      "unitAssignmentBasis": "直角三角形三邊成等差數列的邊長比與周長計算。",
      "blocks": [
        {
          "type": "text",
          "text": "若一直角三角形的三邊長呈現等差數列，則當斜邊為 $10$ 時，此三角形的周長為＿＿＿＿。"
        }
      ]
    },
    # Q13
    {
      "type": "fill",
      "sourceNumber": "一-13",
      "page": 2,
      "difficulty": "medium",
      "primaryUnitId": "nanyi-9-1-1-2",
      "unitIds": ["nanyi-9-1-1-2"],
      "unitAssignmentBasis": "梯形兩對角線中點連線段性質與長度求法。",
      "blocks": [
        {
          "type": "text",
          "text": "如圖，梯形 $ABCD$ 中，$\\overline{AD} // \\overline{BC}$，$\\overline{AD} < \\overline{BC}$，且 $E$、$F$ 分別為兩對角線 $\\overline{DB}$、$\\overline{AC}$ 的中點。若 $\\overline{EF} = 6$，$\\overline{BC} = 24$，則 $\\overline{AD} = $＿＿＿＿。"
        },
        {
          "type": "svg",
          "maxHeight": 130,
          "svg": svg_q13
        }
      ]
    },
    # Q14(1)
    {
      "type": "fill",
      "sourceNumber": "一-14(1)",
      "page": 2,
      "difficulty": "easy",
      "primaryUnitId": "nanyi-9-1-3-2",
      "unitIds": ["nanyi-9-1-3-2"],
      "unitAssignmentBasis": "三角形重心分中線為 2:1 之比例性質。",
      "blocks": [
        {
          "type": "text",
          "text": "如圖，$\\triangle ABC$ 中，$D$、$E$ 分別為 $\\overline{BC}$、$\\overline{AC}$ 之中點，且 $\\overline{AD}$ 交 $\\overline{BE}$ 於 $P$ 點，求 $\\overline{AP} : \\overline{AD} = $＿＿＿＿。"
        },
        {
          "type": "svg",
          "maxHeight": 135,
          "svg": svg_q14
        }
      ]
    },
    # Q14(2)
    {
      "type": "fill",
      "sourceNumber": "一-14(2)",
      "page": 2,
      "difficulty": "easy",
      "primaryUnitId": "nanyi-9-1-3-2",
      "unitIds": ["nanyi-9-1-3-2"],
      "unitAssignmentBasis": "三角形重心三中線將三角形六等分面積之性質。",
      "blocks": [
        {
          "type": "text",
          "text": "如圖，$\\triangle ABC$ 中，$D$、$E$ 分別為 $\\overline{BC}$、$\\overline{AC}$ 之中點，且 $\\overline{AD}$ 交 $\\overline{BE}$ 於 $P$ 點。若 $\\triangle BPD$ 面積為 $4$，則 $\\triangle ABC$ 的面積＝＿＿＿＿。"
        },
        {
          "type": "svg",
          "maxHeight": 135,
          "svg": svg_q14
        }
      ]
    },
    # Q15
    {
      "type": "fill",
      "sourceNumber": "一-15",
      "page": 2,
      "difficulty": "medium",
      "primaryUnitId": "nanyi-9-1-3-2",
      "unitIds": ["nanyi-9-1-3-2", "nanyi-9-1-1-2"],
      "unitAssignmentBasis": "三角形角平分線分線段比例性質與內心頂點比例。",
      "blocks": [
        {
          "type": "text",
          "text": "如圖，$\\triangle ABC$ 中，$\\overline{AB} = 6$，$\\overline{AC} = 8$，$\\overline{BC} = 12$，$\\overline{AD}$ 平分 $\\angle BAC$，$\\overline{BI}$ 平分 $\\angle ABC$，兩線交於 $I$ 點，則 $\\overline{AI} : \\overline{ID} = $＿＿＿＿。"
        },
        {
          "type": "svg",
          "maxHeight": 110,
          "svg": svg_q15
        }
      ]
    },
    # Q16
    {
      "type": "fill",
      "sourceNumber": "一-16",
      "page": 2,
      "difficulty": "medium",
      "primaryUnitId": "nanyi-9-1-3-2",
      "unitIds": ["nanyi-9-1-3-2"],
      "unitAssignmentBasis": "等腰三角形中重心與內心位置之幾何線段距離計算。",
      "blocks": [
        {
          "type": "text",
          "text": "如圖，$I$ 點是等腰 $\\triangle ABC$ 的內心，$G$ 點是重心，$\\overline{AB} = \\overline{AC} = 10$，$\\overline{AG} = 4$，求 $\\overline{IG} = $＿＿＿＿。"
        },
        {
          "type": "svg",
          "maxHeight": 135,
          "svg": svg_q16
        }
      ]
    },
    # Q17
    {
      "type": "fill",
      "sourceNumber": "一-17",
      "page": 2,
      "difficulty": "easy",
      "primaryUnitId": "nanyi-9-1-3-2",
      "unitIds": ["nanyi-9-1-3-2"],
      "unitAssignmentBasis": "正方形內切圓與外接圓所圍環狀區域面積計算。",
      "blocks": [
        {
          "type": "text",
          "text": "如圖，設一正方形 $ABCD$ 邊長為 $8$，求此正方形內切圓及外接圓所圍的環狀區域面積＝＿＿＿＿。"
        },
        {
          "type": "svg",
          "maxHeight": 155,
          "svg": svg_q17
        }
      ]
    },
    # Q18
    {
      "type": "fill",
      "sourceNumber": "一-18",
      "page": 2,
      "difficulty": "hard",
      "primaryUnitId": "nanyi-9-1-3-2",
      "unitIds": ["nanyi-9-1-3-2"],
      "unitAssignmentBasis": "直角三角形外心、重心、內心坐標幾何距離之綜合計算。",
      "blocks": [
        {
          "type": "text",
          "text": "$O$、$G$、$I$ 三點分別為直角三角形 $ABC$ 的外心、重心與內心，兩股長 $\\overline{AB} = 18$，$\\overline{BC} = 24$，則 $\\overline{GO} - \\overline{IO} = $＿＿＿＿。"
        }
      ]
    },
    # Q19
    {
      "type": "fill",
      "sourceNumber": "一-19",
      "page": 2,
      "difficulty": "hard",
      "primaryUnitId": "nanyi-9-1-3-1",
      "unitIds": ["nanyi-9-1-3-1", "nanyi-9-1-2-2"],
      "unitAssignmentBasis": "直角三角形斜邊中線性質與等腰三角形角度綜合推理。",
      "blocks": [
        {
          "type": "text",
          "text": "如圖，$\\overline{BE} \\perp \\overline{AC}$ 於 $E$ 點，$\\overline{CD} \\perp \\overline{AB}$ 於 $D$ 點，$F$ 為 $\\overline{BC}$ 的中點，連 $\\overline{DF}$、$\\overline{EF}$、$\\overline{DE}$。若 $\\angle A = 86^\\circ$，則 $\\angle FDE = $＿＿＿＿度。"
        },
        {
          "type": "svg",
          "maxHeight": 140,
          "svg": svg_q19
        }
      ]
    },
    # Q20
    {
      "type": "fill",
      "sourceNumber": "一-20",
      "page": 2,
      "difficulty": "hard",
      "primaryUnitId": "nanyi-9-1-3-2",
      "unitIds": ["nanyi-9-1-3-2", "nanyi-9-1-1-3"],
      "unitAssignmentBasis": "相似三角形對應邊比例、圓內接四邊形判定與外心半徑求法。",
      "blocks": [
        {
          "type": "text",
          "text": "若 $A$、$E$、$C$ 三點共線，且 $\\triangle ABE \\sim \\triangle BCE \\sim \\triangle ACD$，已知 $\\overline{AB} = 5$、$\\overline{BE} = 4$，請在四邊形 $ABCD$ 中找一點 $P$ 使得 $P$ 點到 $A$、$B$、$C$、$D$ 這四點等距離，求 $\\overline{PA} = $＿＿＿＿。"
        },
        {
          "type": "svg",
          "maxHeight": 145,
          "svg": svg_q20
        }
      ]
    },
    # Q21
    {
      "type": "fill",
      "sourceNumber": "一-21",
      "page": 2,
      "difficulty": "hard",
      "primaryUnitId": "nanyi-9-1-3-2",
      "unitIds": ["nanyi-9-1-3-2", "nanyi-9-1-1-3"],
      "unitAssignmentBasis": "相似直角三角形內切圓半徑、內心坐標與四邊形分割求面積。",
      "blocks": [
        {
          "type": "text",
          "text": "若 $\\triangle ABC \\sim \\triangle DAC$，且 $B$、$C$、$D$ 三點共線，已知 $\\overline{AB} = 10$、$\\overline{AC} = 8$，若 $E$ 為 $\\triangle ABC$ 內心、$F$ 為 $\\triangle DAC$ 內心，依順序連接 $BEFD$ 四點後，求所圍成的四邊形 $BEFD$ 面積＝＿＿＿＿。"
        },
        {
          "type": "svg",
          "maxHeight": 135,
          "svg": svg_q21
        }
      ]
    },
    # 二-1
    {
      "type": "written",
      "sourceNumber": "二-1",
      "page": 3,
      "difficulty": "medium",
      "primaryUnitId": "nanyi-9-1-1-3",
      "unitIds": ["nanyi-9-1-1-3", "nanyi-9-1-1-2"],
      "unitAssignmentBasis": "正三角形中點垂線、平行線截比例線段與相似三角形面積比。",
      "blocks": [
        {
          "type": "text",
          "text": "如圖，$\\triangle ABC$ 為正三角形，$D$ 為 $\\overline{BC}$ 中點，$\\overline{DE} \\perp \\overline{AC}$ 於 $E$ 點，$\\overline{EF} // \\overline{BC}$，則："
        },
        {
          "type": "text",
          "text": "(1) $\\overline{EF} : \\overline{BC} = $＿＿＿＿。"
        },
        {
          "type": "text",
          "text": "(2) $\\triangle ABD$ 面積是 $\\triangle DCE$ 面積的＿＿＿＿倍。"
        },
        {
          "type": "svg",
          "maxHeight": 135,
          "svg": svg_p3_q1
        }
      ]
    },
    # 二-2
    {
      "type": "written",
      "sourceNumber": "二-2",
      "page": 3,
      "difficulty": "medium",
      "primaryUnitId": "nanyi-9-1-3-2",
      "unitIds": ["nanyi-9-1-3-2"],
      "unitAssignmentBasis": "三角形重心坐標性質（三頂點至直線距離之和為重心至直線距離的三倍）。",
      "blocks": [
        {
          "type": "text",
          "text": "如圖，若 $G$ 為 $\\triangle ABC$ 的重心，直線 $L$ 在 $\\triangle ABC$ 的外部，$\\overline{BD}$、$\\overline{GH}$、$\\overline{AE}$、$\\overline{CF}$ 分別垂直直線 $L$ 於 $D$、$H$、$E$、$F$。若 $\\overline{GH} = 10$，則 $\\overline{BD} + \\overline{GH} + \\overline{AE} + \\overline{CF} = ?$ "
        },
        {
          "type": "svg",
          "maxHeight": 155,
          "svg": svg_p3_q2
        }
      ]
    },
    # 二-3
    {
      "type": "written",
      "sourceNumber": "二-3",
      "page": 3,
      "difficulty": "easy",
      "primaryUnitId": "nanyi-9-1-3-2",
      "unitIds": ["nanyi-9-1-3-2"],
      "unitAssignmentBasis": "三角形重心等分面積性質之素養生活情境應用。",
      "blocks": [
        {
          "type": "text",
          "text": "魯夫一行人來到西索里卡，那裡是一個仍然保存著史前時代景觀的巨大三角叢林。叢林裡除了珍奇異獸之外，還住著三位巨人，分別統治著三塊面積大小不同的土地，為了領土的分配不均決鬥了 $100$ 年，想想看有什麼辦法可以讓三位巨人統治的面積大小是一樣的？請提出你的解決方法，每提出一種方法可得 $3$ 分最多可得 $6$ 分。"
        }
      ]
    }
  ]
}

# Write JSON
json_file = ROOT / f"research/yilan/transcribed/{paper_id}.json"
json_file.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Saved JSON to {json_file}")

# Generate Markdown
md_lines = [
    "# 中華國中 109學年度第一學期第三次段考數學科試卷 九年級",
    "",
    f"paperId: `{paper_id}`",
    "",
    "## 卷首與版面核對",
    "",
    "- 學校：宜蘭縣立中華國民中學",
    "- 試卷名稱：宜蘭縣中華國民中學一○九學年度第一學期第三次段考數學科試卷 九年級",
    "- 規範標籤：109學年度第1學期9年級第3次段考",
    f"- 來源SHA256：`{pdf_sha256}`",
    "- 頁數與題數：試卷本文2頁，第3頁為答案卷兼綜合題，含官方教師手寫解答。第一部分選擇與填空題22格、第二部分綜合題3題，合計25題（24計分項目），滿分104分（最高以100分計）完全吻合。",
    "- 向量SVG：全卷共15幅純向量幾何SVG圖形，全部使用語意化標籤，零image、零base64、零tspan、零CSS/style標籤。",
    "",
    "## 試題內文",
    "",
    "### 第一部分選擇與填空題（每格 4 分，共 88 分）",
    "",
    "1. 下列哪一個是外心？",
    "   (A) 三角形三高的交點  (B) 三角形三內角平分線的交點  (C) 三角形三邊垂直平分線的交點  (D) 三角形三中線的交點",
    "   - 難度：easy；分單元：nanyi-9-1-3-2",
    "",
    "2. 下列敘述何者正確？",
    "   (A) 若 $a \\cdot b$ 為偶數，則 $a$ 和 $b$ 皆為偶數",
    "   (B) 若 $a \\cdot b$ 為正數，則 $a$ 或 $b$ 只有一個為正數",
    "   (C) 若 $n$ 為偶數，則 $n^3$ 為奇數",
    "   (D) 若 $n$ 為任意數，則 $(n+1)^2 \\ge 2n+1$",
    "   - 難度：easy；分單元：nanyi-9-1-3-1",
    "",
    "3. 如圖，$\\overline{AC}$ 與 $\\overline{BD}$ 交於 $M$ 點，且 $\\overline{BM} = \\overline{DM}$，$\\overline{AM} = \\overline{CM}$。試問下列證明 $\\overline{BC} = \\overline{AD}$ 的過程中，哪一個選項是錯誤的？",
    "   (A) $\\because \\overline{BM} = \\overline{DM}$，$\\overline{CM} = \\overline{AM}$",
    "   (B) 且 $\\angle BMC = \\angle DMA$ (對頂角相等)",
    "   (C) $\\therefore \\triangle BMC \\cong \\triangle DMA$ ( SSS 全等性質 )",
    "   (D) 故 $\\overline{BC} = \\overline{AD}$",
    "   - 難度：easy；分單元：nanyi-9-1-3-1；含向量SVG圖形",
    "",
    "4. 如附圖，已知 $ABCD$ 是正方形，$A$ 在 $L$ 上，$\\overline{DE} \\perp L$，$\\overline{BF} \\perp L$，垂足分別為 $E$、$F$ ( $\\overline{AE} \\neq \\overline{AF}$ )。求證：$\\triangle ADE \\cong \\triangle BAF$。",
    "   從下列選項中，選出可填入 (甲) 中的正確證明過程。",
    "   (A) $\\because \\overline{DE} \\perp L$，$\\overline{BF} \\perp L$，$\\angle 7 = 90^\\circ$ $\\therefore \\overline{DE} = \\overline{BF}$",
    "   (B) $\\because \\overline{DE} \\perp L$，$\\overline{BF} \\perp L$，$\\angle 7 = 90^\\circ$ $\\therefore \\angle 1 = \\angle 4$",
    "   (C) $\\because \\angle 7 = 90^\\circ$，$\\angle 5 = \\angle 6 = 90^\\circ$ $\\therefore \\angle 2 = \\angle 3$",
    "   (D) $\\because \\angle 7 = \\angle 5 = 90^\\circ$ $\\therefore \\angle 1 + \\angle 2 = \\angle 2 + \\angle 3$ $\\therefore \\angle 1 = \\angle 3$",
    "   - 難度：medium；分單元：nanyi-9-1-3-1；含向量SVG圖形",
    "",
    "5. 下列敘述何者錯誤？",
    "   (A) 正多邊形一定有外接圓與內切圓，且它們有同心圓  (B) 正多邊形為線對稱圖形  (C) 若多邊形各內角平分線交於一點 $G$，則 $G$ 點為此多邊形的內心  (D) 多邊形的外心一定存在，且外心到各頂點等距離",
    "   - 難度：easy；分單元：nanyi-9-1-3-2",
    "",
    "6. 如圖，$\\overline{AD}$、$\\overline{BC}$ 交於 $E$ 點，根據下列何者不能證明 $\\triangle ABE \\cong \\triangle DCE$？",
    "   (A) $E$ 是 $\\overline{BC}$ 中點，且 $\\angle B = \\angle C$  (B) $\\overline{AB} // \\overline{CD}$  (C) $\\overline{AD}$、$\\overline{BC}$ 互相平分  (D) $\\overline{AB} \\perp \\overline{AD}$，$\\overline{AD} \\perp \\overline{CD}$，$\\overline{BE} = \\overline{CE}$",
    "   - 難度：easy；分單元：nanyi-9-1-3-1；含向量SVG圖形",
    "",
    "7. 如圖，$P$ 為矩形 $ABCD$ 外一點。若 $\\overline{PB} = \\overline{PC}$，則利用＿＿＿＿全等性質可得知 $\\triangle PAB \\cong \\triangle PDC$。",
    "   - 難度：easy；分單元：nanyi-9-1-3-1；含向量SVG圖形",
    "",
    "8. 若 $O$ 點為 $\\triangle ABC$ 的外心，$\\overline{OA} = 5x-3$，$\\overline{OC} = -2x+11$，則 $\\overline{OB} = $＿＿＿＿。",
    "   - 難度：easy；分單元：nanyi-9-1-3-2",
    "",
    "9. $\\triangle ABC$ 中，$\\overline{AB} = 8$，$\\overline{BC} = 12$，$\\overline{AC} = 9$，若 $\\triangle ABC$ 的內切圓半徑為 $3$，則 $\\triangle ABC$ 的面積＝＿＿＿＿。",
    "   - 難度：easy；分單元：nanyi-9-1-3-2",
    "",
    "10. 如圖，已知 $O$ 點為銳角 $\\triangle ABC$ 的外心，$\\overline{AB} = \\overline{AC} = 10$，$\\overline{BC} = 12$，且 $\\overleftrightarrow{AO}$ 交 $\\overline{BC}$ 於 $D$ 點，求 $\\triangle ABC$ 的外接圓半徑＝＿＿＿＿。",
    "    - 難度：medium；分單元：nanyi-9-1-3-2；含向量SVG圖形",
    "",
    "11. 在鈍角 $\\triangle ABC$ 中，$O$ 點為外心，若 $\\angle BAC = 150^\\circ$，則 $\\angle BOC$ 的度數＝＿＿＿＿度。",
    "    - 難度：medium；分單元：nanyi-9-1-3-2",
    "",
    "12. 若一直角三角形的三邊長呈現等差數列，則當斜邊為 $10$ 時，此三角形的周長為＿＿＿＿。",
    "    - 難度：easy；分單元：nanyi-9-1-3-1",
    "",
    "13. 如圖，梯形 $ABCD$ 中，$\\overline{AD} // \\overline{BC}$，$\\overline{AD} < \\overline{BC}$，且 $E$、$F$ 分別為兩對角線 $\\overline{DB}$、$\\overline{AC}$ 的中點。若 $\\overline{EF} = 6$，$\\overline{BC} = 24$，則 $\\overline{AD} = $＿＿＿＿。",
    "    - 難度：medium；分單元：nanyi-9-1-1-2；含向量SVG圖形",
    "",
    "14. 如圖，$\\triangle ABC$ 中，$D$、$E$ 分別為 $\\overline{BC}$、$\\overline{AC}$ 之中點，且 $\\overline{AD}$ 交 $\\overline{BE}$ 於 $P$ 點，",
    "    (1) $\\overline{AP} : \\overline{AD} = $＿＿＿＿。",
    "    (2) 若 $\\triangle BPD$ 面積為 $4$，則 $\\triangle ABC$ 的面積＝＿＿＿＿。",
    "    - 難度：easy；分單元：nanyi-9-1-3-2；含向量SVG圖形",
    "",
    "15. 如圖，$\\triangle ABC$ 中，$\\overline{AB} = 6$，$\\overline{AC} = 8$，$\\overline{BC} = 12$，$\\overline{AD}$ 平分 $\\angle BAC$，$\\overline{BI}$ 平分 $\\angle ABC$，兩線交於 $I$ 點，則 $\\overline{AI} : \\overline{ID} = $＿＿＿＿。",
    "    - 難度：medium；分單元：nanyi-9-1-3-2；含向量SVG圖形",
    "",
    "16. 如圖，$I$ 點是等腰 $\\triangle ABC$ 的內心，$G$ 點是重心，$\\overline{AB} = \\overline{AC} = 10$，$\\overline{AG} = 4$，求 $\\overline{IG} = $＿＿＿＿。",
    "    - 難度：medium；分單元：nanyi-9-1-3-2；含向量SVG圖形",
    "",
    "17. 如圖，設一正方形 $ABCD$ 邊長為 $8$，求此正方形內切圓及外接圓所圍的環狀區域面積＝＿＿＿＿。",
    "    - 難度：easy；分單元：nanyi-9-1-3-2；含向量SVG圖形",
    "",
    "18. $O$、$G$、$I$ 三點分別為直角三角形 $ABC$ 的外心、重心與內心，兩股長 $\\overline{AB} = 18$，$\\overline{BC} = 24$，則 $\\overline{GO} - \\overline{IO} = $＿＿＿＿。",
    "    - 難度：hard；分單元：nanyi-9-1-3-2",
    "",
    "19. 如圖，$\\overline{BE} \\perp \\overline{AC}$ 於 $E$ 點，$\\overline{CD} \\perp \\overline{AB}$ 於 $D$ 點，$F$ 為 $\\overline{BC}$ 的中點，連 $\\overline{DF}$、$\\overline{EF}$、$\\overline{DE}$。若 $\\angle A = 86^\\circ$，則 $\\angle FDE = $＿＿＿＿度。",
    "    - 難度：hard；分單元：nanyi-9-1-3-1；含向量SVG圖形",
    "",
    "20. 若 $A$、$E$、$C$ 三點共線，且 $\\triangle ABE \\sim \\triangle BCE \\sim \\triangle ACD$，已知 $\\overline{AB} = 5$、$\\overline{BE} = 4$，請在四邊形 $ABCD$ 中找一點 $P$ 使得 $P$ 點到 $A$、$B$、$C$、$D$ 這四點等距離，求 $\\overline{PA} = $＿＿＿＿。",
    "    - 難度：hard；分單元：nanyi-9-1-3-2；含向量SVG圖形",
    "",
    "21. 若 $\\triangle ABC \\sim \\triangle DAC$，且 $B$、$C$、$D$ 三點共線，已知 $\\overline{AB} = 10$、$\\overline{AC} = 8$，若 $E$ 為 $\\triangle ABC$ 內心、$F$ 為 $\\triangle DAC$ 內心，依順序連接 $BEFD$ 四點後，求所圍成的四邊形 $BEFD$ 面積＝＿＿＿＿。",
    "    - 難度：hard；分單元：nanyi-9-1-3-2；含向量SVG圖形",
    "",
    "### 第二部分綜合題（第 1 題各 3 分、第 2 題 4 分、第 3 題 6 分，共 16 分）",
    "",
    "1. 如圖，$\\triangle ABC$ 為正三角形，$D$ 為 $\\overline{BC}$ 中點，$\\overline{DE} \\perp \\overline{AC}$ 於 $E$ 點，$\\overline{EF} // \\overline{BC}$，則：",
    "   (1) $\\overline{EF} : \\overline{BC} = $＿＿＿＿。",
    "   (2) $\\triangle ABD$ 面積是 $\\triangle DCE$ 面積的＿＿＿＿倍。",
    "   - 難度：medium；分單元：nanyi-9-1-1-3；含向量SVG圖形",
    "2. 如圖，若 $G$ 為 $\\triangle ABC$ 的重心，直線 $L$ 在 $\\triangle ABC$ 的外部，$\\overline{BD}$、$\\overline{GH}$、$\\overline{AE}$、$\\overline{CF}$ 分別垂直直線 $L$ 於 $D$、$H$、$E$、$F$。若 $\\overline{GH} = 10$，則 $\\overline{BD} + \\overline{GH} + \\overline{AE} + \\overline{CF} = ?$ ",
    "   - 難度：medium；分單元：nanyi-9-1-3-2；含向量SVG圖形",
    "3. 魯夫一行人來到西索里卡，那裡是一個仍然保存著史前時代景觀的巨大三角叢林。叢林裡除了珍奇異獸之外，還住著三位巨人，分別統治著三塊面積大小不同的土地，為了領土的分配不均決鬥了 $100$ 年，想想看有什麼辦法可以讓三位巨人統治的面積大小是一樣的？請提出你的解決方法，每提出一種方法可得 $3$ 分最多可得 $6$ 分。",
    "   - 難度：easy；分單元：nanyi-9-1-3-2",
    "",
    "## 盤點清單與未完成原因",
    "",
    "- 大題題數與配分盤點：",
    "  - 第一部分選擇與填空題：22格，每格4分，共88分（選擇6題、填空16題）。",
    "  - 第二部分綜合題：3題（第1題2小題各3分、第2題4分、第3題6分），共16分。",
    "  - 全卷合計25題（24計分項目），總分88+16=104分（最高以100分計）完全吻合。",
    "- 向量SVG重繪盤點：全卷共15幅純向量幾何SVG圖形（無未繪製圖形），零image、零base64、零tspan、無style/class CSS。",
    "- 視覺覆核：已完整對照原卷影像 page-01、page-02、page-03 與官方教師手寫解答，所有數字、線段符號、公式無任何遺漏，無缺字，文字區塊無內嵌換行符號。",
    "- 未完成原因：無。全卷25題已全數文字化與向量化完工。",
    "",
    "## 交付資料（包好唯一JSON區塊）",
    "",
    "```json",
    json.dumps(data, ensure_ascii=False, indent=2),
    "```",
    ""
]

md_file = ROOT / f"research/yilan/transcribed/{paper_id}.md"
md_file.write_text("\n".join(md_lines), encoding="utf-8")
print(f"Saved MD to {md_file}")
