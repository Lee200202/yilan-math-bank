"""Build transcription JSON for paper 1eLubRDPNY4xg91wn88cKQ4NcFmoupS_U
宜蘭縣中華國民中學一○九學年度第一學期第二次段考數學科試卷 九年級
"""
import hashlib
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

paper_id = '1eLubRDPNY4xg91wn88cKQ4NcFmoupS_U'
pdf_path = ROOT / f'research/zhonghua_raw/{paper_id}.pdf'
if not pdf_path.exists():
    pdf_path = ROOT / f'public/papers/{paper_id}.pdf'
pdf_sha256 = hashlib.sha256(pdf_path.read_bytes()).hexdigest()

font_attr = 'font-family="\'TW-Kai\', \'BiauKai\', \'DFKai-SB\', serif" font-size="16" font-style="italic"'
normal_font = 'font-family="\'TW-Kai\', \'BiauKai\', \'DFKai-SB\', serif" font-size="14" font-style="normal"'
small_font = 'font-family="\'TW-Kai\', \'BiauKai\', \'DFKai-SB\', serif" font-size="12" font-style="normal"'

def clean_svg(svg: str) -> str:
    return ' '.join(svg.strip().split())

# SVG Q2
svg_q2 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 205" width="200" height="205">
  <path d="M 95,175 L 84,156 A 22,22 0 0,1 106,156 Z" fill="#e0e0e0" stroke="#111" stroke-width="1"/>
  <line x1="95" y1="175" x2="20" y2="45" stroke="#111" stroke-width="1.3"/>
  <line x1="95" y1="175" x2="170" y2="45" stroke="#111" stroke-width="1.3"/>
  <path d="M 77,144 A 35,35 0 0,1 113,144" fill="none" stroke="#111" stroke-width="1.2"/>
  <path d="M 65,123 A 60,60 0 0,1 125,123" fill="none" stroke="#111" stroke-width="1.2"/>
  <path d="M 40,80 A 110,110 0 0,1 150,80" fill="none" stroke="#111" stroke-width="1.2"/>
  <path d="M 20,45 A 150,150 0 0,1 170,45" fill="none" stroke="#111" stroke-width="1.4"/>
  <text x="95" y="142" {small_font} fill="#111" text-anchor="middle">60°</text>
  <g {font_attr} fill="#111">
    <text x="95" y="195" text-anchor="middle">O</text>
    <text x="8" y="48">A</text>
    <text x="176" y="48">B</text>
    <text x="28" y="83">C</text>
    <text x="156" y="83">D</text>
    <text x="52" y="125">E</text>
    <text x="132" y="125">F</text>
    <text x="64" y="148">G</text>
    <text x="120" y="148">H</text>
  </g>
</svg>''')

# SVG Q3
svg_q3 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 210 210" width="210" height="210">
  <circle cx="100" cy="100" r="75" fill="none" stroke="#111" stroke-width="1.3"/>
  <line x1="49" y1="45" x2="151" y2="45" stroke="#111" stroke-width="1.3"/>
  <line x1="100" y1="100" x2="100" y2="45" stroke="#111" stroke-width="1.1"/>
  <path d="M 100,53 L 108,53 L 108,45" fill="none" stroke="#111" stroke-width="0.9"/>
  <line x1="50" y1="46" x2="26" y2="110" stroke="#111" stroke-width="1.3"/>
  <line x1="100" y1="100" x2="38" y2="78" stroke="#111" stroke-width="1.1"/>
  <path d="M 35,86 L 43,89 L 46,81" fill="none" stroke="#111" stroke-width="0.9"/>
  <line x1="35" y1="128" x2="155" y2="160" stroke="#111" stroke-width="1.3"/>
  <line x1="100" y1="100" x2="95" y2="144" stroke="#111" stroke-width="1.1"/>
  <path d="M 97,136 L 105,138 L 103,146" fill="none" stroke="#111" stroke-width="0.9"/>
  <line x1="165" y1="68" x2="172" y2="140" stroke="#111" stroke-width="1.3"/>
  <line x1="100" y1="100" x2="168" y2="104" stroke="#111" stroke-width="1.1"/>
  <path d="M 160,103 L 160,95 L 168,96" fill="none" stroke="#111" stroke-width="0.9"/>
  <circle cx="100" cy="100" r="2.5" fill="#111"/>
  <g {font_attr} fill="#111">
    <text x="110" y="96">O</text>
    <text x="175" y="148">A</text>
    <text x="168" y="65">B</text>
    <text x="153" y="40">C</text>
    <text x="42" y="40">D</text>
    <text x="38" y="42">E</text>
    <text x="10" y="118">F</text>
    <text x="18" y="135">G</text>
    <text x="156" y="172">H</text>
    <text x="172" y="102">P</text>
    <text x="86" y="58">Q</text>
    <text x="24" y="78">R</text>
    <text x="82" y="156">S</text>
  </g>
</svg>''')

# SVG Q4
svg_q4 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 210 200" width="210" height="200">
  <circle cx="100" cy="105" r="65" fill="none" stroke="#111" stroke-width="1.3"/>
  <line x1="15" y1="128" x2="85" y2="30" stroke="#111" stroke-width="1.2"/>
  <line x1="55" y1="155" x2="50" y2="75" stroke="#111" stroke-width="1.2"/>
  <line x1="50" y1="75" x2="95" y2="40" stroke="#111" stroke-width="1.2"/>
  <line x1="55" y1="155" x2="95" y2="40" stroke="#111" stroke-width="1.2"/>
  <line x1="55" y1="155" x2="125" y2="130" stroke="#111" stroke-width="1.2"/>
  <line x1="50" y1="75" x2="125" y2="130" stroke="#111" stroke-width="1.2"/>
  <line x1="55" y1="155" x2="175" y2="55" stroke="#111" stroke-width="1.2"/>
  <line x1="50" y1="75" x2="175" y2="55" stroke="#111" stroke-width="1.2"/>
  <path d="M 125,130 L 110,125 A 15,15 0 0,0 115,135 Z" fill="#aaa"/>
  <path d="M 95,40 L 90,52 A 15,15 0 0,0 85,46 Z" fill="#aaa"/>
  <path d="M 175,55 L 160,56 A 15,15 0 0,0 162,65 Z" fill="#aaa"/>
  <path d="M 50,75 L 45,86 A 12,12 0 0,0 52,90 Z" fill="#aaa"/>
  <text x="105" y="132" {small_font} fill="#111">1</text>
  <text x="82" y="58" {small_font} fill="#111">2</text>
  <text x="150" y="66" {small_font} fill="#111">3</text>
  <text x="44" y="100" {small_font} fill="#111">4</text>
  <g {font_attr} fill="#111">
    <text x="85" y="24">L</text>
    <text x="94" y="32">C</text>
    <text x="180" y="58">E</text>
    <text x="130" y="135">D</text>
    <text x="42" y="168">A</text>
    <text x="32" y="78">B</text>
  </g>
