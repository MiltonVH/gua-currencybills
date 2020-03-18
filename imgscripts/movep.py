import shutil
import random


src = 'C:/Users/toshiba/Documents/workspace/Identificador/dataset/train/cinco_rev/'
dst = 'C:/Users/toshiba/Documents/workspace/Identificador/dataset/test/cinco_rev/'

a = [i for i in range(1, 399)]

for i in range(148):
    b = random.choice(a)
    fuente = src + 'ima' + str(b) + '.jpg'
    destino = dst +'ima' + str(b) + '.jpg'
    shutil.move(fuente, destino)
    a.remove(b)
