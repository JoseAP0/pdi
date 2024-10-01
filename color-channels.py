import numpy as np

imagem = cv2.imread('cavalo.jpg')
cv2.imshow('cavalo', imagem)

azul, verde, vermelho = cv2.split(imagem)

imagem_mesclada = cv2.merge((azul, verde, vermelho))

imagem_invertida = cv2.merge((vermelho, verde, azul))

blank = np.zeros(imagem.shape[:2], dtype='uint8')

canal_azul = cv2.merge([azul,blank,blank])
canal_azul_gimp = cv2.merge([azul,azul,azul])
canal_verde = cv2.merge([blank,verde,blank])
canal_verde_gimp = cv2.merge([verde,verde,verde])
canal_vermelho = cv2.merge([blank,blank,vermelho])
canal_vermelho_gimp = cv2.merge([vermelho,vermelho,vermelho])

cv2.imwrite('Azul.png', canal_azul)
cv2.imshow('Azul.png', canal_azul)
cv2.imwrite('Azul_gimp.png', canal_azul_gimp)
cv2.imshow('Azul_gimp.png', canal_azul_gimp)
cv2.imwrite('Verde.png', canal_verde)
cv2.imshow('Verde.png', canal_verde)
cv2.imwrite('Verde_gimp.png', canal_verde_gimp)
cv2.imshow('Verde_gimp.png', canal_verde_gimp)
cv2.imwrite('Vermelho.png', canal_vermelho)
cv2.imshow('Vermelho.png', canal_vermelho)
cv2.imwrite('Vermelho_gimp.png', canal_vermelho_gimp)
cv2.imshow('Vermelho_gimp.png', canal_vermelho_gimp)
cv2.imwrite("imagem_mesclada.png", imagem_mesclada)
cv2.imshow("imagem_mesclada.png", imagem_mesclada)
cv2.imwrite("imagem_invertida.png", imagem_invertida)
cv2.imshow("imagem_invertida.png", imagem_invertida)
