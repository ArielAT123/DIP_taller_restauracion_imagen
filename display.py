"""Etapa 5a: utilidades de visualización de las ventanas de video."""
import cv2


def show_frames(frame, ruidosa, restaurada, realzada, noise_name, filter_name):
    """Muestra las 4 etapas del proceso con etiquetas en las imágenes."""
    n_img = cv2.putText(ruidosa.copy(), f"Ruido: {noise_name}", (15, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, 255, 2, cv2.LINE_AA)
    f_img = cv2.putText(restaurada.copy(), f"Filtro: {filter_name}", (15, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, 255, 2, cv2.LINE_AA)
    cv2.imshow("1. Original", frame)
    cv2.imshow("2. Con Ruido", n_img)
    cv2.imshow("3. Restaurada", f_img)
    cv2.imshow("4. Realzada", realzada)


def wait_key():
    """Lee la tecla presionada (no bloqueante)."""
    return cv2.waitKey(1) & 0xFF
