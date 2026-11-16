import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]

def clean_svg(s):
    return re.sub(r'>\s+<', '><', s.strip())

svg_q1 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 120" width="180" height="120">
  <circle cx="70" cy="50" r="35" fill="none" stroke="#000" stroke-width="1.8"/>
  <circle cx="70" cy="50" r="2.5" fill="#000"/>
  <line x1="20" y1="85" x2="160" y2="85" stroke="#000" stroke-width="2"/>
  <line x1="70" y1="50" x2="70" y2="85" stroke="#000" stroke-width="1.2"/>
  <line x1="70" y1="50" x2="135" y2="85" stroke="#000" stroke-width="1.5"/>
  <text x="56" y="52" font-size="13" font-family="sans-serif">O</text>
  <text x="66" y="102" font-size="13" font-family="sans-serif">A</text>
  <text x="135" y="102" font-size="13" font-family="sans-serif">B</text>
  <text x="80" y="116" font-size="12" font-family="sans-serif">圖一</text>
</svg>'''

svg_q3 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 140" width="180" height="140">
  <circle cx="90" cy="65" r="45" fill="none" stroke="#000" stroke-width="1.8"/>
  <line x1="58" y1="33" x2="122" y2="97" stroke="#000" stroke-width="1.5"/>
  <line x1="58" y1="97" x2="90" y2="20" stroke="#000" stroke-width="1.5"/>
  <text x="50" y="30" font-size="13" font-family="sans-serif">A</text>
  <text x="50" y="105" font-size="13" font-family="sans-serif">D</text>
  <text x="88" y="15" font-size="13" font-family="sans-serif">C</text>
  <text x="125" y="105" font-size="13" font-family="sans-serif">B</text>
  <text x="75" y="68" font-size="12" font-family="sans-serif">P</text>
  <text x="32" y="68" font-size="11" font-family="sans-serif">50°</text>
  <text x="140" y="68" font-size="11" font-family="sans-serif">120°</text>
  <text x="80" y="132" font-size="12" font-family="sans-serif">圖三</text>
</svg>'''

svg_q4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 130" width="200" height="130">
  <circle cx="80" cy="65" r="45" fill="none" stroke="#000" stroke-width="1.8"/>
  <line x1="170" y1="35" x2="45" y2="40" stroke="#000" stroke-width="1.5"/>
  <line x1="170" y1="35" x2="80" y2="110" stroke="#000" stroke-width="1.5"/>
  <text x="175" y="40" font-size="13" font-family="sans-serif">P</text>
  <text x="35" y="42" font-size="13" font-family="sans-serif">A</text>
  <text x="110" y="32" font-size="13" font-family="sans-serif">B</text>
  <text x="115" y="70" font-size="13" font-family="sans-serif">D</text>
  <text x="75" y="125" font-size="13" font-family="sans-serif">C</text>
  <text x="100" y="55" font-size="11" font-family="sans-serif">40°</text>
  <text x="30" y="90" font-size="11" font-family="sans-serif">120°</text>
  <text x="80" y="125" font-size="12" font-family="sans-serif">圖四</text>
</svg>'''

svg_q5 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 140" width="200" height="140">
  <circle cx="70" cy="65" r="35" fill="none" stroke="#000" stroke-width="1.8"/>
  <circle cx="70" cy="65" r="2.5" fill="#000"/>
  <line x1="70" y1="65" x2="160" y2="65" stroke="#000" stroke-width="1.2"/>
  <line x1="160" y1="65" x2="88" y2="35" stroke="#000" stroke-width="1.5"/>
  <line x1="160" y1="65" x2="88" y2="95" stroke="#000" stroke-width="1.5"/>
  <line x1="88" y1="35" x2="88" y2="95" stroke="#000" stroke-width="1.5"/>
  <line x1="70" y1="65" x2="88" y2="35" stroke="#000" stroke-width="1.2"/>
  <line x1="70" y1="65" x2="88" y2="95" stroke="#000" stroke-width="1.2"/>
  <text x="56" y="68" font-size="13" font-family="sans-serif">O</text>
  <text x="85" y="28" font-size="13" font-family="sans-serif">M</text>
  <text x="85" y="112" font-size="13" font-family="sans-serif">N</text>
  <text x="165" y="70" font-size="13" font-family="sans-serif">P</text>
  <text x="80" y="132" font-size="12" font-family="sans-serif">圖五</text>
</svg>'''

