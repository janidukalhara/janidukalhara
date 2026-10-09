"""Frame Platane/snk output without altering contribution data or its route.
Usage: python scripts/style_snake.py [output directory]
Python standard library only. The generator's original SVG is nested intact.
"""
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

SVG = 'http://www.w3.org/2000/svg'
ET.register_namespace('', SVG)

def style(path: Path, dark: bool):
    root = ET.fromstring(path.read_text())
    # Catch malformed upstream output before publishing a blank card.
    if not root.findall(f'{{{SVG}}}rect'):
        raise ValueError(f'No contribution cells in {path}')
    bg, panel, border, fg, muted = (('#0A101F','#0E182B','#293953','#E8EEF9','#94A3BC') if dark else ('#F7F9FF','#FFFFFF','#CBD5E6','#1C2840','#5D6E88'))
    accent = '#22D3EE' if dark else '#0891B2'
    snake = '#34D399' if dark else '#059669'
    colors = ['#26344B','#514681','#7C3AED','#A78BFA','#22D3EE'] if dark else ['#E5EAF3','#DDD6FE','#C4B5FD','#8B5CF6','#0891B2']
    css = root.find(f'{{{SVG}}}style')
    if css is None:
        raise ValueError('Generated snake has no animation styles')
    css.text = re.sub(r'--cs:[^;}]+', f'--cs:{snake}', css.text)
    for i,color in enumerate(colors):
        css.text = re.sub(rf'--c{i}:[^;}}]+', f'--c{i}:{color}', css.text)
    css.text = re.sub(r'--ce:[^;}]+', f'--ce:{colors[0]}', css.text)
    # Keep all cells, tail segments and the collection bar synchronized.
    css.text = re.sub(r'(\d+)ms', lambda m: f'{round(int(m[1])*.85)}ms', css.text)
    css.text += f'.s{{stroke:{snake};stroke-width:.7;filter:drop-shadow(0 0 2px {snake})}}.s.s0{{fill:{"#D1FAE5" if dark else "#047857"};stroke-width:1.2}}'
    css.text += '@media(prefers-reduced-motion:reduce){.c,.s,.u{animation:none!important}.s{filter:none}}'
    root.set('x','35');root.set('y','112');root.set('width','930');root.set('height','203')
    nested = ET.tostring(root,encoding='unicode')
    legend = ''.join(f'<rect x="{771+i*23}" y="331" width="14" height="14" rx="3" fill="{c}"/>' for i,c in enumerate(colors))
    content = f'''<svg xmlns="{SVG}" width="1000" height="374" viewBox="0 0 1000 374" role="img" aria-labelledby="title desc">
<title id="title">Janidu Kalhara's contribution arcade</title>
<desc id="desc">An emerald snake follows my real GitHub contribution calendar, collecting activity squares. Refreshed every 12 hours. Violet to cyan squares indicate increasing activity.</desc>
<style>text{{font-family:Consolas,"Liberation Mono",monospace}}.status{{animation:breathe 2s ease-in-out infinite}}@keyframes breathe{{50%{{opacity:.4}}}}@media(prefers-reduced-motion:reduce){{.status{{animation:none}}}}</style>
<defs><linearGradient id="accent"><stop stop-color="{accent}"/><stop offset=".5" stop-color="#A78BFA"/><stop offset="1" stop-color="{snake}"/></linearGradient></defs>
<rect x="1" y="1" width="998" height="372" rx="18" fill="{bg}" stroke="{border}"/>
<path d="M24 1H976" stroke="url(#accent)" stroke-width="2"/>
<circle cx="29" cy="27" r="4" fill="#FB7185"/><circle cx="45" cy="27" r="4" fill="#FBBF24"/><circle cx="61" cy="27" r="4" fill="#34D399"/>
<text x="83" y="31" font-size="12" fill="{muted}">janidu@github:~ / contributions --play</text>
<circle class="status" cx="854" cy="27" r="3" fill="{snake}"/><text x="868" y="31" font-size="11" fill="{muted}">AUTO / 12H</text>
<path d="M1 48H999" stroke="{border}"/>
<text x="30" y="83" font-size="21" font-weight="700" fill="{fg}" letter-spacing="1.5">CONTRIBUTION ARCADE</text>
<text x="30" y="105" font-size="12" fill="{muted}">Every commit moves the story forward.</text>
<text x="968" y="84" font-size="12" text-anchor="end" fill="{accent}">365 DAYS / ONE TRAIL</text>
<rect x="23" y="119" width="954" height="197" rx="10" fill="{panel}" stroke="{border}"/>
{nested}
<text x="32" y="345" font-size="12" fill="{muted}">EAT. BUILD. REPEAT.</text>
<text x="752" y="343" font-size="11" fill="{muted}" text-anchor="end">LESS</text>{legend}<text x="894" y="343" font-size="11" fill="{muted}">MORE</text>
</svg>'''
    ET.fromstring(content)
    path.write_text(content)
    print(f'Styled {path.name}')

if __name__ == '__main__':
    output=Path(sys.argv[1] if len(sys.argv)>1 else 'dist')
    for name,dark in [('github-snake.svg',False),('github-snake-dark.svg',True)]:
        style(output/name,dark)
