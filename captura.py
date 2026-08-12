import cv2


def obtener_camara(indice: int = 0) -> cv2.VideoCapture:
    cap = cv2.VideoCapture(indice)
    if not cap.isOpened():
        raise RuntimeError("No se pudo abrir la cámara")
    return cap


def leer_frame(cap: cv2.VideoCapture):
    ok, frame = cap.read()
    if not ok:
        return None
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


def liberar_camara(cap: cv2.VideoCapture) -> None:
    cap.release()
