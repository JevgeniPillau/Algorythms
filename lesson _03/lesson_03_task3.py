'''3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.'''

print('interchange minimal and maximal elements in array')

from random import random

arr_length = int(input('Please insert desired array length\n'
                       'in range from 3 to 10: '))                               # user input for array length
print()
array = [0] * arr_length                                                         # generate an array
for i in range(arr_length):                                                      # for each empty element in array
    array[i] = int(random() * 100)                                               # fill array with random number
    print(array[i], end=' ')                                                     # print out filled array

index_min = array.index(min(array))                                              # define min index in array
index_max = array.index(max(array))                                              # define max index in array
print('\n\narray indexes count start from 0')
print(f'array minimum number {min(array)} has index {index_min + 1}\n'           # f string with indexes increase
      f'array maximum number {max(array)} has index {index_max + 1}\n')
array[index_min], array[index_max] = array[index_max], array[index_min]          # swap min, max to max, min

for i in range(arr_length):
    print(array[i], end=' ')
print()
