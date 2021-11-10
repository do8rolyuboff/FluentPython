fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits))  # Порождает новый список строк, отсортированный в алфавитном порядке.
print(fruits)  # Инспекция исходного списка показывает, что он не изменился.
sorted(fruits, reverse=True)  # Это сортировка в обратном алфавитном порядке.
sorted(fruits, key=len)  # Новый список строк, отсортированный уже по длине.
fruits.sort()  # Этот метод сортирует список на месте и возвращает -> None
print(fruits)  # Теперь массив fruits отсортирован.
