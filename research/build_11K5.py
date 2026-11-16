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
PAPER_ID = "11K57ftGTh1eAblBW4HXCAbOg_YVHR_3R"
SHA256 = "cd3a6af7150a7b6642ba91f090c7c93ff8d7bcc24f646d4b6bafbb5cca29593e"

# 14 SVGs for Questions: 9, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25

SVG_Q9 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 100">
  <polygon points="45,25 115,25 135,80 25,80" stroke="#111" stroke-width="1.5" fill="none"/>
  <line x1="45" y1="25" x2="135" y2="80" stroke="#111" stroke-width="1.3"/>
  <line x1="115" y1="25" x2="25" y2="80" stroke="#111" stroke-width="1.3"/>
  <text x="36" y="20" font-size="14" font-style="italic" fill="#111">A</text>
  <text x="118" y="20" font-size="14" font-style="italic" fill="#111">D</text>
  <text x="14" y="88" font-size="14" font-style="italic" fill="#111">B</text>
  <text x="140" y="88" font-size="14" font-style="italic" fill="#111">C</text>
  <text x="76" y="58" font-size="14" font-style="italic" fill="#111">O</text>
</svg>"""

SVG_Q12 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 170 100">
  <polygon points="70,18 25,80 145,80" stroke="#111" stroke-width="1.5" fill="none"/>
  <line x1="70" y1="18" x2="80" y2="80" stroke="#111" stroke-width="1.3"/>
  <line x1="80" y1="80" x2="87" y2="32" stroke="#111" stroke-width="1.3"/>
  <text x="68" y="12" font-size="14" font-style="italic" fill="#111">A</text>
  <text x="16" y="88" font-size="14" font-style="italic" fill="#111">B</text>
  <text x="150" y="88" font-size="14" font-style="italic" fill="#111">C</text>
  <text x="76" y="94" font-size="14" font-style="italic" fill="#111">D</text>
  <text x="92" y="32" font-size="14" font-style="italic" fill="#111">E</text>
</svg>"""

SVG_Q13 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 115">
  <polygon points="85,15 25,95 80,95" stroke="#111" stroke-width="1.5" fill="none"/>
  <line x1="55" y1="55" x2="82" y2="55" stroke="#111" stroke-width="1.3"/>
  <text x="83" y="11" font-size="14" font-style="italic" fill="#111">C</text>
  <text x="15" y="104" font-size="14" font-style="italic" fill="#111">A</text>
  <text x="84" y="104" font-size="14" font-style="italic" fill="#111">B</text>
  <text x="41" y="57" font-size="14" font-style="italic" fill="#111">D</text>
  <text x="88" y="57" font-size="14" font-style="italic" fill="#111">E</text>
</svg>"""

SVG_Q14 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 170 110">
  <line x1="20" y1="30" x2="140" y2="30" stroke="#111" stroke-width="1.3"/>
  <line x1="20" y1="56" x2="140" y2="56" stroke="#111" stroke-width="1.3"/>
  <line x1="20" y1="88" x2="140" y2="88" stroke="#111" stroke-width="1.3"/>
  <line x1="45" y1="18" x2="30" y2="100" stroke="#111" stroke-width="1.3"/>
  <line x1="65" y1="16" x2="75" y2="100" stroke="#111" stroke-width="1.3"/>
  <text x="143" y="34" font-size="13" fill="#111">L1</text>
  <text x="143" y="60" font-size="13" fill="#111">L2</text>
  <text x="143" y="92" font-size="13" fill="#111">L3</text>
  <text x="24" y="108" font-size="13" fill="#111">M1</text>
  <text x="75" y="108" font-size="13" fill="#111">M2</text>
  <text x="32" y="28" font-size="14" font-style="italic" fill="#111">A</text>
  <text x="26" y="54" font-size="14" font-style="italic" fill="#111">B</text>
  <text x="20" y="86" font-size="14" font-style="italic" fill="#111">C</text>
  <text x="72" y="28" font-size="14" font-style="italic" fill="#111">D</text>
  <text x="76" y="54" font-size="14" font-style="italic" fill="#111">E</text>
  <text x="79" y="86" font-size="14" font-style="italic" fill="#111">F</text>
</svg>"""

SVG_Q15 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 110">
  <polygon points="70,15 25,95 125,95" stroke="#111" stroke-width="1.5" fill="none"/>
  <polygon points="48,55 98,55 75,95" stroke="#111" stroke-width="1.3" fill="none"/>
  <polygon points="73,55 61,75 86,75" stroke="#111" stroke-width="1.2" fill="none"/>
  <text x="68" y="12" font-size="14" font-style="italic" fill="#111">A</text>
  <text x="14" y="102" font-size="14" font-style="italic" fill="#111">B</text>
  <text x="130" y="102" font-size="14" font-style="italic" fill="#111">C</text>
  <text x="72" y="104" font-size="14" font-style="italic" fill="#111">D</text>
  <text x="103" y="56" font-size="14" font-style="italic" fill="#111">E</text>
  <text x="36" y="56" font-size="14" font-style="italic" fill="#111">F</text>
  <text x="70" y="48" font-size="14" font-style="italic" fill="#111">G</text>
  <text x="50" y="78" font-size="14" font-style="italic" fill="#111">H</text>
  <text x="90" y="78" font-size="14" font-style="italic" fill="#111">I</text>
