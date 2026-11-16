"""Builder script for 1Qr-pmnrx6rlxD0fqQlWHaAnallMJ17I4.json (中華國中 108-1 G9 E1).
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT_PATH = ROOT / "research/yilan/transcribed/1Qr-pmnrx6rlxD0fqQlWHaAnallMJ17I4.json"

def clean_svg(svg: str) -> str:
    return ' '.join(svg.strip().split())

SVG_CHOICE_2 = """<svg viewBox="0 0 220 140" width="220" height="140" xmlns="http://www.w3.org/2000/svg">
  <line x1="20" y1="30" x2="190" y2="30" stroke="#000" stroke-width="1.5" />
  <line x1="20" y1="65" x2="190" y2="65" stroke="#000" stroke-width="1.5" />
  <line x1="20" y1="115" x2="190" y2="115" stroke="#000" stroke-width="1.5" />
  <line x1="42" y1="12" x2="62" y2="130" stroke="#000" stroke-width="1.5" />
  <line x1="150" y1="12" x2="117" y2="130" stroke="#000" stroke-width="1.5" />
  <text x="195" y="34" font-family="Kai, serif" font-size="14" font-style="italic">L₁</text>
  <text x="195" y="69" font-family="Kai, serif" font-size="14" font-style="italic">L₂</text>
  <text x="195" y="119" font-family="Kai, serif" font-size="14" font-style="italic">L₃</text>
  <text x="32" y="28" font-family="Kai, serif" font-size="15" font-style="italic">A</text>
  <text x="37" y="68" font-family="Kai, serif" font-size="15" font-style="italic">B</text>
  <text x="45" y="120" font-family="Kai, serif" font-size="15" font-style="italic">C</text>
  <text x="153" y="28" font-family="Kai, serif" font-size="15" font-style="italic">D</text>
  <text x="143" y="68" font-family="Kai, serif" font-size="15" font-style="italic">E</text>
  <text x="129" y="120" font-family="Kai, serif" font-size="15" font-style="italic">F</text>
</svg>"""

SVG_CHOICE_3 = """<svg viewBox="0 0 200 130" width="200" height="130" xmlns="http://www.w3.org/2000/svg">
  <polygon points="70,25 170,25 130,105 30,105" fill="none" stroke="#000" stroke-width="1.5" />
  <line x1="70" y1="25" x2="130" y2="105" stroke="#000" stroke-width="1.5" />
  <line x1="30" y1="105" x2="110" y2="25" stroke="#000" stroke-width="1.5" />
  <text x="65" y="18" font-family="Kai, serif" font-size="15" font-style="italic">A</text>
  <text x="110" y="18" font-family="Kai, serif" font-size="15" font-style="italic">E</text>
  <text x="175" y="22" font-family="Kai, serif" font-size="15" font-style="italic">D</text>
  <text x="15" y="115" font-family="Kai, serif" font-size="15" font-style="italic">B</text>
  <text x="135" y="115" font-family="Kai, serif" font-size="15" font-style="italic">C</text>
  <text x="92" y="58" font-family="Kai, serif" font-size="15" font-style="italic">F</text>
</svg>"""

SVG_CHOICE_4 = """<svg viewBox="0 0 180 150" width="180" height="150" xmlns="http://www.w3.org/2000/svg">
  <polygon points="75,20 25,130 155,130" fill="none" stroke="#000" stroke-width="1.5" />
  <line x1="55" y1="64" x2="107" y2="64" stroke="#000" stroke-width="1.5" />
  <path d="M 66,24 Q 15,75 22,126" fill="none" stroke="#000" stroke-width="1" stroke-dasharray="3,3" />
  <text x="3" y="78" font-family="Kai, serif" font-size="13">10</text>
  <text x="56" y="44" font-family="Kai, serif" font-size="13">4</text>
  <text x="75" y="14" font-family="Kai, serif" font-size="15" font-style="italic">A</text>
  <text x="40" y="68" font-family="Kai, serif" font-size="15" font-style="italic">D</text>
  <text x="15" y="142" font-family="Kai, serif" font-size="15" font-style="italic">B</text>
  <text x="115" y="68" font-family="Kai, serif" font-size="15" font-style="italic">E</text>
  <text x="160" y="142" font-family="Kai, serif" font-size="15" font-style="italic">C</text>
