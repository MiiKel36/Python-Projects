import cv2 as cv
import os
import time

def Restart():
    """
    Reinicia a captura de vídeo e encerra o script atual.
    """
    capVideo()
    exit()

def decidirLargura(frame):
    """
    Decide a escala para a largura desejada para o ASCII.
    Retorna a escala apropriada.
    """
    lar, alt = frame.shape

    for i in range(1, lar * alt):
        larCalc = int(frame.shape[1] * i / 100)
        altCalc = int(frame.shape[0] * i / 250)
        if desejoLargura <= larCalc:
            return i

def ascii(video):
    """
    Converte os frames de vídeo em caracteres ASCII.
    """
    ascii_art = []
    ASCII_CHARS = " .:-=+*#%@"
    ASCII_CHARS_LEN = len(ASCII_CHARS) - 1

    for i in range(len(video) - 1):
        getNum = (video[i] * ASCII_CHARS_LEN) / 255
        ascii_art.append(ASCII_CHARS[int(getNum)])

        if (i + 1) % largura == 0:
            ascii_art.append('\n')

    ascii_output = "".join(ascii_art)
    print(ascii_output)

def capVideo():
    """
    Captura o vídeo, converte em escala de cinza e redimensiona os frames para ASCII.
    """
    videoPath = ''
    capSrc = cv.VideoCapture(videoPath)
    global desejoLargura

    desejoLarguraINPUT = input('Escreva a largura desejada --> ').replace(" ", "")

    if not desejoLarguraINPUT.isdigit() or desejoLarguraINPUT == '':
        print('\033[1;31m\nAlgo deu errado, ou você colou um caracter que não é um número ou não colocou nada.\033[m\n')
        Restart()

    desejoLargura = int(desejoLarguraINPUT)

    while capSrc.isOpened():
        ret, frame = capSrc.read()
        if not ret:
            break

        cap = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        resizeVideo = resizeFrame(cap)

        global altura, largura
        altura, largura = resizeVideo.shape

        video = resizeVideo.reshape(altura * largura)

        ascii(video)

    capSrc.release()

def resizeFrame(frame):
    """
    Redimensiona o frame de acordo com a escala calculada.
    """
    scale = decidirLargura(frame)
    width = int(frame.shape[1] * scale / 100)
    height = int(frame.shape[0] * scale / 250)
    dim = (width, height)

    resized_frame = cv.resize(frame, dim, interpolation=cv.INTER_AREA)
    return resized_frame

# Inicia a captura de vídeo e conversão para ASCII
capVideo()
