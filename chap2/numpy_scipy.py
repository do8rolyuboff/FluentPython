# Простые операции со строками и столбцами из модуля numpy.ndanay
import os
import random

import numpy
a = numpy.arange(12)  # Построить и распечатать массив ndarray, содержащий целые числа от 0 до 11.
print(a, type(a))
print(a.shape)
a.shape = 3, 4  # Изменить форму массива, добавив еще одно измерение, затем распечатать результат.
print(a)
print(a[2])
print(a[1, 2])
print(a[:, 1])
print(a.transpose())  # Создать новый массив, транспонировав исходный.


# NumPy также поддерживает загрузку, сохранение и применение операций сразу ко всем элементам массива numpy.ndarray:


if not os.path.isfile('floats-10M-lines.txt'):
	with open('floats-10M-lines.txt', 'w') as file:
		for idx in range(10000):  #
			print("{}".format(str(random.random())), file=file)

floats = numpy.loadtxt('floats-10M-lines.txt')
print(floats[-3:])
floats *= .5
print(floats[-3:])
from time import perf_counter as pc
stime = pc()
floats /= 3
etime = pc()
print("stime: {}; etime: {}; elapsed: {}".format(stime, etime, etime-stime))
numpy.save('floats.bin', floats)
floats2 = numpy.load('floats.bin.npy', 'r+')
floats2 *= 6
print("floats2[-3:]: {}".format(floats2[-3:]))