</svg>''')

# SVG Q5
svg_q5 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 195 190" width="195" height="190">
  <circle cx="95" cy="95" r="65" fill="none" stroke="#111" stroke-width="1.3"/>
  <line x1="35" y1="65" x2="155" y2="65" stroke="#111" stroke-width="1.3"/>
  <line x1="35" y1="125" x2="155" y2="125" stroke="#111" stroke-width="1.3"/>
  <line x1="35" y1="65" x2="155" y2="125" stroke="#111" stroke-width="1.2"/>
  <line x1="95" y1="95" x2="155" y2="65" stroke="#111" stroke-width="1.2"/>
  <circle cx="95" cy="95" r="2.5" fill="#111"/>
  <path d="M 88,91 A 8,8 0 0,1 102,91" fill="none" stroke="#111" stroke-width="1"/>
  <text x="95" y="82" {small_font} fill="#111" text-anchor="middle">125°</text>
  <g {font_attr} fill="#111">
    <text x="18" y="65">A</text>
    <text x="162" y="65">B</text>
    <text x="18" y="132">C</text>
    <text x="162" y="132">D</text>
    <text x="95" y="115" text-anchor="middle">O</text>
  </g>
</svg>''')

# SVG Q6
svg_q6 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 195 185" width="195" height="185">
  <defs>
    <marker id="arr6" viewBox="0 0 8 8" refX="5" refY="4" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 6 4 L 0 6.5 z" fill="#111"/>
    </marker>
  </defs>
  <line x1="20" y1="95" x2="165" y2="95" stroke="#111" stroke-width="1.3" marker-end="url(#arr6)"/>
  <line x1="85" y1="165" x2="85" y2="20" stroke="#111" stroke-width="1.3" marker-end="url(#arr6)"/>
  <line x1="20" y1="45" x2="160" y2="45" stroke="#111" stroke-width="1.2"/>
  <circle cx="50" cy="140" r="2.5" fill="#111"/>
  <text x="145" y="40" {font_attr} fill="#111">y=10</text>
  <text x="172" y="100" {font_attr} fill="#111">x</text>
  <text x="85" y="14" {font_attr} fill="#111" text-anchor="middle">y</text>
  <text x="15" y="155" {font_attr} fill="#111">A(-5,-12)</text>
</svg>''')

# SVG Q7
svg_q7 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 180" width="220" height="180">
  <circle cx="75" cy="95" r="50" fill="#e8e8e8" stroke="#111" stroke-width="1.3"/>
  <circle cx="75" cy="95" r="2.5" fill="#111"/>
  <line x1="190" y1="95" x2="97" y2="50" stroke="#111" stroke-width="1.2"/>
  <line x1="190" y1="95" x2="97" y2="140" stroke="#111" stroke-width="1.2"/>
  <line x1="75" y1="95" x2="97" y2="50" stroke="#111" stroke-width="1.1"/>
  <line x1="75" y1="95" x2="97" y2="140" stroke="#111" stroke-width="1.1"/>
  <line x1="75" y1="95" x2="190" y2="95" stroke="#111" stroke-width="1.1"/>
  <line x1="97" y1="50" x2="97" y2="140" stroke="#111" stroke-width="1.2"/>
  <g {font_attr} fill="#111">
    <text x="55" y="98">O</text>
    <text x="97" y="40" text-anchor="middle">A</text>
    <text x="97" y="158" text-anchor="middle">B</text>
    <text x="195" y="98">P</text>
  </g>
</svg>''')

# SVG Q8
svg_q8 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 195 195" width="195" height="195">
  <circle cx="95" cy="95" r="65" fill="none" stroke="#111" stroke-width="1.3"/>
  <circle cx="95" cy="95" r="2.5" fill="#111"/>
  <line x1="50" y1="36" x2="32" y2="120" stroke="#111" stroke-width="1.2"/>
  <line x1="32" y1="120" x2="132" y2="154" stroke="#111" stroke-width="1.2"/>
  <line x1="140" y1="36" x2="158" y2="120" stroke="#111" stroke-width="1.2"/>
  <line x1="158" y1="120" x2="58" y2="154" stroke="#111" stroke-width="1.2"/>
  <g {font_attr} fill="#111">
    <text x="105" y="92">O</text>
    <text x="38" y="30">A</text>
    <text x="145" y="30">D</text>
    <text x="18" y="128">B</text>
    <text x="165" y="128">E</text>
    <text x="50" y="170">F</text>
    <text x="136" y="170">C</text>
  </g>
</svg>''')

# SVG Q9
svg_q9 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 210 180" width="210" height="180">
  <circle cx="105" cy="90" r="45" fill="none" stroke="#111" stroke-width="1.3"/>
  <circle cx="105" cy="90" r="2.5" fill="#111"/>
  <polygon points="95,45 155,55 145,145 25,115" fill="none" stroke="#111" stroke-width="1.3"/>
  <text x="48" y="75" {font_attr} fill="#111">13-y</text>
  <text x="85" y="145" {font_attr} fill="#111">2y+4</text>
  <text x="150" y="102" {font_attr} fill="#111">5x-2</text>
  <text x="125" y="40" {font_attr} fill="#111" text-anchor="middle">2x+1</text>
  <g {font_attr} fill="#111">
    <text x="105" y="78" text-anchor="middle">O</text>
    <text x="88" y="38">A</text>
    <text x="12" y="122">B</text>
    <text x="148" y="162">C</text>
    <text x="160" y="50">D</text>
  </g>
</svg>''')

