# Массивы
# Создание, сохранение и загрузка большого массива чисел с плавающей точкой

from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))  # Создать массив чисел с плавающей точкой двойной точности.
print(floats[-1])
fp = open('floats.bin', 'wb')
floats.tofile(fp)  # Сохранить массив в двоичном файле.
fp.close()
floats2 = array('d')  # Создать пустой массив чисел с плавающей точкой двойной точности.
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)  # Прочитать 10 миллионов чисел из двоичного файла.
fp.close()
print(floats2[-1])
print(floats2 == floats)

