"""Etapa 2a: Ruido impulsivo -> sal, pimienta y sal y pimienta."""
import numpy as np


def _random_coords(shape, amount):
    n = int(amount * shape[0] * shape[1])
    return np.random.randint(0, shape[0], n), np.random.randint(0, shape[1], n)


def add_salt(img, amount: float = 0.02):
    """Ruido tipo sal: píxeles puestos en blanco (255)."""
    out = img.copy()
    out[_random_coords(img.shape, amount)] = 255
    return out


def add_pepper(img, amount: float = 0.02):
    """Ruido tipo pimienta: píxeles puestos en negro (0)."""
    out = img.copy()
    out[_random_coords(img.shape, amount)] = 0
    return out


def add_salt_pepper(img, amount: float = 0.02):
    """Combinación de sal y pimienta, cada una a la mitad de densidad."""
    return add_pepper(add_salt(img, amount / 2), amount / 2)
