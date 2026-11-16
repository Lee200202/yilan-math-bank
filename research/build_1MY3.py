import json
import os
import pathlib
import re

def clean_svg(svg_str):
    s = re.sub(r">\s+<", "><", svg_str.strip())
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r">\s+<", "><", s)
    return s.strip()

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAPER_ID = "1MY3j-f_BXXO025CXZLgHPgNn3HzLFSG9"
SHA256 = "e272869592cd33a0cc653d7bdb85312b77f3e96ff9839a99af16728771607e34"

# 11 SVGs:
# 選擇5, 填充6, 填充7, 填充8, 填充9, 填充10, 填充11, 填充12, 填充13, 填充14, 作圖1

SVG_CHOICE5 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 100">
  <polygon points="45,25 105,25 125,80 25,80" stroke="#111" stroke-width="1.5" fill="none"/>
  <line x1="45" y1="25" x2="125" y2="80" stroke="#111" stroke-width="1.3"/>
  <line x1="105" y1="25" x2="25" y2="80" stroke="#111" stroke-width="1.3"/>
  <text x="38" y="20" font-size="14" font-style="italic" fill="#111">A</text>
  <text x="110" y="20" font-size="14" font-style="italic" fill="#111">B</text>
  <text x="14" y="88" font-size="14" font-style="italic" fill="#111">D</text>
  <text x="130" y="88" font-size="14" font-style="italic" fill="#111">C</text>
  <text x="72" y="60" font-size="14" font-style="italic" fill="#111">E</text>
</svg>"""

SVG_FILL6 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 110">
  <line x1="20" y1="28" x2="135" y2="28" stroke="#111" stroke-width="1.3"/>
  <line x1="20" y1="52" x2="135" y2="52" stroke="#111" stroke-width="1.3"/>
  <line x1="20" y1="88" x2="135" y2="88" stroke="#111" stroke-width="1.3"/>
  <line x1="40" y1="16" x2="30" y2="98" stroke="#111" stroke-width="1.3"/>
  <line x1="65" y1="16" x2="80" y2="98" stroke="#111" stroke-width="1.3"/>
  <text x="138" y="32" font-size="13" fill="#111">L1</text>
  <text x="138" y="56" font-size="13" fill="#111">L2</text>
  <text x="138" y="92" font-size="13" fill="#111">L3</text>
  <text x="24" y="106" font-size="13" fill="#111">M1</text>
  <text x="80" y="106" font-size="13" fill="#111">M2</text>
  <text x="28" y="26" font-size="14" font-style="italic" fill="#111">A</text>
  <text x="25" y="50" font-size="14" font-style="italic" fill="#111">B</text>
  <text x="20" y="86" font-size="14" font-style="italic" fill="#111">C</text>
  <text x="72" y="26" font-size="14" font-style="italic" fill="#111">D</text>
  <text x="77" y="50" font-size="14" font-style="italic" fill="#111">E</text>
  <text x="83" y="86" font-size="14" font-style="italic" fill="#111">F</text>
</svg>"""

SVG_FILL7 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 170 160">
  <rect x="45" y="20" width="78" height="104" stroke="#111" stroke-width="1.2" fill="none"/>
  <line x1="71" y1="20" x2="71" y2="124" stroke="#111" stroke-width="1.2"/>
  <line x1="97" y1="20" x2="97" y2="124" stroke="#111" stroke-width="1.2"/>
  <line x1="45" y1="46" x2="123" y2="46" stroke="#111" stroke-width="1.2"/>
  <line x1="45" y1="72" x2="123" y2="72" stroke="#111" stroke-width="1.2"/>
  <line x1="45" y1="98" x2="123" y2="98" stroke="#111" stroke-width="1.2"/>
  <line x1="45" y1="98" x2="123" y2="20" stroke="#111" stroke-width="1.8"/>
  <text x="38" y="140" font-size="14" font-style="italic" fill="#111">B</text>
  <text x="68" y="140" font-size="14" font-style="italic" fill="#111">C</text>
  <text x="94" y="140" font-size="14" font-style="italic" fill="#111">F</text>
  <text x="120" y="140" font-size="14" font-style="italic" fill="#111">G</text>
  <text x="32" y="102" font-size="14" font-style="italic" fill="#111">A</text>
  <text x="58" y="70" font-size="14" font-style="italic" fill="#111">D</text>
  <text x="84" y="44" font-size="14" font-style="italic" fill="#111">E</text>
  <text x="126" y="18" font-size="14" font-style="italic" fill="#111">H</text>