</svg>"""

SVG_FILL_3 = """<svg viewBox="0 0 180 130" width="180" height="130" xmlns="http://www.w3.org/2000/svg">
  <polygon points="90,20 25,115 155,115" fill="none" stroke="#000" stroke-width="1.5" />
  <line x1="47" y1="83" x2="133" y2="83" stroke="#000" stroke-width="1.5" />
  <text x="90" y="14" font-family="Kai, serif" font-size="15" font-style="italic">A</text>
  <text x="32" y="86" font-family="Kai, serif" font-size="15" font-style="italic">D</text>
  <text x="15" y="125" font-family="Kai, serif" font-size="15" font-style="italic">B</text>
  <text x="140" y="86" font-family="Kai, serif" font-size="15" font-style="italic">E</text>
  <text x="160" y="125" font-family="Kai, serif" font-size="15" font-style="italic">C</text>
</svg>"""

SVG_FILL_4 = """<svg viewBox="0 0 180 150" width="180" height="150" xmlns="http://www.w3.org/2000/svg">
  <polygon points="90,18 20,135 160,135" fill="none" stroke="#000" stroke-width="1.5" />
  <line x1="72" y1="47" x2="108" y2="47" stroke="#000" stroke-width="1.5" />
  <line x1="55" y1="76" x2="125" y2="76" stroke="#000" stroke-width="1.5" />
  <text x="90" y="12" font-family="Kai, serif" font-size="15" font-style="italic">A</text>
  <text x="56" y="50" font-family="Kai, serif" font-size="15" font-style="italic">F</text>
  <text x="115" y="50" font-family="Kai, serif" font-size="15" font-style="italic">G</text>
  <text x="38" y="80" font-family="Kai, serif" font-size="15" font-style="italic">D</text>
  <text x="132" y="80" font-family="Kai, serif" font-size="15" font-style="italic">E</text>
  <text x="10" y="145" font-family="Kai, serif" font-size="15" font-style="italic">B</text>
  <text x="165" y="145" font-family="Kai, serif" font-size="15" font-style="italic">C</text>
</svg>"""

SVG_FILL_5 = """<svg viewBox="0 0 190 130" width="190" height="130" xmlns="http://www.w3.org/2000/svg">
  <polygon points="47,59 25,110 165,110" fill="none" stroke="#000" stroke-width="1.5" />
  <line x1="47" y1="59" x2="47" y2="110" stroke="#000" stroke-width="1.5" />
  <path d="M 47,102 L 55,102 L 55,110" fill="none" stroke="#000" stroke-width="1" />
  <path d="M 40,63 L 44,72 L 51,68" fill="none" stroke="#000" stroke-width="1" />
  <text x="45" y="50" font-family="Kai, serif" font-size="15" font-style="italic">A</text>
  <text x="13" y="118" font-family="Kai, serif" font-size="15" font-style="italic">B</text>
  <text x="44" y="126" font-family="Kai, serif" font-size="15" font-style="italic">D</text>
  <text x="172" y="118" font-family="Kai, serif" font-size="15" font-style="italic">C</text>
</svg>"""

SVG_FILL_6 = """<svg viewBox="0 0 190 120" width="190" height="120" xmlns="http://www.w3.org/2000/svg">
  <polygon points="55,25 135,25 170,95 20,95" fill="none" stroke="#000" stroke-width="1.5" />
  <line x1="20" y1="95" x2="82" y2="25" stroke="#000" stroke-width="1.5" />
  <line x1="170" y1="95" x2="82" y2="25" stroke="#000" stroke-width="1.5" />
  <text x="45" y="20" font-family="Kai, serif" font-size="15" font-style="italic">A</text>
  <text x="80" y="18" font-family="Kai, serif" font-size="15" font-style="italic">E</text>
  <text x="142" y="20" font-family="Kai, serif" font-size="15" font-style="italic">D</text>
  <text x="10" y="105" font-family="Kai, serif" font-size="15" font-style="italic">B</text>
  <text x="175" y="105" font-family="Kai, serif" font-size="15" font-style="italic">C</text>
