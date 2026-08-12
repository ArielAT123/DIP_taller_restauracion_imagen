from ruidos import agregar_ruido_sal, agregar_ruido_gaussiano
from filtros import filtro_minimo, filtro_media_aritmetica

CONFIGURACIONES = [
    ("Sal", agregar_ruido_sal, "Minimo", filtro_minimo),
    ("Gaussiano", agregar_ruido_gaussiano, "Media Aritmetica", filtro_media_aritmetica),
]


