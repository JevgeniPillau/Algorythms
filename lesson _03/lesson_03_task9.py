'''9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.'''

from random import random

columns = 10
rows = 5
array = []
for i in range(rows):
    array_new = []
    for j in range(columns):
        number = int(random() * 100)
        array_new.append(number)
        print(f'{number}', end=' ')
    array.append(array_new)
    print()

maximal_num = -1
for j in range(columns):
    minimal_num = 100
    for i in range(rows):
        if array[i][j] < minimal_num:
            minimal_num = array[i][j]
    if minimal_num > maximal_num:
        maximal_num = minimal_num
print(f'Максимальное число среди минимальных: {maximal_num}')