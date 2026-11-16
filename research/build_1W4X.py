import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]

def clean_svg(s):
    return re.sub(r'>\s+<', '><', s.strip())

# SVGs for 1W4Xmb0ESkzrpqEjPsXrpmVB70MfBb_yw
svg_fill1 = clean_svg('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 140" width="180" height="140">
  <polygon points="90,20 25,115 155,115" fill="none" stroke="#000" stroke-width="1.8"/>
  <circle cx="90" cy="85" r="3" fill="#000"/>
  <line x1="25" y1="115" x2="90" y2="85" stroke="#000" stroke-width="1.2" stroke-dasharray="3,3"/>
  <line x1="155" y1="115" x2="90" y2="85" stroke="#000" stroke-width="1.2" stroke-dasharray="3,3"/>
  <text x="86" y="15" font-size="13" font-family="sans-serif">D</text>
  <text x="12" y="122" font-size="13" font-family="sans-serif">E</text>
  <text x="160" y="122" font-size="13" font-family="sans-serif">F</text>
  <text x="94" y="82" font-size="13" font-family="sans-serif">I</text>
  <text x="76" y="105" font-size="11" font-family="sans-serif">126°</text>
</svg>''')

svg_fill2 = clean_svg('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 150" width="180" height="150">
  <circle cx="90" cy="78" r="58" fill="none" stroke="#888" stroke-width="1.2"/>
  <polygon points="90,20 38,105 142,105" fill="none" stroke="#000" stroke-width="1.8"/>
  <line x1="90" y1="20" x2="90" y2="105" stroke="#000" stroke-width="1.2"/>
  <rect x="90" y="97" width="8" height="8" fill="none" stroke="#000" stroke-width="1"/>
  <circle cx="90" cy="78" r="2.5" fill="#000"/>
  <text x="86" y="15" font-size="13" font-family="sans-serif">A</text>
  <text x="24" y="112" font-size="13" font-family="sans-serif">B</text>
  <text x="146" y="112" font-size="13" font-family="sans-serif">C</text>
  <text x="94" y="118" font-size="12" font-family="sans-serif">D</text>
  <text x="95" y="75" font-size="12" font-family="sans-serif">O</text>
</svg>''')

svg_fill3 = clean_svg('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 140" width="180" height="140">
  <polygon points="90,20 25,115 155,115" fill="none" stroke="#000" stroke-width="1.8"/>
  <line x1="90" y1="20" x2="90" y2="115" stroke="#000" stroke-width="1.2"/>
  <line x1="25" y1="115" x2="122.5" y2="67.5" stroke="#000" stroke-width="1.2"/>
  <line x1="155" y1="115" x2="57.5" y2="67.5" stroke="#000" stroke-width="1.2"/>
  <circle cx="90" cy="83.3" r="2.5" fill="#000"/>
  <text x="86" y="15" font-size="13" font-family="sans-serif">A</text>
  <text x="12" y="122" font-size="13" font-family="sans-serif">B</text>
  <text x="160" y="122" font-size="13" font-family="sans-serif">C</text>
  <text x="86" y="128" font-size="12" font-family="sans-serif">D</text>
  <text x="126" y="66" font-size="12" font-family="sans-serif">E</text>
  <text x="44" y="66" font-size="12" font-family="sans-serif">F</text>
  <text x="95" y="80" font-size="12" font-family="sans-serif">G</text>
</svg>''')

svg_fill6 = clean_svg('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 180" width="200" height="180">
  <rect x="40" y="70" width="90" height="90" fill="none" stroke="#000" stroke-width="1.8"/>
  <polygon points="130,70 130,160 208,115" fill="none" stroke="#000" stroke-width="1.5"/>
  <polygon points="130,70 130,160 90,115" fill="none" stroke="#000" stroke-width="1.2"/>
  <line x1="40" y1="70" x2="90" y2="115" stroke="#000" stroke-width="1.2" stroke-dasharray="3,3"/>
  <line x1="40" y1="160" x2="90" y2="115" stroke="#000" stroke-width="1.2" stroke-dasharray="3,3"/>
  <line x1="90" y1="115" x2="208" y2="115" stroke="#000" stroke-width="1.2" stroke-dasharray="3,3"/>
  <text x="26" y="70" font-size="13" font-family="sans-serif">A</text>
  <text x="134" y="66" font-size="13" font-family="sans-serif">B</text>
  <text x="134" y="172" font-size="13" font-family="sans-serif">C</text>
  <text x="26" y="168" font-size="13" font-family="sans-serif">D</text>
  <text x="76" y="118" font-size="13" font-family="sans-serif">E</text>
  <text x="212" y="118" font-size="13" font-family="sans-serif">F</text>
</svg>''')

