import cv2

def show_video(video_path='', window_name='video'):
    """
    Exibe um vídeo. Para finalizar pressione a tecla "q" minúscula (quit).
    Parâmetros:
        video_path..: Path e nome do arquivo de vídeo
        window_name.: Nome da janela de exibição do vídeo
    """
    
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cap = cv2.VideoCapture(video_path)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 680)
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1024)
    
    while True:
        ok, frame = cap.read()
        if not ok: 
            break
        cv2.imshow(window_name, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