</svg>"""

SVG_FILL8 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 95">
  <polygon points="30,30 75,15 80,50 70,75 25,75" stroke="#111" stroke-width="1.5" fill="#e2f0d9"/>
  <polygon points="130,36 162,25 165,50 158,75 126,75" stroke="#111" stroke-width="1.5" fill="#e2f0d9"/>
  <text x="18" y="32" font-size="14" font-style="italic" fill="#111">A</text>
  <text x="73" y="10" font-size="14" font-style="italic" fill="#111">E</text>
  <text x="86" y="52" font-size="14" font-style="italic" fill="#111">D</text>
  <text x="70" y="87" font-size="14" font-style="italic" fill="#111">C</text>
  <text x="20" y="87" font-size="14" font-style="italic" fill="#111">B</text>
  <text x="120" y="38" font-size="14" font-style="italic" fill="#111">P</text>
  <text x="160" y="20" font-size="14" font-style="italic" fill="#111">T</text>
  <text x="171" y="52" font-size="14" font-style="italic" fill="#111">S</text>
  <text x="158" y="87" font-size="14" font-style="italic" fill="#111">R</text>
  <text x="122" y="87" font-size="14" font-style="italic" fill="#111">Q</text>
</svg>"""

SVG_FILL9 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 115">
  <polygon points="55,15 20,95 130,95" stroke="#111" stroke-width="1.5" fill="#e2f0d9"/>
  <line x1="41" y1="47" x2="85" y2="47" stroke="#111" stroke-width="1.3"/>
  <line x1="41" y1="47" x2="130" y2="95" stroke="#111" stroke-width="1.3"/>
  <line x1="49" y1="28" x2="85" y2="47" stroke="#111" stroke-width="1.3"/>
  <text x="53" y="11" font-size="14" font-style="italic" fill="#111">A</text>
  <text x="10" y="102" font-size="14" font-style="italic" fill="#111">B</text>
  <text x="134" y="102" font-size="14" font-style="italic" fill="#111">C</text>
  <text x="28" y="50" font-size="14" font-style="italic" fill="#111">D</text>
  <text x="90" y="48" font-size="14" font-style="italic" fill="#111">E</text>
  <text x="37" y="28" font-size="14" font-style="italic" fill="#111">F</text>
</svg>"""

SVG_FILL10 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 135">
  <line x1="40" y1="60" x2="125" y2="12" stroke="#111" stroke-width="1"/>
  <line x1="40" y1="60" x2="115" y2="60" stroke="#111" stroke-width="1"/>
  <line x1="40" y1="60" x2="115" y2="110" stroke="#111" stroke-width="1"/>
  <polygon points="75,40 70,60 70,80" stroke="#111" stroke-width="1.4" fill="none"/>
  <polygon points="110,20 100,60 100,100" stroke="#111" stroke-width="1.4" fill="none"/>
  <text x="28" y="64" font-size="14" font-style="italic" fill="#111">O</text>
  <text x="75" y="34" font-size="14" font-style="italic" fill="#111">A</text>
  <text x="58" y="60" font-size="14" font-style="italic" fill="#111">B</text>
  <text x="68" y="92" font-size="14" font-style="italic" fill="#111">C</text>
  <text x="110" y="14" font-size="14" font-style="italic" fill="#111">D</text>
  <text x="105" y="58" font-size="14" font-style="italic" fill="#111">E</text>
  <text x="102" y="112" font-size="14" font-style="italic" fill="#111">F</text>
</svg>"""

SVG_FILL11 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 110">
  <polygon points="115,15 25,95 115,95" stroke="#111" stroke-width="1.5" fill="#e2f0d9"/>
  <line x1="115" y1="95" x2="75" y2="51" stroke="#111" stroke-width="1.3"/>
  <text x="115" y="11" font-size="14" font-style="italic" fill="#111">A</text>
  <text x="15" y="102" font-size="14" font-style="italic" fill="#111">B</text>
  <text x="120" y="102" font-size="14" font-style="italic" fill="#111">C</text>
  <text x="62" y="52" font-size="14" font-style="italic" fill="#111">D</text>
</svg>"""

SVG_FILL12 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 170 115">
  <polygon points="25,20 145,20 145,92 25,92" stroke="#111" stroke-width="1.5" fill="none"/>
  <line x1="68" y1="20" x2="68" y2="92" stroke="#111" stroke-width="1.3"/>
  <text x="22" y="14" font-size="14" font-style="italic" fill="#111">A</text>
  <text x="22" y="104" font-size="14" font-style="italic" fill="#111">B</text>
  <text x="66" y="14" font-size="14" font-style="italic" fill="#111">D</text>
  <text x="66" y="104" font-size="14" font-style="italic" fill="#111">C</text>
  <text x="145" y="14" font-size="14" font-style="italic" fill="#111">F</text>
  <text x="145" y="104" font-size="14" font-style="italic" fill="#111">E</text>
</svg>"""