</svg>"""

SVG_FILL_8 = """<svg viewBox="0 0 190 130" width="190" height="130" xmlns="http://www.w3.org/2000/svg">
  <polygon points="35,20 80,115 175,115" fill="none" stroke="#000" stroke-width="1.5" />
  <line x1="73" y1="99" x2="110" y2="71" stroke="#000" stroke-width="1.5" />
  <text x="25" y="18" font-family="Kai, serif" font-size="15" font-style="italic">A</text>
  <text x="60" y="105" font-family="Kai, serif" font-size="15" font-style="italic">D</text>
  <text x="78" y="128" font-family="Kai, serif" font-size="15" font-style="italic">B</text>
  <text x="116" y="65" font-family="Kai, serif" font-size="15" font-style="italic">E</text>
  <text x="182" y="122" font-family="Kai, serif" font-size="15" font-style="italic">C</text>
</svg>"""

SVG_FILL_11 = """<svg viewBox="0 0 190 140" width="190" height="140" xmlns="http://www.w3.org/2000/svg">
  <polygon points="70,30 120,30 170,125 20,125" fill="none" stroke="#000" stroke-width="1.5" />
  <line x1="70" y1="30" x2="170" y2="125" stroke="#000" stroke-width="1.5" />
  <line x1="120" y1="30" x2="20" y2="125" stroke="#000" stroke-width="1.5" />
  <line x1="62" y1="78" x2="128" y2="78" stroke="#000" stroke-width="1.5" />
  <text x="65" y="22" font-family="Kai, serif" font-size="15" font-style="italic">A</text>
  <text x="125" y="22" font-family="Kai, serif" font-size="15" font-style="italic">B</text>
  <text x="95" y="46" font-family="Kai, serif" font-size="15" font-style="italic">G</text>
  <text x="66" y="93" font-family="Kai, serif" font-size="15" font-style="italic">E</text>
  <text x="117" y="93" font-family="Kai, serif" font-size="15" font-style="italic">F</text>
  <text x="10" y="135" font-family="Kai, serif" font-size="15" font-style="italic">D</text>
  <text x="175" y="135" font-family="Kai, serif" font-size="15" font-style="italic">C</text>
</svg>"""

SVG_FILL_12 = """<svg viewBox="0 0 200 140" width="200" height="140" xmlns="http://www.w3.org/2000/svg">
  <line x1="15" y1="115" x2="165" y2="115" stroke="#000" stroke-width="1.5" />
  <polygon points="65,37 20,115 110,115" fill="none" stroke="#000" stroke-width="1.5" />
  <polygon points="132,76 110,115 155,115" fill="none" stroke="#000" stroke-width="1.5" />
  <line x1="20" y1="115" x2="132" y2="76" stroke="#000" stroke-width="1.5" />
  <line x1="95" y1="89" x2="95" y2="115" stroke="#000" stroke-width="1.5" />
  <path d="M 95,107 L 103,107 L 103,115" fill="none" stroke="#000" stroke-width="1" />
  <text x="65" y="28" font-family="Kai, serif" font-size="15" font-style="italic">A</text>
  <text x="10" y="125" font-family="Kai, serif" font-size="15" font-style="italic">B</text>
  <text x="88" y="128" font-family="Kai, serif" font-size="15" font-style="italic">P</text>
  <text x="112" y="128" font-family="Kai, serif" font-size="15" font-style="italic">C</text>
  <text x="162" y="125" font-family="Kai, serif" font-size="15" font-style="italic">D</text>
  <text x="135" y="68" font-family="Kai, serif" font-size="15" font-style="italic">E</text>
  <text x="94" y="82" font-family="Kai, serif" font-size="15" font-style="italic">F</text>
