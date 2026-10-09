"""Rebuild the README terminal. Python 3 + Pillow, NumPy, SciPy.
Portrait is Janidu's supplied photo. Logo masks derive from Skill Icons (MIT).
No JavaScript, external fonts, image embeds, or external resources in SVG output.
"""
from pathlib import Path
from html import escape
import numpy as np
from PIL import Image, ImageOps, ImageEnhance, ImageFilter, ImageDraw, ImageFont
from scipy import ndimage
from scipy.optimize import linear_sum_assignment
from scipy.spatial.distance import cdist
ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT/'scripts/data'
rng=np.random.default_rng(2026)
W,H=300,340

def portrait():
    im=Image.open(ROOT/'assets/janidu.jpg').convert('RGB').crop((0,100,1023,1260)).resize((W,H),Image.Resampling.LANCZOS)
    rgb=np.asarray(im).astype(float)
    # The studio backdrop is blue. Fill enclosed regions so the tie remains.
    bg=(rgb[:,:,2]>rgb[:,:,0]*1.18)&(rgb[:,:,2]>rgb[:,:,1]*1.1)
    mask=ndimage.binary_fill_holes(ndimage.binary_closing(~bg,iterations=2))
    labs,n=ndimage.label(mask); sizes=np.bincount(labs.ravel());sizes[0]=0
    mask=labs==sizes.argmax()
    gray=ImageOps.autocontrast(im.convert('L'),cutoff=1)
    gray=ImageEnhance.Contrast(gray).enhance(1.3).filter(ImageFilter.UnsharpMask(radius=3,percent=140,threshold=3))
    a=np.asarray(gray).astype(float)/255
    points=[]
    for inverse in [False,True]:
        f=((1-a) if inverse else a).copy(); f=np.clip(f,.045,.97); f[~mask]=0
        out=np.zeros((H,W),bool)
        for y in range(H):
            xs=range(W) if y%2==0 else range(W-1,-1,-1); d=1 if y%2==0 else -1
            for x in xs:
                if not mask[y,x]:continue
                old=f[y,x]; v=float(old>=.5); out[y,x]=v; e=old-v
                for dx,dy,k in [(d,0,7/16),(-d,1,3/16),(0,1,5/16),(d,1,1/16)]:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<W and ny<H and mask[ny,nx]:f[ny,nx]+=e*k
        ys,xs=np.where(out&mask);points.append(np.column_stack((xs,ys)).astype(np.int16))
    return points

def sample_mask(name):
    im=Image.open(DATA/f'{name}.png').convert('RGBA')
    m=np.array(im)[:,:,3]>128
    y,x=np.where(m); pts=np.column_stack([x,y]).astype(float)
    # Farthest-point sampling spreads dots evenly across the logo silhouette.
    selected=[]; dist=np.full(len(pts),np.inf); j=int(rng.integers(len(pts)))
    for _ in range(900):
        selected.append(j); dist=np.minimum(dist,((pts-pts[j])**2).sum(1)); j=int(dist.argmax())
    return pts[selected]+[20,40]

def path(points):
    # Horizontal pixel runs keep full-resolution dither compact.
    p=points[np.lexsort((points[:,0],points[:,1]))];result=[];i=0
    while i<len(p):
        x,y=map(int,p[i]);j=i+1
        while j<len(p) and p[j,1]==y and p[j,0]==p[j-1,0]+1:j+=1
        result.append(f'M{x} {y}h{j-i}v1h-{j-i}z');i=j
    return ''.join(result)

portraits=portrait()
for n,p in zip(['portrait-dark','portrait-light'],portraits):np.save(DATA/(n+'.npy'),p)
code=Image.new('RGBA',(260,260));draw=ImageDraw.Draw(code)
f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',115)
draw.text((130,126),'</>',font=f,anchor='mm',fill='white');code.save(DATA/'code.png')
logos=[sample_mask(n) for n in ['react','python','code']]
for i in range(1,3):
    _,idx=linear_sum_assignment(cdist(logos[i-1],logos[i],metric='sqeuclidean'));logos[i]=logos[i][idx]
np.save(DATA/'logo-points.npy',np.array(logos).astype(np.float32))
rows=[
 ('Subject','Janidu Kalhara'),('Role','Full-Stack Software Engineer'),('Origin','Sri Lanka'),
 ('Education','BSc (Hons) Computer Science'),('Specialism','Software Engineering'),
 ('Honours','First Class / Kingston University, UK'),('Campus','ESOFT, Sri Lanka'),
 ('Status','Open to internships + junior roles'),
 ('Core.Lang','TypeScript, JavaScript, Python, C#, PHP'),
 ('Core.Frontend','React, Next.js, Tailwind CSS'),
 ('Core.Backend','Node.js, Express, FastAPI, Laravel, .NET'),
 ('Core.Data','PostgreSQL, MySQL, MongoDB'),('Core.AI','YOLO, OpenCV, OCR/NLP, Gemini'),
 ('ToolChain','Git, GitHub, Postman, Figma'),
 ('Grid.Mail','janidukalhara99@gmail.com'),('Grid.GitHub','github.com/janidukalhara'),('Grid.LinkedIn','linkedin.com/in/janidu-perera')]

