"""Builds index.html: categorised menu, price under each product."""
import sys, json, os
sys.path.insert(0, os.path.dirname(__file__))
from menu import M, PRICE
CATS = [
 ("hot-coffee","قهوه گرم","turkish-coffee espresso-double flat-white macchiato americano mocha saffron-latte lotugino macchiato-caramel vanilla-latte hazelnut-latte coconut-latte honey-cinnamon-latte cappuccino cortado"),
 ("hot","نوشیدنی گرم و دمنوش","hot-chocolate sahlab masala saffron-milk hot-matcha-latte iraqi-tea green-tea red-karbala-tea deep-calm apple-cinnamon golden-sour"),
 ("iced-coffee","قهوه سرد","iced-americano iced-latte iced-vanilla-latte iced-caramel-latte iced-coconut-latte iced-strawberry-latte v60 cold-brew"),
 ("frappe","فراپه","mocha-frappe caramel-frappe vanilla-frappe"),
 ("matcha","ماچا","iced-matcha iced-strawberry-matcha iced-mango-matcha"),
 ("shake","میلک‌شیک","chocolate-milkshake lotus-milkshake pistachio-milkshake nuts-honey-milkshake oreo-milkshake"),
 ("smoothie","اسموتی","fruit-smoothie orange-smoothie tinax-smoothie soul-smoothie"),
 ("mojito","موهیتو","classic-mojito lemon-mojito strawberry-mojito fruit-mojito passion-mojito blueberry-mojito"),
 ("mocktail","موکتل","sourkila loverkila blue-mocktail"),
 ("juice","آبمیوه","orange-juice strawberry-juice mango-juice banana-juice banana-strawberry banana-chocolate strawberry-mango"),
 ("crepe","کرپ","chocolate-crepe lotus-crepe pistachio-crepe sushi-crepe bokja-crepe"),
 ("waffle","وافل","chocolate-waffle lotus-waffle pistachio-waffle"),
]
by = {m[0]: m for m in M}
def fa(n): return str(n).translate(str.maketrans('0123456789','۰۱۲۳۴۵۶۷۸۹'))
def pr(c): return fa(f'{PRICE[c]:,}').replace(',','٬')+' تومان'
seen=set(); data=[]
for k,t,s in CATS:
    its=[]
    for slug in s.split():
        m=by[slug]; seen.add(slug)
        its.append(dict(s=slug,f=m[3],e=m[4],p=pr(m[2])))
    data.append(dict(k=k,t=t,i=its))
assert seen==set(by), set(by)-seen
html='''<!doctype html><html lang="fa" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>منوی کافه سعدی</title>
<style>
*{box-sizing:border-box;margin:0}
body{background:#b04226;color:#fff6e6;font-family:Tahoma,system-ui,sans-serif;text-align:center;padding-bottom:40px}
header img{width:120px;margin:18px auto 4px;display:block}
h1{font-size:21px;color:#ffe2a3;margin-bottom:8px}
nav{position:sticky;top:0;z-index:5;background:#b04226;padding:8px 10px;display:flex;gap:8px;overflow-x:auto;white-space:nowrap;scrollbar-width:none;box-shadow:0 2px 8px rgba(60,10,0,.3)}
nav button{flex:none;background:#8f3017;color:#fff6e6;border:1px solid #ffe2a3;border-radius:20px;padding:7px 15px;font:inherit;font-size:14px;cursor:pointer}
nav button.on{background:#ffe2a3;color:#6b1d0b}
main{max-width:1000px;margin:auto;padding:0 12px}
h2{color:#ffe2a3;font-size:19px;margin:22px 0 10px;display:flex;align-items:center;gap:10px}
h2::before,h2::after{content:"";flex:1;height:1px;background:#ffe2a3;opacity:.45}
.g{display:grid;grid-template-columns:repeat(auto-fill,minmax(155px,1fr));gap:12px}
figure{background:#8f3017;border-radius:12px;overflow:hidden}
figure img{width:100%;display:block;cursor:pointer}
figcaption{padding:7px 6px 9px;font-size:14px}
figcaption b{display:block;font-size:15px}
figcaption span{color:#ffe2a3;font-size:14px}
#o{position:fixed;inset:0;background:rgba(40,8,0,.93);display:none;align-items:center;justify-content:center;z-index:9}
#o img{max-width:96vw;max-height:96vh}
</style></head><body>
<header><img src="img/logo.png" alt="کافه سعدی"><h1>منوی کافه سعدی</h1></header>
<nav id="n"></nav><main id="m"></main>
<div id="o" onclick="this.style.display='none'"><img id="b" alt=""></div>
<script>
const D=__DATA__,n=document.getElementById('n'),m=document.getElementById('m');
function render(k){m.innerHTML='';D.filter(c=>k=='all'||c.k==k).forEach(c=>{const h=document.createElement('h2');h.textContent=c.t;m.appendChild(h);const g=document.createElement('div');g.className='g';c.i.forEach(i=>{const f=document.createElement('figure');const im=document.createElement('img');im.loading='lazy';im.src='img/thumb/'+i.s+'.jpg';im.alt=i.f+' - '+i.e;im.onclick=()=>{b.src='img/cards/'+i.s+'.jpg';o.style.display='flex'};const cp=document.createElement('figcaption');cp.innerHTML='<b></b><span></span>';cp.firstChild.textContent=i.f;cp.lastChild.textContent=i.p;f.append(im,cp);g.appendChild(f)});m.appendChild(g)});window.scrollTo(0,0)}
[['all','همه']].concat(D.map(c=>[c.k,c.t])).forEach(([k,t],x)=>{const bt=document.createElement('button');bt.textContent=t;if(!x)bt.className='on';bt.onclick=()=>{n.querySelectorAll('button').forEach(y=>y.className='');bt.className='on';render(k)};n.appendChild(bt)});
render('all');
</script></body></html>'''.replace('__DATA__',json.dumps(data,ensure_ascii=False))
open('index.html','w').write(html)
