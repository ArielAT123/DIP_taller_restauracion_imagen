import cv2


def mostrar_frames(frame, ruidosa, restaurada, realzada, nombre_ruido, nombre_filtro):
    n_img = cv2.putText(ruidosa.copy(), f"Ruido: {nombre_ruido}", (15, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, 255, 2, cv2.LINE_AA)
    f_img = cv2.putText(restaurada.copy(), f"Filtro: {nombre_filtro}", (15, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, 255, 2, cv2.LINE_AA)
    cv2.imshow("1. Original", frame)
    cv2.imshow("2. Con Ruido", n_img)
    cv2.imshow("3. Restaurada", f_img)
    cv2.imshow("4. Realzada", realzada)


def esperar_tecla():
    return cv2.waitKey(1) & 0xFF
