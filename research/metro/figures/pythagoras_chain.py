"""Exact vector redraw of 自強110-1-2 選擇5: chain of right triangles with squares
甲(24) 乙(36) 丙(48) 丁(60) and three 12 cm² squares. Writes the SVG into the transcription."""
import json
import math
import pathlib
import sys

def add(a, b): return (a[0] + b[0], a[1] + b[1])
def sub(a, b): return (a[0] - b[0], a[1] - b[1])
def dot(a, b): return a[0] * b[0] + a[1] * b[1]
def scale(a, k): return (a[0] * k, a[1] * k)

def outward_square(p, q, away):
    """Square on segment pq on the side opposite to point `away`."""
    v = sub(q, p)
    n = (-v[1], v[0])
    if dot(n, sub(away, p)) > 0:
        n = (v[1], -v[0])
    return [p, q, add(q, n), add(p, n)]

r12 = math.sqrt(12)
Q, R, S, T = (0, 0), (6, 0), (6, 6), (0, 6)            # 乙 (36)
V = (-math.sqrt(8), 2)                                   # right angle, QV=√12, TV=√24
jia = outward_square(T, V, Q)                            # 甲 (24)
s1 = outward_square(Q, V, T)                             # 12
W = (6 + r12, 0)                                         # right angle at R
s2 = outward_square(R, W, S)                             # 12
bing = outward_square(S, W, R)                           # 丙 (48): S, W, X, U
X, U = bing[2], bing[3]
d = sub(X, U); d = scale(d, 1 / math.hypot(*d))
Y = add(X, scale((-d[1], d[0]) if dot((-d[1], d[0]), sub(S, X)) < 0 else (d[1], -d[0]), r12))
s3 = outward_square(X, Y, U)                             # 12
ding = outward_square(U, Y, X)                           # 丁 (60)
yi = [Q, R, S, T]

shapes = {'甲': jia, '乙': yi, '丙': bing, '丁': ding}
small = [s1, s2, s3]
tris = [[Q, V, T], [R, W, S], [X, Y, U]]
pts = [p for poly in list(shapes.values()) + small for p in poly]
minx, maxx = min(p[0] for p in pts), max(p[0] for p in pts)
miny, maxy = min(p[1] for p in pts), max(p[1] for p in pts)
k, pad = 13, 10
def P(p): return (round((p[0] - minx) * k + pad, 1), round((maxy - p[1]) * k + pad, 1))
def poly(points, fill):
    return '<path d="M' + 'L'.join(f'{x} {y}' for x, y in map(P, points)) + f'Z" fill="{fill}"/>'
def centre(points):
    return P((sum(p[0] for p in points) / len(points), sum(p[1] for p in points) / len(points)))
W_, H_ = round((maxx - minx) * k + 2 * pad), round((maxy - miny) * k + 2 * pad)
parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W_} {H_}"><g stroke="#111" stroke-width="1.2">']
parts += [poly(p, '#fff') for p in shapes.values()] + [poly(p, '#ececec') for p in small] + [poly(t, 'none') for t in tris]
parts.append('</g><g font-family="serif" font-size="16" fill="#111">')
for name, p in shapes.items():
    x, y = centre(p)
    label = name + ('（60）' if name == '丁' else '')
    parts.append(f'<text x="{x - (22 if name == "丁" else 8)}" y="{y + 6}">{label}</text>')
for p in small:
    x, y = centre(p)
    parts.append(f'<text x="{x - 9}" y="{y + 5}" font-size="13">12</text>')
parts.append('</g></svg>')
svg = ''.join(parts)

root = pathlib.Path(sys.argv[1])
f = root / 'research/metro/transcribed/metro-taoyuan-07d9937bb9f62b48.json'
d = json.loads(f.read_text(encoding='utf-8'))
for q in d['questions']:
    for b in q['blocks']:
        if b.get('type') == 'svg' and (b['svg'] == 'SQUARES_SVG' or '丁（60）' in b['svg']):
            b['svg'] = svg
f.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding='utf-8')
print(W_, H_, len(svg))
