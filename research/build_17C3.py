"""Build transcription JSON for paper 17C3PWkCd70-YBrSqFByUL8cWZzbp1PcB
宜蘭縣中華國民中學一一○學年度第一學期第三次段考數學科試卷 九年級
"""
import hashlib
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent

paper_id = "17C3PWkCd70-YBrSqFByUL8cWZzbp1PcB"
pdf_path = ROOT / f"public/papers/{paper_id}.pdf"
pdf_sha256 = hashlib.sha256(pdf_path.read_bytes()).hexdigest()

def clean_svg(s: str) -> str:
    s = re.sub(r'<!--.*?-->', '', s, flags=re.DOTALL)
    s = re.sub(r'>\s+<', '><', s)
    return s.strip()

font_italic = 'font-family="\'TW-Kai\', \'BiauKai\', \'DFKai-SB\', serif" font-size="14" font-style="italic"'
font_roman = 'font-family="\'TW-Kai\', \'BiauKai\', \'DFKai-SB\', serif" font-size="13"'
font_small = 'font-family="\'TW-Kai\', \'BiauKai\', \'DFKai-SB\', serif" font-size="11"'

# 1. Q3 SVG: Triangle ABC with axis of symmetry AD, midpoint E
svg_q3 = clean_svg(f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 155 135" width="155" height="135">
  <polygon points="75,20 25,110 125,110" fill="none" stroke="#111" stroke-width="1.5" />
  <line x1="75" y1="20" x2="75" y2="110" stroke="#111" stroke-width="1.4" />
  <line x1="75" y1="110" x2="50" y2="65" stroke="#111" stroke-width="1.4" />
  <polyline points="75,102 83,102 83,110" fill="none" stroke="#111" stroke-width="1.2" />
  <g {font_italic} fill="#111">
    <text x="75" y="14" text-anchor="middle">A</text>
    <text x="14" y="115">B</text>
    <text x="130" y="115">C</text>
    <text x="72" y="124">D</text>
    <text x="38" y="62">E</text>
  </g>
</svg>""")

# 2. Q4 SVG: Triangle ABC, bisector L1 with R, AQ with P, PS perpendicular to AC
svg_q4 = clean_svg(f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 165 135" width="165" height="135">
  <polygon points="70,25 25,110 145,110" fill="none" stroke="#111" stroke-width="1.5" />
  <line x1="15" y1="50" x2="105" y2="98" stroke="#111" stroke-width="1.3" />
  <line x1="70" y1="25" x2="80" y2="110" stroke="#111" stroke-width="1.4" />
  <line x1="73" y1="51" x2="94" y2="52" stroke="#111" stroke-width="1.3" />
  <polyline points="47,62 53,65 50,71" fill="none" stroke="#111" stroke-width="1.1" />
  <polyline points="91,48 94,45 97,49" fill="none" stroke="#111" stroke-width="1.1" />
  <g {font_italic} fill="#111">
    <text x="70" y="16" text-anchor="middle">A</text>
    <text x="14" y="115">B</text>
    <text x="150" y="115">C</text>
    <text x="12" y="46">L₁</text>
    <text x="36" y="68">R</text>
    <text x="63" y="56">P</text>
    <text x="78" y="124">Q</text>
    <text x="100" y="50">S</text>
  </g>
</svg>""")

# 3. Q5 SVG: Triangle ABC with AD and angles 1, 2
svg_q5 = clean_svg(f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 150 130" width="150" height="130">
  <polygon points="75,25 25,105 125,105" fill="none" stroke="#111" stroke-width="1.5" />
  <line x1="75" y1="25" x2="75" y2="105" stroke="#111" stroke-width="1.4" />
  <g {font_italic} fill="#111">
    <text x="75" y="16" text-anchor="middle">A</text>
    <text x="14" y="110">B</text>
    <text x="130" y="110">C</text>
    <text x="72" y="120">D</text>
  </g>
  <g {font_small} fill="#111">
    <text x="66" y="98">1</text>
    <text x="78" y="98">2</text>
  </g>
</svg>""")

# 4. Q7 SVG: Isosceles triangle ABC with CD
svg_q7 = clean_svg(f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 115 145" width="115" height="145">
  <polygon points="50,25 25,125 75,125" fill="#e0f2fe" stroke="#111" stroke-width="1.5" />
  <line x1="75" y1="125" x2="35" y2="85" stroke="#111" stroke-width="1.3" stroke-dasharray="2,2" />
  <g {font_italic} fill="#111">
    <text x="50" y="16" text-anchor="middle">A</text>
    <text x="12" y="132">B</text>
    <text x="82" y="132">C</text>
    <text x="24" y="85">D</text>
  </g>
</svg>""")

