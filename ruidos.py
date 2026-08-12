import numpy as np


def agregar_ruido_sal(img):
    out = img.copy()
    h, w = out.shape[:2]
    par = int(round(h * w * 0.01))
    for _ in range(par):
        a = np.random.randint(0, h)
        b = np.random.randint(0, w)
        out[a, b] = 255
    return out


def agregar_ruido_gaussiano(img):
    out = img.copy()
    h, w = out.shape[:2]
    u = 127
    var = 100.0
    div = 2.5 * var
    pixel = h * w
    i_vals = np.arange(256)
    num = (i_vals - u) ** 2.0
    dem = 2.0 * (var ** 2)
    e = np.exp(-num / dem)
    per = np.round(pixel * (1.0 / div) * e).astype(int)
    v = per + 20
    validos = np.where(v > 0)[0]
    grid_y, grid_x = np.ogrid[:h, :w]
    mask = (grid_y + grid_x) % 2 == 0
    num_pixels = np.count_nonzero(mask)
    valores = np.random.choice(validos, size=num_pixels) - u
    out[mask] = np.clip(out[mask].astype(np.int32) + valores, 0, 255).astype(np.uint8)
    return out