# SVG Q10
svg_q10 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 195 190" width="195" height="190">
  <circle cx="95" cy="95" r="60" fill="#edf4fa" stroke="#111" stroke-width="1.3"/>
  <line x1="95" y1="35" x2="95" y2="155" stroke="#111" stroke-width="1.3"/>
  <line x1="45" y1="60" x2="150" y2="112" stroke="#111" stroke-width="1.2"/>
  <circle cx="95" cy="95" r="2.5" fill="#111"/>
  <g {font_attr} fill="#111">
    <text x="95" y="26" text-anchor="middle">A</text>
    <text x="95" y="170" text-anchor="middle">B</text>
    <text x="78" y="100">O</text>
    <text x="100" y="82">P</text>
    <text x="30" y="60">C</text>
    <text x="155" y="118">D</text>
  </g>
</svg>''')

# SVG Q11
svg_q11 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 215 195" width="215" height="195">
  <circle cx="75" cy="75" r="50" fill="none" stroke="#111" stroke-width="1.2"/>
  <polygon points="25,75 60,123 108,108 121,75" fill="#ebebeb" stroke="#111" stroke-width="1.2"/>
  <line x1="25" y1="75" x2="185" y2="75" stroke="#111" stroke-width="1.1"/>
  <line x1="60" y1="123" x2="185" y2="75" stroke="#111" stroke-width="1.1"/>
  <line x1="25" y1="75" x2="90" y2="160" stroke="#111" stroke-width="1.1"/>
  <line x1="121" y1="75" x2="90" y2="160" stroke="#111" stroke-width="1.1"/>
  <g {font_attr} fill="#111">
    <text x="12" y="78">A</text>
    <text x="50" y="135">B</text>
    <text x="114" y="115">C</text>
    <text x="125" y="70">D</text>
    <text x="192" y="78">P</text>
    <text x="88" y="175">Q</text>
  </g>
</svg>''')

# SVG Q12
svg_q12 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 170" width="200" height="170">
  <circle cx="45" cy="95" r="25" fill="none" stroke="#111" stroke-width="1.3"/>
  <circle cx="145" cy="95" r="45" fill="none" stroke="#111" stroke-width="1.3"/>
  <line x1="45" y1="95" x2="145" y2="95" stroke="#111" stroke-width="1.1"/>
  <line x1="35" y1="132" x2="150" y2="32" stroke="#111" stroke-width="1.2"/>
  <line x1="45" y1="95" x2="60" y2="115" stroke="#111" stroke-width="1"/>
  <line x1="145" y1="95" x2="118" y2="58" stroke="#111" stroke-width="1"/>
  <circle cx="45" cy="95" r="2.5" fill="#111"/>
  <circle cx="145" cy="95" r="2.5" fill="#111"/>
  <g {font_attr} fill="#111">
    <text x="38" y="85">O1</text>
    <text x="152" y="105">O2</text>
    <text x="52" y="128">A</text>
    <text x="112" y="52">B</text>
    <text x="152" y="28">L</text>
  </g>
</svg>''')

# SVG Q13
svg_q13 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 205 185" width="205" height="185">
  <circle cx="50" cy="120" r="28" fill="#fdeee7" stroke="#111" stroke-width="1.3"/>
  <circle cx="135" cy="115" r="45" fill="#edeefa" stroke="#111" stroke-width="1.3"/>
  <line x1="98" y1="30" x2="22" y2="115" stroke="#111" stroke-width="1.2"/>
  <line x1="98" y1="30" x2="175" y2="95" stroke="#111" stroke-width="1.2"/>
  <line x1="30" y1="105" x2="162" y2="85" stroke="#111" stroke-width="1.2"/>
  <line x1="50" y1="120" x2="30" y2="105" stroke="#111" stroke-width="1"/>
  <line x1="50" y1="120" x2="63" y2="100" stroke="#111" stroke-width="1"/>
  <line x1="135" y1="115" x2="96" y2="95" stroke="#111" stroke-width="1"/>
  <line x1="135" y1="115" x2="162" y2="85" stroke="#111" stroke-width="1"/>
  <line x1="30" y1="105" x2="63" y2="100" stroke="#111" stroke-width="1"/>
  <line x1="96" y1="95" x2="162" y2="85" stroke="#111" stroke-width="1"/>
  <circle cx="50" cy="120" r="2.5" fill="#111"/>
  <circle cx="135" cy="115" r="2.5" fill="#111"/>
  <g {font_attr} fill="#111">
    <text x="98" y="22" text-anchor="middle">A</text>
    <text x="18" y="108">B</text>
    <text x="168" y="85">C</text>
    <text x="60" y="92">D</text>
    <text x="92" y="88">E</text>
    <text x="45" y="140">O1</text>
    <text x="135" y="135">O2</text>
  </g>
</svg>''')

# SVG Q14
svg_q14 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 205 185" width="205" height="185">
  <defs>
    <marker id="arr14" viewBox="0 0 8 8" refX="5" refY="4" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 6 4 L 0 6.5 z" fill="#111"/>
    </marker>
  </defs>
  <line x1="15" y1="140" x2="180" y2="140" stroke="#111" stroke-width="1.3" marker-end="url(#arr14)"/>
  <line x1="35" y1="165" x2="35" y2="25" stroke="#111" stroke-width="1.3" marker-end="url(#arr14)"/>
  <circle cx="105" cy="95" r="45" fill="#f6b2ca" stroke="#111" stroke-width="1.3"/>
  <circle cx="105" cy="95" r="2.5" fill="#111"/>
  <line x1="18" y1="157" x2="150" y2="25" stroke="#111" stroke-width="1.2"/>
  <text x="145" y="20" {font_attr} fill="#111">y=x</text>
  <text x="185" y="144" {font_attr} fill="#111">x</text>
  <text x="35" y="18" {font_attr} fill="#111" text-anchor="middle">y</text>
  <g {font_attr} fill="#111">
    <text x="42" y="154">P</text>
    <text x="105" y="155" text-anchor="middle">C</text>
    <text x="52" y="115">A</text>
    <text x="142" y="45">B</text>
    <text x="115" y="98">O</text>
  </g>