# 5. Q8 SVG: Square ABCD and square AEFG
svg_q8 = clean_svg(f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 155 135" width="155" height="135">
  <rect x="50" y="40" width="70" height="70" fill="none" stroke="#111" stroke-width="1.5" />
  <rect x="15" y="40" width="35" height="35" fill="#e0f2fe" stroke="#111" stroke-width="1.3" />
  <polygon points="50,40 120,40 50,75" fill="#fce7f3" stroke="none" />
  <line x1="120" y1="40" x2="50" y2="75" stroke="#111" stroke-width="1.4" />
  <line x1="50" y1="110" x2="15" y2="40" stroke="#111" stroke-width="1.4" />
  <g {font_italic} fill="#111">
    <text x="6" y="38">G</text>
    <text x="48" y="30">A</text>
    <text x="126" y="38">D</text>
    <text x="4" y="82">F</text>
    <text x="56" y="75">E</text>
    <text x="48" y="124">B</text>
    <text x="126" y="120">C</text>
  </g>
</svg>""")

# 6. Q11 SVG: Triangle ABC with dashed outline
svg_q11 = clean_svg(f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 140 115" width="140" height="115">
  <polygon points="70,25 30,95 110,95" fill="none" stroke="#111" stroke-width="1.4" stroke-dasharray="3,3" />
  <g {font_italic} fill="#111">
    <text x="70" y="16" text-anchor="middle">A</text>
    <text x="18" y="102">B</text>
    <text x="116" y="102">C</text>
  </g>
</svg>""")

# 7. Q12 SVG: Right triangle ABC with centroid G
svg_q12 = clean_svg(f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 135 125" width="135" height="125">
  <polygon points="25,95 95,95 95,30" fill="#fce7f3" stroke="#111" stroke-width="1.5" />
  <line x1="95" y1="30" x2="60" y2="95" stroke="#111" stroke-width="1.3" />
  <line x1="95" y1="95" x2="60" y2="62.5" stroke="#111" stroke-width="1.3" />
  <polyline points="87,95 87,87 95,87" fill="none" stroke="#111" stroke-width="1.2" />
  <circle cx="72" cy="73" r="2" fill="#111" />
  <g {font_italic} fill="#111">
    <text x="95" y="22" text-anchor="middle">A</text>
    <text x="102" y="102">B</text>
    <text x="14" y="102">C</text>
    <text x="56" y="108">D</text>
    <text x="48" y="60">E</text>
    <text x="76" y="70">G</text>
  </g>
</svg>""")

# 8. Q17 SVG: Triangle ABC, centroid G, line AGD, GE perpendicular to BC
svg_q17 = clean_svg(f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 145 130" width="145" height="130">
  <polygon points="100,25 20,105 125,105" fill="none" stroke="#111" stroke-width="1.5" />
  <line x1="100" y1="25" x2="72" y2="105" stroke="#111" stroke-width="1.3" />
  <line x1="82" y1="70" x2="82" y2="105" stroke="#111" stroke-width="1.3" />
  <polyline points="82,97 88,97 88,105" fill="none" stroke="#111" stroke-width="1.2" />
  <circle cx="82" cy="70" r="2" fill="#111" />
  <g {font_italic} fill="#111">
    <text x="100" y="18" text-anchor="middle">A</text>
    <text x="10" y="112">B</text>
    <text x="64" y="118">D</text>
    <text x="82" y="118">E</text>
    <text x="130" y="112">C</text>
    <text x="72" y="70">G</text>
  </g>
</svg>""")

# 9. Part 2 Q1 SVG: Triangle ABC, incenter I, DE // BC
svg_p2_q1 = clean_svg(f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 150 130" width="150" height="130">
  <polygon points="75,25 30,110 125,110" fill="#fef9c3" stroke="#111" stroke-width="1.5" />
  <line x1="45" y1="80" x2="105" y2="80" stroke="#111" stroke-width="1.4" />
  <circle cx="75" cy="80" r="2.5" fill="#111" />
  <g {font_italic} fill="#111">
    <text x="75" y="16" text-anchor="middle">A</text>
    <text x="20" y="118">B</text>
    <text x="130" y="118">C</text>
    <text x="34" y="82">D</text>
    <text x="110" y="82">E</text>
    <text x="75" y="94" text-anchor="middle">I</text>
  </g>
</svg>""")

# 10. Part 2 Q2 SVG: Symmetric figure with AB=AC, AD=AE
svg_p2_q2 = clean_svg(f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 150 135" width="150" height="135">
  <line x1="75" y1="20" x2="30" y2="115" stroke="#111" stroke-width="1.5" />
  <line x1="75" y1="20" x2="120" y2="115" stroke="#111" stroke-width="1.5" />
  <line x1="45" y1="70" x2="120" y2="115" stroke="#111" stroke-width="1.4" />
  <line x1="105" y1="70" x2="30" y2="115" stroke="#111" stroke-width="1.4" />
  <g {font_italic} fill="#111">
    <text x="75" y="14" text-anchor="middle">A</text>
    <text x="32" y="68">B</text>
    <text x="112" y="68">C</text>
    <text x="20" y="125">D</text>
    <text x="124" y="125">E</text>
  </g>
</svg>""")

