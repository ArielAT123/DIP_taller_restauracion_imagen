import numpy as np


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


def filtro_media_aritmetica(img, size: int = 3):
    h, w = img.shape[:2]
    pad = size // 2
    padded = np.pad(img, pad, mode='edge').astype(np.int32)
    out = np.zeros((h, w), dtype=np.uint8)
    n = size * size
    for i in range(h):
        for j in range(w):
            suma = 0
            for r in range(size):
                for c in range(size):
                    suma += padded[i + r, j + c]
            out[i, j] = suma // n
    return out
