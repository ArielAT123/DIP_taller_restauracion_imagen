import numpy as np
import cv2


def filtro_media_aritmetica(img, size: int = 3):
    return cv2.blur(img, (size, size))


def filtro_contra_armonico(img, size: int = 3, r: float = 1.5):
    f = img.astype(np.float64) + 1e-6
    kernel = np.ones((size, size), dtype=np.float64)
    num = cv2.filter2D(f ** (r + 1), -1, kernel)
    den = cv2.filter2D(f ** r, -1, kernel)
    out = num / (den + 1e-6)
    return np.clip(out, 0, 255).astype(np.uint8)