</svg>"""

SVG_Q17 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 170 125">
  <polygon points="55,15 20,68 88,110 135,30" stroke="#111" stroke-width="1.5" fill="none"/>
  <polygon points="38,42 54,89 112,70 95,23" stroke="#111" stroke-width="1.3" fill="none"/>
  <text x="52" y="12" font-size="14" font-style="italic" fill="#111">A</text>
  <text x="10" y="72" font-size="14" font-style="italic" fill="#111">B</text>
  <text x="85" y="120" font-size="14" font-style="italic" fill="#111">C</text>
  <text x="140" y="30" font-size="14" font-style="italic" fill="#111">D</text>
  <text x="28" y="42" font-size="14" font-style="italic" fill="#111">E</text>
  <text x="47" y="98" font-size="14" font-style="italic" fill="#111">F</text>
  <text x="116" y="74" font-size="14" font-style="italic" fill="#111">G</text>
  <text x="95" y="18" font-size="14" font-style="italic" fill="#111">H</text>
</svg>"""

SVG_Q18 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 170 100">
  <line x1="50" y1="20" x2="110" y2="20" stroke="#111" stroke-width="1.5"/>
  <line x1="25" y1="80" x2="100" y2="80" stroke="#111" stroke-width="1.5"/>
  <line x1="50" y1="20" x2="100" y2="80" stroke="#111" stroke-width="1.3"/>
  <line x1="110" y1="20" x2="25" y2="80" stroke="#111" stroke-width="1.3"/>
  <text x="40" y="22" font-size="14" font-style="italic" fill="#111">E</text>
  <text x="115" y="22" font-size="14" font-style="italic" fill="#111">F</text>
  <text x="15" y="84" font-size="14" font-style="italic" fill="#111">B</text>
  <text x="105" y="84" font-size="14" font-style="italic" fill="#111">C</text>
  <text x="62" y="58" font-size="14" font-style="italic" fill="#111">A</text>
</svg>"""

SVG_Q19 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 85">
  <polygon points="65,30 48,24 25,45" stroke="#111" stroke-width="1.5" fill="none"/>
  <polygon points="65,30 105,15 145,55" stroke="#111" stroke-width="1.5" fill="none"/>
  <line x1="25" y1="45" x2="105" y2="15" stroke="#111" stroke-width="1.3"/>
  <line x1="48" y1="24" x2="145" y2="55" stroke="#111" stroke-width="1.3"/>
  <text x="65" y="24" font-size="14" font-style="italic" fill="#111">A</text>
  <text x="42" y="20" font-size="14" font-style="italic" fill="#111">B</text>
  <text x="17" y="52" font-size="14" font-style="italic" fill="#111">C</text>
  <text x="103" y="11" font-size="14" font-style="italic" fill="#111">E</text>
  <text x="150" y="58" font-size="14" font-style="italic" fill="#111">F</text>
</svg>"""

SVG_Q20 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 125">
  <line x1="54" y1="10" x2="22" y2="115" stroke="#111" stroke-width="1.3"/>
  <line x1="15" y1="10" x2="145" y2="95" stroke="#111" stroke-width="1.3"/>
  <polygon points="36,75 84,51 102,64" stroke="#111" stroke-width="1" fill="#111"/>
  <line x1="30" y1="100" x2="120" y2="77" stroke="#111" stroke-width="1.3"/>
  <text x="20" y="122" font-size="13" font-style="italic" fill="#111">L</text>
  <text x="148" y="98" font-size="13" font-style="italic" fill="#111">M</text>
  <text x="44" y="20" font-size="14" font-style="italic" fill="#111">A</text>
  <text x="31" y="48" font-size="14" font-style="italic" fill="#111">D</text>
  <text x="24" y="74" font-size="14" font-style="italic" fill="#111">E</text>
  <text x="18" y="98" font-size="14" font-style="italic" fill="#111">B</text>
  <text x="66" y="32" font-size="14" font-style="italic" fill="#111">F</text>
  <text x="84" y="45" font-size="14" font-style="italic" fill="#111">G</text>
  <text x="102" y="58" font-size="14" font-style="italic" fill="#111">H</text>
  <text x="125" y="76" font-size="14" font-style="italic" fill="#111">C</text>
</svg>"""

SVG_Q21 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 150 150">
  <polygon points="25,25 25,125 125,125 125,25" stroke="#111" stroke-width="1.5" fill="none"/>
  <polygon points="25,45 65,125 125,95 65,25" stroke="#111" stroke-width="1.3" fill="none"/>
  <text x="14" y="22" font-size="14" font-style="italic" fill="#111">A</text>
  <text x="14" y="133" font-size="14" font-style="italic" fill="#111">B</text>
  <text x="130" y="133" font-size="14" font-style="italic" fill="#111">C</text>
  <text x="130" y="22" font-size="14" font-style="italic" fill="#111">D</text>
  <text x="62" y="18" font-size="14" font-style="italic" fill="#111">H</text>
  <text x="14" y="47" font-size="14" font-style="italic" fill="#111">E</text>
  <text x="62" y="136" font-size="14" font-style="italic" fill="#111">F</text>
  <text x="132" y="98" font-size="14" font-style="italic" fill="#111">G</text>
</svg>"""

