import cv2
from capture import get_camera, read_frame, release_camera
from pipeline import CONFIGS
from enhancement import sharpen
from display import show_frames, wait_key

def main():
    cap = get_camera()
    idx, last_key = 0, 255
    print("Teclas -> [n] cambiar ruido, [q] salir")
    while True:
        frame = read_frame(cap)
        if frame is None:
            break
        n_name, n_func, f_name, f_func = CONFIGS[idx]
        ruidosa = n_func(frame)
        restaurada = f_func(ruidosa)
        realzada = sharpen(restaurada)
        show_frames(frame, ruidosa, restaurada, realzada, n_name, f_name)
        key = wait_key()
        if key == ord('q'):
            break
        if key == ord('n') and last_key != ord('n'):
            idx = (idx + 1) % len(CONFIGS)
        last_key = key
    release_camera(cap)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
