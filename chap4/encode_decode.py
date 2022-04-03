s = 'café'
print(len(s))  # Строка 'café' состоит из четырех символов Unicode

b = s.encode('utf8')  # Преобразуем str в bytes, пользуясь кодировкой UTF-8
print(b)  # Литералы типа bytes начинаются префиксом b
print(len(b))  # Объект b типа bytes состоит из пяти байто

b.decode('utf8')  # Преобразуем bytes обратно в str, пользуясь кодировкой UTF-8

cafe = bytes('café', encoding='utf_8')  # bytes можно получить из str, если известна кодировка
print(cafe)

print(cafe[0])  # Каждый элемент - целое число в диапазоне range(256)
print(type(cafe[:1]))  # Срезы bytes также имеют тип bytes, даже если срез состоит из одного байта