# 11. Part 2 Q3 SVG: Triangle ABC with medians and shaded triangle GBH
svg_p2_q3 = clean_svg(f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 155 135" width="155" height="135">
  <polygon points="20,110 93,110 72,80" fill="#cbd5e1" stroke="none" />
  <polygon points="65,20 20,110 130,110" fill="none" stroke="#111" stroke-width="1.5" />
  <line x1="20" y1="110" x2="97.5" y2="65" stroke="#111" stroke-width="1.3" />
  <line x1="130" y1="110" x2="42.5" y2="65" stroke="#111" stroke-width="1.3" />
  <line x1="72" y1="80" x2="93" y2="110" stroke="#111" stroke-width="1.3" />
  <circle cx="72" cy="80" r="2" fill="#111" />
  <g {font_italic} fill="#111">
    <text x="65" y="14" text-anchor="middle">A</text>
    <text x="10" y="118">B</text>
    <text x="134" y="118">C</text>
    <text x="92" y="124">H</text>
    <text x="104" y="65">D</text>
    <text x="30" y="65">E</text>
    <text x="74" y="74">G</text>
  </g>
</svg>""")

# 12. Part 2 Q4 SVG: Right triangle ABC, CD, and centroids G1, G2
svg_p2_q4 = clean_svg(f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 135 125" width="135" height="125">
  <polygon points="20,95 95,95 95,25" fill="none" stroke="#111" stroke-width="1.5" />
  <line x1="95" y1="95" x2="57.5" y2="60" stroke="#111" stroke-width="1.3" />
  <line x1="57" y1="83" x2="83" y2="60" stroke="#111" stroke-width="1.3" stroke-dasharray="2,2" />
  <polyline points="87,95 87,87 95,87" fill="none" stroke="#111" stroke-width="1.2" />
  <circle cx="57" cy="83" r="2" fill="#111" />
  <circle cx="83" cy="60" r="2" fill="#111" />
  <g {font_italic} fill="#111">
    <text x="95" y="18" text-anchor="middle">A</text>
    <text x="10" y="102">B</text>
    <text x="102" y="102">C</text>
    <text x="46" y="56">D</text>
    <text x="44" y="85">G₁</text>
    <text x="88" y="56">G₂</text>
  </g>
</svg>""")

