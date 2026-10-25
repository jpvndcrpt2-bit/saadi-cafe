"""Cleans every original photo into img/cutout/<id>.png (transparent background, cropped)."""
import glob, os
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage as ndi

FILL = {'p01','p31','p32','p34','p35','p36'}

def cutout(path):
    im = Image.open(path).convert('RGBA')
    a = np.array(im)
    if (a[:, :, 3] < 10).mean() < 0.02:               # opaque photo with white background
        rgb = a[:, :, :3].astype(int)
        near_white = (rgb.min(axis=2) > 235)
        lab, n = ndi.label(near_white)
        border = set(np.unique(np.r_[lab[0], lab[-1], lab[:, 0], lab[:, -1]])) - {0}
        bg = np.isin(lab, list(border))
        bg = ndi.binary_dilation(bg, iterations=1)
        alpha = np.where(bg, 0, 255).astype('uint8')
        alpha = np.asarray(Image.fromarray(alpha).filter(ImageFilter.GaussianBlur(1.2)))
        a[:, :, 3] = alpha
    else:
        al = a[:, :, 3]
        al = np.where(al < 28, 0, al)                 # kill faint halos
        keep = ndi.binary_dilation(al > 128, iterations=12)
        lab, n = ndi.label(keep)
        if n > 1:
            sizes = ndi.sum(keep, lab, range(1, n + 1))
            ok = [i + 1 for i, s in enumerate(sizes) if s > 0.02 * sizes.max()]
            al = np.where(np.isin(lab, ok), al, 0)
        name = os.path.basename(path)[:-4]
        if name in FILL:                               # glass with see-through holes -> make solid
            m = ndi.binary_opening(al > 60, iterations=3 if name == 'p01' else 1)
            lab, n = ndi.label(m)
            if n > 1:
                sz = ndi.sum(m, lab, range(1, n + 1)); m = lab == (1 + int(np.argmax(sz)))
            m = ndi.binary_fill_holes(ndi.binary_closing(m, iterations=30 if name in ('p34','p35','p36') else 8))
            if name == 'p31':                          # broken mask: use the glass rectangle
                ys, xs = np.where(ndi.binary_opening(al > 60, iterations=1))
                x0, x1 = np.percentile(xs, [2, 98]); y0, y1 = np.percentile(ys, [0.5, 99.5])
                m = np.zeros_like(m); m[int(y0):int(y1), int(x0):int(x1)] = True
            soft = np.asarray(Image.fromarray((m * 255).astype('uint8')).filter(ImageFilter.GaussianBlur(1.2)))
            al = np.maximum(np.where(m, 255, 0), soft).astype('uint8') if name != 'p01' else soft
        a[:, :, 3] = al
    out = Image.fromarray(a)
    return out.crop(out.getchannel('A').getbbox())

if __name__ == '__main__':
    for f in sorted(glob.glob('img/original/*.png')):
        cutout(f).save('img/cutout/' + os.path.basename(f))
    print(len(glob.glob('img/cutout/*.png')))
