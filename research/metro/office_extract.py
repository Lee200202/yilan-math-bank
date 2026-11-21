"""Extract text, formulas (as LaTeX) and embedded images from .docx / .odt without Word or LibreOffice.

Usage: python -X utf8 research/metro/office_extract.py <file.docx|file.odt> <out_dir>
Writes <out_dir>/text.md (reading order; formulas as $...$; [IMG img/NN.png] markers; [TEXTBOX] ... [/TEXTBOX]),
and <out_dir>/img/NN.* (EMF/WMF are also converted to PNG when PIL can on this machine).
"""
import io
import pathlib
import re
import sys
import zipfile
from lxml import etree

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
M = 'http://schemas.openxmlformats.org/officeDocument/2006/math'
R = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
A = 'http://schemas.openxmlformats.org/drawingml/2006/main'
V = 'urn:schemas-microsoft-com:vml'
MC = 'http://schemas.openxmlformats.org/markup-compatibility/2006'


def ln(e):
    return etree.QName(e).localname if isinstance(e.tag, str) else ''


def ns(e):
    return etree.QName(e).namespace if isinstance(e.tag, str) else ''


# ---------------- OMML -> LaTeX ----------------
def kids(e, name):
    return [c for c in e if ln(c) == name]


def kid(e, name):
    for c in e:
        if ln(c) == name:
            return c
    return None


def omml(e):
    t = ln(e)
    if t in ('oMath', 'oMathPara', 'e', 'num', 'den', 'sub', 'sup', 'deg', 'lim', 'fName'):
        return ''.join(omml(c) for c in e if ln(c) not in ('rPr', 'ctrlPr', 'sSupPr', 'sSubPr', 'fPr', 'radPr', 'dPr', 'naryPr', 'accPr', 'barPr', 'eqArrPr', 'mPr', 'funcPr', 'limLowPr', 'limUppPr', 'groupChrPr'))
    if t == 'r':
        txt = ''.join(c.text or '' for c in e if ln(c) == 't')
        for pr in (c for c in e if ln(c) == 'rPr' and ns(c) == W):  # Word run formatting inside an equation: raised/lowered digits
            va = kid(pr, 'vertAlign')
            po = kid(pr, 'position')
            mark = None
            if va is not None:
                mark = {'superscript': '^', 'subscript': '_'}.get(va.get('{%s}val' % W))
            elif po is not None:
                try:
                    pv = int(po.get('{%s}val' % W, '0'))
                except ValueError:
                    pv = 0
                mark = '^' if pv >= 4 else ('_' if pv <= -4 else None)
            if mark and txt.strip():
                return '%s{%s}' % (mark, txt)
        return txt
    if t == 'f':
        typ = kid(e, 'fPr')
        k = kid(typ, 'type') if typ is not None else None
        if k is not None and k.get('{%s}val' % M) == 'lin':
            return '{%s}/{%s}' % (omml(kid(e, 'num')), omml(kid(e, 'den')))
        return '\\dfrac{%s}{%s}' % (omml(kid(e, 'num')), omml(kid(e, 'den')))
    if t == 'rad':
        deg = kid(e, 'deg')
        d = omml(deg) if deg is not None else ''
        return '\\sqrt%s{%s}' % ('[%s]' % d if d else '', omml(kid(e, 'e')))
    if t == 'sSup':
        return '{%s}^{%s}' % (omml(kid(e, 'e')), omml(kid(e, 'sup')))
    if t == 'sSub':
        return '{%s}_{%s}' % (omml(kid(e, 'e')), omml(kid(e, 'sub')))
    if t == 'sSubSup':
        return '{%s}_{%s}^{%s}' % (omml(kid(e, 'e')), omml(kid(e, 'sub')), omml(kid(e, 'sup')))
    if t == 'sPre':
        return '{}_{%s}^{%s}{%s}' % (omml(kid(e, 'sub')), omml(kid(e, 'sup')), omml(kid(e, 'e')))
    if t == 'd':
        pr = kid(e, 'dPr')
        beg, end = '(', ')'
        if pr is not None:
            b = kid(pr, 'begChr')
            en = kid(pr, 'endChr')
            if b is not None:
                beg = b.get('{%s}val' % M, '')
            if en is not None:
                end = en.get('{%s}val' % M, '')
        inner = ','.join(omml(c) for c in kids(e, 'e'))
        l = {'{': '\\left\\{', '}': '\\right\\}', '': '\\left.'}.get(beg, '\\left' + beg)
        r = {'}': '\\right\\}', '{': '\\left\\{', '': '\\right.'}.get(end, '\\right' + end)
        return '%s %s %s' % (l, inner, r)
    if t == 'nary':
        pr = kid(e, 'naryPr')
        ch = '∫'
        if pr is not None and kid(pr, 'chr') is not None:
            ch = kid(pr, 'chr').get('{%s}val' % M, '∫')
        name = {'∑': '\\sum', '∏': '\\prod', '∫': '\\int'}.get(ch, ch)
        s, p = kid(e, 'sub'), kid(e, 'sup')
        return '%s%s%s %s' % (name, '_{%s}' % omml(s) if s is not None and omml(s) else '', '^{%s}' % omml(p) if p is not None and omml(p) else '', omml(kid(e, 'e')))
    if t == 'acc':
        pr = kid(e, 'accPr')
        ch = '̂'
        if pr is not None and kid(pr, 'chr') is not None:
            ch = kid(pr, 'chr').get('{%s}val' % M, ch)
        return {'̅': '\\overline{%s}', '¯': '\\overline{%s}', '→': '\\vec{%s}', '⃗': '\\vec{%s}', '̂': '\\hat{%s}', '^': '\\hat{%s}', '~': '\\tilde{%s}', '̇': '\\dot{%s}'}.get(ch, '\\hat{%s}') % omml(kid(e, 'e'))
    if t == 'bar':
        pr = kid(e, 'barPr')
        pos = kid(pr, 'pos') if pr is not None else None
        if pos is not None and pos.get('{%s}val' % M) == 'bot':
            return '\\underline{%s}' % omml(kid(e, 'e'))
        return '\\overline{%s}' % omml(kid(e, 'e'))
    if t == 'func':
        return '\\mathrm{%s}%s' % (omml(kid(e, 'fName')), omml(kid(e, 'e')))
    if t == 'limLow':
        return '{%s}_{%s}' % (omml(kid(e, 'e')), omml(kid(e, 'lim')))
    if t == 'limUpp':
        return '{%s}^{%s}' % (omml(kid(e, 'e')), omml(kid(e, 'lim')))
    if t == 'groupChr':
        return omml(kid(e, 'e'))
    if t == 'eqArr':
        return '\\begin{cases} %s \\end{cases}' % ' \\\\ '.join(omml(c) for c in kids(e, 'e'))
    if t == 'm':
        rows = []
        for mr in kids(e, 'mr'):
            rows.append(' & '.join(omml(c) for c in kids(mr, 'e')))
        return '\\begin{matrix} %s \\end{matrix}' % ' \\\\ '.join(rows)
    if t == 'box' or t == 'phant' or t == 'borderBox':
        return omml(kid(e, 'e'))
    return ''.join(omml(c) for c in e)


