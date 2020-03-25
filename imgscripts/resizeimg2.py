import cv2


def reziseImage(origin, dest):
    img = cv2.imread(origin)
    rows, cols, d = img.shape
    if cols > 1080:
        aux = cv2.resize(img, None, fx=0.5, fy=0.5)
        if cols == rows:
            dst = cv2.resize(aux, (320, 320))
        else:
            dst = cv2.resize(aux, (320, 240))
    else:
        if cols == rows:
            dst = cv2.resize(img, (320, 320))
        else:
            dst = cv2.resize(img, (320, 240))
    cv2.imwrite(dest, dst)