</svg>''')

# SVG Q15
svg_q15 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 180" width="200" height="180">
  <circle cx="80" cy="90" r="45" fill="none" stroke="#111" stroke-width="1.3"/>
  <circle cx="150" cy="115" r="25" fill="#ebebeb" stroke="#111" stroke-width="1.3"/>
  <line x1="25" y1="135" x2="185" y2="135" stroke="#111" stroke-width="1.3"/>
  <line x1="80" y1="90" x2="80" y2="135" stroke="#111" stroke-width="1"/>
  <line x1="150" y1="115" x2="150" y2="135" stroke="#111" stroke-width="1"/>
  <path d="M 74,135 L 74,129 L 80,129" fill="none" stroke="#111" stroke-width="0.9"/>
  <path d="M 144,135 L 144,129 L 150,129" fill="none" stroke="#111" stroke-width="0.9"/>
  <line x1="80" y1="90" x2="150" y2="115" stroke="#111" stroke-width="1"/>
  <line x1="105" y1="150" x2="145" y2="75" stroke="#111" stroke-width="1.2"/>
  <circle cx="80" cy="90" r="2.5" fill="#111"/>
  <circle cx="150" cy="115" r="2.5" fill="#111"/>
  <circle cx="125" cy="106" r="2" fill="#111"/>
  <g {font_attr} fill="#111">
    <text x="80" y="80" text-anchor="middle">O1</text>
    <text x="150" y="108" text-anchor="middle">O2</text>
    <text x="120" y="98">C</text>
    <text x="80" y="152" text-anchor="middle">A</text>
    <text x="150" y="152" text-anchor="middle">B</text>
    <text x="118" y="152">D</text>
  </g>
</svg>''')

# SVG Q16
svg_q16 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 195" width="200" height="195">
  <circle cx="100" cy="100" r="65" fill="none" stroke="#111" stroke-width="1.3"/>
  <polygon points="42,120 158,120 135,155 65,155" fill="none" stroke="#111" stroke-width="1.3"/>
  <line x1="42" y1="120" x2="100" y2="35" stroke="#111" stroke-width="1.2"/>
  <line x1="158" y1="120" x2="100" y2="35" stroke="#111" stroke-width="1.2"/>
  <g {font_attr} fill="#111">
    <text x="100" y="26" text-anchor="middle">E</text>
    <text x="24" y="125">A</text>
    <text x="165" y="125">B</text>
    <text x="52" y="170">D</text>
    <text x="138" y="170">C</text>
  </g>
</svg>''')

# SVG Q17
svg_q17 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 215 180" width="215" height="180">
  <circle cx="85" cy="95" r="50" fill="none" stroke="#111" stroke-width="1.3"/>
  <line x1="185" y1="95" x2="70" y2="40" stroke="#111" stroke-width="1.2"/>
  <line x1="185" y1="95" x2="70" y2="150" stroke="#111" stroke-width="1.2"/>
  <line x1="110" y1="56" x2="38" y2="108" stroke="#111" stroke-width="1.1"/>
  <line x1="110" y1="134" x2="48" y2="60" stroke="#111" stroke-width="1.1"/>
  <g {font_attr} fill="#111">
    <text x="114" y="48">A</text>
    <text x="114" y="148">B</text>
    <text x="192" y="98">P</text>
    <text x="22" y="115">C</text>
    <text x="36" y="55">D</text>
    <text x="80" y="110">O</text>
  </g>
</svg>''')

# SVG Q18
svg_q18 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 205 190" width="205" height="190">
  <circle cx="75" cy="80" r="55" fill="none" stroke="#111" stroke-width="1.3"/>
  <circle cx="130" cy="115" r="30" fill="none" stroke="#111" stroke-width="1.3"/>
  <line x1="112" y1="36" x2="165" y2="110" stroke="#111" stroke-width="1.2"/>
  <line x1="120" y1="48" x2="95" y2="135" stroke="#111" stroke-width="1.1"/>
  <line x1="152" y1="95" x2="95" y2="135" stroke="#111" stroke-width="1.1"/>
  <line x1="120" y1="48" x2="122" y2="90" stroke="#111" stroke-width="1.1"/>
  <line x1="152" y1="95" x2="122" y2="90" stroke="#111" stroke-width="1.1"/>
  <g {font_attr} fill="#111">
    <text x="112" y="95">A</text>
    <text x="85" y="148">B</text>
    <text x="125" y="42">C</text>
    <text x="158" y="95">D</text>
  </g>
</svg>''')

# SVG Q19
svg_q19 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 215 185" width="215" height="185">
  <circle cx="55" cy="105" r="25" fill="none" stroke="#111" stroke-width="1.3"/>
  <circle cx="125" cy="105" r="50" fill="none" stroke="#111" stroke-width="1.3"/>
  <line x1="20" y1="125" x2="195" y2="125" stroke="#111" stroke-width="1.2"/>
  <line x1="40" y1="125" x2="95" y2="52" stroke="#111" stroke-width="1.2"/>
  <line x1="95" y1="52" x2="165" y2="125" stroke="#111" stroke-width="1.2"/>
  <circle cx="55" cy="105" r="2.5" fill="#111"/>
  <circle cx="125" cy="105" r="2.5" fill="#111"/>
  <g {font_attr} fill="#111">
    <text x="40" y="98">O1</text>
    <text x="125" y="95">O2</text>
    <text x="30" y="140">C</text>
    <text x="68" y="140">B</text>
    <text x="165" y="140">E</text>
    <text x="62" y="78">A</text>
    <text x="95" y="42" text-anchor="middle">D</text>
  </g>
</svg>''')

