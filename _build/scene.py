"""Illustrative (not real) satellite scene rendered in three 'bands'.
Ridged mountains in the north, a braided river, a patchwork of fields on the plains."""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage as ndi

W, H = 2000, 1250


def octave(scale, seed):
    r = np.random.default_rng(seed)
    g = r.random((H // scale + 4, W // scale + 4))
    z = ndi.zoom(g, scale, order=3)
    return z[:H, :W]


def fbm(scales, seed, ridged=False):
    out, tot, amp = np.zeros((H, W)), 0, 1.0
    for i, s in enumerate(scales):
        n = octave(s, seed + i)
        if ridged:
            n = 1 - np.abs(2 * n - 1)
        out += amp * n
        tot += amp
        amp *= .5
    return out / tot


def norm(a):
    return (a - a.min()) / (a.max() - a.min())


Y, X = np.mgrid[0:H, 0:W]
y = Y / H
x = X / W

# warp field
wx = (fbm([400, 200], 11) - .5) * 160
wy = (fbm([400, 200], 13) - .5) * 160
Xw = np.clip(X + wx, 0, W - 1)
Yw = np.clip(Y + wy, 0, H - 1)

ridges = fbm([250, 125, 62, 31, 15, 8, 4], 1, ridged=True)
ridges = ndi.map_coordinates(ridges, [Yw, Xw], order=1)
hills = fbm([300, 150, 75, 37, 18, 9, 4], 40)
mountain_mask = np.clip(1.05 - y * 1.9 + (fbm([500], 70) - .5) * .6, 0, 1) ** 1.3
elev = norm(mountain_mask * (.4 + ridges ** 2.2 * 1.1) + .18 * hills)

# river: a meandering polyline, then distance transform
t = np.linspace(0, 1, 2000)
rx = (.16 + .66 * t + .06 * np.sin(t * 11) + .025 * np.sin(t * 37 + 1)) * W
ry = (.0 + 1.0 * t) * H
riv = np.zeros((H, W), bool)
riv[np.clip(ry.astype(int), 0, H - 1), np.clip(rx.astype(int), 0, W - 1)] = True
# tributaries from the mountains
rng = np.random.default_rng(5)
starts = [(.06, .08, .30), (.42, .02, .38), (.70, .05, .50), (.93, .15, .62)]
for k, (sxf, syf, jf) in enumerate(starts):
    sx, sy = sxf * W, syf * H
    j = int(jf * len(t))
    ex, ey = rx[j], ry[j]
    tt = np.linspace(0, 1, 800)
    px = sx + (ex - sx) * tt + 25 * np.sin(tt * 9 + k)
    py = sy + (ey - sy) * tt + 15 * np.sin(tt * 7 + k * 2)
    riv[np.clip(py.astype(int), 0, H - 1), np.clip(px.astype(int), 0, W - 1)] = True
dist = ndi.distance_transform_edt(~riv)
main_w = 1.2 + 5.5 * y
water = dist < main_w * (0.75 + .5 * octave(30, 99))
flood = np.exp(-(dist / 70) ** 2) * np.clip((y - .25) / .2, 0, 1)

# field patchwork on the plains: warped grid cells, each with its own crop state
cell = 13
cx = ((X + wx * .3) * np.cos(.35) - (Y + wy * .3) * np.sin(.35)) // cell
cy = ((X + wx * .3) * np.sin(.35) + (Y + wy * .3) * np.cos(.35)) // (cell * 1.6)
h = (np.sin(cx * 12.9898 + cy * 78.233) * 43758.5453) % 1
plains = np.clip((.62 - elev) / .25, 0, 1) * np.clip((y - .35) / .2, 0, 1)
crop = np.where(h < .45, .7, np.where(h < .7, .45, .22))  # green crop, sparse, bare
crop = ndi.gaussian_filter(crop, 1.2) * .7 + .3 * norm(fbm([120, 60, 30], 22))
veg = norm(fbm([200, 100, 50, 25, 12], 21)) * (1 - elev) ** .5
veg = veg * (1 - plains) + crop * plains + .35 * flood
veg = np.clip(veg, 0, 1)
snow = np.clip((elev - .66) / .08, 0, 1) * np.clip(ridges * 1.4, 0, 1)

gy, gx = np.gradient(elev * 260)
shade = np.clip(1 + (-gx * .7 - gy * .5) * .9, .35, 1.4)
urban = ndi.gaussian_filter(((octave(40, 300) > .86) & (plains > .5) & (octave(2, 301) > .45)).astype(float), .8)


def finish(rgb, name):
    rgb = rgb * shade[..., None]
    rgb = rgb + (octave(3, 500)[..., None] - .5) * .04  # sensor grain
    Image.fromarray(np.clip(rgb * 255, 0, 255).astype(np.uint8)).save(
        f"{sys.argv[1]}/scene-{name}.jpg", quality=78, optimize=True, progressive=True)


def lerp(a, b, t):
    return a + (np.asarray(b) - a) * t[..., None]


base = np.ones((H, W, 3))
tc = lerp(base * [.66, .58, .46], [.50, .47, .44], np.clip((elev - .4) * 2.5, 0, 1))
tc = lerp(tc, [.24, .36, .17], veg * (1 - snow) * .9)
tc = lerp(tc, [.68, .66, .64], urban * .8)
tc = lerp(tc, [.96, .97, 1.0], snow)
tc[water] = [.12, .24, .30]
finish(tc, "true")

fc = lerp(base * [.58, .55, .53], [.45, .45, .5], np.clip((elev - .4) * 2.5, 0, 1))
fc = lerp(fc, [.86, .12, .16], veg * (1 - snow) * .95)
fc = lerp(fc, [.55, .7, .78], urban * .8)
fc = lerp(fc, [.9, .97, 1.0], snow)
fc[water] = [.03, .05, .18]
finish(fc, "false")

lst = np.clip(.88 - elev * 1.05 + .18 * (1 - veg) * plains - .35 * flood + .25 * urban, 0, 1)
lst[water] = .22
stops = np.array([[.04, .04, .22], [.28, .08, .52], [.72, .18, .42], [.97, .52, .14], [1, .94, .55]])
idx = lst * (len(stops) - 1)
i0 = np.clip(idx.astype(int), 0, len(stops) - 2)
th = stops[i0] + (stops[i0 + 1] - stops[i0]) * (idx - i0)[..., None]
shade_keep = shade
shade = 1 + (shade - 1) * .35  # thermal shows little relief shading
finish(th, "thermal")
print("ok")