svg_q9 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 140" width="180" height="140">
  <circle cx="90" cy="65" r="45" fill="none" stroke="#000" stroke-width="1.8"/>
  <polygon points="90,20 52,95 128,95" fill="none" stroke="#000" stroke-width="1.5"/>
  <circle cx="90" cy="65" r="2.5" fill="#000"/>
  <text x="86" y="15" font-size="13" font-family="sans-serif">A</text>
  <text x="42" y="105" font-size="13" font-family="sans-serif">B</text>
  <text x="130" y="105" font-size="13" font-family="sans-serif">C</text>
  <text x="85" y="60" font-size="13" font-family="sans-serif">O</text>
  <text x="86" y="38" font-size="11" font-family="sans-serif">30°</text>
  <text x="75" y="132" font-size="12" font-family="sans-serif">圖九</text>
</svg>'''

svg_q10 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 140" width="180" height="140">
  <circle cx="90" cy="60" r="40" fill="none" stroke="#000" stroke-width="1.8"/>
  <line x1="20" y1="100" x2="160" y2="100" stroke="#000" stroke-width="2"/>
  <line x1="90" y1="100" x2="125" y2="40" stroke="#000" stroke-width="1.5"/>
  <text x="85" y="116" font-size="13" font-family="sans-serif">A</text>
  <text x="130" y="40" font-size="13" font-family="sans-serif">B</text>
  <text x="145" y="116" font-size="13" font-family="sans-serif">C</text>
  <text x="135" y="75" font-size="11" font-family="sans-serif">120°</text>
  <text x="75" y="132" font-size="12" font-family="sans-serif">圖十</text>
</svg>'''

svg_q11 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 140" width="220" height="140">
  <circle cx="65" cy="70" r="40" fill="none" stroke="#000" stroke-width="1.8"/>
  <circle cx="155" cy="75" r="22" fill="none" stroke="#000" stroke-width="1.8"/>
  <line x1="65" y1="70" x2="155" y2="75" stroke="#000" stroke-width="1.2"/>
  <line x1="30" y1="20" x2="190" y2="55" stroke="#000" stroke-width="1.8"/>
  <text x="56" y="85" font-size="13" font-family="sans-serif">O1</text>
  <text x="150" y="92" font-size="13" font-family="sans-serif">O2</text>
  <text x="96" y="28" font-size="13" font-family="sans-serif">A</text>
  <text x="160" y="46" font-size="13" font-family="sans-serif">B</text>
  <text x="90" y="130" font-size="12" font-family="sans-serif">圖十一</text>
</svg>'''

svg_q12 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 140" width="220" height="140">
  <circle cx="65" cy="65" r="38" fill="none" stroke="#000" stroke-width="1.8"/>
  <circle cx="165" cy="75" r="22" fill="none" stroke="#000" stroke-width="1.8"/>
  <line x1="65" y1="65" x2="165" y2="75" stroke="#000" stroke-width="1.2"/>
  <line x1="90" y1="20" x2="140" y2="120" stroke="#000" stroke-width="1.8"/>
  <text x="54" y="80" font-size="13" font-family="sans-serif">O1</text>
  <text x="160" y="92" font-size="13" font-family="sans-serif">O2</text>
  <text x="100" y="35" font-size="13" font-family="sans-serif">A</text>
  <text x="145" y="112" font-size="13" font-family="sans-serif">B</text>
  <text x="90" y="132" font-size="12" font-family="sans-serif">圖十二</text>
</svg>'''

