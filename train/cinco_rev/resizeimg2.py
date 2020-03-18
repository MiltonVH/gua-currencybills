import cv2
import numpy as np


for i in range(1, 399):
    img = cv2.imread('C:/Users/toshiba/Documents/fotos/original/cinco_back_o/ima' + str(i) + '.jpg')
    rows, cols, d = img.shape

    if rows > cols:
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        rows, cols, d = img.shape

    if cols > 1080:
        aux = cv2.resize(img, None, fx=0.5, fy=0.5)
        img = cv2.resize(aux, (320, 240))
    elif cols > 320 and rows > 275:
        img = cv2.resize(img, (320, 240))

    cv2.imwrite('ima' + str(i) + '.jpg', img)
