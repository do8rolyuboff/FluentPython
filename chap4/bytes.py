cafe = bytes('café', encoding='utf_8')  # bytes можно получить из str, если известна кодировка
print(cafe)

print(cafe[0])  # Каждый элемент - целое число в диапазоне range(256)
print(type(cafe[:1]))  # Срезы bytes также имеют тип bytes, даже если срез состоит из одного байта

import array

numbers = array.array('h', [-2, -1, 0, 1, 2])  # Код типа 'h' означанет создание масива 16-разрядных целых
octets = bytes(numbers)  # В объекте octets хранится копия байтов, из которых составлены числа в массиве numbers
print(octets)  # 10 байтов, представляющих пять 16-разрядных целых