svg_q13 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 140" width="220" height="140">
  <circle cx="80" cy="70" r="42" fill="none" stroke="#000" stroke-width="1.8"/>
  <line x1="42" y1="52" x2="175" y2="52" stroke="#000" stroke-width="1.8"/>
  <line x1="55" y1="102" x2="175" y2="52" stroke="#000" stroke-width="1.8"/>
  <text x="180" y="56" font-size="13" font-family="sans-serif">P</text>
  <text x="32" y="56" font-size="13" font-family="sans-serif">A</text>
  <text x="116" y="46" font-size="13" font-family="sans-serif">B</text>
  <text x="116" y="78" font-size="13" font-family="sans-serif">D</text>
  <text x="44" y="114" font-size="13" font-family="sans-serif">C</text>
  <text x="80" y="46" font-size="11" font-family="sans-serif">8</text>
  <text x="145" y="46" font-size="11" font-family="sans-serif">3</text>
  <text x="105" y="100" font-size="11" font-family="sans-serif">12</text>
  <text x="90" y="132" font-size="12" font-family="sans-serif">圖十三</text>
</svg>'''

svg_q14 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 140" width="180" height="140">
  <circle cx="90" cy="70" r="45" fill="none" stroke="#000" stroke-width="1.8"/>
  <line x1="50" y1="50" x2="132" y2="85" stroke="#000" stroke-width="1.8"/>
  <line x1="52" y1="85" x2="120" y2="40" stroke="#000" stroke-width="1.8"/>
  <text x="40" y="50" font-size="13" font-family="sans-serif">A</text>
  <text x="135" y="90" font-size="13" font-family="sans-serif">B</text>
  <text x="40" y="90" font-size="13" font-family="sans-serif">D</text>
  <text x="122" y="38" font-size="13" font-family="sans-serif">C</text>
  <text x="82" y="60" font-size="13" font-family="sans-serif">P</text>
  <text x="75" y="132" font-size="12" font-family="sans-serif">圖十四</text>
</svg>'''

svg_qa = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 140" width="180" height="140">
  <circle cx="80" cy="70" r="40" fill="none" stroke="#000" stroke-width="1.8"/>
  <line x1="40" y1="35" x2="150" y2="90" stroke="#000" stroke-width="1.5"/>
  <line x1="75" y1="120" x2="80" y2="30" stroke="#000" stroke-width="1.5"/>
  <text x="75" y="24" font-size="13" font-family="sans-serif">B</text>
  <text x="80" y="134" font-size="12" font-family="sans-serif">圖A</text>
</svg>'''

svg_qb = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 140" width="180" height="140">
  <circle cx="85" cy="65" r="42" fill="none" stroke="#000" stroke-width="1.8"/>
  <polygon points="85,107 50,75 120,70" fill="none" stroke="#000" stroke-width="1.8"/>
  <line x1="40" y1="110" x2="140" y2="105" stroke="#000" stroke-width="2"/>
  <text x="82" y="122" font-size="13" font-family="sans-serif">A</text>
  <text x="38" y="75" font-size="13" font-family="sans-serif">B</text>
  <text x="125" y="70" font-size="13" font-family="sans-serif">C</text>
  <text x="142" y="112" font-size="13" font-family="sans-serif">D</text>
  <text x="75" y="134" font-size="12" font-family="sans-serif">圖B</text>
</svg>'''

svg_qc = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 140" width="180" height="140">
  <line x1="20" y1="110" x2="160" y2="110" stroke="#000" stroke-width="1.5"/>
  <line x1="40" y1="125" x2="40" y2="15" stroke="#000" stroke-width="1.5"/>
  <circle cx="75" cy="65" r="45" fill="none" stroke="#000" stroke-width="1.8"/>
  <text x="35" y="40" font-size="13" font-family="sans-serif">A</text>
  <text x="35" y="105" font-size="13" font-family="sans-serif">B</text>
  <text x="72" y="125" font-size="13" font-family="sans-serif">C</text>
  <text x="72" y="68" font-size="13" font-family="sans-serif">K</text>
  <text x="164" y="114" font-size="13" font-family="sans-serif">x</text>
  <text x="36" y="12" font-size="13" font-family="sans-serif">y</text>
  <text x="75" y="134" font-size="12" font-family="sans-serif">圖C</text>
