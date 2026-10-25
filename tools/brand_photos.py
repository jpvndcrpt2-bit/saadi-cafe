"""Places each cut-out product photo on the identical Saadi Café background."""
import sys, glob, os, hashlib
from PIL import Image, ImageFilter
S=1080; BOX=(800,640); BASE_Y=1010   # product box and baseline (bottom edge)
bg=Image.open('img/background.jpg').convert('RGB')
seen=set(); n=0
for f in sorted(glob.glob('img/original/*.png')):
    h=hashlib.md5(open(f,'rb').read()).hexdigest()
    if h in seen: continue
    seen.add(h)
    im=Image.open(f).convert('RGBA'); im=im.crop(im.getchannel('A').getbbox())
    k=min(BOX[0]/im.width, BOX[1]/im.height); im=im.resize((round(im.width*k),round(im.height*k)),Image.LANCZOS)
    x=(S-im.width)//2; y=BASE_Y-im.height
    out=bg.copy().convert('RGBA')
    # soft contact shadow
    sh=Image.new('RGBA',(S,S),(0,0,0,0)); a=im.getchannel('A').point(lambda v:int(v*0.55))
    shadow=Image.new('RGBA',im.size,(40,5,0,255)); shadow.putalpha(a)
    sh.paste(shadow,(x+6,y+22),shadow); sh=sh.filter(ImageFilter.GaussianBlur(22))
    out=Image.alpha_composite(out,sh); out.alpha_composite(im,(x,y))
    n+=1; out.convert('RGB').save(f'img/branded/{os.path.basename(f)[:-4]}.jpg',quality=92)
print(n)