# SVG W1
svg_w1 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 160" width="200" height="160">
  <line x1="25" y1="130" x2="175" y2="130" stroke="#111" stroke-width="1.4"/>
  <line x1="25" y1="130" x2="115" y2="40" stroke="#111" stroke-width="1.4"/>
  <circle cx="80" cy="75" r="3" fill="#111"/>
  <g {font_attr} fill="#111">
    <text x="10" y="135">O</text>
    <text x="180" y="135">B</text>
    <text x="122" y="38">A</text>
    <text x="66" y="70">T</text>
  </g>
</svg>''')

# SVG W2
svg_w2 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
  <circle cx="100" cy="100" r="70" fill="none" stroke="#111" stroke-width="1.3"/>
  <circle cx="78" cy="80" r="45" fill="none" stroke="#111" stroke-width="1.2"/>
  <circle cx="78" cy="145" r="20" fill="none" stroke="#111" stroke-width="1.2"/>
  <line x1="100" y1="100" x2="78" y2="80" stroke="#111" stroke-width="1.1"/>
  <line x1="78" y1="80" x2="78" y2="145" stroke="#111" stroke-width="1.1"/>
  <line x1="100" y1="100" x2="78" y2="145" stroke="#111" stroke-width="1.1"/>
  <circle cx="100" cy="100" r="2.5" fill="#111"/>
  <circle cx="78" cy="80" r="2.5" fill="#111"/>
  <circle cx="78" cy="145" r="2.5" fill="#111"/>
  <g {font_attr} fill="#111">
    <text x="105" y="92">O1</text>
    <text x="70" y="72">O2</text>
    <text x="60" y="152">O3</text>
  </g>
</svg>''')

# SVG W3
svg_w3 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 185" width="200" height="185">
  <polygon points="25,150 170,150 170,45" fill="none" stroke="#111" stroke-width="1.4"/>
  <path d="M 162,150 L 162,142 L 170,142" fill="none" stroke="#111" stroke-width="1"/>
  <circle cx="148" cy="128" r="22" fill="none" stroke="#111" stroke-width="1.3"/>
  <circle cx="104" cy="128" r="22" fill="none" stroke="#111" stroke-width="1.3"/>
  <circle cx="126" cy="90" r="22" fill="none" stroke="#111" stroke-width="1.3"/>
  <circle cx="148" cy="128" r="2" fill="#111"/>
  <circle cx="104" cy="128" r="2" fill="#111"/>
  <circle cx="126" cy="90" r="2" fill="#111"/>
  <g {font_attr} fill="#111">
    <text x="165" y="165">B</text>
    <text x="165" y="38">A</text>
    <text x="12" y="152">C</text>
  </g>
</svg>''')

# SVG W4
svg_w4 = clean_svg(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 210 165" width="210" height="165">
  <polygon points="95,30 25,125 135,125" fill="none" stroke="#111" stroke-width="1.4"/>
  <circle cx="135" cy="75" r="50" fill="none" stroke="#111" stroke-width="1.3"/>
  <circle cx="135" cy="75" r="2.5" fill="#111"/>
  <line x1="95" y1="30" x2="135" y2="125" stroke="#111" stroke-width="1.4"/>
  <line x1="135" y1="125" x2="170" y2="78" stroke="#111" stroke-width="1.4"/>
  <g {font_attr} fill="#111">
    <text x="95" y="20" text-anchor="middle">A</text>
    <text x="12" y="132">B</text>
    <text x="135" y="140" text-anchor="middle">C</text>
    <text x="108" y="45">D</text>
    <text x="175" y="78">E</text>
    <text x="135" y="90" text-anchor="middle">O</text>
  </g>
</svg>''')

