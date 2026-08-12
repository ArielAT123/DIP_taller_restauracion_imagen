import numpy as np


def filtro_mediana(img, size: int = 3):
    h, w = img.shape[:2]
    pad = size // 2
    padded = np.pad(img, pad, mode='edge')
    out = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            vals = []
            for r in range(size):
                for c in range(size):
                    vals.append(padded[i + r, j + c])
            vals.sort()
            out[i, j] = vals[len(vals) // 2]
    return out


def filtro_maximo(img, size: int = 3):
    h, w = img.shape[:2]
    pad = size // 2
    padded = np.pad(img, pad, mode='edge')
    out = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            val_max = 0
            for r in range(size):
                for c in range(size):
                    val = padded[i + r, j + c]
                    if val > val_max:
                        val_max = val
            out[i, j] = val_max
    return out


def filtro_minimo(img, size: int = 3):
    h, w = img.shape[:2]
    pad = size // 2
    padded = np.pad(img, pad, mode='edge')
    out = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            val_min = 255
            for r in range(size):
                for c in range(size):
                    val = padded[i + r, j + c]
                    if val < val_min:
                        val_min = val
            out[i, j] = val_min
    return out


def filtro_punto_medio(img, size: int = 3):
    h, w = img.shape[:2]
    pad = size // 2
    padded = np.pad(img, pad, mode='edge').astype(np.float32)
    out = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            val_min = 255.0
            val_max = 0.0
            for r in range(size):
                for c in range(size):
                    val = padded[i + r, j + c]
                    if val < val_min:
                        val_min = val
                    if val > val_max:
                        val_max = val
            out[i, j] = int((val_min + val_max) / 2.0)
    return out


def filtro_media_aritmetica(img, size: int = 3):
    h, w = img.shape[:2]
    pad = size // 2
    padded = np.pad(img, pad, mode='edge').astype(np.float32)
    out = np.zeros((h, w), dtype=np.uint8)
    n = size * size
    for i in range(h):
        for j in range(w):
            suma = 0.0
            for r in range(size):
                for c in range(size):
                    suma += padded[i + r, j + c]
            out[i, j] = int(suma / n)
    return out


def filtro_contra_armonico(img, size: int = 3, r: float = 1.5):
    h, w = img.shape[:2]
    pad = size // 2
    padded = np.pad(img, pad, mode='edge').astype(np.float64) + 1e-6
    out = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            num = 0.0
            den = 0.0
            for kr in range(size):
                for kc in range(size):
                    val = padded[i + kr, j + kc]
                    num += val ** (r + 1)
                    den += val ** r
            val_out = num / (den + 1e-6)
            if val_out > 255.0:
                val_out = 255.0
            elif val_out < 0.0:
                val_out = 0.0
            out[i, j] = int(val_out)
    return out
 