import cv2


for i in range(1, 187):
    img = cv2.imread('../../original/negativo_o/imagen' + str(i) + '.jpg')
    rows, cols, d = img.shape
    if cols == 1920:
        aux = cv2.resize(img, None, fx=0.5, fy=0.5)
        dst = cv2.resize(aux, (320, 320))
    elif cols == 1280:
        aux = cv2.resize(img, None, fx=0.5, fy=0.5)
        dst = cv2.resize(aux, (320, 240))
    else:
        dst = cv2.resize(img, (320, 240))
    cv2.imwrite('img' + str(i) + '.jpg', dst)
