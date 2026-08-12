import numpy as np


def agregar_ruido_sal(img):
    out = img.copy()
    h, w = out.shape[:2]
    par = int(round(h * w * 0.01))
    a = np.random.randint(0, h, par)
    b = np.random.randint(0, w, par)
    out[a, b] = 255
    return out


def agregar_ruido_pimienta(img):
    out = img.copy()
    h, w = out.shape[:2]
    par = int(round(h * w * 0.01))
    a = np.random.randint(0, h, par)
    b = np.random.randint(0, w, par)
    out[a, b] = 0
    return out


def agregar_ruido_sal_pimienta(img):
    out = agregar_ruido_sal(img)
    return agregar_ruido_pimienta(out)
