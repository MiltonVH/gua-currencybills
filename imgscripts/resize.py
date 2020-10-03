

from collections import namedtuple
from pathlib import Path
import random
import cv2

ftrain = Path(Path.cwd().parent.__str__()) / 'train'
fval = Path(Path.cwd().parent.__str__()) / 'val'
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
random.shuffle(data)

destino = odata / 'doscientos_rev/img'

count = 1
for img in data:
    if img.label == 'web_200_rev':
        reziseImage(img.path, str(destino) + str(count) + '.jpg')
        count += 1