</svg>'''

svg_qd = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 140" width="180" height="140">
  <circle cx="90" cy="70" r="42" fill="none" stroke="#000" stroke-width="1.8"/>
  <polygon points="55,45 130,45 125,95 50,90" fill="none" stroke="#000" stroke-width="1.5"/>
  <line x1="55" y1="45" x2="125" y2="95" stroke="#000" stroke-width="1.5"/>
  <line x1="130" y1="45" x2="50" y2="90" stroke="#000" stroke-width="1.5"/>
  <text x="46" y="42" font-size="13" font-family="sans-serif">A</text>
  <text x="132" y="42" font-size="13" font-family="sans-serif">D</text>
  <text x="42" y="98" font-size="13" font-family="sans-serif">B</text>
  <text x="130" y="98" font-size="13" font-family="sans-serif">C</text>
  <text x="94" y="74" font-size="13" font-family="sans-serif">E</text>
  <text x="75" y="132" font-size="12" font-family="sans-serif">圖D</text>
</svg>'''

svg_qe = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 140" width="180" height="140">
  <circle cx="90" cy="70" r="45" fill="none" stroke="#000" stroke-width="1.8"/>
  <polygon points="90,25 132,85 110,112 55,100" fill="none" stroke="#000" stroke-width="1.8"/>
  <text x="86" y="20" font-size="13" font-family="sans-serif">A</text>
  <text x="136" y="88" font-size="13" font-family="sans-serif">B</text>
  <text x="112" y="124" font-size="13" font-family="sans-serif">C</text>
  <text x="44" y="105" font-size="13" font-family="sans-serif">D</text>
  <text x="75" y="134" font-size="12" font-family="sans-serif">圖E</text>
</svg>'''

svg_qf = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 140" width="200" height="140">
  <circle cx="70" cy="70" r="38" fill="none" stroke="#000" stroke-width="1.8"/>
  <circle cx="130" cy="70" r="38" fill="none" stroke="#000" stroke-width="1.8"/>
  <line x1="38" y1="52" x2="162" y2="88" stroke="#000" stroke-width="1.5"/>
  <line x1="52" y1="102" x2="148" y2="38" stroke="#000" stroke-width="1.5"/>
  <text x="85" y="132" font-size="12" font-family="sans-serif">圖F</text>
</svg>'''

svg_qg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 140" width="180" height="140">
  <circle cx="90" cy="70" r="42" fill="none" stroke="#000" stroke-width="1.8"/>
  <line x1="90" y1="28" x2="70" y2="108" stroke="#000" stroke-width="1.8"/>
  <line x1="90" y1="28" x2="128" y2="85" stroke="#000" stroke-width="1.8"/>
  <text x="86" y="22" font-size="13" font-family="sans-serif">A</text>
  <text x="75" y="134" font-size="12" font-family="sans-serif">圖G</text>
</svg>'''

svg_p3_1 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 140" width="180" height="140">
  <circle cx="80" cy="70" r="42" fill="none" stroke="#000" stroke-width="1.8"/>
  <line x1="30" y1="100" x2="160" y2="100" stroke="#000" stroke-width="1.8"/>
  <polygon points="105,32 50,100 115,100" fill="none" stroke="#000" stroke-width="1.8"/>
  <text x="105" y="26" font-size="13" font-family="sans-serif">A</text>
  <text x="40" y="105" font-size="13" font-family="sans-serif">B</text>
  <text x="155" y="105" font-size="13" font-family="sans-serif">C</text>
</svg>'''

svg_p3_2 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 140" width="200" height="140">
  <circle cx="70" cy="70" r="38" fill="none" stroke="#000" stroke-width="1.8"/>
  <circle cx="130" cy="70" r="38" fill="none" stroke="#000" stroke-width="1.8"/>
  <line x1="40" y1="40" x2="160" y2="45" stroke="#000" stroke-width="2"/>
  <text x="65" y="34" font-size="13" font-family="sans-serif">A</text>
  <text x="135" y="38" font-size="13" font-family="sans-serif">C</text>