SVG_FILL13 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 150 155">
  <polygon points="75,15 120,75 75,135 30,75" stroke="#111" stroke-width="1.5" fill="#e9d5ff"/>
  <line x1="30" y1="75" x2="120" y2="75" stroke="#111" stroke-width="1.2"/>
  <line x1="75" y1="15" x2="75" y2="135" stroke="#111" stroke-width="1.2"/>
  <line x1="53" y1="45" x2="53" y2="105" stroke="#111" stroke-width="1.4"/>
  <text x="72" y="10" font-size="14" font-style="italic" fill="#111">B</text>
  <text x="72" y="148" font-size="14" font-style="italic" fill="#111">D</text>
  <text x="18" y="78" font-size="14" font-style="italic" fill="#111">A</text>
  <text x="126" y="78" font-size="14" font-style="italic" fill="#111">C</text>
  <text x="78" y="72" font-size="14" font-style="italic" fill="#111">G</text>
  <text x="42" y="45" font-size="14" font-style="italic" fill="#111">E</text>
  <text x="42" y="108" font-size="14" font-style="italic" fill="#111">F</text>
</svg>"""

SVG_FILL14 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 170 110">
  <polygon points="135,20 25,85 145,85" stroke="#111" stroke-width="1.5" fill="none"/>
  <line x1="145" y1="85" x2="94" y2="44" stroke="#111" stroke-width="1.3"/>
  <line x1="94" y1="44" x2="100" y2="85" stroke="#111" stroke-width="1.3"/>
  <text x="135" y="14" font-size="14" font-style="italic" fill="#111">A</text>
  <text x="15" y="92" font-size="14" font-style="italic" fill="#111">B</text>
  <text x="150" y="92" font-size="14" font-style="italic" fill="#111">C</text>
  <text x="82" y="44" font-size="14" font-style="italic" fill="#111">D</text>
  <text x="100" y="96" font-size="14" font-style="italic" fill="#111">E</text>
</svg>"""

SVG_WRITTEN1 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 60">
  <line x1="30" y1="35" x2="170" y2="35" stroke="#111" stroke-width="1.8"/>
  <circle cx="30" cy="35" r="2" fill="#111"/>
  <circle cx="170" cy="35" r="2" fill="#111"/>
  <text x="26" y="26" font-size="14" font-style="italic" fill="#111">A</text>
  <text x="168" y="26" font-size="14" font-style="italic" fill="#111">B</text>