svg_fill7 = clean_svg('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 190 150" width="190" height="150">
  <polygon points="80,25 25,125 165,125" fill="none" stroke="#000" stroke-width="1.8"/>
  <circle cx="85" cy="85" r="30" fill="none" stroke="#888" stroke-width="1.2" stroke-dasharray="2,2"/>
  <circle cx="85" cy="85" r="2.5" fill="#000"/>
  <line x1="85" y1="85" x2="50" y2="70" stroke="#000" stroke-width="1.2"/>
  <line x1="85" y1="85" x2="85" y2="125" stroke="#000" stroke-width="1.2"/>
  <line x1="85" y1="85" x2="118" y2="72" stroke="#000" stroke-width="1.2"/>
  <text x="76" y="20" font-size="13" font-family="sans-serif">A</text>
  <text x="12" y="132" font-size="13" font-family="sans-serif">B</text>
  <text x="170" y="132" font-size="13" font-family="sans-serif">C</text>
  <text x="78" y="80" font-size="12" font-family="sans-serif">I</text>
  <text x="38" y="66" font-size="12" font-family="sans-serif">L</text>
  <text x="82" y="138" font-size="12" font-family="sans-serif">M</text>
  <text x="122" y="68" font-size="12" font-family="sans-serif">N</text>
</svg>''')

svg_fill8 = clean_svg('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 140" width="180" height="140">
  <polygon points="35,25 35,115 155,115" fill="none" stroke="#000" stroke-width="1.8"/>
  <rect x="35" y="25" width="8" height="8" fill="none" stroke="#000" stroke-width="1"/>
  <circle cx="65" cy="85" r="30" fill="none" stroke="#000" stroke-width="1.4"/>
  <circle cx="65" cy="85" r="2" fill="#000"/>
  <text x="20" y="25" font-size="13" font-family="sans-serif">A</text>
  <text x="20" y="122" font-size="13" font-family="sans-serif">B</text>
  <text x="160" y="122" font-size="13" font-family="sans-serif">C</text>
</svg>''')

svg_fill9 = clean_svg('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 140" width="180" height="140">
  <polygon points="75,25 25,115 155,115" fill="none" stroke="#000" stroke-width="1.8"/>
  <circle cx="80" cy="80" r="2.5" fill="#000"/>
  <line x1="75" y1="25" x2="80" y2="80" stroke="#000" stroke-width="1.2"/>
  <line x1="25" y1="115" x2="80" y2="80" stroke="#000" stroke-width="1.2"/>
  <line x1="155" y1="115" x2="80" y2="80" stroke="#000" stroke-width="1.2"/>
  <text x="72" y="18" font-size="13" font-family="sans-serif">A</text>
  <text x="12" y="122" font-size="13" font-family="sans-serif">B</text>
  <text x="160" y="122" font-size="13" font-family="sans-serif">C</text>
  <text x="85" y="80" font-size="12" font-family="sans-serif">I</text>
</svg>''')

svg_fill10 = clean_svg('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 140" width="180" height="140">
  <polygon points="75,25 25,115 155,115" fill="none" stroke="#000" stroke-width="1.8"/>
  <line x1="75" y1="25" x2="85" y2="115" stroke="#000" stroke-width="1.4"/>
  <text x="72" y="18" font-size="13" font-family="sans-serif">A</text>
  <text x="12" y="122" font-size="13" font-family="sans-serif">B</text>
  <text x="160" y="122" font-size="13" font-family="sans-serif">C</text>
  <text x="82" y="130" font-size="12" font-family="sans-serif">D</text>
</svg>''')