# ---------------- MathML (ODT) -> LaTeX ----------------
def mml(e):
    t = ln(e)
    c = [x for x in e if isinstance(x.tag, str)]
    if t in ('math', 'mrow', 'mstyle', 'semantics', 'mpadded', 'menclose'):
        return ''.join(mml(x) for x in c if ln(x) != 'annotation')
    if t in ('mi', 'mn', 'mtext', 'ms'):
        return (e.text or '').strip() if t != 'mtext' else (e.text or '')
    if t == 'mo':
        s = (e.text or '').strip()
        return {'×': '\\times ', '÷': '\\div ', '±': '\\pm ', '≤': '\\le ', '≥': '\\ge ', '≠': '\\ne ', '∠': '\\angle ', '°': '^\\circ ', '△': '\\triangle ', '∥': '\\parallel ', '⊥': '\\perp ', '≅': '\\cong ', '∼': '\\sim ', '→': '\\to ', '≈': '\\approx ', 'π': '\\pi ', '−': '-', '·': '\\cdot ', '∴': '\\therefore ', '∵': '\\because '}.get(s, s)
    if t == 'mfrac':
        return '\\dfrac{%s}{%s}' % (mml(c[0]), mml(c[1]))
    if t == 'msqrt':
        return '\\sqrt{%s}' % ''.join(mml(x) for x in c)
    if t == 'mroot':
        return '\\sqrt[%s]{%s}' % (mml(c[1]), mml(c[0]))
    if t == 'msup':
        return '{%s}^{%s}' % (mml(c[0]), mml(c[1]))
    if t == 'msub':
        return '{%s}_{%s}' % (mml(c[0]), mml(c[1]))
    if t == 'msubsup':
        return '{%s}_{%s}^{%s}' % (mml(c[0]), mml(c[1]), mml(c[2]))
    if t == 'mover':
        o = mml(c[1]).strip()
        return {'¯': '\\overline{%s}', '→': '\\overrightarrow{%s}', '^': '\\hat{%s}', '⌢': '\\overset{\\frown}{%s}'}.get(o, '\\overset{' + o + '}{%s}') % mml(c[0])
    if t == 'munder':
        return '\\underset{%s}{%s}' % (mml(c[1]), mml(c[0]))
    if t == 'munderover':
        return '{%s}_{%s}^{%s}' % (mml(c[0]), mml(c[1]), mml(c[2]))
    if t == 'mfenced':
        o, cl = e.get('open', '('), e.get('close', ')')
        return '\\left%s %s \\right%s' % (o, ','.join(mml(x) for x in c), cl)
    if t == 'mtable':
        return '\\begin{matrix} %s \\end{matrix}' % ' \\\\ '.join(' & '.join(mml(td) for td in tr) for tr in c)
    if t == 'mtr' or t == 'mtd':
        return ''.join(mml(x) for x in c)
    if t == 'annotation':
        return ''
    return ''.join(mml(x) for x in c)