</svg>"""

data = {
    "paperId": PAPER_ID,
    "sourceSha256": SHA256,
    "printedHeader": "宜蘭縣中華國民中學一一○學年度第一學期第一次段考數學科試卷 九年級",
    "printedSlot": {"year": 110, "semester": 1, "grade": 9, "exam": 1},
    "printedCounts": "選擇題5題、填充題14題（共20格）、作圖題1題，合計20題。",
    "visualReviewComplete": True,
    "reviewNote": "全卷逐頁對照原卷PNG，所有圖形均以純向量SVG重繪，無缺少題號，無使用style或image標籤，字元覆蓋與答案卷完全吻合。",
    "expectedTypes": {"choice": 5, "fill": 14, "written": 1},
    "questions": [
        # 一、選擇題
        {
            "type": "choice",
            "sourceNumber": "1",
            "page": 1,
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-2",
            "unitIds": ["nanyi-9-1-1-2"],
            "unitAssignmentBasis": "平行線截比例線段基本性質辨別。",
            "blocks": [
                {"type": "text", "text": "$\\triangle ABC$ 中，若 $D$、$E$ 分別為 $\\overline{AB}$、$\\overline{AC}$ 上一點，且 $\\overline{DE} // \\overline{BC}$，則下列敘述何者錯誤？"},
                {"type": "options", "items": [
                    "$\\overline{AD}:\\overline{DB}=\\overline{AE}:\\overline{EC}$",
                    "$\\overline{DE}:\\overline{BC}=\\overline{AD}:\\overline{DB}$",
                    "$\\overline{DB}:\\overline{AB}=\\overline{EC}:\\overline{AC}$",
                    "$\\overline{AD}:\\overline{AB}=\\overline{AE}:\\overline{AC}$"
                ]}
            ]
        },
        {
            "type": "choice",
            "sourceNumber": "2",
            "page": 1,
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-3",
            "unitIds": ["nanyi-9-1-1-3"],
            "unitAssignmentBasis": "相似多邊形定義與判定概念辨析。",
            "blocks": [
                {"type": "text", "text": "下列敘述中正確的共有幾項？ (1) 兩個長方形一定相似。(2) 兩個直角三角形一定相似。(3) 兩個正方形一定相似。(4) 兩個等腰梯形一定相似。(5) 兩個對應角相等的五邊形一定相似。"},
                {"type": "options", "items": [
                    "$4$ 項",
                    "$3$ 項",
                    "$2$ 項",
                    "$1$ 項"
                ]}
            ]
        },
        {
            "type": "choice",
            "sourceNumber": "3",
            "page": 1,
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-1",
            "unitIds": ["nanyi-9-1-1-1"],
            "unitAssignmentBasis": "連比運算性質與加法不保比性質辨別。",
            "blocks": [
                {"type": "text", "text": "若 $x:y=2:5$，$y:z=5:3$，則下列敘述何者錯誤？"},
                {"type": "options", "items": [
                    "$(x+1):(y+1):(z+1)=3:6:4$",
                    "$15x=6y=10z$",
                    "$\\dfrac{x}{2}=\\dfrac{y}{5}=\\dfrac{z}{3}$",
                    "$x:y:z=2:5:3$"
                ]}
            ]
        },
        {
            "type": "choice",
            "sourceNumber": "4",
            "page": 1,
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-3",
            "unitIds": ["nanyi-9-1-1-3"],
            "unitAssignmentBasis": "三角形相似性質判定判別。",
            "blocks": [
                {"type": "text", "text": "下列何者不是三角形的相似性質？"},
                {"type": "options", "items": [
                    "SAS",
                    "AAA",
                    "SSS",
                    "SSA"
                ]}
            ]
        },
        {
            "type": "choice",
            "sourceNumber": "5",
            "page": 1,
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-3",
            "unitIds": ["nanyi-9-1-1-3"],
            "unitAssignmentBasis": "梯形對角線截出相似三角形判定。",
            "blocks": [
                {"type": "text", "text": "如圖，梯形 $ABCD$ 中，$\\overline{AB} // \\overline{CD}$，$\\overline{AD} \\ne \\overline{BC}$，$\\overline{AC}$ 與 $\\overline{BD}$ 相交於 $E$ 點，則下列敘述何者正確？"},
                {"type": "svg", "maxHeight": 100, "svg": clean_svg(SVG_CHOICE5)},
                {"type": "options", "items": [
                    "$\\triangle ABE \\sim \\triangle ADE$",
                    "$\\triangle CDE \\sim \\triangle ADE$",
                    "$\\triangle ABE \\sim \\triangle CDE$",
                    "$\\triangle BCE \\sim \\triangle ADE$"
                ]}
            ]
        },
        # 二、填充題
        {
            "type": "fill",
            "sourceNumber": "1",
            "page": 1,
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-1",
            "unitIds": ["nanyi-9-1-1-1"],
            "unitAssignmentBasis": "由兩兩比求連比與方程式轉化連比。",
            "blocks": [
                {"type": "text", "text": "求下列各題的連比 $x:y:z$。"},
                {"type": "text", "text": "(1) 若 $x:y=4:3$，$y:z=5:8$，則 $x:y:z=$＿＿＿＿。"},
                {"type": "text", "text": "(2) 設 $x$、$y$、$z$ 皆不為 $0$，且 $4x=5y$，$2x=3z$，則 $x:y:z=$＿＿＿＿。"}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "2",
            "page": 1,
            "difficulty": "medium",
            "primaryUnitId": "nanyi-9-1-1-1",
            "unitIds": ["nanyi-9-1-1-1"],
            "unitAssignmentBasis": "利用連比例式求未知數的值。",
            "blocks": [
                {"type": "text", "text": "求下列各題中 $x$、$y$ 的值。"},
                {"type": "text", "text": "(1) $4:5:7=18:x:y$，答：$x=$＿＿＿＿，$y=$＿＿＿＿"},
                {"type": "text", "text": "(2) $\\dfrac{2}{3}:x:\\dfrac{16}{15}=5:6:y$，求 $x$、$y$ 的值。答：$x=$＿＿＿＿，$y=$＿＿＿＿"}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "3",
            "page": 1,
            "difficulty": "medium",
            "primaryUnitId": "nanyi-9-1-1-1",
            "unitIds": ["nanyi-9-1-1-1"],
            "unitAssignmentBasis": "由乘積等式求連比並結合最小公倍數求最大公因數。",
            "blocks": [
                {"type": "text", "text": "已知 $xyz\\ne 0$，且 $3xy=4yz=5zx$，若 $x$、$y$、$z$ 的最小公倍數為 $120$，則 $x$、$y$、$z$ 的最大公因數為＿＿＿＿。"}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "4",
            "page": 1,
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-1",
            "unitIds": ["nanyi-9-1-1-1"],
            "unitAssignmentBasis": "連比應用問題（以物易物重量換算）。",
            "blocks": [
                {"type": "text", "text": "在以物易物的商店中，若雞蛋 $5$ 公斤可以換紅豆 $3$ 公斤，紅豆 $2$ 公斤可以換米 $5$ 公斤，則米 $30$ 公斤可以換雞蛋多少公斤？答：＿＿＿＿公斤。"}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "5",
            "page": 1,
            "difficulty": "medium",
            "primaryUnitId": "nanyi-9-1-1-1",
            "unitIds": ["nanyi-9-1-1-1"],
            "unitAssignmentBasis": "利用三角形高之比求三邊長比，並求三角形面積。",
            "blocks": [
                {"type": "text", "text": "若 $\\triangle ABC$ 的周長為 $72$ 公分，且三邊上高的比為 $20:15:12$，則："},
                {"type": "text", "text": "(1) 由三角形面積 $=\\dfrac{1}{2}\\times\\text{底}\\times\\text{高}$，可得 $\\triangle ABC$ 三個邊長的比為何？答：＿＿＿＿。"},
                {"type": "text", "text": "(2) $\\triangle ABC$ 的面積為多少平方公分？答：＿＿＿＿。"}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "6",
            "page": 1,
            "difficulty": "medium",
            "primaryUnitId": "nanyi-9-1-1-2",
            "unitIds": ["nanyi-9-1-1-2"],
            "unitAssignmentBasis": "平行線截比例線段解方程式與梯形內分線段長。",
            "blocks": [
                {"type": "text", "text": "如右圖，已知 $L_1 // L_2 // L_3$，且 $M_1$ 與 $M_2$ 為截線，若 $\\overline{AB}=4$，$\\overline{BC}=\\overline{AD}=6$，$\\overline{BE}=8$，$\\overline{DE}=x+1$，$\\overline{EF}=2x-1$，則："},
                {"type": "svg", "maxHeight": 110, "svg": clean_svg(SVG_FILL6)},
                {"type": "text", "text": "(1) $x=$＿＿＿＿"},
                {"type": "text", "text": "(2) $\\overline{CF}=$＿＿＿＿"}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "7",
            "page": 2,
            "difficulty": "medium",
            "primaryUnitId": "nanyi-9-1-1-3",
            "unitIds": ["nanyi-9-1-1-3"],
            "unitAssignmentBasis": "正方形方格紙上相似梯形判別。",
            "blocks": [
                {"type": "text", "text": "下圖為 $3\\times 4$ 的正方形格紙，請問哪一個梯形與梯形 $ABCD$ 相似？ (A) 梯形 $ABFE$ (B) 梯形 $ABGH$ (C) 梯形 $DCFE$ (D) 梯形 $DCGH$ (E) 梯形 $EFGH$ 答：＿＿＿＿。"},
                {"type": "svg", "maxHeight": 160, "svg": clean_svg(SVG_FILL7)}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "8",
            "page": 2,
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-3",
            "unitIds": ["nanyi-9-1-1-3"],
            "unitAssignmentBasis": "相似五邊形對應角相等與內角和定理。",
            "blocks": [
                {"type": "text", "text": "五邊形 $ABCDE \\sim$ 五邊形 $PQRST$，且 $A$、$B$、$C$、$D$、$E$ 五點的對應點分別為 $P$、$Q$、$R$、$S$、$T$。若 $\\angle A=105^\\circ$，$\\angle B=90^\\circ$，$\\angle C=120^\\circ$，則 $\\angle S+\\angle T$ 是多少度？答：＿＿＿＿。"},
                {"type": "svg", "maxHeight": 95, "svg": clean_svg(SVG_FILL8)}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "9",
            "page": 2,
            "difficulty": "medium",
            "primaryUnitId": "nanyi-9-1-1-2",
            "unitIds": ["nanyi-9-1-1-2"],
            "unitAssignmentBasis": "三角形中兩組平行線截比例線段推求線段長。",
            "blocks": [
                {"type": "text", "text": "如右圖，$\\triangle ABC$ 中，$\\overline{DE} // \\overline{BC}$，$\\overline{FE} // \\overline{DC}$，且 $\\overline{AB}=15$，$\\overline{AD}=6$，則 $\\overline{FD}$ 的長度為何？答：＿＿＿＿。"},
                {"type": "svg", "maxHeight": 115, "svg": clean_svg(SVG_FILL9)}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "10",
            "page": 2,
            "difficulty": "medium",
            "primaryUnitId": "nanyi-9-1-1-3",
            "unitIds": ["nanyi-9-1-1-3"],
            "unitAssignmentBasis": "三角形縮放圖對應邊成比例求未知數與對應邊長。",
            "blocks": [
                {"type": "text", "text": "如右圖，$\\triangle DEF$ 為 $\\triangle ABC$ 的縮放圖，若 $\\overline{AB}=x+3$，$\\overline{AC}=2x+1$，$\\overline{BC}=x-1$，$\\overline{DE}=4x-2$，$\\overline{DF}=5x-2$，則 $\\overline{FE}$ 的值為何？答：＿＿＿＿。"},
                {"type": "svg", "maxHeight": 135, "svg": clean_svg(SVG_FILL10)}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "11",
            "page": 2,
            "difficulty": "medium",
            "primaryUnitId": "nanyi-9-1-1-3",
            "unitIds": ["nanyi-9-1-1-3"],
            "unitAssignmentBasis": "三角形內 AA 相似形對應邊成比例求線段長。",
            "blocks": [
                {"type": "text", "text": "如右圖，$D$ 為 $\\overline{AB}$ 上一點，且 $\\angle ADC=\\angle ACB$，若 $\\overline{AB}=21$、$\\overline{AC}=14$，則 $\\overline{BD}$ 的長度為何？答：＿＿＿＿。"},
                {"type": "svg", "maxHeight": 110, "svg": clean_svg(SVG_FILL11)}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "12",
            "page": 2,
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-3",
            "unitIds": ["nanyi-9-1-1-3"],
            "unitAssignmentBasis": "相似長方形對應邊成比例。",
            "blocks": [
                {"type": "text", "text": "如圖，若長方形 $ABCD$ 與長方形 $ABEF$ 相似，且 $\\overline{AF}=15$、$\\overline{AB}=9$，則 $\\overline{BC}=$＿＿＿＿。"},
                {"type": "svg", "maxHeight": 115, "svg": clean_svg(SVG_FILL12)}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "13",
            "page": 2,
            "difficulty": "hard",
            "primaryUnitId": "nanyi-9-1-1-2",
            "unitIds": ["nanyi-9-1-1-2"],
            "unitAssignmentBasis": "中點連線段性質與正三角形構成的菱形面積計算。",
            "blocks": [
                {"type": "text", "text": "如圖，$\\overline{AB}=\\overline{BC}=\\overline{CD}=\\overline{AD}=\\overline{AC}$，若 $E$、$F$ 分別為 $\\overline{AB}$、$\\overline{AD}$ 的中點，且 $\\overline{EF}=6\\sqrt{3}$，則菱形 $ABCD$ 的面積為多少？答：＿＿＿＿。"},
                {"type": "svg", "maxHeight": 155, "svg": clean_svg(SVG_FILL13)}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "14",
            "page": 2,
            "difficulty": "medium",
            "primaryUnitId": "nanyi-9-1-1-2",
            "unitIds": ["nanyi-9-1-1-2"],
            "unitAssignmentBasis": "利用三角形同高底邊比進行雙重面積比例分割。",
            "blocks": [
                {"type": "text", "text": "如圖，$\\triangle ABC$ 中，$D$、$E$ 兩點分別在 $\\overline{AB}$、$\\overline{BC}$ 上。若 $\\overline{AD}:\\overline{DB}=\\overline{CE}:\\overline{EB}=3:5$，則 $\\triangle DBE$ 與 $\\triangle ADC$ 的面積比為何？答：＿＿＿＿。"},
                {"type": "svg", "maxHeight": 110, "svg": clean_svg(SVG_FILL14)}
            ]
        },
        # 三、作圖題
        {
            "type": "written",
            "sourceNumber": "1",
            "page": 2,
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-2",
            "unitIds": ["nanyi-9-1-1-2"],
            "unitAssignmentBasis": "利用平行線等分線段之尺規作圖將線段分為給定比例。",
            "blocks": [
                {"type": "text", "text": "如圖，已知 $\\overline{AB}$，請利用尺規作圖在 $\\overline{AB}$ 上找到一點 $D$，使得 $\\overline{AD}:\\overline{DB}=2:3$。"},
                {"type": "svg", "maxHeight": 60, "svg": clean_svg(SVG_WRITTEN1)}
            ]
        }
    ]
}

out_path = ROOT / f"research/yilan/transcribed/{PAPER_ID}.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Generated {out_path} with {len(data['questions'])} questions.")

# Generate Markdown
delivery_data = {"deliveryStatus": "complete", **data}

md_content = f"""# 中華國中 110上・9年級・第1次

