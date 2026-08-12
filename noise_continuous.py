"""Etapa 2b: Ruido continuo -> uniforme y gaussiano."""
import numpy as np


def add_uniform(img, low: float = -40, high: float = 40):
    """Suma ruido con distribución uniforme en [low, high]."""
    noise = np.random.uniform(low, high, img.shape)
    out = img.astype(np.float32) + noise
    return np.clip(out, 0, 255).astype(np.uint8)


def add_gaussian(img, mean: float = 0, sigma: float = 20):
    """Suma ruido con distribución normal (mean, sigma)."""
    noise = np.random.normal(mean, sigma, img.shape)
    out = img.astype(np.float32) + noise
    return np.clip(out, 0, 255).astype(np.uint8)
