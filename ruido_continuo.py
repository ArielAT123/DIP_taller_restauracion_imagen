import numpy as np


def agregar_ruido_uniforme(img, low: float = -40, high: float = 40):
    noise = np.random.uniform(low, high, img.shape)
    out = img.astype(np.float32) + noise
    return np.clip(out, 0, 255).astype(np.uint8)


def agregar_ruido_gaussiano(img, mean: float = 0, sigma: float = 20):
    noise = np.random.normal(mean, sigma, img.shape)
    out = img.astype(np.float32) + noise
    return np.clip(out, 0, 255).astype(np.uint8)