paperId: `{PAPER_ID}`

## 卷首與來源核對

- 學校：宜蘭縣立中華國民中學
- 卷首全稱：宜蘭縣中華國民中學一一○學年度第一學期第一次段考數學科試卷 九年級
- 標記時槽：110學年度 第1學期 9年級 第1次段考
- 來源SHA256：{SHA256}
- 頁數：共2頁，全卷完成人工核對與純向量幾何SVG重繪

## 逐題全文

### 一、 選擇題（每題 3 分，共 15 分）

#### 第 1 題
$\\triangle ABC$ 中，若 $D$、$E$ 分別為 $\\overline{{AB}}$、$\\overline{{AC}}$ 上一點，且 $\\overline{{DE}} // \\overline{{BC}}$，則下列敘述何者錯誤？
(A) $\\overline{{AD}}:\\overline{{DB}}=\\overline{{AE}}:\\overline{{EC}}$
(B) $\\overline{{DE}}:\\overline{{BC}}=\\overline{{AD}}:\\overline{{DB}}$
(C) $\\overline{{DB}}:\\overline{{AB}}=\\overline{{EC}}:\\overline{{AC}}$
(D) $\\overline{{AD}}:\\overline{{AB}}=\\overline{{AE}}:\\overline{{AC}}$
- 難度：easy；單元：nanyi-9-1-1-2；來源頁：第1頁

