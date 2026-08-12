import cv2
import numpy as np


def filtro_mediana(img, size: int = 3):
    return cv2.medianBlur(img, size)


def filtro_maximo(img, size: int = 3):
    kernel = np.ones((size, size), np.uint8)
    return cv2.dilate(img, kernel)


def filtro_minimo(img, size: int = 3):
    kernel = np.ones((size, size), np.uint8)
    return cv2.erode(img, kernel)


def filtro_punto_medio(img, size: int = 3):
    kernel = np.ones((size, size), np.uint8)
    mx = cv2.dilate(img, kernel).astype(np.float32)
    mn = cv2.erode(img, kernel).astype(np.float32)
    res = (mx + mn) / 2.0
    return np.clip(res, 0, 255).astype(np.uint8)


