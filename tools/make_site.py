"""Builds index.html (categorised menu with price under each product). Run from repo root after make_cards.py."""
import sys, os
sys.path.insert(0, 'menu')
from menu45 import M, PRICE
from PIL import Image
CATS = [("hot", "نوشیدنی‌های گرم", 0, 10), ("cold", "نوشیدنی‌های سرد", 10, 20), ("juice", "آبمیوه‌ها", 20, 25),
        ("shake", "میلک‌شیک‌ها", 25, 30), ("cake", "کیک و کروسان", 30, 45)]
def fa(n): return str(n).translate(str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹'))
def price(c): return fa(f'{PRICE[c]:,}').replace(',', '٬') + ' تومان'
os.makedirs('img/thumb', exist_ok=True)
for it in M:
    Image.open(f'img/cards/{it[0]}.jpg').resize((540, 675), Image.LANCZOS).save(f'img/thumb/{it[0]}.jpg', quality=82)
nav = ''.join(f'<a href="#{k}">{t}</a>' for k, t, a, b in CATS)
secs = ''
for k, t, a, b in CATS:
    figs = ''.join(f'<figure data-full="img/cards/{it[0]}.jpg"><img loading="lazy" src="img/thumb/{it[0]}.jpg" alt="{it[3]}"><figcaption><b>{it[3]}</b><span>{price(it[1])}</span></figcaption></figure>' for it in M[a:b])
    secs += f'<section id="{k}"><h2>{t}</h2><div class="g">{figs}</div></section>'
html = f'''<!doctype html><html lang="fa" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>منوی کافه سعدی</title>
<style>
:root{{--bg:#9a3a20;--ink:#fff6e6;--gold:#ffe2a3}}
*{{box-sizing:border-box;margin:0}}body{{background:var(--bg) url(img/background.jpg) center/cover fixed;color:var(--ink);font-family:Vazirmatn,Tahoma,sans-serif;padding-bottom:40px}}
header{{text-align:center;padding:22px 16px 8px}}header img{{width:96px;height:96px;border-radius:50%}}header h1{{font-size:26px;margin-top:6px;color:var(--gold)}}
nav{{position:sticky;top:0;z-index:5;display:flex;gap:8px;overflow-x:auto;padding:10px 16px;background:rgba(110,30,12,.92);backdrop-filter:blur(6px)}}
nav a{{flex:none;color:var(--ink);text-decoration:none;padding:7px 14px;border:1px solid var(--gold);border-radius:999px;font-size:15px}}
section{{padding:18px 16px 0;max-width:1100px;margin:auto;scroll-margin-top:60px}}h2{{color:var(--gold);font-size:22px;margin-bottom:12px}}
.g{{display:grid;grid-template-columns:repeat(2,1fr);gap:12px}}@media(min-width:700px){{.g{{grid-template-columns:repeat(4,1fr)}}}}
figure{{background:rgba(0,0,0,.18);border-radius:14px;overflow:hidden;cursor:pointer}}figure img{{width:100%;display:block}}
figcaption{{display:flex;justify-content:space-between;gap:6px;padding:8px 10px;font-size:14px}}figcaption span{{color:var(--gold);white-space:nowrap}}
#lb{{position:fixed;inset:0;background:rgba(0,0,0,.88);display:none;align-items:center;justify-content:center;z-index:9}}#lb img{{max-width:96vw;max-height:94vh;border-radius:12px}}
</style></head><body>
<header><img src="img/logo.png" alt="کافه سعدی"><h1>منوی کافه سعدی</h1></header>
<nav>{nav}</nav>{secs}
<div id="lb"><img alt=""></div>
<script>const lb=document.getElementById('lb'),li=lb.querySelector('img');document.querySelectorAll('figure').forEach(f=>f.onclick=()=>{{li.src=f.dataset.full;lb.style.display='flex'}});lb.onclick=()=>lb.style.display='none'</script>
</body></html>'''
open('index.html', 'w', encoding='utf-8').write(html)
print('ok', len(html))