data = {
  "paperId": paper_id,
  "sourceSha256": pdf_sha256,
  "printedHeader": "宜蘭縣中華國民中學一一○學年度第一學期第三次段考數學科試卷 九年級",
  "printedSlot": {
    "year": 110,
    "semester": 1,
    "grade": 9,
    "exam": 3
  },
  "deliveryStatus": "complete",
  "printedCounts": "第一部分選填題19格（含選擇7題、填空12題）、第二部分證明計算題4題，合計23題（24計分項目）。",
  "visualReviewComplete": True,
  "reviewNote": "全卷逐頁逐題完整對照（試卷2頁含原卷手寫解答），忠實重繪全部12幅純向量幾何SVG圖形，無任何失真或缺字。",
  "expectedTypes": {
    "choice": 7,
    "fill": 12,
    "written": 4
  },
  "questions": [
    # 第一部分選填題（每格 4 分，共 76 分）
    # Q1(1)
    {
      "type": "choice",
      "sourceNumber": "一-1(1)",
      "page": 1,
      "difficulty": "easy",
      "primaryUnitId": "nanyi-9-1-3-2",
      "unitIds": ["nanyi-9-1-3-2"],
      "unitAssignmentBasis": "三角形外心定義為三邊中垂線交點。",
      "blocks": [
        {
          "type": "text",
          "text": "有關三角形的三心，外心為三角形三條何者的交點？"
        },
        {
          "type": "options",
          "items": [
            "中垂線",
            "角平分線",
            "中線",
            "高"
          ]
        }
      ]
    },
    # Q1(2)
    {
      "type": "choice",
      "sourceNumber": "一-1(2)",
      "page": 1,
      "difficulty": "easy",
      "primaryUnitId": "nanyi-9-1-3-2",
      "unitIds": ["nanyi-9-1-3-2"],
      "unitAssignmentBasis": "三角形內心定義為三內角平分線交點。",
      "blocks": [
        {
          "type": "text",
          "text": "有關三角形的三心，內心為三角形三條何者的交點？"
        },
        {
          "type": "options",
          "items": [
            "中垂線",
            "角平分線",
            "中線",
            "高"
          ]
        }
      ]
    },
    # Q1(3)
    {
      "type": "choice",
      "sourceNumber": "一-1(3)",
      "page": 1,
      "difficulty": "easy",
      "primaryUnitId": "nanyi-9-1-3-2",
      "unitIds": ["nanyi-9-1-3-2"],
      "unitAssignmentBasis": "三角形重心定義為三邊中線交點。",
      "blocks": [
        {
          "type": "text",
          "text": "有關三角形的三心，重心為三角形三條何者的交點？"
        },
        {
          "type": "options",
          "items": [
            "中垂線",
            "角平分線",
            "中線",
            "高"
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
      "unitAssignmentBasis": "奇數與偶數的代數性質與推理證明判斷。",
      "blocks": [
        {
          "type": "text",
          "text": "已知 $a$ 為奇數，$b$ 為偶數，下列敘述何者錯誤？"
        },
        {
          "type": "options",
          "items": [
            "$a$ 的平方被 $4$ 除後餘數必為 $1$",
            "$b$ 的平方必為 $4$ 的倍數",
            "$b$ 的正平方根必為偶數",
            "四個連續整數的和必為偶數"
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
      "unitIds": ["nanyi-9-1-3-1", "nanyi-9-1-1-2"],
      "unitAssignmentBasis": "等腰三角形對稱軸性質與直角三角形斜邊中線性質。",
      "blocks": [
        {
          "type": "text",
          "text": "如圖，$\\overline{AD}$ 是 $\\triangle ABC$ 的對稱軸，$\\overline{AB} \\neq \\overline{BC}$，若 $E$ 是 $\\overline{AB}$ 的中點，則下列何者錯誤？"
        },
        {
          "type": "svg",
          "maxHeight": 135,
          "svg": svg_q3
        },
        {
          "type": "options",
          "items": [
            "$\\triangle ABD \\cong \\triangle ACD$",
            "$\\overline{AE} = \\overline{DE}$",
            "$\\overline{DE} // \\overline{AC}$",
            "$\\overline{DE} = \\overline{BD}$"
          ]
        }
      ]
    },
    # Q4
    {
      "type": "choice",
      "sourceNumber": "一-4",
      "page": 1,
      "difficulty": "easy",
      "primaryUnitId": "nanyi-9-1-3-1",
      "unitIds": ["nanyi-9-1-3-1"],
      "unitAssignmentBasis": "垂直平分線性質與角平分線性質的推論與應用。",
      "blocks": [
        {
          "type": "text",
          "text": "如圖，$\\triangle ABC$ 中，$\\overline{AB} \\neq \\overline{AC}$，直線 $L_1$ 為 $\\overline{AB}$ 的垂直平分線，與 $\\overline{AB}$ 交於 $R$；$\\overline{AQ}$ 為 $\\angle BAC$ 的平分線且交 $L_1$ 於 $P$，交 $\\overline{BC}$ 於 $Q$ 點，若 $\\overline{PS} \\perp \\overline{AC}$ 於 $S$，則下列三個推論何者正確？(甲) $\\overline{AP} = \\overline{BP}$ (乙) $\\overline{BP} = \\overline{CP}$ (丙) $\\overline{PR} = \\overline{PS}$。"
        },
        {
          "type": "svg",
          "maxHeight": 135,
          "svg": svg_q4
        },
        {
          "type": "options",
          "items": [
            "甲",
            "丙",
            "甲乙丙",
            "甲丙"
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
      "primaryUnitId": "nanyi-9-1-3-1",
      "unitIds": ["nanyi-9-1-3-1"],
      "unitAssignmentBasis": "幾何推理證明的步驟順序排列（SSS 全等證明）。",
      "blocks": [
        {
          "type": "text",
          "text": "如圖，$\\triangle ABC$ 中，$\\overline{AB} = \\overline{AC}$，$\\overline{BD} = \\overline{CD}$。證明 $\\overline{AD} \\perp \\overline{BC}$。則下列其推理證明的步驟順序為何？"
        },
        {
          "type": "text",
          "text": "(甲) $\\because \\overline{AB} = \\overline{AC}$，$\\overline{BD} = \\overline{CD}$，$\\overline{AD} = \\overline{AD}$；(乙) $\\therefore \\triangle ABD \\cong \\triangle ACD$ (SSS 全等性質)；(丙) $\\because \\angle 1 = \\angle 2$，又 $\\angle 1 + \\angle 2 = 180^\\circ$，$\\therefore \\angle 1 = \\angle 2 = 90^\\circ$；(丁) 故 $\\overline{AD} \\perp \\overline{BC}$。"
        },
        {
          "type": "svg",
          "maxHeight": 130,
          "svg": svg_q5
        },
        {
          "type": "options",
          "items": [
            "甲 $\\to$ 乙 $\\to$ 丙 $\\to$ 丁",
            "丙 $\\to$ 乙 $\\to$ 甲 $\\to$ 丁",
            "甲 $\\to$ 丙 $\\to$ 丁 $\\to$ 乙",
            "乙 $\\to$ 丙 $\\to$ 丁 $\\to$ 甲"
          ]
        }
      ]
    },
    # Q6
    {
      "type": "fill",
      "sourceNumber": "一-6",
      "page": 1,
      "difficulty": "medium",
      "primaryUnitId": "nanyi-9-1-3-2",
      "unitIds": ["nanyi-9-1-3-2", "nanyi-9-1-2-2"],
      "unitAssignmentBasis": "三角形外心與頂角關係（銳角與鈍角三角形分類討論）。",
      "blocks": [
        {
          "type": "text",
          "text": "$\\triangle ABC$ 中，$O$ 點為外心，若 $\\angle BOC = 130^\\circ$，則 $\\angle BAC = $＿＿＿＿度。"
        }
      ]
    },
    # Q7
    {
      "type": "fill",
      "sourceNumber": "一-7",
      "page": 1,
      "difficulty": "medium",
      "primaryUnitId": "nanyi-9-1-1-3",
      "unitIds": ["nanyi-9-1-1-3"],
      "unitAssignmentBasis": "等腰三角形中構造相似三角形求線段長。",
      "blocks": [
        {
          "type": "text",
          "text": "等腰 $\\triangle ABC$ 中，$\\overline{AB} = \\overline{AC} = 16$，$\\overline{BC} = 8$，過 $C$ 點作 $\\overline{CD} = \\overline{BC}$，交 $\\overline{AB}$ 於 $D$ 點，則 $\\overline{AD} = $＿＿＿＿。"
        },
        {
          "type": "svg",
          "maxHeight": 145,
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
      "primaryUnitId": "nanyi-9-1-3-1",
      "unitIds": ["nanyi-9-1-3-1"],
      "unitAssignmentBasis": "正方形性質與 SAS 三角形全等性質判定。",
      "blocks": [
        {
          "type": "text",
          "text": "如圖，四邊形 $ABCD$ 及四邊形 $AEFG$ 皆為正方形，其中 $E$ 點在 $\\overline{AB}$ 上。利用＿＿＿＿全等性質可知 $\\triangle ADE \\cong \\triangle ABG$。"
        },
        {
          "type": "svg",
          "maxHeight": 135,
          "svg": svg_q8
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
      "unitAssignmentBasis": "外心到三頂點等距之性質列式求外接圓半徑。",
      "blocks": [
        {
          "type": "text",
          "text": "若 $O$ 點為 $\\triangle ABC$ 的外心，且 $\\overline{OA} = 5x+8$、$\\overline{OB} = 3x+8$，則 $\\overline{CO}$ 為＿＿＿＿。"
        }
      ]
    },
    # Q10
    {
      "type": "fill",
      "sourceNumber": "一-10",
      "page": 1,
      "difficulty": "easy",
      "primaryUnitId": "nanyi-9-1-3-2",
      "unitIds": ["nanyi-9-1-3-2"],
      "unitAssignmentBasis": "直角三角形外心為斜邊中點及外接圓面積計算。",
      "blocks": [
        {
          "type": "text",
          "text": "$O$ 點為 $\\triangle ABC$ 的外心，$\\overline{AO}$ 交 $\\overline{BC}$ 於 $D$ 點，若 $\\overline{AB} = 8$，$\\overline{AC} = 15$，$\\overline{BC} = 17$，則 $\\triangle ABC$ 外接圓面積為＿＿＿＿。"
        }
      ]
    },
    # Q11
    {
      "type": "fill",
      "sourceNumber": "一-11",
      "page": 2,
      "difficulty": "easy",
      "primaryUnitId": "nanyi-9-1-3-2",
      "unitIds": ["nanyi-9-1-3-2"],
      "unitAssignmentBasis": "等腰三角形面積與內切圓半徑公式求法。",
      "blocks": [
        {
          "type": "text",
          "text": "如圖，$\\triangle ABC$ 中，$\\overline{AB} = \\overline{AC} = 5$、$\\overline{BC} = 6$，則其內切圓半徑為＿＿＿＿。"
        },
        {
          "type": "svg",
          "maxHeight": 115,
          "svg": svg_q11
        }
      ]
    },
    # Q12
    {
      "type": "fill",
      "sourceNumber": "一-12",
      "page": 2,
      "difficulty": "medium",
      "primaryUnitId": "nanyi-9-1-3-2",
      "unitIds": ["nanyi-9-1-3-2"],
      "unitAssignmentBasis": "直角三角形斜邊中線長等於斜邊一半及重心分比性質。",
      "blocks": [
        {
          "type": "text",
          "text": "如圖，若 $G$ 點為直角 $\\triangle ABC$ 的重心，其中 $D$、$E$ 分別在 $\\overline{BC}$、$\\overline{AC}$ 上，且 $\\overline{AC} = 18$，則 $\\overline{EG}$ 長度為＿＿＿＿。"
        },
        {
          "type": "svg",
          "maxHeight": 125,
          "svg": svg_q12
        }
      ]
    },
    # Q13
    {
      "type": "fill",
      "sourceNumber": "一-13",
      "page": 2,
      "difficulty": "easy",
      "primaryUnitId": "nanyi-9-1-3-2",
      "unitIds": ["nanyi-9-1-3-2"],
      "unitAssignmentBasis": "正三角形內切圓半徑計算。",
      "blocks": [
        {
          "type": "text",
          "text": "若正 $\\triangle ABC$ 的邊長為 $3$，則其內切圓的半徑為＿＿＿＿。"
        }
      ]
    },
    # Q14
    {
      "type": "fill",
      "sourceNumber": "一-14",
      "page": 2,
      "difficulty": "easy",
      "primaryUnitId": "nanyi-9-1-3-1",
      "unitIds": ["nanyi-9-1-3-1"],
      "unitAssignmentBasis": "直角三角形三邊成等差數列比例性質代入求比值。",
      "blocks": [
        {
          "type": "text",
          "text": "若一個直角三角形的三邊長成等差數列，且三角形三邊長從小排到大分別為 $a$、$b$、$c$，則 $(a+b+c) : (a+2b-c) = $＿＿＿＿。"
        }
      ]
    },
    # Q15
    {
      "type": "fill",
      "sourceNumber": "一-15",
      "page": 2,
      "difficulty": "easy",
      "primaryUnitId": "nanyi-9-1-3-2",
      "unitIds": ["nanyi-9-1-3-2"],
      "unitAssignmentBasis": "等腰三角形重心三等分面積性質。",
      "blocks": [
        {
          "type": "text",
          "text": "等腰 $\\triangle ABC$ 中，$\\overline{AB} = \\overline{AC} = 13$，若 $G$ 點為重心，且 $\\overline{AG} = 8$，則 $\\triangle ABG$ 面積為＿＿＿＿。"
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
      "unitAssignmentBasis": "等腰直角三角形外心與內心座標及兩點距離計算。",
      "blocks": [
        {
          "type": "text",
          "text": "等腰直角 $\\triangle ABC$ 中，$\\angle ACB = 90^\\circ$，$\\overline{AB} = 24$，$O$、$I$ 兩點分別為 $\\triangle ABC$ 的外心與內心，則 $\\overline{IO} = $＿＿＿＿。"
        }
      ]
    },
    # Q17
    {
      "type": "fill",
      "sourceNumber": "一-17",
      "page": 2,
      "difficulty": "medium",
      "primaryUnitId": "nanyi-9-1-3-2",
      "unitIds": ["nanyi-9-1-3-2"],
      "unitAssignmentBasis": "三角形重心線段比例及畢氏定理求中線長。",
      "blocks": [
        {
          "type": "text",
          "text": "如圖，$G$ 為 $\\triangle ABC$ 的重心，直線 $AG$ 與 $\\overline{BC}$ 相交於 $D$ 點，$E$ 點在 $\\overline{CD}$ 上且 $\\overline{GE} \\perp \\overline{BC}$。若 $\\overline{BE} = 14$，$\\overline{CE} = 8$，$\\overline{GE} = 4$，則 $\\overline{AG}$ 的長度為＿＿＿＿。"
        },
        {
          "type": "svg",
          "maxHeight": 130,
          "svg": svg_q17
        }
      ]
    },

    # 第二部分證明計算題（須寫上過程，否則不給分，共 24 分）
    # Q1 (written)
    {
      "type": "written",
      "sourceNumber": "二-1",
      "page": 2,
      "difficulty": "medium",
      "primaryUnitId": "nanyi-9-1-3-2",
      "unitIds": ["nanyi-9-1-3-2", "nanyi-9-1-1-3"],
      "unitAssignmentBasis": "三角形內心平行線構造等腰三角形與相似三角形面積比。",
      "blocks": [
        {
          "type": "text",
          "text": "如圖，$I$ 點為 $\\triangle ABC$ 的內心，$I$ 在 $\\overline{DE}$ 上，且 $\\overline{DE} // \\overline{BC}$。若 $\\overline{AB} = 8$、$\\overline{AC} = 7$、$\\overline{BC} = 5$，則："
        },
        {
          "type": "text",
          "text": "(1) $\\triangle ADE$ 周長為多少？"
        },
        {
          "type": "text",
          "text": "(2) $\\triangle ADE \\text{ 面積} : \\triangle ABC \\text{ 面積} = ?$ "
        },
        {
          "type": "svg",
          "maxHeight": 130,
          "svg": svg_p2_q1
        }
      ]
    },
    # Q2 (written)
    {
      "type": "written",
      "sourceNumber": "二-2",
      "page": 2,
      "difficulty": "easy",
      "primaryUnitId": "nanyi-9-1-3-1",
      "unitIds": ["nanyi-9-1-3-1"],
      "unitAssignmentBasis": "幾何全等三角形證明（SAS 全等）。",
      "blocks": [
        {
          "type": "text",
          "text": "已知：如圖，$\\overline{AB} = \\overline{AC}$，$\\overline{AD} = \\overline{AE}$。求證：$\\angle D = \\angle E$。"
        },
        {
          "type": "svg",
          "maxHeight": 135,
          "svg": svg_p2_q2
        }
      ]
    },
    # Q3 (written)
    {
      "type": "written",
      "sourceNumber": "二-3",
      "page": 2,
      "difficulty": "medium",
      "primaryUnitId": "nanyi-9-1-3-2",
      "unitIds": ["nanyi-9-1-3-2"],
      "unitAssignmentBasis": "重心面積性質與底邊分比求三角形面積比值。",
      "blocks": [
        {
          "type": "text",
          "text": "如圖，$\\overline{BD}$、$\\overline{CE}$ 為 $\\triangle ABC$ 的兩條中線，$\\overline{BH} = 2\\overline{HC}$，則 $\\triangle GBH$ 與 $\\triangle ABC$ 的面積比為何？"
        },
        {
          "type": "svg",
          "maxHeight": 135,
          "svg": svg_p2_q3
        }
      ]
    },
    # Q4 (written)
    {
      "type": "written",
      "sourceNumber": "二-4",
      "page": 2,
      "difficulty": "hard",
      "primaryUnitId": "nanyi-9-1-3-2",
      "unitIds": ["nanyi-9-1-3-2", "nanyi-9-1-1-3"],
      "unitAssignmentBasis": "兩子三角形重心連線段與相似形比例綜合計算。",
      "blocks": [
        {
          "type": "text",
          "text": "如圖，$\\triangle ABC$ 中，$\\angle ACB = 90^\\circ$，$D$ 為 $\\overline{AB}$ 上一點，$G_1$、$G_2$ 分別為 $\\triangle BCD$ 與 $\\triangle ADC$ 的重心，若 $\\overline{AC} = 9$、$\\overline{BC} = 12$，則 $\\overline{G_1G_2} = ?$ "
        },
        {
          "type": "svg",
          "maxHeight": 125,
          "svg": svg_p2_q4
        }
      ]
    }
  ]
}

out_file = ROOT / f"research/yilan/transcribed/{paper_id}.json"
out_file.parent.mkdir(parents=True, exist_ok=True)
out_file.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Saved JSON to {out_file}")

# Generate Markdown
md_lines = [
    "# 中華國中 110學年度第一學期第三次段考數學科試卷 九年級",
    "",
    f"paperId: `{paper_id}`",
    "",
    "## 卷首與版面核對",
    "",
    "- 學校：宜蘭縣立中華國民中學",
    "- 試卷名稱：宜蘭縣中華國民中學一一○學年度第一學期第三次段考數學科試卷 九年級",
    "- 規範標籤：110學年度第1學期9年級第3次段考",
    f"- 來源SHA256：`{pdf_sha256}`",
    "- 頁數與題數：試卷本文2頁，含手寫解答。第一部分選填題19格、第二部分證明計算題4題，合計23題（24計分項目），滿分100分完全吻合。",
    "- 向量SVG：全卷共12幅純向量幾何SVG圖形，全部使用語意化標籤，零image、零base64、零tspan、零CSS/style標籤。",
    "",
    "## 試題內文",
    "",
    "### 第一部分選填題（每格 4 分，共 76 分）",
    "",
    "1. 有關三角形的三心，請依照題目填入正確選項：(A) 中垂線 (B) 角平分線 (C) 中線 (D) 高",
    "   (1) 外心為三角形三條何者的交點？",
    "   (2) 內心為三角形三條何者的交點？",
    "   (3) 重心為三角形三條何者的交點？",
    "   - 難度：easy；分單元：nanyi-9-1-3-2",
    "",
    "2. 已知 $a$ 為奇數，$b$ 為偶數，下列敘述何者錯誤？",
    "   (A) $a$ 的平方被 $4$ 除後餘數必為 $1$  (B) $b$ 的平方必為 $4$ 的倍數  (C) $b$ 的正平方根必為偶數  (D) 四個連續整數的和必為偶數",
    "   - 難度：easy；分單元：nanyi-9-1-3-1",
    "",
    "3. 如圖，$\\overline{AD}$ 是 $\\triangle ABC$ 的對稱軸，$\\overline{AB} \\neq \\overline{BC}$，若 $E$ 是 $\\overline{AB}$ 的中點，則下列何者錯誤？",
    "   (A) $\\triangle ABD \\cong \\triangle ACD$  (B) $\\overline{AE} = \\overline{DE}$  (C) $\\overline{DE} // \\overline{AC}$  (D) $\\overline{DE} = \\overline{BD}$",
    "   - 難度：easy；分單元：nanyi-9-1-3-1；含向量SVG圖形",
    "",
    "4. 如圖，$\\triangle ABC$ 中，$\\overline{AB} \\neq \\overline{AC}$，直線 $L_1$ 為 $\\overline{AB}$ 的垂直平分線，與 $\\overline{AB}$ 交於 $R$；$\\overline{AQ}$ 為 $\\angle BAC$ 的平分線且交 $L_1$ 於 $P$，交 $\\overline{BC}$ 於 $Q$ 點，若 $\\overline{PS} \\perp \\overline{AC}$ 於 $S$，則下列三個推論何者正確？(甲) $\\overline{AP} = \\overline{BP}$ (乙) $\\overline{BP} = \\overline{CP}$ (丙) $\\overline{PR} = \\overline{PS}$。",
    "   (A) 甲  (B) 丙  (C) 甲乙丙  (D) 甲丙",
    "   - 難度：easy；分單元：nanyi-9-1-3-1；含向量SVG圖形",
    "",
    "5. 如圖，$\\triangle ABC$ 中，$\\overline{AB} = \\overline{AC}$，$\\overline{BD} = \\overline{CD}$。證明 $\\overline{AD} \\perp \\overline{BC}$。則下列其推理證明的步驟順序為何？",
    "   (A) 甲 $\\to$ 乙 $\\to$ 丙 $\\to$ 丁  (B) 丙 $\\to$ 乙 $\\to$ 甲 $\\to$ 丁  (C) 甲 $\\to$ 丙 $\\to$ 丁 $\\to$ 乙  (D) 乙 $\\to$ 丙 $\\to$ 丁 $\\to$ 甲",
    "   - 難度：easy；分單元：nanyi-9-1-3-1；含向量SVG圖形",
    "",
    "6. $\\triangle ABC$ 中，$O$ 點為外心，若 $\\angle BOC = 130^\\circ$，則 $\\angle BAC = $＿＿＿＿度。",
    "   - 難度：medium；分單元：nanyi-9-1-3-2",
    "",
    "7. 等腰 $\\triangle ABC$ 中，$\\overline{AB} = \\overline{AC} = 16$，$\\overline{BC} = 8$，過 $C$ 點作 $\\overline{CD} = \\overline{BC}$，交 $\\overline{AB}$ 於 $D$ 點，則 $\\overline{AD} = $＿＿＿＿。",
    "   - 難度：medium；分單元：nanyi-9-1-1-3；含向量SVG圖形",
    "",
    "8. 如圖，四邊形 $ABCD$ 及四邊形 $AEFG$ 皆為正方形，其中 $E$ 點在 $\\overline{AB}$ 上。利用＿＿＿＿全等性質可知 $\\triangle ADE \\cong \\triangle ABG$。",
    "   - 難度：easy；分單元：nanyi-9-1-3-1；含向量SVG圖形",
    "",
    "9. 若 $O$ 點為 $\\triangle ABC$ 的外心，且 $\\overline{OA} = 5x+8$、$\\overline{OB} = 3x+8$，則 $\\overline{CO}$ 為＿＿＿＿。",
    "   - 難度：easy；分單元：nanyi-9-1-3-2",
    "",
    "10. $O$ 點為 $\\triangle ABC$ 的外心，$\\overline{AO}$ 交 $\\overline{BC}$ 於 $D$ 點，若 $\\overline{AB} = 8$，$\\overline{AC} = 15$，$\\overline{BC} = 17$，則 $\\triangle ABC$ 外接圓面積為＿＿＿＿。",
    "    - 難度：easy；分單元：nanyi-9-1-3-2",
    "",
    "11. 如圖，$\\triangle ABC$ 中，$\\overline{AB} = \\overline{AC} = 5$、$\\overline{BC} = 6$，則其內切圓半徑為＿＿＿＿。",
    "    - 難度：easy；分單元：nanyi-9-1-3-2；含向量SVG圖形",
    "",
    "12. 如圖，若 $G$ 點為直角 $\\triangle ABC$ 的重心，其中 $D$、$E$ 分別在 $\\overline{BC}$、$\\overline{AC}$ 上，且 $\\overline{AC} = 18$，則 $\\overline{EG}$ 長度為＿＿＿＿。",
    "    - 難度：medium；分單元：nanyi-9-1-3-2；含向量SVG圖形",
    "",
    "13. 若正 $\\triangle ABC$ 的邊長為 $3$，則其內切圓的半徑為＿＿＿＿。",
    "    - 難度：easy；分單元：nanyi-9-1-3-2",
    "",
    "14. 若一個直角三角形的三邊長成等差數列，且三角形三邊長從小排到大分別為 $a$、$b$、$c$，則 $(a+b+c) : (a+2b-c) = $＿＿＿＿。",
    "    - 難度：easy；分單元：nanyi-9-1-3-1",
    "",
    "15. 等腰 $\\triangle ABC$ 中，$\\overline{AB} = \\overline{AC} = 13$，若 $G$ 點為重心，且 $\\overline{AG} = 8$，則 $\\triangle ABG$ 面積為＿＿＿＿。",
    "    - 難度：easy；分單元：nanyi-9-1-3-2",
    "",
    "16. 等腰直角 $\\triangle ABC$ 中，$\\angle ACB = 90^\\circ$，$\\overline{AB} = 24$，$O$、$I$ 兩點分別為 $\\triangle ABC$ 的外心與內心，則 $\\overline{IO} = $＿＿＿＿。",
    "    - 難度：medium；分單元：nanyi-9-1-3-2",
    "",
    "17. 如圖，$G$ 為 $\\triangle ABC$ 的重心，直線 $AG$ 與 $\\overline{BC}$ 相交於 $D$ 點，$E$ 點在 $\\overline{CD}$ 上且 $\\overline{GE} \\perp \\overline{BC}$。若 $\\overline{BE} = 14$，$\\overline{CE} = 8$，$\\overline{GE} = 4$，則 $\\overline{AG}$ 的長度為＿＿＿＿。",
    "    - 難度：medium；分單元：nanyi-9-1-3-2；含向量SVG圖形",
    "",
    "### 第二部分證明計算題（須寫上過程，否則不給分，共 24 分）",
    "",
    "1. 如圖，$I$ 點為 $\\triangle ABC$ 的內心，$I$ 在 $\\overline{DE}$ 上，且 $\\overline{DE} // \\overline{BC}$。若 $\\overline{AB} = 8$、$\\overline{AC} = 7$、$\\overline{BC} = 5$，則：",
    "   (1) $\\triangle ADE$ 周長為多少？",
    "   (2) $\\triangle ADE \\text{ 面積} : \\triangle ABC \\text{ 面積} = ?$ ",
    "   - 難度：medium；分單元：nanyi-9-1-3-2；含向量SVG圖形",
    "2. 已知：如圖，$\\overline{AB} = \\overline{AC}$，$\\overline{AD} = \\overline{AE}$。求證：$\\angle D = \\angle E$。",
    "   - 難度：easy；分單元：nanyi-9-1-3-1；含向量SVG圖形",
    "3. 如圖，$\\overline{BD}$、$\\overline{CE}$ 為 $\\triangle ABC$ 的兩條中線，$\\overline{BH} = 2\\overline{HC}$，則 $\\triangle GBH$ 與 $\\triangle ABC$ 的面積比為何？",
    "   - 難度：medium；分單元：nanyi-9-1-3-2；含向量SVG圖形",
    "4. 如圖，$\\triangle ABC$ 中，$\\angle ACB = 90^\\circ$，$D$ 為 $\\overline{AB}$ 上一點，$G_1$、$G_2$ 分別為 $\\triangle BCD$ 與 $\\triangle ADC$ 的重心，若 $\\overline{AC} = 9$、$\\overline{BC} = 12$，則 $\\overline{G_1G_2} = ?$ ",
    "   - 難度：hard；分單元：nanyi-9-1-3-2；含向量SVG圖形",
    "",
    "## 盤點清單與未完成原因",
    "",
    "- 大題題數與配分盤點：",
    "  - 第一部分選填題：19格，每格4分，共76分（選擇7題、填空12題）。",
    "  - 第二部分證明計算題：4題（含第1題2小題），共24分。",
    "  - 全卷合計23題（24計分項目），總分76+24=100分完全吻合。",
    "- 向量SVG重繪盤點：全卷共12幅純向量幾何SVG圖形（無未繪製圖形），零image、零base64、零tspan、無style/class CSS。",
    "- 視覺覆核：已完整對照原卷影像 page-01、page-02 與手寫解答，所有數字、線段符號、公式無任何遺漏，無缺字，文字區塊無內嵌換行符號。",
    "- 未完成原因：無。全卷23題已全數文字化與向量化完工。",
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
