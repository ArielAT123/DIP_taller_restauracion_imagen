"""Etapa 3a: Filtros de orden -> mediana, máximo, mínimo, punto medio."""
from scipy.ndimage import median_filter, maximum_filter, minimum_filter


def filter_median(img, size: int = 3):
    """Bueno para ruido sal y pimienta."""
    return median_filter(img, size=size)


def filter_max(img, size: int = 3):
    """Bueno para ruido tipo pimienta."""
    return maximum_filter(img, size=size)


def filter_min(img, size: int = 3):
    """Bueno para ruido tipo sal."""
    return minimum_filter(img, size=size)


def filter_midpoint(img, size: int = 3):
    """Promedio de máximo y mínimo; bueno para gaussiano/uniforme."""
    mx = maximum_filter(img, size=size).astype(int)
    mn = minimum_filter(img, size=size).astype(int)
    return ((mx + mn) // 2).astype(img.dtype)
