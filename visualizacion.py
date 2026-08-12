import cv2
import numpy as np


def mostrar_frames(frame, ruidosa, restaurada, realzada, nombre_ruido, nombre_filtro):
    o_img = cv2.putText(frame.copy(), "1. Original", (15, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, 255, 2, cv2.LINE_AA)
    n_img = cv2.putText(ruidosa.copy(), f"2.: {nombre_ruido}", (15, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, 255, 2, cv2.LINE_AA)
    f_img = cv2.putText(restaurada.copy(), f"3.: {nombre_filtro}", (15, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, 255, 2, cv2.LINE_AA)
    r_img = cv2.putText(realzada.copy(), "4. Realzada", (15, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, 255, 2, cv2.LINE_AA)
    top_row = np.hstack((o_img, n_img))
    bottom_row = np.hstack((f_img, r_img))
    mosaico = np.vstack((top_row, bottom_row))
    cv2.namedWindow("Restauracion de Imagen (DIP)", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("Restauracion de Imagen (DIP)", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Restauracion de Imagen (DIP)", mosaico)


def esperar_tecla():
    return cv2.waitKey(1) & 0xFF
