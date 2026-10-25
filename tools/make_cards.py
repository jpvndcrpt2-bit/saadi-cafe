"""Unified Saadi Café product cards: photo on branded background + FA/EN name, ingredients, price."""
import sys, os, asyncio, base64, io
sys.path.insert(0, os.path.dirname(__file__))
from menu import M, PRICE
from PIL import Image, ImageFilter
import numpy as np
W, H = 1080, 1350
FS = '/tmp/w/node_modules/@fontsource/'
FONT = '/tmp/w/node_modules/vazirmatn/fonts/ttf/' if os.path.exists('/tmp/w') else 'fonts/'
def background():
    rng = np.random.default_rng(7)
    yy, xx = np.mgrid[0:H, 0:W]
    vig = 1 - 0.22 * (((xx - W/2)**2 + (yy - H/2)**2) / (W/2)**2 / 1.5)
    n = rng.normal(0, 9, (H, W))
    n = np.asarray(Image.fromarray((n*3+128).clip(0, 255).astype('uint8')).filter(ImageFilter.GaussianBlur(1.1))).astype(float) - 128
    a = np.array([176, 66, 38], float)[None, None, :] * vig[:, :, None] + n[:, :, None] / 3
    bg = Image.fromarray(a.clip(0, 255).astype('uint8'))
    logo = Image.open('img/logo.png').resize((170, 170), Image.LANCZOS)
    bg.paste(logo, ((W-170)//2, 38), logo)
    return bg
BG = background()
def compose(pid):
    bg = BG.copy()
    p = Image.open(f'img/cutout/{pid}.png').convert('RGBA')
    p = p.crop(p.getbbox())
    s = min(780 / p.width, 640 / p.height)
    p = p.resize((int(p.width*s), int(p.height*s)), Image.LANCZOS)
    x, y = (W-p.width)//2, 880 - p.height
    sh = Image.new('RGBA', bg.size, (0, 0, 0, 0))
    ell = Image.new('L', bg.size, 0)
    from PIL import ImageDraw
    ImageDraw.Draw(ell).ellipse([x+p.width*0.12, 880-18, x+p.width*0.88, 880+22], fill=140)
    sh.putalpha(ell.filter(ImageFilter.GaussianBlur(14)))
    bg = Image.alpha_composite(bg.convert('RGBA'), sh)
    bg.alpha_composite(p, (x, y))
    return bg.convert('RGB')
def fa(n): return str(n).translate(str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹'))
def price(c): return fa(f'{PRICE[c]:,}').replace(',', '٬') + ' تومان'
def U(p):
    return 'data:font/woff2;base64,' + base64.b64encode(open(FS + p, 'rb').read()).decode()
CSS = f"""
@font-face{{font-family:L;src:url('{U("aref-ruqaa/files/aref-ruqaa-arabic-700-normal.woff2")}');unicode-range:U+0600-06FF,U+200C-200F,U+FB50-FDFF,U+FE70-FEFF}}
@font-face{{font-family:L;src:url('{U("aref-ruqaa/files/aref-ruqaa-latin-700-normal.woff2")}');unicode-range:U+0000-00FF}}
@font-face{{font-family:E;src:url('{U("lemonada/files/lemonada-arabic-600-normal.woff2")}');unicode-range:U+0600-06FF,U+200C-200F,U+FB50-FDFF,U+FE70-FEFF}}
@font-face{{font-family:E;src:url('{U("lemonada/files/lemonada-latin-600-normal.woff2")}');unicode-range:U+0000-00FF}}
@font-face{{font-family:P;src:url('{U("pacifico/files/pacifico-latin-400-normal.woff2")}')}}
*{{margin:0;box-sizing:border-box}}body{{width:{W}px;height:{H}px;font-family:E,sans-serif;color:#fff6e6;position:relative;overflow:hidden}}
img{{position:absolute;inset:0}}
.t{{position:absolute;left:60px;right:60px;top:905px;text-align:center}}
.fa{{font-family:L;font-weight:700;font-size:92px;line-height:1.3;direction:rtl;text-shadow:0 3px 10px rgba(60,10,0,.35)}}
.en{{font-family:P,cursive;font-size:44px;color:#ffe2a3;margin-top:0}}
.ln{{width:140px;height:3px;background:#ffe2a3;margin:18px auto 14px;opacity:.85}}
.if{{font-family:E;font-size:25px;direction:rtl;line-height:1.7}}
.ie{{font-family:E;font-size:21px;line-height:1.4;margin-top:4px;opacity:.92}}
.lg .if{{font-size:22px;line-height:1.5}}.lg .ie{{font-size:18px}}.lg .fa{{font-size:84px}}
.pr{{position:absolute;bottom:26px;left:0;right:0;text-align:center;font-family:E;font-size:52px;color:#ffe2a3;direction:rtl}}
"""
def html(item, b64):
    slug, pid, c, f, e, i_f, i_e = item
    return f"<html><meta charset=utf-8><style>{CSS}</style><body><img src='data:image/jpeg;base64,{b64}'><div class='t{" lg" if len(i_f)>55 or len(i_e)>80 else ""}'><div class=fa>{f}</div><div class=en>{e}</div><div class=ln></div><div class=if>{i_f}</div><div class=ie>{i_e}</div></div><div class=pr>{price(c)}</div></body></html>"
async def main(only=None):
    from playwright.async_api import async_playwright
    os.makedirs('img/cards', exist_ok=True)
    async with async_playwright() as pw:
        br = await pw.chromium.launch(); pg = await br.new_page(viewport={'width': W, 'height': H})
        for it in M:
            if only and it[0] not in only: continue
            buf = io.BytesIO(); compose(it[1]).save(buf, 'JPEG', quality=93)
            await pg.set_content(html(it, base64.b64encode(buf.getvalue()).decode()))
            await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(300)
            await pg.screenshot(path=f'img/cards/{it[0]}.jpg', type='jpeg', quality=92)
        await br.close()
asyncio.run(main(sys.argv[1:] or None))
