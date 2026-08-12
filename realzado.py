import cv2
import numpy as np


def realzar(img, sigma: float = 1.0, cantidad: float = 1.5):
    blurred = cv2.GaussianBlur(img, (0, 0), sigma)
    out = cv2.addWeighted(img, 1 + cantidad, blurred, -cantidad, 0)
    return np.clip(out, 0, 255).astype(np.uint8)
