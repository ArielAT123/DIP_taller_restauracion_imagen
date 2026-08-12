import numpy as np
import cv2


def filtro_media_aritmetica(img, size: int = 3):
    return cv2.blur(img, (size, size))


def filtro_contra_armonico(img, size: int = 3, q: float = 1.5):
    f = img.astype(np.float64) + 1e-6
    num = cv2.boxFilter(f ** (q + 1), -1, (size, size))
    den = cv2.boxFilter(f ** q, -1, (size, size))
    out = num / den
    return np.clip(out, 0, 255).astype(np.uint8)