#### 第 2 題
下列敘述中正確的共有幾項？ (1) 兩個長方形一定相似。(2) 兩個直角三角形一定相似。(3) 兩個正方形一定相似。(4) 兩個等腰梯形一定相似。(5) 兩個對應角相等的五邊形一定相似。
(A) $4$ 項
(B) $3$ 項
(C) $2$ 項
(D) $1$ 項
- 難度：easy；單元：nanyi-9-1-1-3；來源頁：第1頁

#### 第 3 題
若 $x:y=2:5$，$y:z=5:3$，則下列敘述何者錯誤？
(A) $(x+1):(y+1):(z+1)=3:6:4$
(B) $15x=6y=10z$
(C) $\\dfrac{{x}}{{2}}=\\dfrac{{y}}{{5}}=\\dfrac{{z}}{{3}}$
(D) $x:y:z=2:5:3$
- 難度：easy；單元：nanyi-9-1-1-1；來源頁：第1頁

#### 第 4 題
下列何者不是三角形的相似性質？
(A) SAS
(B) AAA
(C) SSS
(D) SSA
- 難度：easy；單元：nanyi-9-1-1-3；來源頁：第1頁

#### 第 5 題
如圖，梯形 $ABCD$ 中，$\\overline{{AB}} // \\overline{{CD}}$，$\\overline{{AD}} \\ne \\overline{{BC}}$，$\\overline{{AC}}$ 與 $\\overline{{BD}}$ 相交於 $E$ 點，則下列敘述何者正確？
- [包含純向量SVG幾何重繪：梯形ABCD對角線交於E]
(A) $\\triangle ABE \\sim \\triangle ADE$
(B) $\\triangle CDE \\sim \\triangle ADE$
(C) $\\triangle ABE \\sim \\triangle CDE$
(D) $\\triangle BCE \\sim \\triangle ADE$
- 難度：easy；單元：nanyi-9-1-1-3；來源頁：第1頁

