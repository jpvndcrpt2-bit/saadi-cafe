"""Saadi Café new menu: 45 items. Prices (IQD? no - toman): coffee/shake 200k, cold 150k, cake 100k."""
PRICE = {"coffee": 200000, "cold": 150000, "shake": 200000, "cake": 100000}
# container: mug = small signature café mug (hot) | glass = clear glass (cold, juice) | goblet = glass goblet (shake) | plate = cake/croissant
# slug, price class, container, fa, en, fa ingredients, en ingredients, subject for the photo prompt
M = [
# ---- 10 hot drinks (small special café mug)
("espresso","coffee","mug","اسپرسو","Espresso","یک شات اسپرسوی غلیظ","One shot of concentrated espresso","a single espresso with golden crema"),
("americano","coffee","mug","آمریکانو","Americano","اسپرسو + آب داغ","Espresso + hot water","an americano, dark coffee"),
("cappuccino","coffee","mug","کاپوچینو","Cappuccino","اسپرسو + شیر + فوم شیر","Espresso + milk + milk foam","a cappuccino with latte art"),
("latte","coffee","mug","لاته","Latte","اسپرسو + شیر بخارداده","Espresso + steamed milk","a latte with heart latte art"),
("flat-white","coffee","mug","فلت وایت","Flat White","اسپرسو دبل + شیر میکروفوم","Double espresso + microfoam milk","a flat white with thin microfoam"),
("mocha","coffee","mug","موکا","Mocha","اسپرسو + سس شکلات + شیر","Espresso + chocolate sauce + milk","a mocha with chocolate drizzle on foam"),
("macchiato","coffee","mug","ماکیاتو","Macchiato","اسپرسو + کمی فوم شیر","Espresso + a dollop of milk foam","a macchiato with a spot of milk foam"),
("turkish-coffee","coffee","mug","قهوه ترک","Turkish Coffee","قهوه ترک + آب","Turkish coffee + water","Turkish coffee with thick foam"),
("hot-chocolate","cold","mug","هات چاکلت","Hot Chocolate","شکلات تلخ + شیر داغ","Dark chocolate + hot milk","hot chocolate topped with whipped cream and cocoa powder"),
("masala-chai","cold","mug","چای ماسالا","Masala Chai","چای + شیر + ادویهٔ ماسالا","Tea + milk + masala spices","spiced masala chai with a cinnamon stick"),
# ---- 10 cold drinks (clear glass)
("iced-americano","coffee","glass","آیس آمریکانو","Iced Americano","اسپرسو + آب سرد + یخ","Espresso + cold water + ice","an iced americano with ice cubes"),
("iced-latte","coffee","glass","آیس لاته","Iced Latte","اسپرسو + شیر سرد + یخ","Espresso + cold milk + ice","an iced latte with visible milk and coffee layers"),
("iced-caramel-latte","coffee","glass","آیس کارامل لاته","Iced Caramel Latte","اسپرسو + شیر سرد + سس کارامل + یخ","Espresso + cold milk + caramel sauce + ice","an iced caramel latte with caramel drizzle"),
("iced-mocha","coffee","glass","آیس موکا","Iced Mocha","اسپرسو + شیر سرد + سس شکلات + یخ","Espresso + cold milk + chocolate sauce + ice","an iced mocha with chocolate swirl"),
("cold-brew","coffee","glass","کلد برو","Cold Brew","قهوهٔ دم‌آوری سرد + یخ","Slow-steeped cold coffee + ice","dark cold brew coffee over large ice cubes"),
("caramel-frappe","coffee","glass","کارامل فراپه","Caramel Frappé","قهوه + شیر + کارامل + یخ + خامه","Coffee + milk + caramel + ice + whipped cream","a caramel frappé topped with whipped cream and caramel"),
("iced-matcha","cold","glass","آیس ماچا","Iced Matcha","ماچا + شیر + یخ","Matcha + milk + ice","an iced matcha latte with green and white layers"),
("iced-strawberry-matcha","cold","glass","آیس ماچا توت‌فرنگی","Iced Strawberry Matcha","ماچا + شیر + پوره توت‌فرنگی + یخ","Matcha + milk + strawberry puree + ice","a strawberry matcha with pink and green layers"),
("peach-iced-tea","cold","glass","چای سرد هلو","Peach Iced Tea","چای + عصارهٔ هلو + یخ","Tea + peach extract + ice","a peach iced tea with a peach slice"),
("classic-mojito","cold","glass","موهیتو کلاسیک","Classic Mojito","لیمو + نعناع + شربت + سودا + یخ","Lime + mint + syrup + soda + ice","a classic mojito with mint leaves and lime wedges"),
# ---- 5 juices (clear glass)
("orange-juice","cold","glass","آب‌پرتقال","Orange Juice","پرتقال تازه","Fresh oranges","fresh orange juice with an orange slice"),
("strawberry-juice","cold","glass","آب توت‌فرنگی","Strawberry Juice","توت‌فرنگی تازه","Fresh strawberries","strawberry juice with a strawberry on the rim"),
("mango-juice","cold","glass","آب انبه","Mango Juice","انبهٔ رسیده","Ripe mango","thick mango juice with mango cubes"),
("pomegranate-juice","cold","glass","آب انار","Pomegranate Juice","انار تازه","Fresh pomegranate","deep red pomegranate juice with pomegranate seeds"),
("watermelon-juice","cold","glass","آب هندوانه","Watermelon Juice","هندوانهٔ تازه + یخ","Fresh watermelon + ice","watermelon juice with a watermelon wedge"),
# ---- 5 shakes (glass goblet)
("chocolate-shake","shake","goblet","میلک‌شیک شکلات","Chocolate Milkshake","بستنی + شیر + سس شکلات","Ice cream + milk + chocolate sauce","a chocolate milkshake with whipped cream and chocolate drizzle"),
("strawberry-shake","shake","goblet","میلک‌شیک توت‌فرنگی","Strawberry Milkshake","بستنی + شیر + توت‌فرنگی","Ice cream + milk + strawberries","a pink strawberry milkshake with whipped cream and a strawberry"),
("oreo-shake","shake","goblet","میلک‌شیک اوریو","Oreo Milkshake","بستنی + شیر + بیسکوئیت اوریو","Ice cream + milk + Oreo cookies","an Oreo milkshake with whipped cream and cookie crumbs"),
("pistachio-shake","shake","goblet","میلک‌شیک پسته","Pistachio Milkshake","بستنی + شیر + پسته","Ice cream + milk + pistachio","a pistachio milkshake with crushed pistachios on top"),
("lotus-shake","shake","goblet","میلک‌شیک لوتوس","Lotus Milkshake","بستنی + شیر + کرم لوتوس","Ice cream + milk + Lotus spread","a Lotus milkshake with a Biscoff cookie on top"),
# ---- 15 cakes and croissants (plate)
("plain-croissant","cake","plate","کروسان ساده","Plain Croissant","خمیر کروسان کره‌ای","Butter croissant dough","a golden buttery croissant"),
("chocolate-croissant","cake","plate","کروسان شکلات","Chocolate Croissant","کروسان + شکلات","Croissant + chocolate","a chocolate-filled croissant"),
("almond-croissant","cake","plate","کروسان بادام","Almond Croissant","کروسان + کرم بادام + بادام ورقه‌ای","Croissant + almond cream + sliced almonds","an almond croissant dusted with powdered sugar"),
("cheese-croissant","cake","plate","کروسان پنیر","Cheese Croissant","کروسان + پنیر","Croissant + cheese","a cheese croissant"),
("ny-cheesecake","cake","plate","چیزکیک نیویورکی","New York Cheesecake","پنیر خامه‌ای + پایهٔ بیسکوئیتی","Cream cheese + biscuit base","a slice of New York cheesecake"),
("san-sebastian","cake","plate","چیزکیک سن‌سباستین","San Sebastián Cheesecake","پنیر خامه‌ای + خامه، سطح کاراملی","Cream cheese + cream, caramelized top","a slice of burnt San Sebastián cheesecake"),
("lotus-cheesecake","cake","plate","چیزکیک لوتوس","Lotus Cheesecake","پنیر خامه‌ای + کرم لوتوس","Cream cheese + Lotus spread","a Lotus cheesecake slice with Biscoff crumbs"),
("tiramisu","cake","plate","تیرامیسو","Tiramisu","ماسکارپونه + قهوه + بیسکوئیت + کاکائو","Mascarpone + coffee + ladyfingers + cocoa","a square of tiramisu dusted with cocoa"),
("red-velvet","cake","plate","کیک رد ولوت","Red Velvet Cake","کیک کاکائویی قرمز + کرم پنیر","Red cocoa cake + cream cheese frosting","a slice of red velvet cake with cream cheese frosting"),
("carrot-cake","cake","plate","کیک هویج","Carrot Cake","هویج + گردو + دارچین + کرم پنیر","Carrot + walnut + cinnamon + cream cheese","a slice of carrot cake with frosting and walnuts"),
("brownie","cake","plate","براونی","Brownie","شکلات تلخ + گردو","Dark chocolate + walnuts","a fudgy chocolate brownie square"),
("lava-cake","cake","plate","کیک لاوا","Chocolate Lava Cake","کیک شکلاتی با مغز شکلات مذاب","Chocolate cake with molten center","a chocolate lava cake with melted center flowing out"),
("banana-bread","cake","plate","کیک موز","Banana Bread","موز + گردو + دارچین","Banana + walnuts + cinnamon","a slice of banana bread"),
("cinnamon-roll","cake","plate","رول دارچین","Cinnamon Roll","خمیر + دارچین + گلیز","Dough + cinnamon + glaze","a cinnamon roll with white glaze"),
("chocolate-cake","cake","plate","کیک شکلاتی","Chocolate Fudge Cake","کیک کاکائویی + گاناش شکلات","Cocoa cake + chocolate ganache","a slice of chocolate fudge cake"),
]
CONTAINER = {
 "mug": "served in a modern matte sage-green ceramic coffee cup with straight slightly tapered sides and a small square handle, sitting on a matching matte sage-green oval tray-style saucer (a smooth solid single-color matte glaze, no speckles, no pattern)",
 "glass": "served in a tall clear glass tumbler",
 "goblet": "served in a clear footed glass goblet (stemmed milkshake glass)",
 "plate": "on a simple matte sage-green round ceramic plate",
}
STYLE = "Professional studio food photograph, on a clean modern cafe bar counter, with a softly blurred barista bar and espresso machine in the background, soft warm side light, shallow depth of field, clean uncluttered background, vertical 4:5 framing, no text, no logo, no hands, no spoon, no extra objects."
def prompt(m):
    return f"{m[7].capitalize()}, {CONTAINER[m[2]]}. {STYLE}"
if __name__ == "__main__":
    assert len(M) == 45 and len({m[0] for m in M}) == 45
    for m in M: print(m[0] + "\t" + prompt(m))