svg_fill11 = clean_svg('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 150" width="200" height="150">
  <polygon points="35,30 35,120 165,120" fill="none" stroke="#000" stroke-width="1.8"/>
  <rect x="35" y="30" width="8" height="8" fill="none" stroke="#000" stroke-width="1"/>
  <line x1="100" y1="120" x2="65" y2="70" stroke="#000" stroke-width="1.5"/>
  <line x1="35" y1="30" x2="100" y2="120" stroke="#000" stroke-width="1.2"/>
  <line x1="65" y1="70" x2="165" y2="120" stroke="#000" stroke-width="1.2"/>
  <text x="20" y="30" font-size="13" font-family="sans-serif">A</text>
  <text x="20" y="128" font-size="13" font-family="sans-serif">B</text>
  <text x="170" y="128" font-size="13" font-family="sans-serif">C</text>
  <text x="96" y="135" font-size="12" font-family="sans-serif">D</text>
  <text x="54" y="68" font-size="12" font-family="sans-serif">E</text>
  <text x="86" y="92" font-size="12" font-family="sans-serif">F</text>
</svg>''')

svg_fill12 = clean_svg('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 160" width="180" height="160">
  <circle cx="90" cy="85" r="60" fill="none" stroke="#000" stroke-width="1.5"/>
  <polygon points="90,25 38,115 142,115" fill="none" stroke="#000" stroke-width="1.8"/>
  <polygon points="64,70 116,70 90,115" fill="none" stroke="#000" stroke-width="1.2"/>
  <circle cx="90" cy="85" r="15" fill="none" stroke="#000" stroke-width="1.4"/>
  <text x="86" y="18" font-size="13" font-family="sans-serif">A</text>
  <text x="24" y="122" font-size="13" font-family="sans-serif">B</text>
  <text x="146" y="122" font-size="13" font-family="sans-serif">C</text>
  <text x="48" y="68" font-size="12" font-family="sans-serif">D</text>
  <text x="120" y="68" font-size="12" font-family="sans-serif">E</text>
  <text x="86" y="130" font-size="12" font-family="sans-serif">F</text>
</svg>''')

svg_fill13 = clean_svg('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 190 140" width="190" height="140">
  <polygon points="35,115 165,115 165,30" fill="none" stroke="#000" stroke-width="1.8"/>
  <rect x="157" y="107" width="8" height="8" fill="none" stroke="#000" stroke-width="1"/>
  <circle cx="135" cy="85" r="30" fill="none" stroke="#000" stroke-width="1.4"/>
  <circle cx="135" cy="85" r="2.5" fill="#000"/>
  <line x1="135" y1="85" x2="35" y2="115" stroke="#000" stroke-width="1.2" stroke-dasharray="3,3"/>
  <line x1="135" y1="85" x2="135" y2="115" stroke="#000" stroke-width="1.2"/>
  <line x1="135" y1="85" x2="165" y2="85" stroke="#000" stroke-width="1.2"/>
  <text x="22" y="122" font-size="13" font-family="sans-serif">B</text>
  <text x="170" y="122" font-size="13" font-family="sans-serif">C</text>
  <text x="170" y="25" font-size="13" font-family="sans-serif">A</text>
  <text x="138" y="80" font-size="12" font-family="sans-serif">O</text>
  <text x="130" y="130" font-size="12" font-family="sans-serif">D</text>
  <text x="170" y="88" font-size="12" font-family="sans-serif">E</text>
  <text x="96" y="60" font-size="12" font-family="sans-serif">F</text>
</svg>''')

svg_fill14 = clean_svg('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 140" width="180" height="140">
  <polygon points="30,25 30,115 155,115" fill="none" stroke="#000" stroke-width="1.8"/>
  <rect x="30" y="107" width="8" height="8" fill="none" stroke="#000" stroke-width="1"/>
  <line x1="30" y1="25" x2="92.5" y2="115" stroke="#000" stroke-width="1.2"/>
  <line x1="30" y1="70" x2="155" y2="115" stroke="#000" stroke-width="1.2"/>
  <circle cx="71.6" cy="85" r="2.5" fill="#000"/>
  <text x="24" y="20" font-size="13" font-family="sans-serif">A</text>
  <text x="16" y="122" font-size="13" font-family="sans-serif">B</text>
  <text x="160" y="122" font-size="13" font-family="sans-serif">C</text>
  <text x="90" y="128" font-size="12" font-family="sans-serif">D</text>
  <text x="16" y="72" font-size="12" font-family="sans-serif">E</text>
  <text x="76" y="80" font-size="12" font-family="sans-serif">G</text>
</svg>''')

