import numpy as np


def _coordenadas_aleatorias(shape, cantidad):
    n = int(cantidad * shape[0] * shape[1])
    return np.random.randint(0, shape[0], n), np.random.randint(0, shape[1], n)


def agregar_ruido_sal(img, cantidad: float = 0.02):
    out = img.copy()
    out[_coordenadas_aleatorias(img.shape, cantidad)] = 255
    return out


def agregar_ruido_pimienta(img, cantidad: float = 0.02):
    out = img.copy()
    out[_coordenadas_aleatorias(img.shape, cantidad)] = 0
    return out


def agregar_ruido_sal_pimienta(img, cantidad: float = 0.02):
    return agregar_ruido_pimienta(agregar_ruido_sal(img, cantidad / 2), cantidad / 2)