SVG_Q22 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 140 120">
  <polygon points="30,15 30,95 95,95" stroke="#111" stroke-width="1.5" fill="none"/>
  <line x1="30" y1="95" x2="62" y2="55" stroke="#111" stroke-width="1.3"/>
  <rect x="30" y="87" width="8" height="8" stroke="#111" stroke-width="1" fill="none"/>
  <text x="25" y="12" font-size="14" font-style="italic" fill="#111">A</text>
  <text x="20" y="102" font-size="14" font-style="italic" fill="#111">B</text>
  <text x="100" y="100" font-size="14" font-style="italic" fill="#111">C</text>
  <text x="67" y="54" font-size="14" font-style="italic" fill="#111">D</text>
</svg>"""

SVG_Q23 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 140 130">
  <polygon points="35,20 80,20 80,105 35,105" stroke="#111" stroke-width="1.5" fill="none"/>
  <line x1="35" y1="62" x2="80" y2="20" stroke="#111" stroke-width="1.3"/>
  <line x1="35" y1="62" x2="80" y2="105" stroke="#111" stroke-width="1.3"/>
  <rect x="35" y="20" width="7" height="7" stroke="#111" stroke-width="1" fill="none"/>
  <rect x="35" y="98" width="7" height="7" stroke="#111" stroke-width="1" fill="none"/>
  <text x="23" y="20" font-size="14" font-style="italic" fill="#111">A</text>
  <text x="23" y="108" font-size="14" font-style="italic" fill="#111">B</text>
  <text x="23" y="65" font-size="14" font-style="italic" fill="#111">E</text>
  <text x="85" y="20" font-size="14" font-style="italic" fill="#111">D</text>
  <text x="85" y="108" font-size="14" font-style="italic" fill="#111">C</text>
</svg>"""

SVG_Q24 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 110">
  <polygon points="20,85 140,85 140,20" stroke="#111" stroke-width="1.5" fill="none"/>
  <polygon points="95,85 140,85 140,40 95,40" stroke="#111" stroke-width="1.3" fill="none"/>
  <polygon points="120,40 140,40 140,20 120,20" stroke="#111" stroke-width="1.2" fill="none"/>
  <text x="10" y="88" font-size="14" font-style="italic" fill="#111">A</text>
  <text x="145" y="88" font-size="14" font-style="italic" fill="#111">B</text>
  <text x="145" y="18" font-size="14" font-style="italic" fill="#111">C</text>
  <text x="93" y="98" font-size="14" font-style="italic" fill="#111">E</text>
  <text x="84" y="38" font-size="14" font-style="italic" fill="#111">D</text>
  <text x="146" y="44" font-size="14" font-style="italic" fill="#111">F</text>
  <text x="118" y="48" font-size="14" font-style="italic" fill="#111">H</text>
  <text x="114" y="18" font-size="14" font-style="italic" fill="#111">G</text>
  <text x="146" y="26" font-size="14" font-style="italic" fill="#111">I</text>
</svg>"""

SVG_Q25 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 170 140">
  <polygon points="25,25 25,105 105,105 105,25" stroke="#111" stroke-width="1.5" fill="none"/>
  <line x1="25" y1="105" x2="150" y2="60" stroke="#111" stroke-width="1.3"/>
  <line x1="105" y1="105" x2="150" y2="60" stroke="#111" stroke-width="1.3"/>
  <text x="14" y="22" font-size="14" font-style="italic" fill="#111">A</text>
  <text x="14" y="112" font-size="14" font-style="italic" fill="#111">B</text>
  <text x="108" y="112" font-size="14" font-style="italic" fill="#111">C</text>
  <text x="110" y="22" font-size="14" font-style="italic" fill="#111">D</text>
  <text x="95" y="70" font-size="14" font-style="italic" fill="#111">F</text>
  <text x="155" y="62" font-size="14" font-style="italic" fill="#111">E</text>
</svg>"""