</svg>"""

SVG_WRITTEN_1 = """<svg viewBox="0 0 240 130" width="240" height="130" xmlns="http://www.w3.org/2000/svg">
  <polygon points="85,25 15,105 115,105" fill="none" stroke="#000" stroke-width="1.5" />
  <line x1="85" y1="25" x2="60" y2="105" stroke="#000" stroke-width="1.5" />
  <line x1="85" y1="25" x2="85" y2="105" stroke="#000" stroke-width="1.5" />
  <path d="M 85,97 L 77,97 L 77,105" fill="none" stroke="#000" stroke-width="1" />
  <text x="85" y="17" font-family="Kai, serif" font-size="15" font-style="italic">B</text>
  <text x="5" y="112" font-family="Kai, serif" font-size="15" font-style="italic">C</text>
  <text x="53" y="117" font-family="Kai, serif" font-size="15" font-style="italic">P</text>
  <text x="85" y="117" font-family="Kai, serif" font-size="15" font-style="italic">Q</text>
  <text x="122" y="112" font-family="Kai, serif" font-size="15" font-style="italic">A</text>
  <polygon points="201,41 145,105 225,105" fill="none" stroke="#000" stroke-width="1.5" />
  <line x1="201" y1="41" x2="181" y2="105" stroke="#000" stroke-width="1.5" />
  <line x1="201" y1="41" x2="201" y2="105" stroke="#000" stroke-width="1.5" />
  <path d="M 201,97 L 193,97 L 193,105" fill="none" stroke="#000" stroke-width="1" />
  <text x="201" y="33" font-family="Kai, serif" font-size="15" font-style="italic">E</text>
  <text x="135" y="112" font-family="Kai, serif" font-size="15" font-style="italic">F</text>
  <text x="175" y="117" font-family="Kai, serif" font-size="15" font-style="italic">R</text>
  <text x="201" y="117" font-family="Kai, serif" font-size="15" font-style="italic">S</text>
  <text x="232" y="112" font-family="Kai, serif" font-size="15" font-style="italic">D</text>
</svg>"""

SVG_WRITTEN_2 = """<svg viewBox="0 0 200 130" width="200" height="130" xmlns="http://www.w3.org/2000/svg">
  <polygon points="100,30 25,105 165,105" fill="none" stroke="#000" stroke-width="1.5" />
  <text x="100" y="20" font-family="Kai, serif" font-size="16" font-style="italic">A</text>
  <text x="10" y="115" font-family="Kai, serif" font-size="16" font-style="italic">B</text>
  <text x="175" y="115" font-family="Kai, serif" font-size="16" font-style="italic">C</text>
</svg>"""

SVG_WRITTEN_3 = """<svg viewBox="0 0 220 130" width="220" height="130" xmlns="http://www.w3.org/2000/svg">
  <polygon points="50,10 110,10 110,70 50,70" fill="none" stroke="#000" stroke-width="1.5" />
  <polygon points="50,70 84,70 84,104 50,104" fill="none" stroke="#000" stroke-width="1.5" />
  <line x1="84" y1="104" x2="164" y2="104" stroke="#000" stroke-width="1.5" />
  <polygon points="110,10 84,70 164,104 190,44" fill="none" stroke="#000" stroke-width="1.5" />
  <line x1="110" y1="10" x2="84" y2="70" stroke="#000" stroke-width="1.5" />
  <line x1="84" y1="70" x2="164" y2="104" stroke="#000" stroke-width="1.5" />
  <text x="40" y="12" font-family="Kai, serif" font-size="15" font-style="italic">A</text>
  <text x="115" y="10" font-family="Kai, serif" font-size="15" font-style="italic">D</text>
  <text x="40" y="72" font-family="Kai, serif" font-size="15" font-style="italic">B</text>
  <text x="74" y="66" font-family="Kai, serif" font-size="15" font-style="italic">G</text>
  <text x="116" y="72" font-family="Kai, serif" font-size="15" font-style="italic">C</text>
  <text x="40" y="112" font-family="Kai, serif" font-size="15" font-style="italic">E</text>
  <text x="80" y="115" font-family="Kai, serif" font-size="15" font-style="italic">F</text>
  <text x="165" y="115" font-family="Kai, serif" font-size="15" font-style="italic">H</text>
  <text x="196" y="46" font-family="Kai, serif" font-size="15" font-style="italic">I</text>
