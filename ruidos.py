import numpy as np

def agregar_ruido_sal(img, cantidad: float = 0.01):
    out = img.copy()
    h, w = out.shape[:2]
    par = int(round(h * w * cantidad))
    a = np.random.randint(0, h, par)
    b = np.random.randint(0, w, par)
    out[a, b] = 255
    return out


def agregar_ruido_pimienta(img, cantidad: float = 0.01):
    out = img.copy()
    h, w = out.shape[:2]
    par = int(round(h * w * cantidad))
    a = np.random.randint(0, h, par)
    b = np.random.randint(0, w, par)
    out[a, b] = 0
    return out


def agregar_ruido_sal_pimienta(img, cantidad: float = 0.02):
    return agregar_ruido_pimienta(agregar_ruido_sal(img, cantidad / 2), cantidad / 2)


def agregar_ruido_uniforme(img, low: float = -35.0, high: float = 35.0):
    noise = np.random.uniform(low, high, img.shape)
    out = img.astype(np.float32) + noise
    return np.clip(out, 0, 255).astype(np.uint8)


def agregar_ruido_gaussiano(imagen):
    media = 0
    sigma = 20
    alto, ancho = imagen.shape[:2]

    u1 = np.random.uniform(1e-10, 1.0, (alto, ancho))
    u2 = np.random.uniform(1e-10, 1.0, (alto, ancho))

    z = np.sqrt(-2.0 * np.log(u1)) * np.cos(2.0 * np.pi * u2)
    ruido = media + sigma * z

    salida = imagen.astype(np.float32) + ruido
    return np.clip(salida, 0, 255).astype(np.uint8)
