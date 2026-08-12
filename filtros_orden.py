from scipy.ndimage import median_filter, maximum_filter, minimum_filter


def filtro_mediana(img, size: int = 3):
    return median_filter(img, size=size)


def filtro_maximo(img, size: int = 3):
    return maximum_filter(img, size=size)


def filtro_minimo(img, size: int = 3):
    return minimum_filter(img, size=size)


def filtro_punto_medio(img, size: int = 3):
    mx = maximum_filter(img, size=size).astype(int)
    mn = minimum_filter(img, size=size).astype(int)
    return ((mx + mn) // 2).astype(img.dtype)
