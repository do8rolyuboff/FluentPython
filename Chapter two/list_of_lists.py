# Построение списка списков
board = [['_'] * 3 for i in range(3)]
board[0][2] = 'X'
print(board)

# Ошибочный короткий путь
weird_board = [['_'] * 3] * 3
weird_board[1][2] = '0'
print(weird_board)

# Составное присваивание последовательностей
my_list = [1, 2, 3]
print(id(my_list))
my_list *= 2
print(id(my_list))
my_tuple = (1, 2, 3)
print(id(my_tuple))
my_tuple *= 2
print(id(my_tuple))

