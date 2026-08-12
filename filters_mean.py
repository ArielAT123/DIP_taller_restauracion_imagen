"""Etapa 3b: Filtros de media -> aritmética y contra-armónica."""
import numpy as np
import cv2


def filter_arithmetic_mean(img, size: int = 3):
    """Promedio simple en ventana size x size. Bueno para gaussiano."""
    return cv2.blur(img, (size, size))


def filter_contraharmonic(img, size: int = 3, q: float = 1.5):
    """Q > 0 elimina pimienta, Q < 0 elimina sal."""
    f = img.astype(np.float64) + 1e-6
    num = cv2.boxFilter(f ** (q + 1), -1, (size, size))
    den = cv2.boxFilter(f ** q, -1, (size, size))
    out = num / den
    return np.clip(out, 0, 255).astype(np.uint8)
