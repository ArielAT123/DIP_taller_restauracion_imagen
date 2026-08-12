from ruidos import (
    agregar_ruido_sal,
    agregar_ruido_pimienta,
    agregar_ruido_sal_pimienta,
    agregar_ruido_uniforme,
    agregar_ruido_gaussiano,
)
from filtros import (
    filtro_mediana,
    filtro_minimo,
    filtro_maximo,
    filtro_punto_medio,
    filtro_media_aritmetica,
    filtro_contra_armonico,
)

CONFIGURACIONES = [
    ("Sal ", agregar_ruido_sal, "Minimo", filtro_minimo),
    ("Pimienta ", agregar_ruido_pimienta, "Maximo", filtro_maximo),
    ("Sal y Pimienta ", agregar_ruido_sal_pimienta, "Mediana", filtro_mediana),
    ("Uniforme ", agregar_ruido_uniforme, "Punto Medio", filtro_punto_medio),
    ("Gaussiano ", agregar_ruido_gaussiano, "Media Aritmetica", filtro_media_aritmetica),
    ("Sal ", agregar_ruido_sal, "Contra-armonica (R=-1.5)", lambda x: filtro_contra_armonico(x, r=-1.5)),
]
