'''6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.'''

from random import random

arr_length = int(input('Please insert desired array length\n'
                       'in range from 3 to 25: '))                               # user input for array length
print()
array = [0] * arr_length                                                         # generate an array
for i in range(arr_length):
    array[i] = int(random()*50)
    print(f'{array[i]}', end=' ')
print()

min_id = 0
max_id = 0
for i in range(1,arr_length):
    if array[i] < array[min_id]:
        min_id = i
    elif array[i] > array[max_id]:
        max_id = i
print(f'minimal number in array = {array[min_id]}\n'
      f'maximal number in array = {array[max_id]}')

if min_id > max_id:
    min_id, max_id = max_id, min_id

elements_sum = 0
for i in range(min_id+1, max_id):
    elements_sum += array[i]
print(f'sum of elements between min and max  = {elements_sum}')
