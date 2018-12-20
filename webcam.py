import cv2

def webcam(window_name='webcam'):
    """
    Habilita uso de webcam. Para finalizar pressione a tecla "q" minúscula (quit)
    Parâmetros
        window_name..: nome da janela de vídeo
    """
    
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cap = cv2.VideoCapture(0)
    
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1024)
    
    while True:
        _, frame = cap.read()
        cv2.imshow(window_name, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()