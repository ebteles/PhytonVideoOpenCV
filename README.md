# PhytonVideoOpenCV

Conjunto de funcionalidades em python para se trabalhar com vídeo usando OpenCV

### Instalação

conda install opencv
```sh
conda install -c conda-forge opencv
```

### Exemplos 1:
Como exbir um vídeo:
```python
import showVideo as vd
path = './video/video.mp4'
vd.show_video(path) # pressione a letra "q" minúscula para interromper (q = quit)
print('FIM')
```
### Exemplos 2:
Como capturar a webcam
```python
import webcam as wc
wc.webcam() # pressione a letra "q" minúscula para interromper (q = quit)
print('FIM')
```

### Exemplos 3:
Como converter um vídeo em uma sequência de imagens
```python
import videoToFrame as vf
entrada = './video/video.mp4'
saida = './images'
vf.video_to_frame(entrada, saida, verbose=True)
print('FIM')
```

### Exemplos 4:
Como converter uma sequencia de imagens em um vídeo

```python
import frameToVideo as fv
entrada = './images'
fv.frame_to_video(entrada, verbose=True)
```
License
----

MIT
**Free Software, Hell Yeah!**