# ---------------- common output helpers ----------------
class Out:
    def __init__(self, outdir):
        self.dir = pathlib.Path(outdir)
        (self.dir / 'img').mkdir(parents=True, exist_ok=True)
        self.n = 0
        self.lines = []
        self.seen = {}

    def image(self, name, data):
        if name in self.seen:
            return self.seen[name]
        self.n += 1
        ext = pathlib.Path(name).suffix.lower() or '.bin'
        if data[:4] == bytes.fromhex('d7cdc69a'):
            ext = '.wmf'
        elif data[:4] == bytes.fromhex('01000000') and data[40:44] == b' EMF':
            ext = '.emf'
        elif data[:4] == bytes.fromhex('89504e47'):
            ext = '.png'
        elif data[:3] == bytes.fromhex('ffd8ff'):
            ext = '.jpg'
        fn = 'img/%02d%s' % (self.n, ext)
        (self.dir / fn).write_bytes(data)
        if ext in ('.emf', '.wmf'):
            try:
                from PIL import Image
                im = Image.open(io.BytesIO(data))
                try:
                    im.load(dpi=288)
                except TypeError:
                    im.load()
                png = 'img/%02d.png' % self.n
                im.convert('RGB').save(self.dir / png)
                fn = png
            except Exception as ex:
                fn += ' (vector, not auto-converted: %s)' % str(ex)[:40]
        self.seen[name] = fn
        return fn


# ---------------- Symbol-font private-use characters -> Unicode ----------------
SYMBOL = {0xF020: ' ', 0xF0B8: '÷', 0xF0B4: '×', 0xF0B1: '±', 0xF0DE: '⇒', 0xF0DB: '⇔', 0xF0DC: '⇐', 0xF0AE: '→', 0xF0AC: '←',
          0xF0A3: '≤', 0xF0B3: '≥', 0xF0B9: '≠', 0xF0D6: '√', 0xF0B0: '°', 0xF0A5: '∞', 0xF0B7: '•', 0xF0D0: '∠', 0xF0CC: '⊂',
          0xF0BB: '≈', 0xF0BA: '≡', 0xF0CE: '∈', 0xF0D7: '·', 0xF0B2: '″', 0xF0A2: '′', 0xF0D1: '∇', 0xF0C7: '∩', 0xF0C8: '∪',
          0xF0AD: '↑', 0xF0AF: '↓', 0xF0B5: '∝', 0xF0D9: '∧', 0xF0DA: '∨', 0xF0D3: '©', 0xF0A8: '♦', 0xF070: 'π', 0xF071: 'θ',
          0xF061: 'α', 0xF062: 'β', 0xF067: 'γ', 0xF064: 'δ', 0xF044: 'Δ', 0xF053: 'Σ', 0xF057: 'Ω', 0xF06D: 'μ'}


def fix_symbols(text):
    def one(ch):
        o = ord(ch)
        if 0xE000 <= o <= 0xF8FF:
            return SYMBOL.get(o, '[U+%04X]' % o)
        return ch
    return ''.join(one(c) for c in text)


# ---------------- Word EQ fields (legacy equations) -> LaTeX ----------------
EQ_CMD = re.compile(r'\\([A-Za-z])((?:\\[A-Za-z]+[0-9]*)*)\(')


def _match_paren(s, i):
    depth = 0
    for j in range(i, len(s)):
        if s[j] == '(':
            depth += 1
        elif s[j] == ')':
            depth -= 1
            if depth == 0:
                return j
    return len(s) - 1