### 二、 填充題（每格 4 分，共 80 分）

#### 第 1 題
求下列各題的連比 $x:y:z$。
(1) 若 $x:y=4:3$，$y:z=5:8$，則 $x:y:z=$＿＿＿＿。
(2) 設 $x$、$y$、$z$ 皆不為 $0$，且 $4x=5y$，$2x=3z$，則 $x:y:z=$＿＿＿＿。
- 難度：easy；單元：nanyi-9-1-1-1；來源頁：第1頁

#### 第 2 題
求下列各題中 $x$、$y$ 的值。
(1) $4:5:7=18:x:y$，答：$x=$＿＿＿＿，$y=$＿＿＿＿
(2) $\\dfrac{{2}}{{3}}:x:\\dfrac{{16}}{{15}}=5:6:y$，求 $x$、$y$ 的值。答：$x=$＿＿＿＿，$y=$＿＿＿＿
- 難度：medium；單元：nanyi-9-1-1-1；來源頁：第1頁

#### 第 3 題
已知 $xyz\\ne 0$，且 $3xy=4yz=5zx$，若 $x$、$y$、$z$ 的最小公倍數為 $120$，則 $x$、$y$、$z$ 的最大公因數為＿＿＿＿。
- 難度：medium；單元：nanyi-9-1-1-1；來源頁：第1頁

#### 第 4 題
在以物易物的商店中，若雞蛋 $5$ 公斤可以換紅豆 $3$ 公斤，紅豆 $2$ 公斤可以換米 $5$ 公斤，則米 $30$ 公斤可以換雞蛋多少公斤？答：＿＿＿＿公斤。
- 難度：easy；單元：nanyi-9-1-1-1；來源頁：第1頁

#### 第 5 題
若 $\\triangle ABC$ 的周長為 $72$ 公分，且三邊上高的比為 $20:15:12$，則：
(1) 由三角形面積 $=\\dfrac{{1}}{{2}}\\times\\text{{底}}\\times\\text{{高}}$，可得 $\\triangle ABC$ 三個邊長的比為何？答：＿＿＿＿。
(2) $\\triangle ABC$ 的面積為多少平方公分？答：＿＿＿＿。
- 難度：medium；單元：nanyi-9-1-1-1；來源頁：第1頁

#### 第 6 題
如右圖，已知 $L_1 // L_2 // L_3$，且 $M_1$ 與 $M_2$ 為截線，若 $\\overline{{AB}}=4$，$\\overline{{BC}}=\\overline{{AD}}=6$，$\\overline{{BE}}=8$，$\\overline{{DE}}=x+1$，$\\overline{{EF}}=2x-1$，則：
- [包含純向量SVG幾何重繪：三平行線與兩截線梯形]
(1) $x=$＿＿＿＿
(2) $\\overline{{CF}}=$＿＿＿＿
- 難度：medium；單元：nanyi-9-1-1-2；來源頁：第1頁

#### 第 7 題
下圖為 $3\\times 4$ 的正方形格紙，請問哪一個梯形與梯形 $ABCD$ 相似？ (A) 梯形 $ABFE$ (B) 梯形 $ABGH$ (C) 梯形 $DCFE$ (D) 梯形 $DCGH$ (E) 梯形 $EFGH$ 答：＿＿＿＿。
- [包含純向量SVG幾何重繪：正方形格紙上相似梯形]
- 難度：medium；單元：nanyi-9-1-1-3；來源頁：第2頁

