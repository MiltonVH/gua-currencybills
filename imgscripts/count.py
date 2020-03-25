
from collections import namedtuple
from pathlib import Path
import cv2

ftrain = Path(Path.cwd().parent.__str__()) / 'train'
ftest = Path(Path.cwd().parent.__str__()) / 'test'
odata = Path(Path.cwd().parent.parent.__str__()) / 'odata'


def loadImgInfo(path):
    lista = []
    img_id = 0
    imgdata = namedtuple(
        'imgdata', ['path', 'id', 'label'])

    for clases in path.glob('*'):
        for img in clases.glob('*'):
            lista.append(imgdata(img.__str__(),
                                 img_id, clases.name))
        img_id += 1
    return lista


def reziseImage(origin, dest):
    img = cv2.imread(origin)
    rows, cols, d = img.shape
    if rows > cols:
        img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    if cols > 1080:
        aux = cv2.resize(img, None, fx=0.7, fy=0.7)
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


data = loadImgInfo(odata)
print(len(data))
detector = cv2.AKAZE_create()
# img = cv2.imread('C:/Users/toshiba/Desktop/odata2/cinco_back_o/ima8.jpg')
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# kp, des = detector.detectAndCompute(gray_img, None)

# res = cv2.drawKeypoints(img, kp, None, color=(
#     0, 255, 0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# cv2.imshow('res', res)

# while True:
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cv2.destroyAllWindows()


for i in data:
    image = cv2.imread(i.path)
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    kp, des = detector.detectAndCompute(gray_img, None)

    if des is None:
        print(i.path)

# for i in aux2:
#     path = 'C:\\Users\\toshiba\\Desktop\\odata2\\image_net\\' + i.name
#     reziseImage(str(i), path)
