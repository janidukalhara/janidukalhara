"""Generate the profile's original SVG artwork and typing animation.
Run: python -m pip install Pillow; python scripts/generate_visuals.py
"""
from pathlib import Path
from html import escape
import math
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets'
OUT.mkdir(exist_ok=True)
BG = '#080c19'
CYAN = '#56e8f2'
PURPLE = '#ad83ff'
STYLE = '''<style>
text{font-family:Arial,Helvetica,sans-serif}
.float{animation:float 5s ease-in-out infinite}.float2{animation:float 6s ease-in-out -2s infinite}
.dash{animation:dash 14s linear infinite}.pulse{animation:pulse 3s ease-in-out infinite}
.scan{animation:scan 4s ease-in-out infinite}.shine{animation:shine 7s linear infinite}
.bars{transform-box:fill-box;transform-origin:bottom;animation:bars 3s ease-in-out infinite}
@keyframes float{50%{transform:translateY(-12px)}}
@keyframes dash{to{stroke-dashoffset:-480}}
@keyframes pulse{50%{opacity:.45}}
@keyframes scan{50%{transform:translateY(35px)}}
@keyframes shine{from{transform:translateX(-900px)}to{transform:translateX(1150px)}}
@keyframes bars{50%{transform:scaleY(.5)}}
@media(prefers-reduced-motion:reduce){.float,.float2,.dash,.pulse,.scan,.shine,.bars{animation:none}}
</style>'''