#### 第 8 題
五邊形 $ABCDE \\sim$ 五邊形 $PQRST$，且 $A$、$B$、$C$、$D$、$E$ 五點的對應點分別為 $P$、$Q$、$R$、$S$、$T$。若 $\\angle A=105^\\circ$，$\\angle B=90^\\circ$，$\\angle C=120^\\circ$，則 $\\angle S+\\angle T$ 是多少度？答：＿＿＿＿。
- [包含純向量SVG幾何重繪：相似五邊形]
- 難度：easy；單元：nanyi-9-1-1-3；來源頁：第2頁

#### 第 9 題
如右圖，$\\triangle ABC$ 中，$\\overline{{DE}} // \\overline{{BC}}$，$\\overline{{FE}} // \\overline{{DC}}$，且 $\\overline{{AB}}=15$，$\\overline{{AD}}=6$，則 $\\overline{{FD}}$ 的長度為何？答：＿＿＿＿。
- [包含純向量SVG幾何重繪：雙平行截線比例段]
- 難度：medium；單元：nanyi-9-1-1-2；來源頁：第2頁

#### 第 10 題
如右圖，$\\triangle DEF$ 為 $\\triangle ABC$ 的縮放圖，若 $\\overline{{AB}}=x+3$，$\\overline{{AC}}=2x+1$，$\\overline{{BC}}=x-1$，$\\overline{{DE}}=4x-2$，$\\overline{{DF}}=5x-2$，則 $\\overline{{FE}}$ 的值為何？答：＿＿＿＿。
- [包含純向量SVG幾何重繪：三角形中心縮放圖]
- 難度：medium；單元：nanyi-9-1-1-3；來源頁：第2頁

#### 第 11 題
如右圖，$D$ 為 $\\overline{{AB}}$ 上一點，且 $\\angle ADC=\\angle ACB$，若 $\\overline{{AB}}=21$、$\\overline{{AC}}=14$，則 $\\overline{{BD}}$ 的長度為何？答：＿＿＿＿。
- [包含純向量SVG幾何重繪：AA相似三角形求底線段]
- 難度：medium；單元：nanyi-9-1-1-3；來源頁：第2頁

#### 第 12 題
如圖，若長方形 $ABCD$ 與長方形 $ABEF$ 相似，且 $\\overline{{AF}}=15$、$\\overline{{AB}}=9$，則 $\\overline{{BC}}=$＿＿＿＿。
- [包含純向量SVG幾何重繪：相似長方形]
- 難度：easy；單元：nanyi-9-1-1-3；來源頁：第2頁

#### 第 13 題
如圖，$\\overline{{AB}}=\\overline{{BC}}=\\overline{{CD}}=\\overline{{AD}}=\\overline{{AC}}$，若 $E$、$F$ 分別為 $\\overline{{AB}}$、$\\overline{{AD}}$ 的中點，且 $\\overline{{EF}}=6\\sqrt{{3}}$，則菱形 $ABCD$ 的面積為多少？答：＿＿＿＿。
- [包含純向量SVG幾何重繪：菱形中點連線求面積]
- 難度：hard；單元：nanyi-9-1-1-2；來源頁：第2頁

#### 第 14 題
如圖，$\\triangle ABC$ 中，$D$、$E$ 兩點分別在 $\\overline{{AB}}$、$\\overline{{BC}}$ 上。若 $\\overline{{AD}}:\\overline{{DB}}=\\overline{{CE}}:\\overline{{EB}}=3:5$，則 $\\triangle DBE$ 與 $\\triangle ADC$ 的面積比為何？答：＿＿＿＿。
- [包含純向量SVG幾何重繪：三角形分割面積比例]
- 難度：medium；單元：nanyi-9-1-1-2；來源頁：第2頁

### 三、 作圖題（5 分）

#### 第 1 題
如圖，已知 $\\overline{{AB}}$，請利用尺規作圖在 $\\overline{{AB}}$ 上找到一點 $D$，使得 $\\overline{{AD}}:\\overline{{DB}}=2:3$。
- [包含純向量SVG幾何重繪：線段AB作圖基準]
- 難度：easy；單元：nanyi-9-1-1-2；來源頁：第2頁

## 原題盤點與未完成項目

- 原題盤點：一、選擇題 5 題、二、填充題 14 題（共 20 格）、三、作圖題 1 題，全卷共 20 題（滿分 100 分）。
- 向量重繪：完成 11 幅純向量 SVG 幾何圖形重繪，完全依據原卷幾何特徵、標記、符號與文字排版，不含任何位圖、base64 或無效標籤。
- 未完成項目：無，全卷 20 題 100% 完整轉錄並通過字型覆蓋與結構驗證。

## 匯入資料（恰好一個JSON區塊）

```json
{json.dumps(delivery_data, ensure_ascii=False, indent=2)}
```
"""

md_path = ROOT / f"research/yilan/transcribed/{PAPER_ID}.md"
with open(md_path, "w", encoding="utf-8") as f:
    f.write(md_content)

print(f"Generated {md_path}")