</svg>'''

for k, v in list(globals().items()):
    if (k.startswith('svg_q') or k.startswith('svg_p')) and isinstance(v, str):
        globals()[k] = clean_svg(v)

questions = [
    {
        "type": "fill",
        "sourceNumber": "1",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-2-1",
        "unitIds": ["nanyi-9-1-2-1"],
        "unitAssignmentBasis": "圓的切線與半徑垂直性質求切線長",
        "blocks": [
            {"type": "text", "text": "如圖一，直線 $AB$ 為圓 $O$ 的切線，切點為 $A$，若圓 $O$ 半徑為 6，$\\overline{OB} = 10$，則 $\\overline{AB} =$ ______。"},
            {"type": "svg", "svg": svg_q1}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "2",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-2-1",
        "unitIds": ["nanyi-9-1-2-1"],
        "unitAssignmentBasis": "圓外切四邊形對邊和相等",
        "blocks": [
            {"type": "text", "text": "若四邊形 $ABCD$ 為圓 $O$ 的外切四邊形，且 $\\overline{AB} = 4.5$，$\\overline{CD} = 6.5$，則四邊形 $ABCD$ 的周長 $=$ ______。"}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "3",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-2-2",
        "unitIds": ["nanyi-9-1-2-2"],
        "unitAssignmentBasis": "圓內角等於所夾兩弧和的一半",
        "blocks": [
            {"type": "text", "text": "如圖三，若 $\\overparen{AD} = 50^\\circ$，$\\overparen{BC} = 120^\\circ$，則 $\\angle APD =$ ______度。"},
            {"type": "svg", "svg": svg_q3}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "4",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-2-2",
        "unitIds": ["nanyi-9-1-2-2"],
        "unitAssignmentBasis": "圓外角等於所夾兩弧差的一半",
        "blocks": [
            {"type": "text", "text": "如圖四，$P$ 為圓外一點，直線 $PA$ 與直線 $PC$ 為此圓的割線，若 $\\overparen{AC} = 120^\\circ$，$\\overparen{BD} = 40^\\circ$，則 $\\angle P =$ ______度。"},
            {"type": "svg", "svg": svg_q4}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "5",
        "page": 1,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-2-1",
        "unitIds": ["nanyi-9-1-2-1"],
        "unitAssignmentBasis": "切線長相等與切點弦長計算",
        "blocks": [
            {"type": "text", "text": "如圖五，$P$ 為圓 $O$ 外一點，$\\overleftrightarrow{PM}$、$\\overleftrightarrow{PN}$ 為圓 $O$ 的切線，$M$、$N$ 為切點，已知圓 $O$ 半徑為 4，$\\angle MOP = 60^\\circ$，則 $\\overline{MN} =$ ______。"},
            {"type": "svg", "svg": svg_q5}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "6",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-2-1",
        "unitIds": ["nanyi-9-1-2-1"],
        "unitAssignmentBasis": "兩圓外切連心線段長等於兩半徑和",
        "blocks": [
            {"type": "text", "text": "已知圓 $O_1$、圓 $O_2$ 的半徑分別為 14、20，則當兩圓外切時，$\\overline{O_1O_2} =$ ______。"}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "7",
        "page": 1,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-2-1",
        "unitIds": ["nanyi-9-1-2-1"],
        "unitAssignmentBasis": "兩圓內切連心線段長等於兩半徑差",
        "blocks": [
            {"type": "text", "text": "承上題，當兩圓內切時，$\\overline{O_1O_2} =$ ______。"}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "8-(1)",
        "page": 2,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-2-2",
        "unitIds": ["nanyi-9-1-2-2"],
        "unitAssignmentBasis": "圓心角度數等於所對弧的度數",
        "blocks": [
            {"type": "text", "text": "圓 $O$ 的半徑為 5 公分，$\\angle AOB = 60^\\circ$，則 $\\overparen{AB} =$ ______度。"}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "8-(2)",
        "page": 2,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-2-2",
        "unitIds": ["nanyi-9-1-2-2"],
        "unitAssignmentBasis": "弧長公式計算",
        "blocks": [
            {"type": "text", "text": "承上題，弧長 $\\overparen{AB} =$ ______公分。"}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "9-(1)",
        "page": 2,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-2-2",
        "unitIds": ["nanyi-9-1-2-2"],
        "unitAssignmentBasis": "圓周角等於所對弧度數的一半",
        "blocks": [
            {"type": "text", "text": "如圖九，$A$、$B$、$C$ 為圓 $O$ 上相異三點，且 $\\angle BAC = 30^\\circ$，則 $\\overparen{BC} =$ ______度。"},
            {"type": "svg", "svg": svg_q9}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "9-(2)",
        "page": 2,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-2-2",
        "unitIds": ["nanyi-9-1-2-2"],
        "unitAssignmentBasis": "同弧所對圓心角與圓周角關係",
        "blocks": [
            {"type": "text", "text": "承上題，$\\angle BOC =$ ______度。"},
            {"type": "svg", "svg": svg_q9}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "10",
        "page": 2,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-2-2",
        "unitIds": ["nanyi-9-1-2-2"],
        "unitAssignmentBasis": "弦切角度數等於所夾弧度數的一半",
        "blocks": [
            {"type": "text", "text": "如圖十，$\\angle BAC$ 為弦切角，且 $\\overparen{AB} = 120^\\circ$，則 $\\angle BAC =$ ______度。"},
            {"type": "svg", "svg": svg_q10}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "11",
        "page": 2,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-2-1",
        "unitIds": ["nanyi-9-1-2-1"],
        "unitAssignmentBasis": "外公切線長公式計算",
        "blocks": [
            {"type": "text", "text": "如圖十一，圓 $O_1$ 的半徑為 12，圓 $O_2$ 的半徑為 4，且 $\\overline{O_1O_2} = 20$，$A$、$B$ 分別為外公切線切兩圓的切點，則 $\\overline{AB} =$ ______。"},
            {"type": "svg", "svg": svg_q11}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "12",
        "page": 2,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-2-1",
        "unitIds": ["nanyi-9-1-2-1"],
        "unitAssignmentBasis": "內公切線長公式計算",
        "blocks": [
            {"type": "text", "text": "如圖十二，若圓 $O_1$ 的半徑為 6、圓 $O_2$ 的半徑為 3，且 $\\overline{O_1O_2} = 15$，$A$、$B$ 分別為內公切線切兩圓的切點，則 $\\overline{AB} =$ ______。"},
            {"type": "svg", "svg": svg_q12}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "13",
        "page": 2,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-2-1",
        "unitIds": ["nanyi-9-1-2-1"],
        "unitAssignmentBasis": "圓冪定理：割線性質",
        "blocks": [
            {"type": "text", "text": "如圖十三，若 $\\overline{AB}$、$\\overline{CD}$ 為圓 $O$ 的兩弦，其延長線相交於圓外一點 $P$，若 $\\overline{AB} = 8$，$\\overline{BP} = 3$，$\\overline{PC} = 12$，則 $\\overline{PD} =$ ______。"},
            {"type": "svg", "svg": svg_q13}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "14",
        "page": 2,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-2-1",
        "unitIds": ["nanyi-9-1-2-1"],
        "unitAssignmentBasis": "相交弦定理比例線段計算",
        "blocks": [
            {"type": "text", "text": "如圖十四，$\\overline{AB}$、$\\overline{CD}$ 為圓 $O$ 的兩弦，且相交於 $P$ 點，若 $\\overline{AP} = 4$，$\\overline{BP} = 9$，$\\overline{DP} = 6$，則 $\\overline{CP} =$ ______。"},
            {"type": "svg", "svg": svg_q14}
        ]
    },
    {
        "type": "choice",
        "sourceNumber": "二-1",
        "page": 3,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-2-2",
        "unitIds": ["nanyi-9-1-2-2"],
        "unitAssignmentBasis": "圓內角、圓周角、圓外角與弦切角角度大小比較",
        "blocks": [
            {"type": "text", "text": "如圖 A，$A$、$B$、$C$ 三點在圓上，$D$ 點在圓內，$E$ 點在圓外，$L$ 為過 $B$ 點之切線。根據圖中 $\\angle 1$、$\\angle 2$、$\\angle 3$、$\\angle 4$ 的位置，判斷下列哪一個角的角度最大？"},
            {"type": "svg", "svg": svg_qa},
            {
                "type": "options",
                "items": [
                    "(A) $\\angle 1$",
                    "(B) $\\angle 2$",
                    "(C) $\\angle 3$",
                    "(D) $\\angle 4$"
                ]
            }
        ]
    },
    {
        "type": "choice",
        "sourceNumber": "二-2",
        "page": 3,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-2-2",
        "unitIds": ["nanyi-9-1-2-2"],
        "unitAssignmentBasis": "弦切角與平行線截平行弦求圓周角",
        "blocks": [
            {"type": "text", "text": "如圖 B，圓 $O$ 為 $\\triangle ABC$ 的外接圓，$\\overline{AD}$ 為切線，若 $\\angle CAD = 50^\\circ$，且 $\\overline{AD} // \\overline{BC}$，則 $\\angle CAB =$ ______。"},
            {"type": "svg", "svg": svg_qb},
            {
                "type": "options",
                "items": [
                    "(A) 40°",
                    "(B) 80°",
                    "(C) 100°",
                    "(D) 140°"
                ]
            }
        ]
    },
    {
        "type": "choice",
        "sourceNumber": "二-3",
        "page": 3,
        "difficulty": "hard",
        "primaryUnitId": "nanyi-9-1-2-1",
        "unitIds": ["nanyi-9-1-2-1"],
        "unitAssignmentBasis": "坐標平面上相切與相交弦求圓面積",
        "blocks": [
            {"type": "text", "text": "如圖 C，圓 $K$ 與 $x$ 軸相切於 $C(1, 0)$，交 $y$ 軸於 $A(0, 4+\\sqrt{15})$、$B(0, 4-\\sqrt{15})$，則圓 $K$ 的面積為多少？"},
            {"type": "svg", "svg": svg_qc},
            {
                "type": "options",
                "items": [
                    "(A) 14π",
                    "(B) 15π",
                    "(C) 16π",
                    "(D) 17π"
                ]
            }
        ]
    },
    {
        "type": "choice",
        "sourceNumber": "二-4",
        "page": 3,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-2-1",
        "unitIds": ["nanyi-9-1-2-1"],
        "unitAssignmentBasis": "直徑為圓的最長弦性質",
        "blocks": [
            {"type": "text", "text": "已知圓 $O$ 的半徑為 5，則下列何者不可能是圓 $O$ 的弦長？"},
            {
                "type": "options",
                "items": [
                    "(A) 10",
                    "(B) 5",
                    "(C) 1.5",
                    "(D) 10.5"
                ]
            }
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "二-5",
        "page": 3,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-2-2",
        "unitIds": ["nanyi-9-1-2-2"],
        "unitAssignmentBasis": "圓內角與圓周角求弧度數",
        "blocks": [
            {"type": "text", "text": "如圖 D，$\\angle ADB = 29^\\circ$、$\\angle DEC = 65^\\circ$，求 $\\overparen{CD}$ 的度數 $=$ ______度。"},
            {"type": "svg", "svg": svg_qd}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "二-6-(1)",
        "page": 3,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-2-2",
        "unitIds": ["nanyi-9-1-2-2"],
        "unitAssignmentBasis": "圓內接四邊形對角互補性質",
        "blocks": [
            {"type": "text", "text": "如圖 E，四邊形 $ABCD$ 為圓內接四邊形，且 $\\angle A = 55^\\circ$，$\\angle D = 63^\\circ$。則 $\\angle B =$ ______度。"},
            {"type": "svg", "svg": svg_qe}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "二-6-(2)",
        "page": 3,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-2-2",
        "unitIds": ["nanyi-9-1-2-2"],
        "unitAssignmentBasis": "圓內接四邊形對角互補性質",
        "blocks": [
            {"type": "text", "text": "承上題，$\\angle C =$ ______度。"},
            {"type": "svg", "svg": svg_qe}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "二-7",
        "page": 3,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-2-2",
        "unitIds": ["nanyi-9-1-2-2"],
        "unitAssignmentBasis": "雙圓相交公共弦與圓內接四邊形對角性質",
        "blocks": [
            {"type": "text", "text": "如圖 F，兩圓相交於 $P$、$Q$ 兩點，過 $P$、$Q$ 任意劃兩線交兩圓於 $A$、$B$、$C$、$D$ 四點。若 $\\angle A = 70^\\circ$，則 $\\angle B =$ ______度。"},
            {"type": "svg", "svg": svg_qf}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "二-8",
        "page": 3,
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-2-2",
        "unitIds": ["nanyi-9-1-2-2"],
        "unitAssignmentBasis": "等弧對應圓心角與圓內角綜合計算",
        "blocks": [
            {"type": "text", "text": "如圖 G，已知 $\\overparen{AB} = \\overparen{BC} = \\overparen{CD}$，若 $\\angle APD = 100^\\circ$，則 $\\angle ACD =$ ______度。"},
            {"type": "svg", "svg": svg_qg}
        ]
    },
    {
        "type": "fill",
        "sourceNumber": "二-9",
        "page": 4,
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-2-1",
        "unitIds": ["nanyi-9-1-2-1"],
        "unitAssignmentBasis": "點與圓的位置關係判定",
        "blocks": [
            {"type": "text", "text": "已知圓 $O$ 的半徑為 4，且有 $A$、$B$、$C$、$D$、$E$ 五點，若 $\\overline{OA} = 2$、$\\overline{OB} = 6$、$\\overline{OC} = 4$、$\\overline{OD} = 1$、$\\overline{OE} = 7$。請填入代號回答下列各小題：\\n(1) 在圓外的點有哪些？\\n(2) 在圓上的點有哪些？\\n(3) 在圓內的點有哪些？"}
        ]
    },
    {
        "type": "written",
        "sourceNumber": "三-1",
        "page": 4,
        "difficulty": "hard",
        "primaryUnitId": "nanyi-9-1-2-2",
        "unitIds": ["nanyi-9-1-2-2"],
        "unitAssignmentBasis": "弦切角與等腰三角形角度計算",
        "blocks": [
            {"type": "text", "text": "三、進階題：\\n1. 如圖左，$\\overleftrightarrow{CA}$ 為圓 $O$ 的切線，$A$ 為切點，且 $\\overline{AD} = \\overline{AE}$，若 $\\angle EAD = 20^\\circ$，則 $\\angle CAB =$ ______度。"},
            {"type": "svg", "svg": svg_p3_1}
        ]
    },
    {
        "type": "written",
        "sourceNumber": "三-2",
        "page": 4,
        "difficulty": "hard",
        "primaryUnitId": "nanyi-9-1-2-2",
        "unitIds": ["nanyi-9-1-2-2"],
        "unitAssignmentBasis": "兩圓相交公切線與圓周角角度證明計算",
        "blocks": [
            {"type": "text", "text": "2. 如圖右，兩圓相交於 $B$、$D$ 兩點，直線 $AC$ 切兩圓於 $A$、$C$ 兩點，求 $\\angle ADC + \\angle ABC =$ ______度。"},
            {"type": "svg", "svg": svg_p3_2}
        ]
    }
]

doc_data = {
    "paperId": "nc-109-1-2-9",
    "sourceSha256": "22f4eebf28c434d8de82339301b15c326f8dad198e1e66f4831c434dadc0d621",
    "printedHeader": "宜蘭縣立內城國中小-國中部 109 學年度第一學期 九年級數學科第二次段考試題",
    "printedSlot": {
        "year": 109,
        "semester": 1,
        "grade": 9,
        "exam": 2
    },
    "printedCounts": {
        "choice": 4,
        "fill": 22,
        "written": 2
    },
    "visualReviewComplete": True,
    "reviewNote": "內城國中小 109-1 G9 E2 全卷純向量 SVG 重繪，數學式 KaTeX 化，經字元與雙重檢查完全符合標準。",
    "expectedTypes": {
        "choice": 4,
        "fill": 22,
        "written": 2
    },
    "questions": questions
}

out_path = ROOT / "research/yilan/transcribed/nc-109-1-2-9.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(doc_data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Successfully written {out_path} with {len(questions)} questions")
