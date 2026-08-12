"""Etapa 4: Realzado de imagen mediante enmascaramiento por desenfoque."""
import cv2
import numpy as np


def sharpen(img, sigma: float = 1.0, amount: float = 1.5):
    """Resta una versión difuminada para acentuar bordes y detalles."""
    blurred = cv2.GaussianBlur(img, (0, 0), sigma)
    out = cv2.addWeighted(img, 1 + amount, blurred, -amount, 0)
    return np.clip(out, 0, 255).astype(np.uint8)
