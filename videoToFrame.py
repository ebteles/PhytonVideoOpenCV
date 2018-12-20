import os
import cv2

def video_to_frame(video_input, path_output='', ms_interval=0, verbose=False):
    """
    Desmembra um vídeo em frames
    Parâmetros:
        video_input..: path + nome do arquivo de video
        path_output..: path de destino. Se não informado assume o path do vídeo, subpasta "video_output"
        ms_interval..: intervalo entre frames em milissegundos. Se não informado assume valor 0, ou seja, 
                       vai gravar todos os frames
        verbose......: quanto True: exibe mensagens de acompanhamento do processo.
    """
    path_output = path_output.strip()
    if path_output == '':
        path_output = os.path.join(os.path.dirname(path_video), 'video_output')

    if os.path.exists(path_output):
        for f in os.listdir(path_output):
            file = os.path.join(path_output, f)
            if os.path.isfile(file):
                os.unlink(file)
    else:
        os.makedirs(path_output)

    counter = 0
    tempo = 0.0
    cam = cv2.VideoCapture(video_input)

    while True:
        flag, frame = cam.read()
        if flag:
            cv2.imwrite(os.path.join(path_output, '{:0>8}.jpg'.format(counter)), frame)
            counter += 1
            if verbose and counter % 10 == 0:
                print('Frames: {}'.format(counter))
        else:
            if  verbose:
                print('Frames: {}'.format(counter))
                print('Fim')
            break

        if cv2.waitKey(1) == 27:
            if verbose:
                print('Processo interrompido. Tecla [ESC] foi pressionada!')
            break

        if ms_interval > 0:
            if verbose:
                print('Tempo = {}'.format(tempo))
            tempo += ms_interval
            cam.set(cv2.CAP_PROP_POS_MSEC, tempo)

    cv2.destroyAllWindows()