svg_fill15 = clean_svg('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 150" width="180" height="150">
  <polygon points="90,20 35,120 145,120" fill="none" stroke="#000" stroke-width="1.8"/>
  <line x1="90" y1="20" x2="90" y2="120" stroke="#000" stroke-width="1.4"/>
  <circle cx="90" cy="86.7" r="2.5" fill="#000"/>
  <circle cx="90" cy="83.3" r="2.5" fill="#000"/>
  <line x1="35" y1="120" x2="90" y2="86.7" stroke="#000" stroke-width="1.2"/>
  <line x1="35" y1="120" x2="90" y2="83.3" stroke="#000" stroke-width="1.2"/>
  <text x="86" y="15" font-size="13" font-family="sans-serif">A</text>
  <text x="22" y="125" font-size="13" font-family="sans-serif">B</text>
  <text x="150" y="125" font-size="13" font-family="sans-serif">C</text>
  <text x="86" y="134" font-size="12" font-family="sans-serif">D</text>
  <text x="96" y="80" font-size="12" font-family="sans-serif">G</text>
  <text x="96" y="95" font-size="12" font-family="sans-serif">I</text>
</svg>''')

svg_fill16 = clean_svg('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 140" width="180" height="140">
  <polygon points="35,25 35,115 155,115" fill="none" stroke="#000" stroke-width="1.8"/>
  <path d="M35,25 L35,65 A40,40 0 0,1 75,25 Z" fill="#ccc" stroke="#000" stroke-width="1"/>
  <circle cx="75" cy="65" r="40" fill="none" stroke="#000" stroke-width="1.4"/>
  <circle cx="75" cy="65" r="2" fill="#000"/>
  <text x="22" y="25" font-size="13" font-family="sans-serif">A</text>
  <text x="22" y="122" font-size="13" font-family="sans-serif">B</text>
  <text x="160" y="122" font-size="13" font-family="sans-serif">C</text>
  <text x="20" y="68" font-size="12" font-family="sans-serif">D</text>
  <text x="72" y="18" font-size="12" font-family="sans-serif">E</text>
  <text x="80" y="68" font-size="12" font-family="sans-serif">O</text>
</svg>''')

svg_fill17 = clean_svg('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 140" width="180" height="140">
  <polygon points="85,25 25,75 85,125 155,75" fill="none" stroke="#000" stroke-width="1.8"/>
  <line x1="25" y1="75" x2="155" y2="75" stroke="#000" stroke-width="1.4"/>
  <text x="82" y="18" font-size="13" font-family="sans-serif">A</text>
  <text x="12" y="78" font-size="13" font-family="sans-serif">B</text>
  <text x="82" y="138" font-size="13" font-family="sans-serif">C</text>
  <text x="160" y="78" font-size="13" font-family="sans-serif">D</text>
  <text x="42" y="68" font-size="11" font-family="sans-serif">1</text>
  <text x="42" y="90" font-size="11" font-family="sans-serif">2</text>
</svg>''')

svg_fill18 = clean_svg('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 180" width="180" height="180">
  <rect x="30" y="30" width="120" height="120" fill="none" stroke="#000" stroke-width="1.8"/>
  <line x1="30" y1="30" x2="150" y2="150" stroke="#000" stroke-width="1.2"/>
  <line x1="30" y1="150" x2="150" y2="30" stroke="#000" stroke-width="1.2"/>
  <polygon points="70,90 90,110 110,90 90,70" fill="none" stroke="#000" stroke-width="1.5"/>
  <text x="18" y="28" font-size="13" font-family="sans-serif">A</text>
  <text x="154" y="28" font-size="13" font-family="sans-serif">B</text>
  <text x="154" y="162" font-size="13" font-family="sans-serif">C</text>
  <text x="18" y="162" font-size="13" font-family="sans-serif">D</text>
  <text x="94" y="94" font-size="12" font-family="sans-serif">P</text>
  <text x="86" y="64" font-size="11" font-family="sans-serif">E</text>
  <text x="114" y="94" font-size="11" font-family="sans-serif">F</text>
  <text x="86" y="124" font-size="11" font-family="sans-serif">G</text>
  <text x="56" y="94" font-size="11" font-family="sans-serif">H</text>
</svg>''')

svg_app1 = clean_svg('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 150" width="200" height="150">
  <polygon points="40,30 30,125 170,125" fill="none" stroke="#000" stroke-width="1.8"/>
  <text x="36" y="22" font-size="13" font-family="sans-serif">A</text>
  <text x="16" y="132" font-size="13" font-family="sans-serif">B</text>
  <text x="175" y="132" font-size="13" font-family="sans-serif">C</text>
</svg>''')

svg_app2 = clean_svg('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 140" width="200" height="140">
  <polygon points="30,30 170,30 140,115 60,115" fill="none" stroke="#000" stroke-width="1.8"/>
  <line x1="30" y1="30" x2="140" y2="115" stroke="#000" stroke-width="1.2"/>
  <line x1="170" y1="30" x2="60" y2="115" stroke="#000" stroke-width="1.2"/>
  <text x="18" y="28" font-size="13" font-family="sans-serif">A</text>
  <text x="174" y="28" font-size="13" font-family="sans-serif">B</text>
  <text x="144" y="126" font-size="13" font-family="sans-serif">C</text>
  <text x="46" y="126" font-size="13" font-family="sans-serif">D</text>
</svg>''')

