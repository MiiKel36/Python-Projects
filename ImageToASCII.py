import cv2 as cv
import os
import time
import sys


#if has an error on the errorLargura Inputs just restart from ascii
def Restart():
    ascii()
    exit() #close the firts def to open a new


def decidirLargura(image): #decide the width for the ascii
    desejoLarguraINPUT = input('Escreva a largura desejada --> ').replace(" ", "")

    # verfy if has any character that's not a number
    if not desejoLarguraINPUT.isdigit() or desejoLarguraINPUT == None:
        print('\033[1;31m\nAlgo deu errado, ou você colou um caracter que não é um numero ou nao colocou nada \033[m','\n')
        Restart()

    desejoLargura = int(desejoLarguraINPUT)

    lar ,alt = image.shape

    #find the best scle for the width that the user want
    for i in range(1, lar*alt):
        larCalc = int(image.shape[1] * i / 100)
        altCalc = int(image.shape[0] * i/ 250)

        if desejoLargura <= larCalc:
            return i
            break

#resize image
def resizeImage(image):
    scale = decidirLargura(image) #call the func to find the scale
    width = int(image.shape[1] * scale / 100 ) #rewitre the W based on the finded scale
    height = int(image.shape[0] * scale / 250 ) #rewitre the H based on the finded scale
    dim = (width, height)
    print(scale, '-- scale')

    resizeImage = cv.resize(image, dim, interpolation = cv.INTER_AREA) #resize the image
    return resizeImage

#take the image
def imageSrc():
    '''
    Para que funcione, é necessario criar uma pasta no mesmo lugar que se encotra este código, colocar
    sua imagem dentro desta pasta, e quando rodar o app, escrever o nome da imagem e seu formato
    '''
    imagemAsk = input("qual arquivo de imagem vai abrir -->  ")
    imagemkk = "imagem\ "+ imagemAsk
    image_src = cv.imread(imagemkk.replace(" ",""), cv.IMREAD_GRAYSCALE) #search the image on the image folder

    imagem = resizeImage(image_src) #call the func to resize the image

    # take the W and H
    global altura, largura
    altura, largura = imagem.shape
    print(largura, largura, '-- altura, largura')

    return imagem.reshape(altura * largura) #return a array of a single dimension

#create ascii
def ascii():

    ascii = [] #save the ascii characters
    ASCII_CHARS = " .:-=+*#%@" #characters of  garyscale ascii
    ASCII_CHARS_LEN = len(ASCII_CHARS)-1 #len of the var

    image = imageSrc() #call the func of the image

#print the asci
    for i in range(altura * largura):
         getNum = (image[i] * ASCII_CHARS_LEN) / 255
         ascii += ASCII_CHARS[int(getNum)]

         print(ascii[i], end='')
         if (i + 1) % largura == 0:
          print()


ascii()
input()


