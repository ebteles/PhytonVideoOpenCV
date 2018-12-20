import os
import cv2

def frame_to_video(path_input, num_max_frames=0, files=[], verbose=False):
    """
    Compõe vídeo a partir de um conjunto de imagens sequencialmente numeradas em uma pasta.
    O resultado é gravado na pasta 'video_output' dentro de "path_input
    Parâmetros:
        path_input....: pasta contendo imagens sequencialmente numeradas (.jpg)
        num_max_frames: número máximo de frames a ser considerado na composição do vídeo.
                        Se valor for zero (0), considera todos os frames (imagens) da pasta
                        de entrada
        files.........: lista de imagens pré-carregadas
        verbose.......: quanto True: exibe mensagens de acompanhamento do processo.
    """

    if len(files) > 0:
        list_files = files
    else:
        list_files = [f for f in os.listdir(path_input) if f.endswith('.jpg')]
        list_files.sort()

    path_output = os.path.join(path_input, 'video_output')
    if os.path.exists(path_output):
        for f in os.listdir(path_output):
            file = os.path.join(path_output, f)
            if os.path.isfile(file):
                os.unlink(file)
    else:
        os.makedirs(path_output)

    img0 = cv2.imread(os.path.join(path_input, list_files[0]))
    height, width, layers = img0.shape
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    
    saida = cv2.VideoWriter(os.path.join(path_output,'video.avi'), fourcc, 20.0, (width, height)) 

    frames_count = 0
    for f in list_files:
        if verbose and frames_count % 10 == 0:
            print('Frames: {}'.format(frames_count))
        img = cv2.imread(os.path.join(path_input, f))
        saida.write(img)
        frames_count += 1
        if num_max_frames == 0:
            continue
        if frames_count >= num_max_frames:
            break
        if cv2.waitKey(1) == 27:
            if verbose:
                print('Processo interrompido. Tecla [ESC] foi pressionada!')
            break
    if verbose:
        print('salvando {}...'.format(frames_count))
        print('fim')

    saida.release()
    cv2.destroyAllWindows()