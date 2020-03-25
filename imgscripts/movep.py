import glob
import shutil
import random


dest = (
    'cinco_an',
    'cinco_rev',
    'diez_an',
    'diez_rev',
    'veinte_an',
    'veinte_rev'
)

source = (
    'cinco_front_o',
    'cinco_back_o',
    'diez_front_o',
    'diez_back_o',
    'veinte_front_o',
    'veinte_back_o'
)

src = '../../odata/'
train = '../train/'
test = '../test/'
nouse = '../nouse/'

train_number = 250
test_number = 30

for i in range(len(source)):
    clase = glob.glob(src + source[i] + '/*.jpg')

    for j in range(train_number):
        a = random.choice(clase)
        b = train + dest[i] + '/' + a.split('\\')[-1]
        shutil.move(a, b)
        clase.remove(a)

    for j in range(test_number):
        a = random.choice(clase)
        b = test + dest[i] + '/' + a.split('\\')[-1]
        shutil.move(a, b)
        clase.remove(a)

    for a in clase:
        b = nouse + dest[i] + '/' + a.split('\\')[-1]
        shutil.move(a, b)

        # for i in a:
        #     b = random.choice(a)
        #     fuente = src + 'img' + str(b) + '.jpg'
        #     destino = dst + 'ima' + str(b) + '.jpg'
        #     shutil.move(fuente, destino)
        #     a.remove(b)