questions = [
    # 一、填充題
    {
        'type': 'fill',
        'sourceNumber': '1',
        'page': 1,
        'difficulty': 'easy',
        'primaryUnitId': 'nanyi-9-1-2-1',
        'unitIds': ['nanyi-9-1-2-1'],
        'unitAssignmentBasis': '兩圓半徑與連心線段長關係判別兩圓位置關係',
        'blocks': [
            {'type': 'text', 'text': '已知圓 $O_1$、圓 $O_2$ 的半徑分別為 $3$、$7$，試根據所給的條件，完成下列空格。'},
            {
                'type': 'table',
                'header': True,
                'rows': [
                    ['連心線段長', '$11$', '＿＿＿＿', '$6$', '＿＿＿＿'],
                    ['兩圓位置關係', '外離', '外切', '＿＿＿＿', '同心圓']
                ]
            }
        ]
    },
    {
        'type': 'fill',
        'sourceNumber': '2',
        'page': 1,
        'difficulty': 'easy',
        'primaryUnitId': 'nanyi-9-1-2-2',
        'unitIds': ['nanyi-9-1-2-2'],
        'unitAssignmentBasis': '同圓心角下弧度相等與弧長正比於半徑之概念',
        'blocks': [
            {'type': 'text', 'text': '如右圖，$\\wideparen{AB}$、$\\wideparen{CD}$、$\\wideparen{EF}$、$\\wideparen{GH}$ 均為以 $O$ 點為圓心，不同半徑所畫出的四個相異弧，其度數均為 $60^\\circ$，且 $C$、$E$、$G$ 三點均在 $\\overline{OA}$ 上。若 $\\overline{OA} = 3$，$\\overline{OG} = 1$：'},
            {'type': 'svg', 'svg': svg_q2},
            {'type': 'text', 'text': '(1) $\\wideparen{AB}$ 度數＿＿＿＿$\\wideparen{GH}$ 度數。（請填 $>$、$=、$ $<$）'},
            {'type': 'text', 'text': '(2) $\\wideparen{AB}$ 弧長為 $\\wideparen{GH}$ 弧長的＿＿＿＿倍。'}
        ]
    },
    {
        'type': 'fill',
        'sourceNumber': '3',
        'page': 1,
        'difficulty': 'easy',
        'primaryUnitId': 'nanyi-9-1-2-1',
        'unitIds': ['nanyi-9-1-2-1'],
        'unitAssignmentBasis': '圓心到弦之弦心距與弦長反比關係',
        'blocks': [
            {'type': 'text', 'text': '如右圖，在圓 $O$ 中，$\\overline{OP}$、$\\overline{OQ}$、$\\overline{OR}$、$\\overline{OS}$ 分別為弦 $\\overline{AB}$、$\\overline{CD}$、$\\overline{EF}$、$\\overline{GH}$ 的弦心距。已知 $\\overline{AB} = 5$，$\\overline{CD} = 3$，$\\overline{EF} = 3$，$\\overline{GH} = 7$，試判斷 $\\overline{OP}$、$\\overline{OQ}$、$\\overline{OR}$ 與 $\\overline{OS}$ 的大小關係為＿＿＿＿。'},
            {'type': 'svg', 'svg': svg_q3}
        ]
    },
    {
        'type': 'fill',
        'sourceNumber': '4',
        'page': 1,
        'difficulty': 'medium',
        'primaryUnitId': 'nanyi-9-1-2-2',
        'unitIds': ['nanyi-9-1-2-2'],
        'unitAssignmentBasis': '圓內角、圓周角、弦切角與圓外角之大小比較',
        'blocks': [
            {'type': 'text', 'text': '如右圖，$A$、$B$、$C$ 三點在圓上，$D$ 點在圓內，$E$ 點在圓外，直線 $L$ 切圓於 $B$ 點。試判斷 $\\angle 1$、$\\angle 2$、$\\angle 3$、$\\angle 4$ 的大小為＿＿＿＿。'},
            {'type': 'svg', 'svg': svg_q4}
        ]
    },
    {
        'type': 'fill',
        'sourceNumber': '5',
        'page': 1,
        'difficulty': 'easy',
        'primaryUnitId': 'nanyi-9-1-2-2',
        'unitIds': ['nanyi-9-1-2-2'],
        'unitAssignmentBasis': '圓中平行弦截等弧與直徑圓心角度數性質',
        'blocks': [
            {'type': 'text', 'text': '如右圖，$A$、$B$、$C$、$D$ 為圓 $O$ 上相異四點，且 $\\overline{AB} \\parallel \\overline{CD}$，$A$、$O$、$D$ 在同一直線上，若 $\\angle AOB = 125^\\circ$，則 $\\wideparen{AC} =$ ＿＿＿＿度。'},
            {'type': 'svg', 'svg': svg_q5}
        ]
    },
    {
        'type': 'fill',
        'sourceNumber': '6',
        'page': 1,
        'difficulty': 'medium',
        'primaryUnitId': 'nanyi-9-1-2-1',
        'unitIds': ['nanyi-9-1-2-1'],
        'unitAssignmentBasis': '點在圓外與直線與圓相交之半徑不等式範圍',
        'blocks': [
            {'type': 'text', 'text': '以 $O(0 , 0)$ 為圓心，$r$ 為半徑畫圓，當 $A(-5 , -12)$ 在圓外且直線 $y = 10$ 與圓交於兩點。試問半徑 $r$ 的範圍為＿＿＿＿。'},
            {'type': 'svg', 'svg': svg_q6}
        ]
    },
    {
        'type': 'fill',
        'sourceNumber': '7',
        'page': 1,
        'difficulty': 'medium',
        'primaryUnitId': 'nanyi-9-1-2-1',
        'unitIds': ['nanyi-9-1-2-1'],
        'unitAssignmentBasis': '切線長性質與直角三角形斜邊高計算弦長',
        'blocks': [
            {'type': 'text', 'text': '如右圖，$P$ 點在圓 $O$ 外，$\\overline{PA}$ 和 $\\overline{PB}$ 分別與圓 $O$ 相切於 $A$、$B$ 兩點。已知圓 $O$ 的半徑為 $8$，且 $\\overline{PA} = 15$，求 $\\overline{AB} =$ ＿＿＿＿。'},
            {'type': 'svg', 'svg': svg_q7}
        ]
    },
    {
        'type': 'fill',
        'sourceNumber': '8',
        'page': 1,
        'difficulty': 'medium',
        'primaryUnitId': 'nanyi-9-1-2-2',
        'unitIds': ['nanyi-9-1-2-2'],
        'unitAssignmentBasis': '圓周角定理求兩圓周角之和',
        'blocks': [
            {'type': 'text', 'text': '如右圖，在圓 $O$ 中，$\\wideparen{AD} = 90^\\circ$，$\\wideparen{CF} = 70^\\circ$，則 $\\angle B + \\angle E =$ ＿＿＿＿度。'},
            {'type': 'svg', 'svg': svg_q8}
        ]
    },
    {
        'type': 'fill',
        'sourceNumber': '9',
        'page': 1,
        'difficulty': 'easy',
        'primaryUnitId': 'nanyi-9-1-2-1',
        'unitIds': ['nanyi-9-1-2-1'],
        'unitAssignmentBasis': '圓外切四邊形對邊和相等之性質',
        'blocks': [
            {'type': 'text', 'text': '如圖，圓 $O$ 是四邊形 $ABCD$ 的內切圓，若 $\\overline{AB} = 13 - y$，$\\overline{BC} = 2y + 4$，$\\overline{CD} = 5x - 2$，$\\overline{AD} = 2x + 1$，則 $y - x =$ ＿＿＿＿。'},
            {'type': 'svg', 'svg': svg_q9}
        ]
    },
    {
        'type': 'fill',
        'sourceNumber': '10',
        'page': 1,
        'difficulty': 'medium',
        'primaryUnitId': 'nanyi-9-1-2-1',
        'unitIds': ['nanyi-9-1-2-1'],
        'unitAssignmentBasis': '圓內兩相交弦乘積之圓冪性質',
        'blocks': [
            {'type': 'text', 'text': '如右圖，圓 $O$ 的直徑 $\\overline{AB}$ 與弦 $\\overline{CD}$ 交於 $P$ 點。已知圓 $O$ 的直徑為 $12$，$\\overline{OP} = 1$，求 $\\overline{PC} \\times \\overline{PD} =$ ＿＿＿＿。'},
            {'type': 'svg', 'svg': svg_q10}
        ]
    },
    {
        'type': 'fill',
        'sourceNumber': '11',
        'page': 1,
        'difficulty': 'medium',
        'primaryUnitId': 'nanyi-9-1-2-2',
        'unitIds': ['nanyi-9-1-2-2'],
        'unitAssignmentBasis': '圓內接四邊形與兩外角推求內角度數',
        'blocks': [
            {'type': 'text', 'text': '如右圖，圓內接四邊形 $ABCD$ 中，$\\overleftrightarrow{AD}$ 與 $\\overleftrightarrow{BC}$ 交於 $P$ 點，$\\overleftrightarrow{AB}$ 與 $\\overleftrightarrow{CD}$ 交於 $Q$ 點。若 $\\angle P = 15^\\circ$，$\\angle Q = 75^\\circ$，求 $\\angle A =$ ＿＿＿＿度。'},
            {'type': 'svg', 'svg': svg_q11}
        ]
    },
    {
        'type': 'fill',
        'sourceNumber': '12',
        'page': 1,
        'difficulty': 'easy',
        'primaryUnitId': 'nanyi-9-1-2-1',
        'unitIds': ['nanyi-9-1-2-1'],
        'unitAssignmentBasis': '兩圓內公切線線段長公式計算',
        'blocks': [
            {'type': 'text', 'text': '如右圖，直線 $L$ 為圓 $O_1$ 與圓 $O_2$ 的內公切線，$A$、$B$ 為切點。已知圓 $O_1$ 與圓 $O_2$ 的半徑分別為 $3$ 與 $4$，且連心線段 $\\overline{O_1O_2} = 25$，求內公切線段 $\\overline{AB} =$ ＿＿＿＿。'},
            {'type': 'svg', 'svg': svg_q12}
        ]
    },
    {
        'type': 'fill',
        'sourceNumber': '13',
        'page': 2,
        'difficulty': 'medium',
        'primaryUnitId': 'nanyi-9-1-2-2',
        'unitIds': ['nanyi-9-1-2-2'],
        'unitAssignmentBasis': '兩圓切線、弦切角與三角形內角和推算頂角',
        'blocks': [
            {'type': 'text', 'text': '如右圖，$\\overleftrightarrow{AB}$ 切圓 $O_1$ 於 $B$ 點，$\\overleftrightarrow{AC}$ 切圓 $O_2$ 於 $C$ 點，$\\overline{BC}$ 分別交圓 $O_1$、圓 $O_2$ 於 $D$、$E$ 兩點。若 $\\angle BO_1D = 80^\\circ$，$\\angle CO_2E = 110^\\circ$，則 $\\angle A$ 的度數為＿＿＿＿度。'},
            {'type': 'svg', 'svg': svg_q13}
        ]
    },
    {
        'type': 'fill',
        'sourceNumber': '14',
        'page': 2,
        'difficulty': 'hard',
        'primaryUnitId': 'nanyi-9-1-2-1',
        'unitIds': ['nanyi-9-1-2-1'],
        'unitAssignmentBasis': '坐標平面切線性質與圓冪定理求切點坐標',
        'blocks': [
            {'type': 'text', 'text': '如右圖，已知 $P(0 , 0)$、$A(2 , 2)$ 與 $B(9 , 9)$ 均在直線 $y = x$ 上，$O$ 點在第一象限。若圓 $O$ 與直線 $y = x$ 相交於 $A$、$B$ 兩點，且與 $x$ 軸相切於 $C$ 點，求 $C$ 點坐標為＿＿＿＿。'},
            {'type': 'svg', 'svg': svg_q14}
        ]
    },
    {
        'type': 'fill',
        'sourceNumber': '15',
        'page': 2,
        'difficulty': 'hard',
        'primaryUnitId': 'nanyi-9-1-2-1',
        'unitIds': ['nanyi-9-1-2-1'],
        'unitAssignmentBasis': '兩外切圓之公切線長性質與半徑計算',
        'blocks': [
            {'type': 'text', 'text': '如下圖，圓 $O_1$ 與圓 $O_2$ 外切於 $C$ 點，$\\overleftrightarrow{AB}$ 為兩圓的外公切線，$\\overleftrightarrow{CD}$ 為兩圓的內公切線，$A$、$B$、$C$ 三點均為切點，且 $\\overleftrightarrow{AB}$ 與 $\\overleftrightarrow{CD}$ 交於 $D$ 點。已知圓 $O_2$ 的半徑為 $16$，且 $\\overline{CD} = 20$，求圓 $O_1$ 的半徑 $=$ ＿＿＿＿。'},
            {'type': 'svg', 'svg': svg_q15}
        ]
    },
    {
        'type': 'fill',
        'sourceNumber': '16',
        'page': 2,
        'difficulty': 'medium',
        'primaryUnitId': 'nanyi-9-1-2-2',
        'unitIds': ['nanyi-9-1-2-2'],
        'unitAssignmentBasis': '等腰梯形外接圓性質與圓周角度數計算',
        'blocks': [
            {'type': 'text', 'text': '如圖，梯形 $ABCD$ 中，$\\overline{AB} \\parallel \\overline{CD}$，$\\overline{BC} = \\overline{CD} = \\overline{DA}$，$\\angle ADC = 130^\\circ$，$E$ 點在梯形 $ABCD$ 的外接圓上，則 $\\angle AEB =$ ＿＿＿＿度。'},
            {'type': 'svg', 'svg': svg_q16}
        ]
    },
    {
        'type': 'fill',
        'sourceNumber': '17',
        'page': 2,
        'difficulty': 'medium',
        'primaryUnitId': 'nanyi-9-1-2-2',
        'unitIds': ['nanyi-9-1-2-2'],
        'unitAssignmentBasis': '切線外角定理與比例弧長求圓心角度數',
        'blocks': [
            {'type': 'text', 'text': '如下圖，$\\overleftrightarrow{PA}$、$\\overleftrightarrow{PB}$ 分別切圓於 $A$、$B$ 兩點，$\\wideparen{AD} : \\wideparen{CD} : \\wideparen{BC} = 8 : 5 : 10$。若 $\\angle P = 50^\\circ$，則 $\\angle AOD =$ ＿＿＿＿度。'},
            {'type': 'svg', 'svg': svg_q17}
        ]
    },
    {
        'type': 'fill',
        'sourceNumber': '18',
        'page': 2,
        'difficulty': 'medium',
        'primaryUnitId': 'nanyi-9-1-2-2',
        'unitIds': ['nanyi-9-1-2-2'],
        'unitAssignmentBasis': '弦切角與圓周角性質推求兩相交圓角度',
        'blocks': [
            {'type': 'text', 'text': '如右圖，兩圓相交於 $A$、$B$ 兩點，直線 $CD$ 為兩圓的公切線，$C$、$D$ 為切點，$\\angle ACD = 17^\\circ$，$\\angle ADC = 29^\\circ$，則 $\\angle CBD =$ ＿＿＿＿度。'},
            {'type': 'svg', 'svg': svg_q18}
        ]
    },
    {
        'type': 'fill',
        'sourceNumber': '19',
        'page': 2,
        'difficulty': 'hard',
        'primaryUnitId': 'nanyi-9-1-2-1',
        'unitIds': ['nanyi-9-1-2-1'],
        'unitAssignmentBasis': '平行連心線弦長與直徑直角性質綜合求半徑',
        'blocks': [
            {'type': 'text', 'text': '如右圖，平面上兩圓 $O_1$、$O_2$ 交於 $A$、$B$ 兩點，若過 $B$ 點作平行 $\\overline{O_1O_2}$ 的直線，並分別與圓 $O_1$、$O_2$ 相交於 $C$、$E$ 兩點，$C$、$O_1$、$A$、$D$ 在同一直線上，且 $\\overline{AC} = 5$，$\\overline{DE} = 10$，$\\overline{CE} = 2\\sqrt{41}$，則 $O_2$ 半徑長為＿＿＿＿。'},
            {'type': 'svg', 'svg': svg_q19}
        ]
    },

    # 二、作圖、計算題
    {
        'type': 'written',
        'sourceNumber': '1',
        'page': 2,
        'difficulty': 'medium',
        'primaryUnitId': 'nanyi-9-1-3-1',
        'unitIds': ['nanyi-9-1-3-1', 'nanyi-9-1-2-1'],
        'unitAssignmentBasis': '過角邊上一點作與兩邊相切之圓的尺規作圖',
        'blocks': [
            {'type': 'text', 'text': '如圖，$T$ 是 $\\angle AOB$ 中 $\\overline{OA}$ 上一點，請作一圓分別與 $\\overline{OA}$、$\\overline{OB}$ 相切，且與 $\\overline{OA}$ 切於 $T$ 點。'},
            {'type': 'svg', 'svg': svg_w1}
        ]
    },
    {
        'type': 'written',
        'sourceNumber': '2',
        'page': 2,
        'difficulty': 'medium',
        'primaryUnitId': 'nanyi-9-1-2-1',
        'unitIds': ['nanyi-9-1-2-1'],
        'unitAssignmentBasis': '三圓兩兩相切（內切與外切）連心線列式求半徑與面積和',
        'blocks': [
            {'type': 'text', 'text': '如圖，已知圓 $O_2$、$O_3$ 外切；圓 $O_2$、$O_3$ 均內切於圓 $O_1$。若 $\\overline{O_1O_2} = 3$，$\\overline{O_2O_3} = 8$，$\\overline{O_1O_3} = 7$，則三圓面積和為何？'},
            {'type': 'svg', 'svg': svg_w2}
        ]
    },
    {
        'type': 'written',
        'sourceNumber': '3',
        'page': 2,
        'difficulty': 'hard',
        'primaryUnitId': 'nanyi-9-1-2-1',
        'unitIds': ['nanyi-9-1-2-1'],
        'unitAssignmentBasis': '直角三角形內金字塔排列之三等圓半徑計算',
        'blocks': [
            {'type': 'text', 'text': '如右圖，$\\triangle ABC$ 為一直角三角形，三角形內部有三個相同的圓呈金字塔排列，並與三邊皆有相切，若 $\\overline{AB} = 2$，$\\overline{BC} = 2\\sqrt{3}$，則圓半徑為何？'},
            {'type': 'svg', 'svg': svg_w3}
        ]
    },
    {
        'type': 'written',
        'sourceNumber': '4',
        'page': 2,
        'difficulty': 'hard',
        'primaryUnitId': 'nanyi-9-1-1-4',
        'unitIds': ['nanyi-9-1-1-4', 'nanyi-9-1-2-2'],
        'unitAssignmentBasis': '切線弦切角、平行弦與相似三角形綜合求線段長',
        'blocks': [
            {'type': 'text', 'text': '如右圖，$\\triangle ABC$ 中，$\\overline{AB} = 40$，$\\overline{AC} = 32$，有一圓 $O$ 與 $\\overline{BC}$ 相切於 $C$，與 $\\overline{AC}$ 交於 $D$，$\\overline{CE}$ 為圓 $O$ 之一弦，且 $\\overline{CE} \\parallel \\overline{AB}$，若 $\\overline{CE} = 20$，則 $\\overline{AD} = ?$'},
            {'type': 'svg', 'svg': svg_w4}
        ]
    }
]

data = {
    'paperId': paper_id,
    'sourceSha256': pdf_sha256,
    'printedHeader': '宜蘭縣中華國民中學一○九學年度第一學期第二次段考數學科試卷 九年級',
    'printedSlot': {
        'year': 109,
        'semester': 1,
        'grade': 9,
        'exam': 2
    },
    'printedCounts': '填充題19題、作圖計算題4題，共23題。',
    'visualReviewComplete': True,
    'reviewNote': '全卷23題完整轉錄，含22幅純向量幾何SVG圖形忠實重繪，無任何點陣圖片，題號式子完全對齊。',
    'expectedTypes': {
        'choice': 0,
        'fill': 19,
        'written': 4
    },
    'questions': questions
}

out_path = ROOT / f'research/yilan/transcribed/{paper_id}.json'
out_path.parent.mkdir(parents=True, exist_ok=True)
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'Successfully wrote {out_path}')
print(f'Total questions: {len(questions)}')
types = {k: sum(q['type'] == k for q in questions) for k in ('choice', 'fill', 'written')}
diff = {k: sum(q['difficulty'] == k for q in questions) for k in ('easy', 'medium', 'hard')}
print('Types:', types)
print('Difficulty:', diff)
