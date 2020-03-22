from collections import namedtuple
from pathlib import Path

ftrain = Path(Path.cwd().parent.__str__()) / 'train'
ftest = Path(Path.cwd().parent.__str__()) / 'test'


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