</svg>"""


questions = [
    # 選擇題 1~5
    {
        "type": "choice",
        "sourceNumber": "1",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-1-3",
        "unitIds": ["nanyi-9-1-1-3"],
        "unitAssignmentBasis": "判斷各類多邊形（長方形、菱形、正多邊形、等腰三角形）是否必定相似之概念題",
        "blocks": [
            {
                "type": "text",
                "text": "下列敘述何者正確？"
            },
            {
                "type": "options",
                "items": [
                    "任意兩個長方形一定相似",
                    "任意兩個菱形一定相似",
                    "任意兩個正六邊形一定相似",
                    "任意兩個等腰三角形一定相似"
                ]
            }
        ]
    },
    {
        "type": "choice",
        "sourceNumber": "2",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-1-2",
        "unitIds": ["nanyi-9-1-1-2"],
        "unitAssignmentBasis": "平行線截比例線段之基本求值",
        "blocks": [
            {
                "type": "text",
                "text": "如圖，$L_1 // L_2 // L_3$。若 $\\overline{AB} : \\overline{AC} = 1 : 3$，$\\overline{DE} = 5$，則 $\\overline{EF} = ?$"
            },
            {
                "type": "svg",
                "svg": SVG_CHOICE_2
            },
            {
                "type": "options",
                "items": [
                    "15",
                    "10",
                    "5",
                    "4"
                ]
            }
        ]
    },
    {
        "type": "choice",
        "sourceNumber": "3",
        "page": 1,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-1-3",
        "unitIds": ["nanyi-9-1-1-3"],
        "unitAssignmentBasis": "平行四邊形內部利用平行線產生相似三角形求線段比",
        "blocks": [
            {
                "type": "text",
                "text": "如圖，四邊形 $ABCD$ 為平行四邊形，若 $\\overline{AE} : \\overline{ED} = 2 : 3$，則 $\\overline{EF} : \\overline{BF} = ?$"
            },
            {
                "type": "svg",
                "svg": SVG_CHOICE_3
            },
            {
                "type": "options",
                "items": [
                    "2 : 3",
                    "2 : 5",
                    "1 : 2",
                    "1 : 3"
                ]
            }
        ]
    },
    {
        "type": "choice",
        "sourceNumber": "4",
        "page": 1,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-1-2",
        "unitIds": ["nanyi-9-1-1-2"],
        "unitAssignmentBasis": "三角形中線段比能否推得平行線之逆判定分析",
        "blocks": [
            {
                "type": "text",
                "text": "在 $\\triangle ABC$ 中，$D$、$E$ 分別在 $\\overline{AB}$、$\\overline{AC}$ 上，且 $\\overline{AD} = 4$，$\\overline{AB} = 10$，則再加上以下哪一個條件後，不可以推得 $\\overline{DE} // \\overline{BC}$？"
            },
            {
                "type": "svg",
                "svg": SVG_CHOICE_4
            },
            {
                "type": "options",
                "items": [
                    "$\\overline{DE} = 6$，$\\overline{BC} = 15$",
                    "$\\overline{CE} = 9$，$\\overline{AC} = 15$",
                    "$\\overline{AE} = 6$，$\\overline{CE} = 9$",
                    "$\\overline{AE} = 6$，$\\overline{AC} = 15$"
                ]
            }
        ]
    },
    {
        "type": "choice",
        "sourceNumber": "5",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-1-3",
        "unitIds": ["nanyi-9-1-1-3"],
        "unitAssignmentBasis": "多邊形縮放後的周長、邊長比與對應角不變之觀念題",
        "blocks": [
            {
                "type": "text",
                "text": "將周長 100 公分的五邊形 $ABCDE$ 用影印機縮分成 $80\\%$，得一新的五邊形 $A'B'C'D'E'$，若 $\\overline{A'B'} = 20$ 公分，$\\angle A = 30^\\circ$，則下列敘述何者錯誤？"
            },
            {
                "type": "options",
                "items": [
                    "$\\overline{A'B'}$ 的對應邊 $\\overline{AB} = 25$ 公分",
                    "$\\overline{BC} : \\overline{B'C'} = 5 : 4$",
                    "五邊形 $A'B'C'D'E'$ 周長為 80 公分",
                    "$\\angle A$ 的對應角 $\\angle A' = 24^\\circ$"
                ]
            }
        ]
    },

    # 填充題 1~12
    {
        "type": "fill",
        "sourceNumber": "1",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-1-2",
        "unitIds": ["nanyi-9-1-1-2"],
        "unitAssignmentBasis": "直角坐標平面上線段之中點坐標公式",
        "blocks": [
            {
                "type": "text",
                "text": "直角坐標平面上，$A(3 , 8)$、$B(-7 , 10)$，若 $C$ 為 $\\overline{AB}$ 的中點，則 $C$ 點坐標為＿＿＿＿"
            }
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "2",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-1-3",
        "unitIds": ["nanyi-9-1-1-3"],
        "unitAssignmentBasis": "相似三角形SSS判定、對應中線比與周長比",
        "blocks": [
            {
                "type": "text",
                "text": "在 $\\triangle ABC$ 和 $\\triangle DEF$ 中，$\\overline{AB} : \\overline{DE} = \\overline{BC} : \\overline{EF} = \\overline{AC} : \\overline{DF} = 1 : 3$，且 $P$、$Q$ 兩點分別為 $\\overline{BC}$、$\\overline{EF}$ 的中點，則："
            },
            {
                "type": "text",
                "text": "(1) $\\triangle ABC \\sim \\triangle DEF$ 是依據＿＿＿＿相似性質"
            },
            {
                "type": "text",
                "text": "(2) $\\overline{AP} : \\overline{DQ} =$＿＿＿＿"
            },
            {
                "type": "text",
                "text": "(3) $\\triangle ABC$ 周長為 10，則 $\\triangle DEF$ 周長 $=$＿＿＿＿"
            }
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "3",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-1-2",
        "unitIds": ["nanyi-9-1-1-2"],
        "unitAssignmentBasis": "三角形平行線截比例線段求邊長",
        "blocks": [
            {
                "type": "text",
                "text": "如圖，$\\triangle ABC$ 中，$\\overline{DE} // \\overline{BC}$，$\\overline{AD} = 8$，$\\overline{AB} = 12$，$\\overline{AE} = 6$，則 $\\overline{AC} =$＿＿＿＿"
            },
            {
                "type": "svg",
                "svg": SVG_FILL_3
            }
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "4",
        "page": 1,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-1-2",
        "unitIds": ["nanyi-9-1-1-2", "nanyi-9-1-1-3"],
        "unitAssignmentBasis": "三角形兩邊中點連線性質及相似三角形面積比",
        "blocks": [
            {
                "type": "text",
                "text": "如圖，$\\triangle ABC$ 中，$D$、$E$ 分別為 $\\overline{AB}$、$\\overline{AC}$ 的中點，$F$、$G$ 分別為 $\\overline{AD}$、$\\overline{AE}$ 的中點，若 $\\overline{BC} = 20$，則："
            },
            {
                "type": "text",
                "text": "(1) $\\overline{FG} =$＿＿＿＿"
            },
            {
                "type": "text",
                "text": "(2) $\\triangle AFG$ 面積 : 梯形 $FDEG$ 面積 : 梯形 $DBCE$ 面積 $=$＿＿＿＿"
            },
            {
                "type": "svg",
                "svg": SVG_FILL_4
            }
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "5",
        "page": 1,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-1-3",
        "unitIds": ["nanyi-9-1-1-3"],
        "unitAssignmentBasis": "直角三角形母子相似性質求線段長",
        "blocks": [
            {
                "type": "text",
                "text": "如圖，直角 $\\triangle ABC$ 中，$\\angle BAC = 90^\\circ$，$\\overline{AD} \\perp \\overline{BC}$，若 $\\overline{BD} = 4$ 公分，$\\overline{BC} = 25$ 公分，則 $\\overline{AB} =$＿＿＿＿"
            },
            {
                "type": "svg",
                "svg": SVG_FILL_5
            }
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "6",
        "page": 1,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-1-3",
        "unitIds": ["nanyi-9-1-1-2", "nanyi-9-1-1-3"],
        "unitAssignmentBasis": "梯形頂邊上點與底邊端點連線所成三角形之同高面積比",
        "blocks": [
            {
                "type": "text",
                "text": "如圖，梯形 $ABCD$ 中，$\\overline{AD} // \\overline{BC}$，且 $\\overline{AD} = 6$，$\\overline{DE} = 4$，則 $\\triangle ABE$ 面積 : $\\triangle CDE$ 面積 $=$＿＿＿＿"
            },
            {
                "type": "svg",
                "svg": SVG_FILL_6
            }
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "7",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-1-4",
        "unitIds": ["nanyi-9-1-1-4"],
        "unitAssignmentBasis": "太陽平行光下影長與物高成比例之生活應用問題",
        "blocks": [
            {
                "type": "text",
                "text": "阿中的身高為 150 公分，在清晨時測得他被太陽照出的影子長為 180 公分，同一時刻，身旁的阿華影長是 216 公分，則阿華的身高為＿＿＿＿公分。"
            }
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "8",
        "page": 2,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-1-3",
        "unitIds": ["nanyi-9-1-1-3"],
        "unitAssignmentBasis": "三角形SAS相似判定與對應邊成比例求值",
        "blocks": [
            {
                "type": "text",
                "text": "如圖，$\\triangle ABC$ 中，$D$、$E$ 分別在 $\\overline{AB}$、$\\overline{AC}$ 上，且 $\\overline{AD} = 20$、$\\overline{BD} = 4$、$\\overline{AC} = 30$、$\\overline{AE} = 16$、$\\overline{BC} = 12$，則 $\\overline{DE} =$＿＿＿＿"
            },
            {
                "type": "svg",
                "svg": SVG_FILL_8
            }
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "9",
        "page": 2,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-1-3",
        "unitIds": ["nanyi-9-1-1-3"],
        "unitAssignmentBasis": "等腰三角形高與直角三角形母子相似求線段分比",
        "blocks": [
            {
                "type": "text",
                "text": "在 $\\triangle ABC$ 中，$\\overline{AB} = \\overline{AC} = 13$，$\\overline{BC} = 10$，若 $D$ 為 $\\overline{BC}$ 中點，作 $\\overline{DE} \\perp \\overline{AC}$ 交 $\\overline{AC}$ 於 $E$ 點，則 $\\overline{AE} : \\overline{EC} =$＿＿＿＿"
            }
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "10",
        "page": 2,
        "difficulty": "hard",
        "primaryUnitId": "nanyi-9-1-1-3",
        "unitIds": ["nanyi-9-1-1-2", "nanyi-9-1-1-3"],
        "unitAssignmentBasis": "菱形四邊中點連線形成長方形之周長與對角線關係",
        "blocks": [
            {
                "type": "text",
                "text": "菱形 $ABCD$ 中，$E$、$F$、$G$、$H$ 分別為 $\\overline{AB}$、$\\overline{BC}$、$\\overline{CD}$、$\\overline{DA}$ 的中點，若 $\\overline{AB} = 5\\sqrt{2}$，菱形 $ABCD$ 面積為 48，則四邊形 $EFGH$ 周長 $=$＿＿＿＿"
            }
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "11",
        "page": 2,
        "difficulty": "hard",
        "primaryUnitId": "nanyi-9-1-1-3",
        "unitIds": ["nanyi-9-1-1-2", "nanyi-9-1-1-3"],
        "unitAssignmentBasis": "梯形對角線中點連線段與對角線交點形成之相似三角形面積比",
        "blocks": [
            {
                "type": "text",
                "text": "如圖，梯形 $ABCD$ 中，$\\overline{AB} // \\overline{DC}$，$E$、$F$ 兩點分別為對角線 $\\overline{AC}$、$\\overline{BD}$ 的中點，$G$ 為兩對角線交點，若 $\\overline{AB} = 3$，$\\overline{DC} = 11$，則 $\\triangle AGB$ 面積 : $\\triangle FGE$ 面積 $=$＿＿＿＿"
            },
            {
                "type": "svg",
                "svg": SVG_FILL_11
            }
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "12",
        "page": 2,
        "difficulty": "hard",
        "primaryUnitId": "nanyi-9-1-1-3",
        "unitIds": ["nanyi-9-1-1-3", "nanyi-9-1-1-4"],
        "unitAssignmentBasis": "正三角形共底邊直線利用比例線段與垂線求高",
        "blocks": [
            {
                "type": "text",
                "text": "如圖，$\\triangle ABC$ 與 $\\triangle CDE$ 都是正三角形。已知 $\\triangle ABC$ 的邊長為 8 公分，$\\triangle CDE$ 的面積是 $4\\sqrt{3}$ 公分，若 $\\overline{FP} \\perp \\overline{BD}$，則 $\\overline{FP} =$＿＿＿＿"
            },
            {
                "type": "svg",
                "svg": SVG_FILL_12
            }
        ]
    },

    # 非選擇題 1~3
    {
        "type": "written",
        "sourceNumber": "1",
        "page": 2,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-1-3",
        "unitIds": ["nanyi-9-1-1-3", "nanyi-9-1-3-1"],
        "unitAssignmentBasis": "相似三角形之對應角平分線與對應高所成三角形之AA相似幾何證明",
        "blocks": [
            {
                "type": "text",
                "text": "如圖，$\\triangle ABC \\sim \\triangle DEF$，$\\overline{BP}$、$\\overline{ER}$ 分別為 $\\angle ABC$ 與 $\\angle DEF$ 的角平分線，$\\overline{BQ}$、$\\overline{ES}$ 分別為 $\\overline{AC}$、$\\overline{DF}$ 上的高，請證明 $\\triangle BPQ \\sim \\triangle ERS$（4分）"
            },
            {
                "type": "svg",
                "svg": SVG_WRITTEN_1
            }
        ]
    },
    {
        "type": "written",
        "sourceNumber": "2",
        "page": 2,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-1-2",
        "unitIds": ["nanyi-9-1-1-2", "nanyi-9-1-1-4"],
        "unitAssignmentBasis": "尺規作圖利用比例分點將三角形農地按指定面積比分割",
        "blocks": [
            {
                "type": "text",
                "text": "王老先生有塊三角形的農地(如下圖)，若農地的每平方公尺價值都一樣，這塊地總價值 2500 萬，若他想把價值 1500 萬的農地分給大兒子，剩餘的農地分給二兒子，請利用尺規作圖，幫他將大兒子和二兒子的地做好分配。並說明理由。"
            },
            {
                "type": "text",
                "text": "(不需寫作法，需保留作圖痕跡，作圖 5 分，理由 3 分共 8 分)"
            },
            {
                "type": "svg",
                "svg": SVG_WRITTEN_2
            }
        ]
    },
    {
        "type": "written",
        "sourceNumber": "3",
        "page": 2,
        "difficulty": "hard",
        "primaryUnitId": "nanyi-9-1-1-3",
        "unitIds": ["nanyi-9-1-1-3", "nanyi-9-1-1-4"],
        "unitAssignmentBasis": "正方形與矩形幾何中直角三角形相似判定與矩形面積計算",
        "blocks": [
            {
                "type": "text",
                "text": "右圖為兩正方形 $ABCD$、$BEFG$ 和矩形 $DGHI$ 的位置圖，其中 $G$、$F$ 兩點分別在 $\\overline{BC}$、$\\overline{EH}$ 上。若 $\\overline{AB} = 7$，$\\overline{BG} = 4$，則"
            },
            {
                "type": "text",
                "text": "(1) 試說明 $\\triangle GCD \\sim \\triangle GFH$（4分）"
            },
            {
                "type": "text",
                "text": "(2) 矩形 $DGHI$ 的面積為多少？（4分）"
            },
            {
                "type": "svg",
                "svg": SVG_WRITTEN_3
            }
        ]
    }
]

data = {
    "paperId": "1Qr-pmnrx6rlxD0fqQlWHaAnallMJ17I4",
    "title": "宜蘭縣中華國民中學一○八學年度第一學期第一次段考數學科試卷 三年級",
    "sourceSha256": "6be61843dc630a129cbce51c5d88b3ec4fabd75ca9dc37d60fcd38790c92502d",
    "printedHeader": "宜蘭縣中華國民中學一○八學年度第一學期第一次段考數學科試卷 三年級",
    "printedSlot": {
        "year": 108,
        "semester": 1,
        "grade": 9,
        "exam": 1
    },
    "expectedTypes": {
        "choice": 5,
        "fill": 12,
        "written": 3
    },
    "questions": questions
}

for q in questions:
    for b in q["blocks"]:
        if b["type"] == "svg":
            b["svg"] = clean_svg(b["svg"])

OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
with open(OUT_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully wrote {OUT_PATH}")
print(f"Total questions: {len(questions)}")
print(f"Types: {{'choice': {sum(1 for q in questions if q['type']=='choice')}, 'fill': {sum(1 for q in questions if q['type']=='fill')}, 'written': {sum(1 for q in questions if q['type']=='written')}}}")
print(f"Difficulty: {{'easy': {sum(1 for q in questions if q['difficulty']=='easy')}, 'medium': {sum(1 for q in questions if q['difficulty']=='medium')}, 'hard': {sum(1 for q in questions if q['difficulty']=='hard')}}}")