def _split_top(s):
    parts, depth, cur = [], 0, ''
    for ch in s:
        if ch == '(':
            depth += 1
        elif ch == ')':
            depth -= 1
        if ch == ',' and depth == 0:
            parts.append(cur)
            cur = ''
        else:
            cur += ch
    parts.append(cur)
    return parts


def eq2tex(s):
    s = s.strip()
    if s[:2].upper() == 'EQ':
        s = s[2:].strip()
    out, i = [], 0
    while i < len(s):
        m = EQ_CMD.match(s, i)
        if not m:
            out.append(s[i])
            i += 1
            continue
        cmd, opts = m.group(1).lower(), m.group(2).lower()
        j = _match_paren(s, m.end() - 1)
        args = [eq2tex(a) for a in _split_top(s[m.end():j])]
        if cmd == 'f' and len(args) >= 2:
            out.append('\\dfrac{%s}{%s}' % (args[0], args[1]))
        elif cmd == 'r':
            if len(args) >= 2 and args[0].strip():
                out.append('\\sqrt[%s]{%s}' % (args[0], args[1]))
            else:
                out.append('\\sqrt{%s}' % args[-1])
        elif cmd == 's' and '\\up' in opts:
            out.append('^{%s}' % ''.join(args))
        elif cmd == 's' and '\\do' in opts:
            out.append('_{%s}' % ''.join(args))
        elif cmd == 'x' and '\\to' in opts:
            out.append('\\overline{%s}' % ''.join(args))
        elif cmd == 'x' and '\\bo' in opts:
            out.append('\\underline{%s}' % ''.join(args))
        elif cmd == 'x':
            out.append(''.join(args))
        elif cmd == 'o' and len(args) == 2 and args[0].strip() in ('¯', '‾', '―', '—', '－', '_', '￣') and args[1].strip():
            out.append('\\overline{%s}' % args[1].strip())  # segment AB written as an overstruck bar over the letters
        elif cmd == 'o' and len(args) == 2 and args[0].strip() in ('＝', '=') and args[1].strip() in ('～', '~', '∼', '〜'):
            out.append('\\cong ')  # congruent: an equals sign overstruck with a tilde
        elif cmd == 'o' and len(args) == 2 and args[0].strip() in ('＜', '<') and args[1].strip() in ('－', '-', '—', '_', '＿'):
            out.append('\\le ')
        elif cmd == 'o' and len(args) == 2 and args[0].strip() in ('＞', '>') and args[1].strip() in ('－', '-', '—', '_', '＿'):
            out.append('\\ge ')
        elif cmd == 'o' and len(args) == 2 and args[0].strip() in ('＝', '=') and args[1].strip() in ('/', '／', '╱'):
            out.append('\\ne ')
        elif cmd == 'o' and not opts and len(args) == 2 and args[1].strip() and not args[0].strip(' 　_{}'):
            out.append('**%s**' % args[1])
        elif cmd == 'o' and len(args) == 2 and args[0].strip() in ('○', '◯', '〇') and re.sub(r'\D', '', args[1]).isdigit() and 1 <= int(re.sub(r'\D', '', args[1])) <= 50:
            n_ = int(re.sub(r'\D', '', args[1]))
            out.append(chr(0x2460 + n_ - 1) if n_ <= 20 else (chr(0x3251 + n_ - 21) if n_ <= 35 else chr(0x32B1 + n_ - 36)))
        elif cmd == 'o' and len(args) >= 2 and not args[0].strip():
            out.append(''.join(args[1:]))  # overstrike with nothing: just the second part
        else:
            out.append('[EQ-RAW \\%s%s(%s)]' % (cmd, opts, ','.join(args)))
        i = j + 1
    return ''.join(out)


# ---------------- native Word charts ----------------
def chart_text(data):
    root = etree.fromstring(data)
    kinds = [ln(e) for e in root.iter() if isinstance(e.tag, str) and ln(e).endswith('Chart') and ln(e) != 'chart']
    out = []
    for ser in (e for e in root.iter() if isinstance(e.tag, str) and ln(e) == 'ser'):
        def pts(tag):
            node = next((c for c in ser if ln(c) == tag), None)
            if node is None:
                return []
            return [v.text or '' for p in node.iter() if isinstance(p.tag, str) and ln(p) == 'pt' for v in p if ln(v) == 'v']
        name = ''.join(pts('tx'))
        out.append('%s: %s' % (name or 'series', ', '.join('%s=%s' % (c, v) for c, v in zip(pts('cat'), pts('val')))))
    title = ' '.join(t.text or '' for e in root.iter() if isinstance(e.tag, str) and ln(e) == 'title' for t in e.iter() if isinstance(t.tag, str) and ln(t) == 't')
    return '[CHART %s%s | %s]' % ('/'.join(dict.fromkeys(kinds)) or 'chart', (' "%s"' % title.strip()) if title.strip() else '', ' ; '.join(out))


