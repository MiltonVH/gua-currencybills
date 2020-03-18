import cv2
import numpy as np

path_dir = 'C:/Users/toshiba/Documents/fotos/original/negativo_o/'

for i in range(1, 123):
    img = cv2.imread(path_dir + 'img (' + str(i) + ').jpg')
    rows, cols, d = img.shape
    if rows > cols:
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        rows, cols, d = img.shape

    if cols > 1080:
        aux = cv2.resize(img, None, fx=0.5, fy=0.5)
        dst = cv2.resize(aux, (320, 240))
    else:
        dst = cv2.resize(img, (320, 240))

    cv2.imwrite('im' + str(i) + '.jpg', dst)
