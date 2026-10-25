"""Builds the identical Saadi Café background (rust-red grain + logo seal)."""
from PIL import Image, ImageFilter
import numpy as np
S = 1080
rng = np.random.default_rng(7)
base = np.array([133, 25, 3], float)            # rust red sampled from the logo
yy, xx = np.mgrid[0:S, 0:S]
vig = 1 - 0.28 * (((xx - S/2)**2 + (yy - S/2)**2) / (S/2)**2)   # soft vignette
noise = rng.normal(0, 9, (S, S))
noise = np.asarray(Image.fromarray((noise*3+128).clip(0,255).astype('uint8')).filter(ImageFilter.GaussianBlur(1.1))).astype(float)-128
img = base[None,None,:] * vig[:,:,None] + (noise[:,:,None] / 3)
bg = Image.fromarray(img.clip(0,255).astype('uint8'))
logo = Image.open('img/logo.png').resize((170,170), Image.LANCZOS)
bg.paste(logo, ((S-170)//2, 38), logo)
bg.save('img/background.jpg', quality=92)