# ---------------- DOCX ----------------
def docx(path, out):
    z = zipfile.ZipFile(path)
    rels = {}
    if 'word/_rels/document.xml.rels' in z.namelist():
        rr = etree.fromstring(z.read('word/_rels/document.xml.rels'))
        for r in rr:
            rels[r.get('Id')] = r.get('Target')

    def img_for(rid):
        t = rels.get(rid)
        if not t:
            return '[IMG ?]'
        p = ('word/' + t) if not t.startswith('/') else t[1:]
        p = re.sub(r'[^/]+/\.\./', '', p)
        if p in z.namelist():
            return '[IMG %s]' % out.image(p, z.read(p))
        return '[IMG missing %s]' % t

    # Character styles can carry the superscript/subscript (run says only <w:rStyle w:val="af3"/>): resolve them via styles.xml
    style_sup, style_based = {}, {}
    if 'word/styles.xml' in z.namelist():
        for st in kids(etree.fromstring(z.read('word/styles.xml')), 'style'):
            sid = st.get('{%s}styleId' % W)
            bo = kid(st, 'basedOn')
            if bo is not None:
                style_based[sid] = bo.get('{%s}val' % W)
            rp = kid(st, 'rPr')
            if rp is None:
                continue
            va, po = kid(rp, 'vertAlign'), kid(rp, 'position')
            if va is not None and va.get('{%s}val' % W) in ('superscript', 'subscript'):
                style_sup[sid] = '^' if va.get('{%s}val' % W) == 'superscript' else '_'
            elif po is not None:
                try:
                    pv = int(po.get('{%s}val' % W, '0'))
                except ValueError:
                    pv = 0
                if pv >= 4:
                    style_sup[sid] = '^'
                elif pv <= -4:
                    style_sup[sid] = '_'

    def sup_of_style(sid):
        seen = 0
        while sid and seen < 6:
            if sid in style_sup:
                return style_sup[sid]
            sid = style_based.get(sid)
            seen += 1
        return None

    fs = {'mode': None, 'instr': '', 'eq': False, 'nested': False}
    fstack = []

    def field_out():
        ins = fs['instr'].strip()
        fs['eq'] = ins[:2].upper() == 'EQ'
        if not fs['eq']:
            return ''
        tex = eq2tex(ins)
        return tex if not re.search(r'[\\^_{}]', tex) else '$' + tex + '$'

    def run(r):
        s = []
        und = False
        sup = None
        pr = kid(r, 'rPr')
        if pr is not None:
            u = kid(pr, 'u')
            und = u is not None and u.get('{%s}val' % W) not in ('none', '0')
            va = kid(pr, 'vertAlign')
            if va is not None:
                sup = {'superscript': '^', 'subscript': '_'}.get(va.get('{%s}val' % W))
            if sup is None:
                rs = kid(pr, 'rStyle')
                if rs is not None:
                    sup = sup_of_style(rs.get('{%s}val' % W))
            po = kid(pr, 'position')  # raised/lowered text (half-points) is how many old documents write x^2
            if sup is None and po is not None:
                try:
                    pv = int(po.get('{%s}val' % W, '0'))
                except ValueError:
                    pv = 0
                sz = kid(pr, 'sz')
                size = int(sz.get('{%s}val' % W, '24')) if sz is not None else 24
                if pv >= 4 and size <= 22:
                    sup = '^'
                elif pv <= -4 and size <= 22:
                    sup = '_'
        for c in r:
            t = ln(c)
            if t == 'fldChar':
                ty = c.get('{%s}fldCharType' % W)
                if ty == 'begin':
                    if fs['mode'] is not None:  # a field inside another field (e.g. EQ \f(7±{EQ \r(,15)},2)): keep the outer one
                        fstack.append(dict(fs))
                        fs['nested'] = True
                    else:
                        fs['nested'] = False
                    fs['mode'], fs['instr'], fs['eq'] = 'code', '', False
                elif ty == 'separate':
                    if fs['mode'] == 'code':
                        if not fs.get('nested'):
                            s.append(field_out())
                        else:
                            fs['eq'] = fs['instr'].strip()[:2].upper() == 'EQ'
                    fs['mode'] = 'result'
                elif ty == 'end':
                    if fs.get('nested') and fstack:
                        inner = fs['instr'].strip()
                        parent = fstack.pop()
                        fs.clear()
                        fs.update(parent)
                        if fs['mode'] == 'code' and inner[:2].upper() == 'EQ':
                            fs['instr'] += inner[2:].strip()  # splice the inner equation code into the outer one
                    else:
                        if fs['mode'] == 'code':
                            s.append(field_out())
                        fs['mode'] = None
                        fs['eq'] = False
                        fs['nested'] = False
            elif t == 'instrText':
                if fs['mode'] == 'code':
                    piece = c.text or ''
                    if sup and piece.strip() and piece.strip()[0].isalnum():  # raised/lowered text inside an EQ field code
                        piece = ('\\s\\up6(' if sup == '^' else '\\s\\do3(') + piece + ')'
                    fs['instr'] += piece
            elif fs['mode'] == 'code':
                continue  # hidden field-code content (e.g. QUOTE fields): only the displayed result counts
            elif t == 't':
                if not (fs['mode'] == 'result' and fs['eq']):
                    s.append(c.text or '')
            elif t == 'tab':
                s.append('\t')
            elif t in ('br', 'cr'):
                s.append('\n' if c.get('{%s}type' % W) != 'page' else '\n[PAGE]\n')
            elif t == 'sym':
                s.append(chr(int(c.get('{%s}char' % W, '0'), 16)) if c.get('{%s}char' % W) else '')
            elif t == 'drawing' or t == 'pict' or t == 'object':
                s.append(drawing(c))
            elif t == 'AlternateContent':
                s.append(alt(c))
        txt = ''.join(s)
        if und and txt.strip() == '':
            return '____' if txt else ''
        if sup and txt.strip() and '$' not in txt:
            return '%s{%s}' % (sup, txt)
        return txt

    def alt(c):
        ch = [x for x in c if ln(x) == 'Choice'] or [x for x in c if ln(x) == 'Fallback']
        return ''.join(inline(x) for x in ch[0]) if ch else ''

    def drawing(c):
        res = []
        for b in c.iter('{%s}blip' % A):
            res.append(img_for(b.get('{%s}embed' % R)))
        for b in c.iter('{%s}imagedata' % V):
            res.append(img_for(b.get('{%s}id' % R)))
        tb = [x for x in c.iter('{%s}txbxContent' % W)]
        for x in tb[:1]:
            res.append('[TEXTBOX] ' + ' / '.join(block(p) for p in x if ln(p) in ('p', 'tbl')) + ' [/TEXTBOX]')
        for x in c.iter():  # native Word chart (word/charts/chartN.xml): pie / bar / line data
            if isinstance(x.tag, str) and ln(x) == 'chart' and ns(x).endswith('/chart'):
                rid = x.get('{%s}id' % R)
                tgt = rels.get(rid)
                if tgt:
                    cp = re.sub(r'[^/]+/\.\./', '', ('word/' + tgt) if not tgt.startswith('/') else tgt[1:])
                    if cp in z.namelist():
                        res.append(chart_text(z.read(cp)))
        shapes = 0
        for x in c.iter():
            if not isinstance(x.tag, str):
                continue
            n = ln(x)
            if (ns(x) == V and n in ('rect', 'oval', 'line', 'polyline', 'roundrect', 'curve', 'arc', 'shape')) or n in ('wsp', 'cxnSp'):
                shapes += 1
        if shapes and not any(r_.startswith('[IMG') for r_ in res):
            res.append('[DRAWING-SHAPE vector figure (%d shapes); redraw from context]' % shapes)
        return ''.join(res)

    def inline(e):
        t = ln(e)
        if t == 'r':
            return run(e)
        if fs['mode'] == 'code' and t in ('oMath', 'oMathPara', 'AlternateContent', 'drawing', 'pict', 'object'):
            return ''
        if t in ('hyperlink', 'ins', 'smartTag', 'sdt', 'sdtContent', 'fldSimple'):
            return ''.join(inline(x) for x in e)
        if t == 'oMath':
            return '$' + omml(e) + '$'
        if t == 'oMathPara':
            return '$$' + omml(e) + '$$'
        if t == 'AlternateContent':
            return alt(e)
        if t in ('drawing', 'pict', 'object'):
            return drawing(e)
        return ''

    # --- automatic numbering labels (e.g. "(A)", "1.", "甲、") ---
    numdefs, nummap = {}, {}
    if 'word/numbering.xml' in z.namelist():
        nroot = etree.fromstring(z.read('word/numbering.xml'))
        for an in kids(nroot, 'abstractNum'):
            lv = {}
            for l in kids(an, 'lvl'):
                nf, lt, st = kid(l, 'numFmt'), kid(l, 'lvlText'), kid(l, 'start')
                lv[int(l.get('{%s}ilvl' % W, '0'))] = (nf.get('{%s}val' % W) if nf is not None else 'decimal',
                                                      lt.get('{%s}val' % W) if lt is not None else '%1.',
                                                      int(st.get('{%s}val' % W)) if st is not None else 1)
            numdefs[an.get('{%s}abstractNumId' % W)] = lv
        for nm in kids(nroot, 'num'):
            a = kid(nm, 'abstractNumId')
            if a is not None:
                nummap[nm.get('{%s}numId' % W)] = a.get('{%s}val' % W)
    counters = {}

    def fmt_num(n, f):
        if f == 'decimal':
            return str(n)
        if f == 'upperLetter':
            return chr(64 + (n - 1) % 26 + 1)
        if f == 'lowerLetter':
            return chr(96 + (n - 1) % 26 + 1)
        if f in ('upperRoman', 'lowerRoman'):
            vals = [(10, 'x'), (9, 'ix'), (5, 'v'), (4, 'iv'), (1, 'i')]
            r_, m_ = '', n
            for v_, s_ in vals:
                while m_ >= v_:
                    r_ += s_
                    m_ -= v_
            return r_.upper() if f == 'upperRoman' else r_
        if f in ('ideographTraditional', 'ideographLegalTraditional'):
            return '甲乙丙丁戊己庚辛壬癸'[(n - 1) % 10]
        if f in ('chineseCounting', 'taiwaneseCounting', 'chineseCountingThousand', 'ideographDigital'):
            return '〇一二三四五六七八九十'[n] if n <= 10 else str(n)
        if f in ('decimalEnclosedCircle', 'decimalEnclosedCircleChinese'):
            return chr(0x2460 + n - 1) if 1 <= n <= 20 else str(n)
        if f == 'decimalFullWidth':
            return ''.join(chr(0xFF10 + int(d)) for d in str(n))
        if f == 'bullet':
            return '•'
        return str(n)

    def numlabel(numpr):
        ni, il = kid(numpr, 'numId'), kid(numpr, 'ilvl')
        nid = ni.get('{%s}val' % W) if ni is not None else None
        lvl = int(il.get('{%s}val' % W)) if il is not None else 0
        if not nid or nid == '0' or nid not in nummap or nummap[nid] not in numdefs:
            return '(auto-numbered)'
        defs = numdefs[nummap[nid]]
        cs = counters.setdefault(nid, {})
        cs[lvl] = cs.get(lvl, defs.get(lvl, ('', '', 1))[2] - 1) + 1
        for k_ in [k_ for k_ in cs if k_ > lvl]:
            del cs[k_]
        f, txt, st = defs.get(lvl, ('decimal', '%1.', 1))
        for k_ in range(lvl + 1):
            fk = defs.get(k_, ('decimal', '', 1))[0]
            txt = txt.replace('%%%d' % (k_ + 1), fmt_num(cs.get(k_, defs.get(k_, ('', '', 1))[2]), fk))
        return '{auto:%s}' % txt

    def block(e):
        t = ln(e)
        if t == 'p':
            pp = kid(e, 'pPr')
            lab = ''
            if pp is not None and kid(pp, 'numPr') is not None:
                lab = numlabel(kid(pp, 'numPr')) + ' '
            s = ''.join(inline(c) for c in e)
            return lab + s
        if t == 'tbl':
            rows = []
            for tr in kids(e, 'tr'):
                rows.append(' | '.join(' / '.join(block(p) for p in tc if ln(p) in ('p', 'tbl')) for tc in kids(tr, 'tc')))
            return '[TABLE]\n' + '\n'.join(rows) + '\n[/TABLE]'
        if t == 'sdt':
            c = kid(e, 'sdtContent')
            return '\n'.join(block(x) for x in c) if c is not None else ''
        return ''

    root = etree.fromstring(z.read('word/document.xml'))
    body = kid(root, 'body')
    for e in body:
        s = block(e)
        if s.strip():
            out.lines.append(s)
    heads = []
    for hf in sorted(n for n in z.namelist() if re.match(r'word/header\d*\.xml', n)):
        hroot = etree.fromstring(z.read(hf))
        ht = ' '.join(''.join(t_.text or '' for t_ in p_.iter('{%s}t' % W)) for p_ in hroot.iter('{%s}p' % W)).strip()
        if ht and ht not in heads:
            heads.append(ht)
    for ht in reversed(heads):
        out.lines.insert(0, '[HEADER] ' + ht)


