"""Inline <style>/class CSS of transcribed SVG figures into presentation attributes.

The PDF typesetter and the print path read SVG attributes only, so figures drawn with
`<style> .line{fill:none;stroke:#000}` classes print as solid black shapes. This rewrites
each svg/optionFigures block so every element carries its own attributes, removes
<style>, empty <defs> and class attributes. Drawing geometry is untouched.

Usage: python scripts/inline_svg_css.py [--write] research/*/transcribed/<id>.json ...
Without --write it only reports what would change.
"""
import json
import pathlib
import re
import sys

KEEP = {'stroke', 'stroke-width', 'fill', 'stroke-linecap', 'stroke-linejoin', 'stroke-dasharray', 'font-size', 'font-style',
        'font-weight', 'text-anchor', 'dominant-baseline', 'opacity', 'fill-opacity', 'stroke-opacity', 'fill-rule'}
STYLE = re.compile(r'<style\b[^>]*>(.*?)</style>', re.S | re.I)
RULE = re.compile(r'([^{}]+)\{([^{}]*)\}')
TAG = re.compile(r'<([a-zA-Z][\w:-]*)((?:\s+[^<>]*?)?)(/?)>')
ATTR = re.compile(r'([\w:-]+)\s*=\s*"([^"]*)"')


def parse_css(css):
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    by_class, by_tag = {}, {}
    for selectors, body in RULE.findall(css):
        decls = {}
        for d in body.split(';'):
            if ':' in d:
                k, v = d.split(':', 1)
                k, v = k.strip().lower(), v.strip().replace('!important', '').strip()
                if k in KEEP:
                    decls[k] = re.sub(r'^([\d.]+)px$', r'\1', v)
        for sel in selectors.split(','):
            sel = sel.strip()
            if re.fullmatch(r'\.[\w-]+', sel):
                by_class.setdefault(sel[1:], {}).update(decls)
            elif re.fullmatch(r'[a-zA-Z]+', sel):
                by_tag.setdefault(sel, {}).update(decls)
            elif sel:
                raise ValueError(f'Unsupported CSS selector: {sel}')
    return by_class, by_tag


def inline(svg):
    m = STYLE.search(svg)
    by_class, by_tag = parse_css('\n'.join(STYLE.findall(svg))) if m else ({}, {})
    svg = STYLE.sub('', svg)
    svg = re.sub(r'<defs>\s*</defs>', '', svg)

    def fix(match):
        name, attrs, close = match.group(1), match.group(2), match.group(3)
        if name in ('svg', 'defs', 'style'):
            tag = re.sub(r'\sclass="[^"]*"', '', match.group(0))
            # invalid length values make browsers log console errors; the viewBox alone sizes the figure
            return re.sub(r'\s(?:height="auto"|width="100%"|height="100%")', '', tag)
        attributes = dict(ATTR.findall(attrs))
        merged = dict(by_tag.get(name, {}))
        for cls in attributes.pop('class', '').split():
            merged.update(by_class.get(cls, {}))
        if 'style' in attributes:
            for d in attributes.pop('style').split(';'):
                if ':' in d:
                    k, v = d.split(':', 1)
                    if k.strip().lower() in KEEP:
                        merged[k.strip().lower()] = re.sub(r'^([\d.]+)px$', r'\1', v.strip())
        attributes.update(merged)
        if not attributes and not attrs.strip():
            return match.group(0)
        return f'<{name} ' + ' '.join(f'{k}="{v}"' for k, v in attributes.items()) + f'{close}>'
    return TAG.sub(fix, svg)


def needs_inline(svg):
    return bool(re.search(r'<style\b|\sclass=|<(?!svg\b)[a-zA-Z][^<>]*\sstyle=|\sheight="auto"|\swidth="100%"|\sheight="100%"', svg, re.I))


if __name__ == '__main__':
    write = '--write' in sys.argv
    changed = 0
    for name in [a for a in sys.argv[1:] if not a.startswith('--')]:
        path = pathlib.Path(name)
        t = json.loads(path.read_text(encoding='utf-8'))
        n = 0
        for q in t['questions']:
            for b in q['blocks']:
                if b['type'] in ('svg', 'optionFigures') and needs_inline(b['svg']):
                    b['svg'] = inline(b['svg'])
                    if needs_inline(b['svg']):
                        raise ValueError(f'{path.stem} {q["sourceNumber"]}: CSS still present after inlining')
                    n += 1
        if n:
            changed += n
            print(f'{path.stem}: {n} figures {"inlined" if write else "need inlining"}')
            if write:
                path.write_text(json.dumps(t, ensure_ascii=False, indent=1), encoding='utf-8')
    print(f'total {changed}')