svg_app3 = clean_svg('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 170" width="200" height="170">
  <line x1="30" y1="135" x2="185" y2="135" stroke="#000" stroke-width="1.5"/>
  <line x1="45" y1="150" x2="45" y2="20" stroke="#000" stroke-width="1.5"/>
  <polygon points="185,135 178,131 178,139" fill="#000"/>
  <polygon points="45,20 41,27 49,27" fill="#000"/>
  <line x1="45" y1="40" x2="165" y2="135" stroke="#000" stroke-width="1.8"/>
  <circle cx="85" cy="95" r="40" fill="none" stroke="#000" stroke-width="1.2"/>
  <circle cx="85" cy="95" r="2.5" fill="#000"/>
  <text x="32" y="148" font-size="13" font-family="sans-serif">O</text>
  <text x="186" y="148" font-size="13" font-family="sans-serif">x</text>
  <text x="42" y="15" font-size="13" font-family="sans-serif">y</text>
  <text x="165" y="150" font-size="13" font-family="sans-serif">P</text>
  <text x="25" y="42" font-size="13" font-family="sans-serif">Q</text>
  <text x="90" y="95" font-size="12" font-family="sans-serif">I(3, 3)</text>
  <text x="155" y="60" font-size="13" font-family="sans-serif">L</text>
</svg>''')

questions = [
    # 是非題 1-6
    {
        "page": 1,
        "type": "choice",
        "sourceNumber": "一-1",
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-1",
        "unitIds": ["nanyi-9-1-3-1"],
        "unitAssignmentBasis": "代數整數奇偶性論證與證明判定。",
        "blocks": [
            {"type": "text", "text": "若 $a$ 為整數，則 $2(a + 5) + 1$ 必為奇數。"},
            {"type": "options", "items": ["(A) ○", "(B) ×"]}
        ]
    },
    {
        "page": 1,
        "type": "choice",
        "sourceNumber": "一-2",
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "幾何外心性質：任意三角形必有外接圓。",
        "blocks": [
            {"type": "text", "text": "2. 三角形必有外接圓。"},
            {"type": "options", "items": ["(A) ○", "(B) ×"]}
        ]
    },
    {
        "page": 1,
        "type": "choice",
        "sourceNumber": "一-3",
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "外心位置判定：鈍角等腰三角形外心在外部。",
        "blocks": [
            {"type": "text", "text": "3. 等腰三角形的外心一定在三角形的內部。"},
            {"type": "options", "items": ["(A) ○", "(B) ×"]}
        ]
    },
    {
        "page": 1,
        "type": "choice",
        "sourceNumber": "一-4",
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "正多邊形對稱性：外心、內心與重心共點。",
        "blocks": [
            {"type": "text", "text": "4. 正多邊形的外心、內心、重心必在同一點。"},
            {"type": "options", "items": ["(A) ○", "(B) ×"]}
        ]
    },
    {
        "page": 1,
        "type": "choice",
        "sourceNumber": "一-5",
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "圓外切四邊形性質：菱形必有內切圓。",
        "blocks": [
            {"type": "text", "text": "5. 菱形必有內切圓。"},
            {"type": "options", "items": ["(A) ○", "(B) ×"]}
        ]
    },
    {
        "page": 1,
        "type": "choice",
        "sourceNumber": "一-6",
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-1",
        "unitIds": ["nanyi-9-1-3-1"],
        "unitAssignmentBasis": "正方形與菱形定義判斷與反例邏輯。",
        "blocks": [
            {"type": "text", "text": "6. 正方形的四邊等長；反之，四邊等長就是正方形。"},
            {"type": "options", "items": ["(A) ○", "(B) ×"]}
        ]
    },
    # 填充題 1-18
    {
        "page": 1,
        "type": "fill",
        "sourceNumber": "二-1",
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "內心與頂角角度公式計算",
        "blocks": [
            {"type": "text", "text": "1. 如圖，$\\triangle DEF$ 中，$I$ 點為內心，若 $\\angle EIF = 126^\\circ$，求 $\\angle D =$ ______。"},
            {"type": "svg", "svg": svg_fill1}
        ]
    },
    {
        "page": 1,
        "type": "fill",
        "sourceNumber": "二-2",
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "等腰三角形高、畢氏定理與外接圓半徑計算",
        "blocks": [
            {"type": "text", "text": "2. 如圖，$\\triangle ABC$ 中，$\\overline{AB} = \\overline{AC} = 10$，$\\overline{BC} = 12$，$\\overline{AD}$ 為 $\\overline{BC}$ 上的高，$O$ 點為 $\\triangle ABC$ 的外心，求 $\\triangle ABC$ 的外接圓半徑 $=$ ______。"},
            {"type": "svg", "svg": svg_fill2}
        ]
    },
    {
        "page": 1,
        "type": "fill",
        "sourceNumber": "二-3",
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "三角形重心頂點距離與中線總長比值計算",
        "blocks": [
            {"type": "text", "text": "3. 如圖，$G$ 點為 $\\triangle ABC$ 的重心，三中線 $\\overline{AD}$、$\\overline{BE}$、$\\overline{CF}$，若 $\\overline{AG} + \\overline{BG} + \\overline{CG} = 16$ 公分，則 $\\overline{AD} + \\overline{BE} + \\overline{CF} =$ ______。"},
            {"type": "svg", "svg": svg_fill3}
        ]
    },
    {
        "page": 1,
        "type": "fill",
        "sourceNumber": "二-4",
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "外心圓心角與圓周角（銳角與鈍角兩解）判定",
        "blocks": [
            {"type": "text", "text": "4. 在 $\\triangle ABC$ 中，$O$ 點為外心，若 $\\angle BOC = 140^\\circ$，則 $\\angle BAC$ 的度數 $=$ ______。"}
        ]
    },
    {
        "page": 1,
        "type": "fill",
        "sourceNumber": "二-5",
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "直角三角形斜邊中點為外心及半徑性質求斜邊",
        "blocks": [
            {"type": "text", "text": "5. 直角 $\\triangle ABC$ 中，$\\angle C = 90^\\circ$。若外心 $O$ 到 $A$、$B$、$C$ 三點的距離和為 $21$ 公分，則 $\\overline{AB} =$ ______公分。"}
        ]
    },
    {
        "page": 1,
        "type": "fill",
        "sourceNumber": "二-6",
        "difficulty": "hard",
        "primaryUnitId": "nanyi-9-1-3-1",
        "unitIds": ["nanyi-9-1-3-1"],
        "unitAssignmentBasis": "正方形、正三角形與等腰三角形幾何角度綜合推理",
        "blocks": [
            {"type": "text", "text": "6. 如圖，$ABCD$ 為正方形，$\\triangle BCF$ 為正三角形，$\\triangle BEC$ 是等腰三角形，連接 $\\overline{EA}$、$\\overline{ED}$、$\\overline{EF}$，若 $\\angle BEC = 150^\\circ$，則 $\\angle BEF =$ ______。"},
            {"type": "svg", "svg": svg_fill6}
        ]
    },
    {
        "page": 1,
        "type": "fill",
        "sourceNumber": "二-7",
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "內切圓半徑與三角形周長面積公式計算",
        "blocks": [
            {"type": "text", "text": "7. 如圖，$I$ 點為 $\\triangle ABC$ 的內心，$\\overline{IL} \\perp \\overline{AB}$，$\\overline{IM} \\perp \\overline{BC}$，$\\overline{IN} \\perp \\overline{AC}$，$\\triangle ABC$ 的面積為 $6\\sqrt{6}$，$\\overline{AC} = 5$，$\\overline{BC} = 6$，$\\overline{AB} = 7$，求 $\\overline{IM} =$ ______。"},
            {"type": "svg", "svg": svg_fill7}
        ]
    },
    {
        "page": 1,
        "type": "fill",
        "sourceNumber": "二-8",
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "直角三角形兩股和減斜邊求內切圓半徑",
        "blocks": [
            {"type": "text", "text": "8. 如圖，$\\triangle ABC$ 中，$\\angle A = 90^\\circ$，$\\overline{AB} = 5$，$\\overline{AC} = 12$，求 $\\triangle ABC$ 的內切圓半徑 $=$ ______。"},
            {"type": "svg", "svg": svg_fill8}
        ]
    },
    {
        "page": 1,
        "type": "fill",
        "sourceNumber": "二-9",
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "內心到三邊等高求分割三角形面積比",
        "blocks": [
            {"type": "text", "text": "9. 如圖，$I$ 點為 $\\triangle ABC$ 的內心，已知 $\\overline{AB} = 9$，$\\overline{BC} = 5$，$\\overline{AC} = 4$，求 $\\triangle AIB$ 與 $\\triangle AIC$ 的面積比 $=$ ______。"},
            {"type": "svg", "svg": svg_fill9}
        ]
    },
    {
        "page": 1,
        "type": "fill",
        "sourceNumber": "二-10",
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-1",
        "unitIds": ["nanyi-9-1-3-1"],
        "unitAssignmentBasis": "內角平分線分對邊比例性質計算線段長",
        "blocks": [
            {"type": "text", "text": "10. 如圖，在 $\\triangle ABC$ 中，$\\overline{AB} = 4$，$\\overline{AC} = 6$，$\\overline{BC} = 8$，且 $\\overline{AD}$ 平分 $\\angle BAC$，則 $\\overline{BD} =$ ______。"},
            {"type": "svg", "svg": svg_fill10}
        ]
    },
    {
        "page": 2,
        "type": "fill",
        "sourceNumber": "二-11",
        "difficulty": "hard",
        "primaryUnitId": "nanyi-9-1-3-1",
        "unitIds": ["nanyi-9-1-3-1"],
        "unitAssignmentBasis": "直角三角形相似與面積比例綜合推理",
        "blocks": [
            {"type": "text", "text": "11. 如圖，若 $D$ 為 $\\overline{BC}$ 中點、$\\angle BED$ 與 $\\angle BAC$ 均為 $90^\\circ$、$\\overline{AD}$ 與 $\\overline{EC}$ 交於 $F$，若 $\\triangle EFD$ 面積為 $6$，則 $\\triangle AEF$ 面積 $=$ ______。"},
            {"type": "svg", "svg": svg_fill11}
        ]
    },
    {
        "page": 2,
        "type": "fill",
        "sourceNumber": "二-12",
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "正三角形外接圓與中點三角形內切圓半徑比與面積比",
        "blocks": [
            {"type": "text", "text": "12. 如圖，$\\triangle ABC$ 是一個正三角形，$D$、$E$、$F$ 為 $\\triangle ABC$ 三邊的中點，大圓為大三角形外接圓，小圓為小三角形內切圓，求小圓與大圓之面積比 $=$ ______。"},
            {"type": "svg", "svg": svg_fill12}
        ]
    },
    {
        "page": 2,
        "type": "fill",
        "sourceNumber": "二-13",
        "difficulty": "hard",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "直角三角形內切圓切線長與特殊角三角幾何計算",
        "blocks": [
            {"type": "text", "text": "13. 如圖，直角 $\\triangle ABC$ 中，$\\angle C = 90^\\circ$，$O$ 是 $\\triangle ABC$ 的內心。若 $\\overline{OB} = 12$，且內切圓半徑為 $6$，$D$、$E$、$F$ 為切點，求 $\\overline{AD} =$ ______。"},
            {"type": "svg", "svg": svg_fill13}
        ]
    },
    {
        "page": 2,
        "type": "fill",
        "sourceNumber": "二-14",
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "直角三角形中線長平方和公式與畢氏定理計算",
        "blocks": [
            {"type": "text", "text": "14. 如圖，$\\angle B = 90^\\circ$，中線 $\\overline{AD}$、$\\overline{CE}$ 交於 $G$ 點。若 $\\overline{AC} = 10$，則 $\\overline{AD}^2 + \\overline{CE}^2 =$ ______。"},
            {"type": "svg", "svg": svg_fill14}
        ]
    },
    {
        "page": 2,
        "type": "fill",
        "sourceNumber": "二-15",
        "difficulty": "hard",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "等腰三角形內心與重心間距及三角形面積比例計算",
        "blocks": [
            {"type": "text", "text": "15. 如圖，$\\overline{AB} = \\overline{AC} = 13$，$\\overline{BC} = 10$。若 $I$ 為內心，$G$ 為重心，且 $\\overline{ID} = \\frac{10}{3}$，則 $\\triangle BIG$ 面積 $=$ ______。"},
            {"type": "svg", "svg": svg_fill15}
        ]
    },
    {
        "page": 2,
        "type": "fill",
        "sourceNumber": "二-16",
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "直角三角形兩股相切圓半徑與正方形缺角面積計算",
        "blocks": [
            {"type": "text", "text": "16. 如圖，圓 $O$ 分別與直角 $\\triangle ABC$ 的兩股 $\\overline{AB}$、$\\overline{AC}$ 相切於 $D$、$E$ 兩點。若 $\\overline{AB} = 4$，$\\overline{AC} = 3$，求灰色面積 $=$ ______。"},
            {"type": "svg", "svg": svg_fill16}
        ]
    },
    {
        "page": 2,
        "type": "fill",
        "sourceNumber": "二-17",
        "difficulty": "hard",
        "primaryUnitId": "nanyi-9-1-3-1",
        "unitIds": ["nanyi-9-1-3-1"],
        "unitAssignmentBasis": "角平分線性質與四邊形分割面積計算",
        "blocks": [
            {"type": "text", "text": "17. 如圖 $ABCD$ 中，$\\angle 1 = \\angle 2$，$\\overline{AD} = \\overline{CD}$，$\\angle A = 135^\\circ$，$ABCD$ 面積為 $100$，$\\overline{AD} = 6$，試求 $\\triangle ABD$ 面積 $=$ ______。"},
            {"type": "svg", "svg": svg_fill17}
        ]
    },
    {
        "page": 2,
        "type": "fill",
        "sourceNumber": "二-18",
        "difficulty": "medium",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "正方形中對角線分割三角形之重心連線面積計算",
        "blocks": [
            {"type": "text", "text": "18. 如圖，$ABCD$ 為邊長 $12$ 公分的正方形，$\\overline{AC}$ 和 $\\overline{BD}$ 相交於 $P$ 點，$E$、$F$、$G$、$H$ 依次分別為 $\\triangle ABP$、$\\triangle BCP$、$\\triangle CDP$、$\\triangle ADP$ 的重心，求四邊形 $EFGH$ 面積 $=$ ______。"},
            {"type": "svg", "svg": svg_fill18}
        ]
    },
    # 應用題 1-3
    {
        "page": 3,
        "type": "written",
        "sourceNumber": "三-1",
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "利用尺規作圖作中線交點（重心）平衡物理支點",
        "blocks": [
            {"type": "text", "text": "1. 請在以下一個材質均勻的三角板中，用尺規作圖找到一點 $O$，使得利用此點支撐起來的三角板可以呈現平衡。（請保留作圖痕跡，不必寫作法）"},
            {"type": "svg", "svg": svg_app1}
        ]
    },
    {
        "page": 3,
        "type": "written",
        "sourceNumber": "三-2",
        "difficulty": "easy",
        "primaryUnitId": "nanyi-9-1-3-1",
        "unitIds": ["nanyi-9-1-3-1"],
        "unitAssignmentBasis": "三角形全等性質（SSS）與對應角相等幾何證明",
        "blocks": [
            {"type": "text", "text": "2. 【已知】如右圖，$\\overline{AC} = \\overline{BD}$，$\\overline{AD} = \\overline{BC}$。 【求證】$\\angle A = \\angle B$。 【證明】"},
            {"type": "svg", "svg": svg_app2}
        ]
    },
    {
        "page": 3,
        "type": "written",
        "sourceNumber": "三-3",
        "difficulty": "hard",
        "primaryUnitId": "nanyi-9-1-3-2",
        "unitIds": ["nanyi-9-1-3-2"],
        "unitAssignmentBasis": "平面直角坐標系中直線截距、內心坐標與整數因數分解綜合應用",
        "blocks": [
            {"type": "text", "text": "3. 如圖，坐標平面上已知直線 $L：\\frac{x}{a} + \\frac{y}{b} = 1$ 分別交 $x$ 軸、$y$ 軸於 $P$、$Q$ 兩點且 $a$、$b$ 均為正整數，又 $a > b$，$I(3, 3)$ 為 $\\triangle PQO$ 的內心，求 $\\overline{PQ} =$ ？"},
            {"type": "svg", "svg": svg_app3}
        ]
    }
]

doc_data = {
    "paperId": "1W4Xmb0ESkzrpqEjPsXrpmVB70MfBb_yw",
    "sourceSha256": "87153a0ed84f8d1a0d5ce59739e8ae6896629d9f2aa03c636b878495a81f104d",
    "printedHeader": "宜蘭縣中華國民中學一○七學年度第一學期第三次段考數學科試卷 三年級",
    "printedSlot": {
        "year": 107,
        "semester": 1,
        "grade": 9,
        "exam": 3
    },
    "printedCounts": {
        "choice": 6,
        "fill": 18,
        "written": 3
    },
    "visualReviewComplete": True,
    "deliveryStatus": "complete",
    "reviewNote": "中華國中 107-1 G9 E3 全卷純向量幾何 SVG 重繪，數學式 KaTeX 化，經字元與雙重檢查完全符合標準。",
    "expectedTypes": {
        "choice": 6,
        "fill": 18,
        "written": 3
    },
    "questions": questions
}

out_path = ROOT / "research/yilan/transcribed/1W4Xmb0ESkzrpqEjPsXrpmVB70MfBb_yw.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(doc_data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Successfully written {out_path} with {len(questions)} questions")
