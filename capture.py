"""Etapa 1: Captura de video desde la cámara."""
import cv2


def get_camera(index: int = 0) -> cv2.VideoCapture:
    """Abre la cámara indicada y valida que esté disponible."""
    cap = cv2.VideoCapture(index)
    if not cap.isOpened():
        raise RuntimeError("No se pudo abrir la cámara")
    return cap


def read_frame(cap: cv2.VideoCapture):
    """Lee un frame y lo retorna en escala de grises (None si falla)."""
    ok, frame = cap.read()
    if not ok:
        return None
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


def release_camera(cap: cv2.VideoCapture) -> None:
    """Libera el recurso de la cámara."""
    cap.release()
