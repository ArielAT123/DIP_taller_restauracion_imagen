from ruido_impulsivo import agregar_ruido_sal, agregar_ruido_pimienta, agregar_ruido_sal_pimienta
from ruido_continuo import agregar_ruido_uniforme, agregar_ruido_gaussiano
from filtros_orden import filtro_mediana, filtro_minimo, filtro_maximo, filtro_punto_medio
from filtros_media import filtro_media_aritmetica, filtro_contra_armonico

CONFIGURACIONES = [
    ("Sal (Minimo)", agregar_ruido_sal, "Minimo", filtro_minimo),
    ("Pimienta (Maximo)", agregar_ruido_pimienta, "Maximo", filtro_maximo),
    ("Sal y Pimienta (Mediana)", agregar_ruido_sal_pimienta, "Mediana", filtro_mediana),
    ("Uniforme (Punto Medio)", agregar_ruido_uniforme, "Punto Medio", filtro_punto_medio),
    ("Gaussiano (Media)", agregar_ruido_gaussiano, "Media Aritmetica", filtro_media_aritmetica),
    ("Sal (Contra-armonico)", agregar_ruido_sal, "Contra-armonica (R=-1.5)", lambda x: filtro_contra_armonico(x, r=-1.5)),
    ("Pimienta (Contra-armonico)", agregar_ruido_pimienta, "Contra-armonica (R=1.5)", lambda x: filtro_contra_armonico(x, r=1.5)),
]

