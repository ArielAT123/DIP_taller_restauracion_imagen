import numpy as np


def agregar_ruido_uniforme(img):
    out = img.copy()
    h, w = out.shape[:2]
    validos = np.arange(88, 170)
    grid_y, grid_x = np.ogrid[:h, :w]
    mask = (grid_y + grid_x) % 2 == 0
    num_pixels = np.count_nonzero(mask)
    valores = np.random.choice(validos, size=num_pixels) - 128
    out[mask] = np.clip(out[mask].astype(np.int32) + valores, 0, 255).astype(np.uint8)
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



