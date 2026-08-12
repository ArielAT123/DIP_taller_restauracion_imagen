"""Etapa combinada: asocia cada ruido con su filtro de restauración ideal."""
from noise_impulsive import add_salt, add_pepper, add_salt_pepper
from noise_continuous import add_uniform, add_gaussian
from filters_order import filter_median, filter_min, filter_max, filter_midpoint
from filters_mean import filter_arithmetic_mean, filter_contraharmonic

CONFIGS = [
    ("Sal (Minimo)", add_salt, "Minimo", filter_min),
    ("Pimienta (Maximo)", add_pepper, "Maximo", filter_max),
    ("Sal y Pimienta (Mediana)", add_salt_pepper, "Mediana", filter_median),
    ("Uniforme (Punto Medio)", add_uniform, "Punto Medio", filter_midpoint),
    ("Gaussiano (Media)", add_gaussian, "Media Aritmetica", filter_arithmetic_mean),
    ("Sal (Contra-armonico)", add_salt, "Contra-armonica (Q=-1.5)", lambda x: filter_contraharmonic(x, q=-1.5)),
    ("Pimienta (Contra-armonico)", add_pepper, "Contra-armonica (Q=1.5)", lambda x: filter_contraharmonic(x, q=1.5)),
]
