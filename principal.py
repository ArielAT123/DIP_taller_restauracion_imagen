import cv2
from captura import obtener_camara, leer_frame, liberar_camara
from flujo import CONFIGURACIONES
from realzado import realzar
from visualizacion import mostrar_frames, esperar_tecla


def principal():
    cap = obtener_camara()
    idx, ultima_tecla = 0, 255
    print("Teclas -> [n] cambiar ruido, [q] salir")
    while True:
        frame = leer_frame(cap)
        if frame is None:
            break
        nombre_ruido, funcion_ruido, nombre_filtro, funcion_filtro = CONFIGURACIONES[idx]
        ruidosa = funcion_ruido(frame)
        restaurada = funcion_filtro(ruidosa)
        realzada = realzar(restaurada)
        mostrar_frames(frame, ruidosa, restaurada, realzada, nombre_ruido, nombre_filtro)
        tecla = esperar_tecla()
        if tecla == ord('q'):
            break
        if tecla == ord('n') and ultima_tecla != ord('n'):
            idx = (idx + 1) % len(CONFIGURACIONES)
        ultima_tecla = tecla
    liberar_camara(cap)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    principal()