# ---------------- ODT ----------------
def odt(path, out):
    z = zipfile.ZipFile(path)
    root = etree.fromstring(z.read('content.xml'))
    T = 'urn:oasis:names:tc:opendocument:xmlns:text:1.0'
    D = 'urn:oasis:names:tc:opendocument:xmlns:drawing:1.0'
    X = 'http://www.w3.org/1999/xlink'
    TB = 'urn:oasis:names:tc:opendocument:xmlns:table:1.0'
    MATH = 'http://www.w3.org/1998/Math/MathML'

    STY = 'urn:oasis:names:tc:opendocument:xmlns:style:1.0'
    supsub = {}
    for sty in root.iter('{%s}style' % STY):
        tp = sty.find('{%s}text-properties' % STY)
        if tp is not None:
            pos = tp.get('{%s}text-position' % STY, '')
            if pos.startswith('super') or (pos[:1].isdigit() and not pos.startswith('0')):
                supsub[sty.get('{%s}name' % STY)] = '^'
            elif pos.startswith('sub') or pos.startswith('-'):
                supsub[sty.get('{%s}name' % STY)] = '_'

    def obj(href):
        p = href.lstrip('./')
        for cand in (p + '/content.xml', p.rstrip('/') + '/content.xml'):
            if cand in z.namelist():
                m = etree.fromstring(z.read(cand))
                return '$' + mml(m) + '$'
        return '[OBJECT %s]' % href

    def inl(e):
        s = []
        if e.text:
            s.append(e.text)
        for c in e:
            t = ln(c)
            if t == 's':
                s.append(' ' * int(c.get('{%s}c' % T, '1')))
            elif t == 'tab':
                s.append('\t')
            elif t == 'line-break':
                s.append('\n')
            elif t == 'frame':
                s.append(frame(c))
            elif t == 'span':
                inner = inl(c)
                pos = supsub.get(c.get('{%s}style-name' % T))
                s.append('%s{%s}' % (pos, inner) if pos and inner.strip() and '$' not in inner else inner)
            elif t == 'a':
                s.append(inl(c))
            elif t == 'object' or t == 'object-ole':
                s.append(obj(c.get('{%s}href' % X, '')))
            elif t == 'image':
                s.append(img(c))
            elif t == 'custom-shape' or t == 'g' or t == 'line' or t == 'rect' or t == 'ellipse' or t == 'polygon' or t == 'path':
                s.append('[DRAWING-SHAPE vector figure; see page render]')
            if c.tail:
                s.append(c.tail)
        return ''.join(s)

    def img(c):
        h = c.get('{%s}href' % X, '')
        if h in z.namelist():
            return '[IMG %s]' % out.image(h, z.read(h))
        return '[IMG ?%s]' % h

    def frame(c):
        res = []
        for x in c:
            t = ln(x)
            if t == 'image':
                res.append(img(x))
            elif t == 'object' or t == 'object-ole':
                res.append(obj(x.get('{%s}href' % X, '')))
            elif t == 'text-box':
                res.append('[TEXTBOX] ' + ' / '.join(blk(p) for p in x) + ' [/TEXTBOX]')
        return ''.join(res)

    def blk(e):
        t = ln(e)
        if t in ('p', 'h'):
            return inl(e)
        if t == 'list':
            return '\n'.join('(auto-numbered) ' + ' '.join(blk(p) for p in li) for li in e)
        if t == 'table':
            rows = []
            for tr in e.iter('{%s}table-row' % TB):
                rows.append(' | '.join(' / '.join(blk(p) for p in tc) for tc in tr if ln(tc) == 'table-cell'))
            return '[TABLE]\n' + '\n'.join(rows) + '\n[/TABLE]'
        return ''

    body = root.find('.//{urn:oasis:names:tc:opendocument:xmlns:office:1.0}text')
    for e in body:
        s = blk(e)
        if s.strip():
            out.lines.append(s)


def main():
    src = pathlib.Path(sys.argv[1])
    out = Out(sys.argv[2])
    ext = src.suffix.lower()
    if ext not in ('.docx', '.odt') and zipfile.is_zipfile(src):
        names = zipfile.ZipFile(src).namelist()
        ext = '.odt' if 'content.xml' in names else ('.docx' if 'word/document.xml' in names else ext)
    if ext == '.docx':
        docx(src, out)
    elif ext == '.odt':
        odt(src, out)
    else:
        raise SystemExit('only .docx/.odt (use antiword for .doc text)')
    (out.dir / 'text.md').write_text(fix_symbols('\n'.join(out.lines)) + '\n', encoding='utf-8')
    print('%s: %d lines, %d images -> %s' % (src.name, len(out.lines), out.n, out.dir))


if __name__ == '__main__':
    main()