def build(theme,mobile=False):
    dark=theme=='dark';p=portraits[0 if dark else 1];rand=np.random.default_rng(42)
    bg='#0A101F' if dark else '#F7F9FF';panel='#0C1528' if dark else '#FFFFFF'
    line='#273854' if dark else '#CAD5E6';fg='#E8EEF9' if dark else '#1C2840'
    muted='#8292AE' if dark else '#5D6E88';violet='#A78BFA' if dark else '#7C3AED';cyan='#22D3EE' if dark else '#0891B2'
    width,height=(600,1728) if mobile else (1180,696)
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
      '<title id="title">Janidu Kalhara — profile terminal</title><desc id="desc">A violet dither portrait morphs into React, Python and code symbols. Full-Stack Software Engineer from Sri Lanka. First Class Computer Science graduate, Kingston University via ESOFT. Open to internships and junior roles.</desc>',
      '''<style>text{font-family:Consolas,"Liberation Mono",monospace}.intro{animation:introEnd 3.2s linear forwards}.seed{opacity:0;animation:seed .7s ease-out forwards}.dense{opacity:0;animation:dense 14.2s 3.2s linear infinite}.band{animation:drift 14.2s 3.2s ease-in-out infinite}.particles{opacity:0;animation:particles 14.2s 3.2s linear infinite}.static{display:none}.live{animation:pulse 2s ease-in-out infinite}.caret{animation:caret 10s steps(28,end) infinite}.cursor{animation:blink 1s steps(2,end) infinite}.typeclip{animation:typing 10s steps(28,end) infinite}.caption{opacity:0;animation:label 14.2s 3.2s linear infinite}.intro-label{animation:introEnd 3.2s linear forwards}.c0{animation-name:label0}.c1{animation-name:label1}.c2{animation-name:label2}.c3{animation-name:label3}
@keyframes seed{to{opacity:1}}@keyframes introEnd{0%,99.99%{opacity:1}100%{opacity:0;visibility:hidden}}@keyframes dense{0%,21.126%,100%{opacity:1}30.282%,90.845%{opacity:0}}@keyframes drift{0%,21.126%,100%{transform:translate(0,0)}30.282%,90.845%{transform:translate(var(--dx),var(--dy))}}@keyframes particles{0%,21.126%,100%{opacity:0}30.282%,90.845%{opacity:1}}@keyframes pulse{50%{opacity:.35}}@keyframes blink{50%{opacity:0}}@keyframes caret{0%,8%,98%,100%{transform:translateX(0)}38%,82%{transform:translateX(505px)}}@keyframes typing{0%,8%,98%,100%{width:0}38%,82%{width:520px}}@keyframes label0{0%,19%,94%,100%{opacity:1}24%,90%{opacity:0}}@keyframes label1{0%,25%,48%,100%{opacity:0}30%,44%{opacity:1}}@keyframes label2{0%,48%,72%,100%{opacity:0}54%,67%{opacity:1}}@keyframes label3{0%,72%,94%,100%{opacity:0}77%,90%{opacity:1}}
@media(prefers-reduced-motion:reduce){.intro,.dense,.particles,.caption,.intro-label{display:none}.static{display:inline}.live,.cursor,.typeclip,.caret{animation:none}.caret{transform:translateX(505px)}.typeclip{width:520px}}
</style>''',
      '<defs><clipPath id="type"><rect class="typeclip" width="520" height="40"/></clipPath><clipPath id="map"><rect width="300" height="340"/></clipPath></defs>',
      f'<rect width="{width}" height="{height}" rx="18" fill="{bg}"/>']
    def text(x,y,t,size=14,color=None,anchor=None,extra=''):
        a=f' text-anchor="{anchor}"' if anchor else ''
        out.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color or fg}"{a} {extra}>{escape(t)}</text>')
    def rect(x,y,w,h,fill,stroke=None,rx=0):out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"'+(f' stroke="{stroke}"' if stroke else '')+'/>')
    text(width/2,25,'ENGINEER / BUILDER / ALWAYS LEARNING',10,muted,'middle', 'letter-spacing="2"')
    out.append(f'<g transform="translate({(width-520)/2},32)">');text(0,28,'Full-Stack Software Engineer',27,violet,extra='clip-path="url(#type)" textLength="505" lengthAdjust="spacingAndGlyphs"');out.append('<g class="caret">');text(0,28,'_',25,cyan,extra='class="cursor"');out.append('</g></g>')
    rect(12,83,width-24,height-96,panel,line,12)
    for x,c in [(34,'#FB7185'),(52,'#FBBF24'),(70,'#34D399')]:out.append(f'<circle cx="{x}" cy="105" r="4.5" fill="{c}"/>')
    text(width/2,110,'janidu@github:~ / profile.sh --live',12,muted,'middle')
    out.append(f'<path d="M12 127H{width-12}" stroke="{line}"/>')
    mx,my=(109,165) if mobile else (34,150)
    out.append(f'<g transform="translate({mx},{my})">')
    text(0,0,'VISUAL.MAP',13,cyan,extra='letter-spacing="1.7"');text(382,0,'01 / 04',11,muted,'end')
    rect(0,18,382,440,bg,line,6)
    # Small corner marks, not a grid or scanning effect.
    out.append(f'<path d="M0 35V18H17M365 18H382V35M0 441V458H17M365 458H382V441" fill="none" stroke="{cyan}"/>')
    out.append(f'<g transform="translate(26,35) scale(1.1)" fill="{violet}" clip-path="url(#map)">')
    out.append(f'<path class="static" d="{path(p)}" shape-rendering="crispEdges"/>')
    ids=rand.integers(0,60,len(p));out.append('<g class="intro" shape-rendering="crispEdges">')
    for i in range(60):out.append(f'<path class="seed" style="animation-delay:{i/60*2:.3f}s" d="{path(p[ids==i])}"/>')
    out.append('</g><g class="dense" shape-rendering="crispEdges">')
    # 94 irregular displacement clusters, assigned with noise to avoid block edges.
    noise=p+rand.normal(0,4,p.shape);b=np.clip((noise[:,1]/H*10).astype(int),0,9)*10+np.clip((noise[:,0]/W*10).astype(int),0,9);b=b%94
    for i in range(94):
        pts=p[b==i]
        if not len(pts):continue
        shift=(logos[0].mean(0)-pts.mean(0))*.42
        out.append(f'<path class="band" style="--dx:{shift[0]:.1f}px;--dy:{shift[1]:.1f}px" d="{path(pts)}"/>')
    out.append('</g><g class="particles">')
    source=p[rand.choice(len(p),900,replace=False)].astype(float)
    _,idx=linear_sum_assignment(cdist(source,logos[0],metric='sqeuclidean'))
    logo=[l[idx] for l in logos]
    times='0;0.2112676;0.3028169;0.4436620;0.5352113;0.6760563;0.7676056;0.9084507;1'
    for i in range(900):
        seq=[source[i],source[i],logo[0][i],logo[0][i],logo[1][i],logo[1][i],logo[2][i],logo[2][i],source[i]]
        out.append(f'<circle cx="{source[i,0]}" cy="{source[i,1]}" r="1.3">')
        for axis,name in [(0,'cx'),(1,'cy')]:
            vals=';'.join(f'{s[axis]:.1f}' for s in seq)
            out.append(f'<animate attributeName="{name}" values="{vals}" keyTimes="{times}" dur="14.2s" begin="3.2s" repeatCount="indefinite"/>')
        out.append('</circle>')
    out.append('</g></g>')
    labels=['JANIDU KALHARA / SOFTWARE ENGINEER','REACT / INTERFACES THAT WORK','PYTHON / INTELLIGENCE IN PRACTICE','FULL STACK / IDEAS INTO CODE']
    text(191,435,labels[0],10,muted,'middle','class="intro-label"')
    text(191,435,labels[0],10,muted,'middle','class="static"')
    for i,label in enumerate(labels):text(191,435,label,10,cyan if i else muted,'middle',f'class="caption c{i}"')
    text(0,483,'●',12,'#10B981');text(18,483,'LEARNING. BUILDING. ITERATING.',11,muted)
    out.append('</g>')
    sx,sy=(34,722) if mobile else (454,150)
    out.append(f'<g transform="translate({sx},{sy})">');rw=532 if mobile else 692
    text(0,0,'SYSTEM.INFO',13,cyan,extra='letter-spacing="1.7"')
    out.append(f'<circle class="live" cx="{rw-44}" cy="-4" r="3" fill="#FB7185"/>');text(rw,0,'LIVE',11,'#FB7185','end')
    rect(0,16,191,26,'#302350' if dark else '#EDE5FF',rx=4);text(10,34,'@janidukalhara',14,violet)
    for i,(label,value) in enumerate(rows):
        y=70+i*(50 if mobile else 25)
        if i in (8,14):out.append(f'<path d="M0 {y-16}H{rw}" stroke="{line}" opacity=".5"/>')
        ll=len(label)*8.05;vl=len(value)*8.05;start=ll+10;end=rw-vl-12
        if end>start and not mobile:out.append(f'<path d="M{start:.1f} {y-3}H{end:.1f}" stroke="{muted}" stroke-dasharray="1 4" opacity=".4"/>')
        text(0,y,label,17 if mobile else 13.4,cyan,extra='' if mobile else f'textLength="{ll:.1f}" lengthAdjust="spacingAndGlyphs"')
        text(0 if mobile else rw,y+24 if mobile else y,value,20 if mobile else 13.4,'#34D399' if dark and label=='Status' else ('#047857' if label=='Status' else fg),None if mobile else 'end',f'textLength="{len(value)*12 if mobile else vl:.1f}" lengthAdjust="spacingAndGlyphs"')
    text(0,956 if mobile else 507,'> building useful software, one commit at a time',12,violet)
    out.append('</g></svg>')
    target=ROOT/'assets'/f'about-{theme}{"-mobile" if mobile else ""}.svg';target.write_text(''.join(out))
    print(target.name,target.stat().st_size,'portrait pixels',len(p))
for theme in ['dark','light']:
    for mobile in [False,True]:build(theme,mobile)
