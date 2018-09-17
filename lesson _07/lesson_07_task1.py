'''1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Вывести на экран исходный и отсортированный массивы.'''

import random

array = [i for i in range(-100, 100)]                               # generate array, range from -100 to 100(not included)
random.shuffle(array)                                               # shuffle generated array randomly
print(f'initial unsorted array in range [-100, 100):\n{array}')
last_num = len(array) - 1                                           # define last number to compare
# print(len(array))
first_num = len(array) - last_num                                   # calculate first number to compare
last_index = len(array)                                             # define last interchange index
while first_num < last_num:                                         # while first num is less than last num:

    for i in range(last_num, first_num - 1, -1):                    # from last number to first number-1, with step -1
        if array[i - 1] > array[i]:                                 # if array item i-1 greater than array item
            array[i - 1], array[i] = array[i], array[i - 1]         # make items interchange
            last_index = i                                          # last index equals to item, for pair of elements
            # with lesser last index
    first_num = last_index                                          # and first num equals to last index

    for i in range(first_num, last_num + 1, +1):                    # from first number to last number +1, step +1
        if array[i - 1] > array[i]:
            array[i - 1], array[i] = array[i], array[i - 1]
            last_index = i
    last_num = last_index

print(f'sorted initial array:\n{array}')