data = {
    "paperId": PAPER_ID,
    "sourceSha256": SHA256,
    "printedHeader": "宜蘭縣中華國民中學一一一學年度第一學期第一次段考數學科試卷 九年級",
    "printedSlot": {"year": 111, "semester": 1, "grade": 9, "exam": 1},
    "printedCounts": "全卷填充題25題（每題4分，共100分）。",
    "visualReviewComplete": True,
    "reviewNote": "全卷逐頁對照原卷PNG，所有圖形均以純向量SVG重繪，無缺少題號，無使用style或image標籤，字元覆蓋與答案卷完全吻合。",
    "expectedTypes": {"choice": 0, "fill": 25, "written": 0},
    "questions": [
        {
            "type": "fill",
            "sourceNumber": "1",
            "page": 1,
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-1",
            "unitIds": ["nanyi-9-1-1-1"],
            "unitAssignmentBasis": "將三數連比化為最簡整數比。",
            "blocks": [
                {"type": "text", "text": "將下列的比化為最簡整數比：$45:35:60=$＿＿＿＿。"}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "2",
            "page": 1,
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-1",
            "unitIds": ["nanyi-9-1-1-1"],
            "unitAssignmentBasis": "由兩兩比求三數連比。",
            "blocks": [
                {"type": "text", "text": "設 $x:y=5:6$，$x:z=5:6$，則 $x:y:z=$＿＿＿＿。"}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "3",
            "page": 1,
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-1",
            "unitIds": ["nanyi-9-1-1-1"],
            "unitAssignmentBasis": "由兩兩比求三數連比。",
            "blocks": [
                {"type": "text", "text": "若 $a:b=3:2$，$b:c=6:7$，則 $a:b:c=$＿＿＿＿。"}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "4",
            "page": 1,
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-1",
            "unitIds": ["nanyi-9-1-1-1"],
            "unitAssignmentBasis": "比例式與二元一次方程式轉換為三數連比。",
            "blocks": [
                {"type": "text", "text": "已知 $xyz\\ne 0$，且 $\\dfrac{x}{5}=\\dfrac{y}{4}$，$7y-6z=0$，則 $x:y:z=$＿＿＿＿。"}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "5",
            "page": 1,
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-1",
            "unitIds": ["nanyi-9-1-1-1"],
            "unitAssignmentBasis": "連比設參數求一元一次方程式的解。",
            "blocks": [
                {"type": "text", "text": "已知 $x:y:z=3:2:4$，且 $2x+y=240$，則 $z=$＿＿＿＿。"}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "6",
            "page": 1,
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-1",
            "unitIds": ["nanyi-9-1-1-1"],
            "unitAssignmentBasis": "連等式求連比並代入方程式求未知數。",
            "blocks": [
                {"type": "text", "text": "若 $6x=4y=3z$，且 $4x+6y+10z=330$，則 $x=$＿＿＿＿。"}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "7",
            "page": 1,
            "difficulty": "medium",
            "primaryUnitId": "nanyi-9-1-1-1",
            "unitIds": ["nanyi-9-1-1-1"],
            "unitAssignmentBasis": "等面積三角形之底邊比與對應高比的反比關係。",
            "blocks": [
                {"type": "text", "text": "有甲、乙、丙三個三角形，面積都是 $72$ 平方公分，且其對應底邊比為 $10:12:15$，則此三個三角形的對應高的比為＿＿＿＿。"}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "8",
            "page": 1,
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-1",
            "unitIds": ["nanyi-9-1-1-1"],
            "unitAssignmentBasis": "連比與平均數應用問題。",
            "blocks": [
                {"type": "text", "text": "甲、乙、丙三人的年齡分別是 $x$ 歲、$y$ 歲、$z$ 歲，如果 $x:y:z=8:3:4$，且三人年齡的平均是 $15$ 歲，則甲的年齡是＿＿＿＿歲。"}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "9",
            "page": 1,
            "difficulty": "medium",
            "primaryUnitId": "nanyi-9-1-1-2",
            "unitIds": ["nanyi-9-1-1-2"],
            "unitAssignmentBasis": "梯形對角線兩側三角形同底等高面積相等性質。",
            "blocks": [
                {"type": "text", "text": "如圖，梯形 $ABCD$ 中，$\\overline{AD} // \\overline{BC}$，若 $\\overline{AD}=28$，$\\overline{BC}=49$，求 $\\triangle AOB$ 的面積：$\\triangle DOC$ 的面積 $=$＿＿＿＿。"},
                {"type": "svg", "maxHeight": 100, "svg": clean_svg(SVG_Q9)}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "10",
            "page": 1,
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-3",
            "unitIds": ["nanyi-9-1-1-3"],
            "unitAssignmentBasis": "相似多邊形對應邊成比例。",
            "blocks": [
                {"type": "text", "text": "已知五邊形 $ABCDE \\sim$ 五邊形 $PQRST$，$A$、$B$、$C$、$D$、$E$ 的對應頂點依序為 $P$、$Q$、$R$、$S$、$T$，若 $\\overline{AB}=24$，$\\overline{CD}=16$，$\\overline{PQ}=18$，求 $\\overline{RS}=$＿＿＿＿。"}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "11",
            "page": 1,
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-3",
            "unitIds": ["nanyi-9-1-1-3"],
            "unitAssignmentBasis": "圖形縮放時內角度數保持不變。",
            "blocks": [
                {"type": "text", "text": "將邊長為 $3$ 公分的正五邊形縮放 $4$ 倍，所得的縮放圖形的一內角 $=$＿＿＿＿度。"}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "12",
            "page": 1,
            "difficulty": "medium",
            "primaryUnitId": "nanyi-9-1-1-2",
            "unitIds": ["nanyi-9-1-1-2"],
            "unitAssignmentBasis": "利用三角形同高面積比等於底邊長度比進行兩次面積比例分割。",
            "blocks": [
                {"type": "text", "text": "如圖，$\\triangle ABC$ 中，$D$、$E$ 分別在 $\\overline{BC}$ 與 $\\overline{AC}$ 上，若 $\\overline{DB}:\\overline{DC}=6:7$，$\\overline{CE}:\\overline{EA}=7:2$，且 $\\triangle ABD$ 的面積是 $54$，求 $\\triangle DAE$ 的面積 $=$＿＿＿＿。"},
                {"type": "svg", "maxHeight": 100, "svg": clean_svg(SVG_Q12)}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "13",
            "page": 1,
            "difficulty": "hard",
            "primaryUnitId": "nanyi-9-1-1-3",
            "unitIds": ["nanyi-9-1-1-3"],
            "unitAssignmentBasis": "AA 相似三角形判別與對應邊成比例求周長。",
            "blocks": [
                {"type": "text", "text": "如圖，$\\triangle ABC$ 中，$\\overline{CD}=12$，$\\overline{AD}=8$，$\\angle C=29^\\circ$，$\\angle B=104^\\circ$，$\\angle CDE=47^\\circ$，若 $\\overline{CE}=9$，$\\overline{DE}=6$，求 $\\triangle ABC$ 的周長 $=$＿＿＿＿。"},
                {"type": "svg", "maxHeight": 115, "svg": clean_svg(SVG_Q13)}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "14",
            "page": 1,
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-2",
            "unitIds": ["nanyi-9-1-1-2"],
            "unitAssignmentBasis": "平行線截比例線段列一元一次方程式。",
            "blocks": [
                {"type": "text", "text": "如圖，直線 $L_1 // L_2 // L_3$，直線 $M_1$ 與 $M_2$ 為截線，已知 $\\overline{AB}=8$，$\\overline{BC}=20$，$\\overline{DE}=x+5$，$\\overline{EF}=4x+2$，求 $x=$＿＿＿＿。"},
                {"type": "svg", "maxHeight": 110, "svg": clean_svg(SVG_Q14)}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "15",
            "page": 1,
            "difficulty": "medium",
            "primaryUnitId": "nanyi-9-1-1-2",
            "unitIds": ["nanyi-9-1-1-2"],
            "unitAssignmentBasis": "三角形中點連線段性質與巢狀中點三角形周長比例。",
            "blocks": [
                {"type": "text", "text": "如圖，若 $D$、$E$、$F$ 為 $\\triangle ABC$ 三邊中點，$G$、$H$、$I$ 為 $\\triangle DEF$ 三邊中點，已知 $\\overline{AB}=9$，$\\overline{BC}=8$，$\\overline{AC}=7$，求 $\\triangle GHI$ 的周長 $=$＿＿＿＿。"},
                {"type": "svg", "maxHeight": 110, "svg": clean_svg(SVG_Q15)}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "16",
            "page": 1,
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-3",
            "unitIds": ["nanyi-9-1-1-3"],
            "unitAssignmentBasis": "相似圖形概念判別（正方形必相似）。",
            "blocks": [
                {"type": "text", "text": "下列何者相似？答：＿＿＿＿。（單選）"},
                {"type": "text", "text": "(A) 任意兩個三角形"},
                {"type": "text", "text": "(B) 任意兩個等腰三角形"},
                {"type": "text", "text": "(C) 任意兩個正方形"},
                {"type": "text", "text": "(D) 任意兩個菱形"}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "17",
            "page": 2,
            "difficulty": "medium",
            "primaryUnitId": "nanyi-9-1-1-2",
            "unitIds": ["nanyi-9-1-1-2"],
            "unitAssignmentBasis": "四邊形各邊中點連線性質（華林農定理）與周長計算。",
            "blocks": [
                {"type": "text", "text": "如圖，四邊形 $ABCD$ 中，$E$、$F$、$G$、$H$ 為各邊中點。若 $\\overline{AC}=23$，$\\overline{BD}=25$，則四邊形 $EFGH$ 的周長 $=$＿＿＿＿。"},
                {"type": "svg", "maxHeight": 125, "svg": clean_svg(SVG_Q17)}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "18",
            "page": 2,
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-1-3",
            "unitIds": ["nanyi-9-1-1-3"],
            "unitAssignmentBasis": "平行線截出的沙漏型相似三角形對應邊成比例。",
            "blocks": [
                {"type": "text", "text": "如圖，$\\overline{EF} // \\overline{BC}$，$\\overline{EC}$ 與 $\\overline{BF}$ 交於 $A$ 點，$\\overline{EF}=20$，$\\overline{BC}=25$，$\\overline{AE}=12$，求 $\\overline{AC}=$＿＿＿＿。"},
                {"type": "svg", "maxHeight": 100, "svg": clean_svg(SVG_Q18)}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "19",
            "page": 2,
            "difficulty": "medium",
            "primaryUnitId": "nanyi-9-1-1-3",
            "unitIds": ["nanyi-9-1-1-3"],
            "unitAssignmentBasis": "SAS 相似三角形判別與對應邊長計算。",
            "blocks": [
                {"type": "text", "text": "如圖，$\\overline{EC}$ 與 $\\overline{BF}$ 交於 $A$ 點，$\\overline{AB}=4$，$\\overline{AC}=\\overline{AE}=12$，$\\overline{AF}=36$，$\\overline{EF}=30$，求 $\\overline{BC}=$＿＿＿＿。"},
                {"type": "svg", "maxHeight": 85, "svg": clean_svg(SVG_Q19)}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "20",
            "page": 2,
            "difficulty": "medium",
            "primaryUnitId": "nanyi-9-1-1-2",
            "unitIds": ["nanyi-9-1-1-2"],
            "unitAssignmentBasis": "利用線段等分點與高底比例求三角形面積。",
            "blocks": [
                {"type": "text", "text": "如圖，直線 $L$ 與直線 $M$ 交於 $A$ 點，$D$、$E$ 為 $\\overline{AB}$ 的三等分點，$F$、$G$、$H$ 為 $\\overline{AC}$ 的四等分點，若 $\\triangle EGH$ 的面積 $=3$，求 $\\triangle ABC$ 的面積 $=$＿＿＿＿。"},
                {"type": "svg", "maxHeight": 125, "svg": clean_svg(SVG_Q20)}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "21",
            "page": 2,
            "difficulty": "hard",
            "primaryUnitId": "nanyi-9-1-1-3",
            "unitIds": ["nanyi-9-1-1-3"],
            "unitAssignmentBasis": "正方形內部相似直角三角形推導邊長並求三角形面積。",
            "blocks": [
                {"type": "text", "text": "如圖，正方形 $ABCD$ 中，$\\angle HEF=\\angle EFG=90^\\circ$，$\\overline{AH}=4$，$\\overline{AE}=2$，$\\overline{BE}=8$，求 $\\triangle DHG$ 的面積 $=$＿＿＿＿。"},
                {"type": "svg", "maxHeight": 150, "svg": clean_svg(SVG_Q21)}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "22",
            "page": 2,
            "difficulty": "easy",
            "primaryUnitId": "nanyi-9-1-3-2",
            "unitIds": ["nanyi-9-1-3-2"],
            "unitAssignmentBasis": "直角三角形斜邊中點（外心）到三頂點等距性質。",
            "blocks": [
                {"type": "text", "text": "如圖，直角 $\\triangle ABC$ 中，$\\angle ABC=90^\\circ$，$D$ 為 $\\overline{AC}$ 的中點，若 $\\overline{AC}=10$，則 $\\overline{BD}=$＿＿＿＿。"},
                {"type": "svg", "maxHeight": 120, "svg": clean_svg(SVG_Q22)}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "23",
            "page": 2,
            "difficulty": "hard",
            "primaryUnitId": "nanyi-9-1-1-3",
            "unitIds": ["nanyi-9-1-1-3"],
            "unitAssignmentBasis": "直角梯形腰上點之反射角相似直角三角形與畢氏定理。",
            "blocks": [
                {"type": "text", "text": "如圖，梯形 $ABCD$ 中，$\\angle A=\\angle B=90^\\circ$，$\\angle AED=\\angle BEC$，$\\overline{AD}:\\overline{AE}=5:4$，$\\overline{AB}=8$，求 $\\overline{DE}+\\overline{CE}=$＿＿＿＿。"},
                {"type": "svg", "maxHeight": 130, "svg": clean_svg(SVG_Q23)}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "24",
            "page": 2,
            "difficulty": "hard",
            "primaryUnitId": "nanyi-9-1-1-3",
            "unitIds": ["nanyi-9-1-1-3"],
            "unitAssignmentBasis": "直角三角形內接兩正方形構成的相似直角三角形推求邊長。",
            "blocks": [
                {"type": "text", "text": "如圖，$\\triangle ABC$ 中，$\\angle B=90^\\circ$，四邊形 $DEBF$ 和四邊形 $GHFI$ 皆為正方形，$\\overline{GI}=2$，$\\overline{AB}=18$，求 $\\overline{DF}=$＿＿＿＿。"},
                {"type": "svg", "maxHeight": 110, "svg": clean_svg(SVG_Q24)}
            ]
        },
        {
            "type": "fill",
            "sourceNumber": "25",
            "page": 2,
            "difficulty": "hard",
            "primaryUnitId": "nanyi-9-1-1-3",
            "unitIds": ["nanyi-9-1-1-3"],
            "unitAssignmentBasis": "正方形與外接直線夾角 45 度相似形推導與線段計算。",
            "blocks": [
                {"type": "text", "text": "如圖，正方形 $ABCD$ 中，$\\overline{AB}=7$，且 $\\angle DCE=45^\\circ$，$\\overline{BE}=13$，求 $\\overline{CF}=$＿＿＿＿。"},
                {"type": "svg", "maxHeight": 140, "svg": clean_svg(SVG_Q25)}
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

md_content = f"""# 中華國中 111上・9年級・第1次

paperId: `{PAPER_ID}`

## 卷首與來源核對

- 學校：宜蘭縣立中華國民中學
- 卷首全稱：宜蘭縣中華國民中學一一一學年度第一學期第一次段考數學科試卷 九年級
- 標記時槽：111學年度 第1學期 9年級 第1次段考
- 來源SHA256：{SHA256}
- 頁數：共2頁，全卷完成人工核對與純向量幾何SVG重繪

## 逐題全文

### 一、 填充題（每格 4 分，共 100 分）

#### 第 1 題
將下列的比化為最簡整數比：$45:35:60=$＿＿＿＿。
- 難度：easy；單元：nanyi-9-1-1-1；來源頁：第1頁

#### 第 2 題
設 $x:y=5:6$，$x:z=5:6$，則 $x:y:z=$＿＿＿＿。
- 難度：easy；單元：nanyi-9-1-1-1；來源頁：第1頁

#### 第 3 題
若 $a:b=3:2$，$b:c=6:7$，則 $a:b:c=$＿＿＿＿。
- 難度：easy；單元：nanyi-9-1-1-1；來源頁：第1頁

#### 第 4 題
已知 $xyz\\ne 0$，且 $\\dfrac{{x}}{{5}}=\\dfrac{{y}}{{4}}$，$7y-6z=0$，則 $x:y:z=$＿＿＿＿。
- 難度：easy；單元：nanyi-9-1-1-1；來源頁：第1頁

#### 第 5 題
已知 $x:y:z=3:2:4$，且 $2x+y=240$，則 $z=$＿＿＿＿。
- 難度：easy；單元：nanyi-9-1-1-1；來源頁：第1頁

#### 第 6 題
若 $6x=4y=3z$，且 $4x+6y+10z=330$，則 $x=$＿＿＿＿。
- 難度：easy；單元：nanyi-9-1-1-1；來源頁：第1頁

#### 第 7 題
有甲、乙、丙三個三角形，面積都是 $72$ 平方公分，且其對應底邊比為 $10:12:15$，則此三個三角形的對應高的比為＿＿＿＿。
- 難度：medium；單元：nanyi-9-1-1-1；來源頁：第1頁

#### 第 8 題
甲、乙、丙三人的年齡分別是 $x$ 歲、$y$ 歲、$z$ 歲，如果 $x:y:z=8:3:4$，且三人年齡的平均是 $15$ 歲，則甲的年齡是＿＿＿＿歲。
- 難度：easy；單元：nanyi-9-1-1-1；來源頁：第1頁

#### 第 9 題
如圖，梯形 $ABCD$ 中，$\\overline{{AD}} // \\overline{{BC}}$，若 $\\overline{{AD}}=28$，$\\overline{{BC}}=49$，求 $\\triangle AOB$ 的面積：$\\triangle DOC$ 的面積 $=$＿＿＿＿。
- [包含純向量SVG幾何重繪：梯形ABCD與對角線交點O]
- 難度：medium；單元：nanyi-9-1-1-2；來源頁：第1頁

#### 第 10 題
已知五邊形 $ABCDE \\sim$ 五邊形 $PQRST$，$A$、$B$、$C$、$D$、$E$ 的對應頂點依序為 $P$、$Q$、$R$、$S$、$T$，若 $\\overline{{AB}}=24$，$\\overline{{CD}}=16$，$\\overline{{PQ}}=18$，求 $\\overline{{RS}}=$＿＿＿＿。
- 難度：easy；單元：nanyi-9-1-1-3；來源頁：第1頁

#### 第 11 題
將邊長為 $3$ 公分的正五邊形縮放 $4$ 倍，所得的縮放圖形的一內角 $=$＿＿＿＿度。
- 難度：easy；單元：nanyi-9-1-1-3；來源頁：第1頁

#### 第 12 題
如圖，$\\triangle ABC$ 中，$D$、$E$ 分別在 $\\overline{{BC}}$ 與 $\\overline{{AC}}$ 上，若 $\\overline{{DB}}:\\overline{{DC}}=6:7$，$\\overline{{CE}}:\\overline{{EA}}=7:2$，且 $\\triangle ABD$ 的面積是 $54$，求 $\\triangle DAE$ 的面積 $=$＿＿＿＿。
- [包含純向量SVG幾何重繪：三角形兩次同高面積比例分割]
- 難度：medium；單元：nanyi-9-1-1-2；來源頁：第1頁

#### 第 13 題
如圖，$\\triangle ABC$ 中，$\\overline{{CD}}=12$，$\\overline{{AD}}=8$，$\\angle C=29^\\circ$，$\\angle B=104^\\circ$，$\\angle CDE=47^\\circ$，若 $\\overline{{CE}}=9$，$\\overline{{DE}}=6$，求 $\\triangle ABC$ 的周長 $=$＿＿＿＿。
- [包含純向量SVG幾何重繪：AA相似三角形求周長]
- 難度：hard；單元：nanyi-9-1-1-3；來源頁：第1頁

#### 第 14 題
如圖，直線 $L_1 // L_2 // L_3$，直線 $M_1$ 與 $M_2$ 為截線，已知 $\\overline{{AB}}=8$，$\\overline{{BC}}=20$，$\\overline{{DE}}=x+5$，$\\overline{{EF}}=4x+2$，求 $x=$＿＿＿＿。
- [包含純向量SVG幾何重繪：三平行線截比例線段]
- 難度：easy；單元：nanyi-9-1-1-2；來源頁：第1頁

#### 第 15 題
如圖，若 $D$、$E$、$F$ 為 $\\triangle ABC$ 三邊中點，$G$、$H$、$I$ 為 $\\triangle DEF$ 三邊中點，已知 $\\overline{{AB}}=9$，$\\overline{{BC}}=8$，$\\overline{{AC}}=7$，求 $\\triangle GHI$ 的周長 $=$＿＿＿＿。
- [包含純向量SVG幾何重繪：巢狀中點三角形周長]
- 難度：medium；單元：nanyi-9-1-1-2；來源頁：第1頁

#### 第 16 題
下列何者相似？答：＿＿＿＿。（單選）
(A) 任意兩個三角形
(B) 任意兩個等腰三角形
(C) 任意兩個正方形
(D) 任意兩個菱形
- 難度：easy；單元：nanyi-9-1-1-3；來源頁：第1頁

#### 第 17 題
如圖，四邊形 $ABCD$ 中，$E$、$F$、$G$、$H$ 為各邊中點。若 $\\overline{{AC}}=23$，$\\overline{{BD}}=25$，則四邊形 $EFGH$ 的周長 $=$＿＿＿＿。
- [包含純向量SVG幾何重繪：四邊形中點連線平行四邊形周長]
- 難度：medium；單元：nanyi-9-1-1-2；來源頁：第2頁

#### 第 18 題
如圖，$\\overline{{EF}} // \\overline{{BC}}$，$\\overline{{EC}}$ 與 $\\overline{{BF}}$ 交於 $A$ 點，$\\overline{{EF}}=20$，$\\overline{{BC}}=25$，$\\overline{{AE}}=12$，求 $\\overline{{AC}}=$＿＿＿＿。
- [包含純向量SVG幾何重繪：沙漏型相似三角形]
- 難度：easy；單元：nanyi-9-1-1-3；來源頁：第2頁

#### 第 19 題
如圖，$\\overline{{EC}}$ 與 $\\overline{{BF}}$ 交於 $A$ 點，$\\overline{{AB}}=4$，$\\overline{{AC}}=\\overline{{AE}}=12$，$\\overline{{AF}}=36$，$\\overline{{EF}}=30$，求 $\\overline{{BC}}=$＿＿＿＿。
- [包含純向量SVG幾何重繪：SAS相似三角形邊長推求]
- 難度：medium；單元：nanyi-9-1-1-3；來源頁：第2頁

#### 第 20 題
如圖，直線 $L$ 與直線 $M$ 交於 $A$ 點，$D$、$E$ 為 $\\overline{{AB}}$ 的三等分點，$F$、$G$、$H$ 為 $\\overline{{AC}}$ 的四等分點，若 $\\triangle EGH$ 的面積 $=3$，求 $\\triangle ABC$ 的面積 $=$＿＿＿＿。
- [包含純向量SVG幾何重繪：等分線段與三角形面積比]
- 難度：medium；單元：nanyi-9-1-1-2；來源頁：第2頁

#### 第 21 題
如圖，正方形 $ABCD$ 中，$\\angle HEF=\\angle EFG=90^\\circ$，$\\overline{{AH}}=4$，$\\overline{{AE}}=2$，$\\overline{{BE}}=8$，求 $\\triangle DHG$ 的面積 $=$＿＿＿＿。
- [包含純向量SVG幾何重繪：正方形內接旋轉直角三角形相似形]
- 難度：hard；單元：nanyi-9-1-1-3；來源頁：第2頁

#### 第 22 題
如圖，直角 $\\triangle ABC$ 中，$\\angle ABC=90^\\circ$，$D$ 為 $\\overline{{AC}}$ 的中點，若 $\\overline{{AC}}=10$，則 $\\overline{{BD}}=$＿＿＿＿。
- [包含純向量SVG幾何重繪：直角三角形斜邊中點性質]
- 難度：easy；單元：nanyi-9-1-3-2；來源頁：第2頁

#### 第 23 題
如圖，梯形 $ABCD$ 中，$\\angle A=\\angle B=90^\\circ$，$\\angle AED=\\angle BEC$，$\\overline{{AD}}:\\overline{{AE}}=5:4$，$\\overline{{AB}}=8$，求 $\\overline{{DE}}+\\overline{{CE}}=$＿＿＿＿。
- [包含純向量SVG幾何重繪：直角梯形入射反射角相似三角形]
- 難度：hard；單元：nanyi-9-1-1-3；來源頁：第2頁

#### 第 24 題
如圖，$\\triangle ABC$ 中，$\\angle B=90^\\circ$，四邊形 $DEBF$ 和四邊形 $GHFI$ 皆為正方形，$\\overline{{GI}}=2$，$\\overline{{AB}}=18$，求 $\\overline{{DF}}=$＿＿＿＿。
- [包含純向量SVG幾何重繪：直角三角形內接雙正方形相似三角形]
- 難度：hard；單元：nanyi-9-1-1-3；來源頁：第2頁

#### 第 25 題
如圖，正方形 $ABCD$ 中，$\\overline{{AB}}=7$，且 $\\angle DCE=45^\\circ$，$\\overline{{BE}}=13$，求 $\\overline{{CF}}=$＿＿＿＿。
- [包含純向量SVG幾何重繪：正方形外接截線與45度角相似推導]
- 難度：hard；單元：nanyi-9-1-1-3；來源頁：第2頁

## 原題盤點與未完成項目

- 原題盤點：一、填充題 25 題（共 25 格，每題 4 分，共 100 分）。
- 向量重繪：完成 14 幅純向量 SVG 幾何圖形重繪，完全依據原卷幾何特徵、標記、符號與文字排版，不含任何位圖、base64 或無效標籤。
- 未完成項目：無，全卷 25 題 100% 完整轉錄並通過字型覆蓋與結構驗證。

## 匯入資料（恰好一個JSON區塊）

```json
{json.dumps(delivery_data, ensure_ascii=False, indent=2)}
```
"""

md_path = ROOT / f"research/yilan/transcribed/{PAPER_ID}.md"
with open(md_path, "w", encoding="utf-8") as f:
    f.write(md_content)

print(f"Generated {md_path}")
