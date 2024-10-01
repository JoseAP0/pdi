from PIL import Image, ImageDraw, ImageEnhance
from skimage import measure

#Abrir a imagem imagem
Image.open('/mama_contorno1.jpg')

#Converter a imagem em escala de cinza 
imagem_cinza imagem.convert('L')

#Converter a iamgem em uma matriz numpy
matriz_imagem = np.array(imagem_cinza)

#Detectar os contornos 
contornos = measure.find_contours(matriz_imagem, 0.8)

#Desenhar os contornos na imagem original 
desenhar = ImageDraw.Draw(imagem)

for contorno in contornos:
  for i in range(len(contorno) 1):
    desenhar.line((contorno [i][1], contorno [i][0], contorno [i+1][1], contorno [i+1][0]),   fill='red', width=2)

#Aumentar o contraste
realcar = ImageEnhance.Contrast(imagem)
imagem = realcar.enhance(15.5) 

#Mostrar a imagem com os contornos 
imagem.save('mama_contorno.jpg')