def svg(w,h,title,body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title>{STYLE}{body}</svg>'

stars=''.join(f'<circle class="pulse" style="animation-delay:-{i%5}s" cx="{30+(i*137)%1060}" cy="{24+(i*79)%310}" r="{1+i%2*.45}" fill="{CYAN if i%2 else PURPLE}" opacity=".6"/>' for i in range(32))
header=f'''<defs>
<linearGradient id="bg" x2="1" y2="1"><stop stop-color="#101127"/><stop offset=".5" stop-color="{BG}"/><stop offset="1" stop-color="#10233a"/></linearGradient>
<linearGradient id="neon"><stop stop-color="{CYAN}"/><stop offset=".5" stop-color="#c0acff"/><stop offset="1" stop-color="#fc82cd"/></linearGradient>
<linearGradient id="shine"><stop stop-color="white" stop-opacity="0"/><stop offset=".5" stop-color="white" stop-opacity=".65"/><stop offset="1" stop-color="white" stop-opacity="0"/></linearGradient>
<radialGradient id="glow"><stop stop-color="#a56bff" stop-opacity=".28"/><stop offset="1" stop-color="#a56bff" stop-opacity="0"/></radialGradient>
<clipPath id="name"><text x="560" y="183" font-size="73" font-weight="800" letter-spacing="-2" text-anchor="middle">JANIDU KALHARA</text></clipPath>
</defs>
<rect width="1120" height="354" rx="22" fill="url(#bg)"/>
<ellipse cx="560" cy="140" rx="510" ry="185" fill="url(#glow)"/>
{stars}
<path d="M20 21h1080v312H20z" fill="none" stroke="#253049" stroke-width="1"/>
<path class="dash" d="M20 21h1080v312H20z" fill="none" stroke="url(#neon)" stroke-width="2" stroke-dasharray="100 460"/>
<text x="560" y="72" text-anchor="middle" fill="{CYAN}" font-size="14" letter-spacing="5">HELLO WORLD / I'M</text>
<text x="560" y="183" text-anchor="middle" fill="url(#neon)" font-size="73" font-weight="800" letter-spacing="-2">JANIDU KALHARA</text>
<g clip-path="url(#name)"><rect class="shine" x="0" y="98" width="160" height="105" fill="url(#shine)" transform="skewX(-15)"/></g>
<text x="560" y="231" text-anchor="middle" fill="#bfcbe4" font-size="21" letter-spacing="2">CODE WITH PURPOSE. BUILD WITH CURIOSITY.</text>
<rect x="383" y="266" width="354" height="34" rx="17" fill="#142134" stroke="#28435d"/>
<circle class="pulse" cx="424" cy="283" r="4" fill="{CYAN}"/>
<text x="444" y="289" fill="#bfeff2" font-size="13" letter-spacing="1">SRI LANKA / OPEN TO OPPORTUNITIES</text>
<g class="float" fill="none" stroke="{CYAN}" stroke-width="2" opacity=".8"><path d="M73 120l-22 22 22 22M105 120l22 22-22 22M94 110l-13 64"/></g>
<g class="float2" fill="none" stroke="{PURPLE}" stroke-width="1.5" opacity=".8"><path d="M1016 108l35 20v40l-35 20-35-20v-40zM981 128l35 20 35-20M1016 148v40"/></g>
<path d="M70 318Q300 278 560 316T1050 318" fill="none" stroke="{CYAN}" opacity=".25"/>
<path class="dash" d="M70 318Q300 278 560 316T1050 318" fill="none" stroke="{CYAN}" stroke-width="2" stroke-dasharray="35 140"/>
'''
(OUT/'hero.svg').write_text(svg(1120,354,'Janidu Kalhara — Full-Stack Software Engineer and AI/ML Enthusiast',header))

divider=f'<defs><linearGradient id="d" gradientUnits="userSpaceOnUse" x1="0" x2="1120" y1="0" y2="0"><stop stop-color="{BG}"/><stop offset=".3" stop-color="{CYAN}"/><stop offset=".7" stop-color="{PURPLE}"/><stop offset="1" stop-color="{BG}"/></linearGradient></defs><path d="M0 15H1120" stroke="url(#d)"/><path class="dash" d="M0 15H1120" stroke="url(#d)" stroke-width="3" stroke-dasharray="60 180"/>'
(OUT/'divider.svg').write_text(svg(1120,30,'Animated cyan and purple divider',divider))

cards=[
 ('culinary','01','COMPUTER VISION','#56e8f2','<g class="scan"><path d="M410 40h72" stroke-width="3"/></g><path d="M422 47V32h15M465 32h15v15M480 75v15h-15M437 90h-15V75"/>'),
 ('medilink','02','HEALTHCARE TECH','#ff88c8','<path class="dash" stroke-dasharray="65 15" d="M399 66h18l8-18 13 35 13-47 12 30h35"/>'),
 ('nexus','03','FULL-STACK COMMERCE','#b599ff','<g class="float"><path d="M421 43h55l-5 47h-45zM436 43V33a12 12 0 0124 0v10"/></g>'),
 ('terramind','04','SUSTAINABILITY + DATA','#8ee6b0','<path d="M407 91h88"/><rect class="bars" x="417" y="61" width="14" height="28"/><rect class="bars" style="animation-delay:-1s" x="442" y="39" width="14" height="50"/><rect class="bars" style="animation-delay:-2s" x="467" y="24" width="14" height="65"/>'),
 ('escrap','05','CIRCULAR ECONOMY','#ffd384','<g class="pulse"><rect x="426" y="36" width="45" height="45" rx="7"/><path d="M437 24v12M458 24v12M437 81v12M458 81v12M414 47h12M414 69h12M471 47h12M471 69h12"/><rect x="438" y="48" width="21" height="21" rx="3"/></g>'),
 ('oeh','06','PRODUCT WORKFLOWS','#81b4ff','<g class="float2"><rect x="425" y="28" width="47" height="61" rx="5"/><path d="M435 44h26M435 56h26M435 68h16"/></g>')]
for slug,num,label,color,icon in cards:
    body=f'<rect x="1" y="1" width="518" height="118" rx="15" fill="{BG}" stroke="#28304b"/><path class="dash" d="M15 118h490" stroke="{color}" stroke-width="2" stroke-dasharray="55 90"/><text x="24" y="43" fill="{color}" font-size="12" letter-spacing="2">PROJECT / {num}</text><text x="24" y="78" fill="#e7ecff" font-size="18" font-weight="700">{label}</text><g fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{icon}</g>'
    (OUT/f'{slug}.svg').write_text(svg(520,120,label,body))

for slug,text,color,w in [('email','EMAIL ME',CYAN,164),('linkedin','LINKEDIN',PURPLE,164),('projects','EXPLORE PROJECTS','#ff88c8',230)]:
    body=f'<rect x="1" y="1" width="{w-2}" height="42" rx="9" fill="{BG}" stroke="{color}"/><circle class="pulse" cx="18" cy="22" r="3" fill="{color}"/><text x="{w/2+5}" y="27" fill="{color}" font-size="13" font-weight="700" letter-spacing="1.4" text-anchor="middle">{text}</text>'
    (OUT/f'{slug}.svg').write_text(svg(w,44,text,body))

# The GIF makes typing visible even in image clients with limited SVG animation.
font_candidates=[Path('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'),Path('C:/Windows/Fonts/consola.ttf')]
fontpath=next((p for p in font_candidates if p.exists()),None)
if fontpath is None: raise SystemExit('Install DejaVu Sans Mono, or adjust font_candidates.')
font=ImageFont.truetype(str(fontpath),29)
phrases=['Full-Stack Software Engineer','React / TypeScript / Node.js','Computer Vision + AI Enthusiast']
frames=[]; durations=[]
for pi,phrase in enumerate(phrases):
    states=[(i,70) for i in range(1,len(phrase)+1)]+[(len(phrase),180)]*10+[(i,35) for i in range(len(phrase)-1,0,-1)]
    for si,(n,duration) in enumerate(states):
        im=Image.new('RGB',(920,84),BG); d=ImageDraw.Draw(im)
        d.rounded_rectangle((1,1,918,82),12,outline='#262d47')
        txt='> '+phrase[:n]; full='> '+phrase
        left=(920-d.textlength(full,font=font))/2
        d.text((left,22),txt,font=font,fill=CYAN if pi!=2 else '#c1a5ff')
        x=left+d.textlength(txt,font=font)+5
        if n<len(phrase) or si%4<2: d.rectangle((x,25,x+12,56),fill=CYAN)
        d.line((32,73,888,73),fill='#182938')
        frames.append(im); durations.append(duration)
frames[0].save(OUT/'typing.gif',save_all=True,append_images=frames[1:],duration=durations,loop=0,optimize=True,disposal=2)
static=Image.new('RGB',(920,84),BG); d=ImageDraw.Draw(static);t='> Full-Stack Software Engineer'; d.text(((920-d.textlength(t,font=font))/2,22),t,font=font,fill=CYAN);static.save(OUT/'typing-static.png')
print(f'Generated original animated SVGs and {len(frames)} typing frames.')
