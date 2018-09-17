'''2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
'''


import random


def sort_by_merge(array):
    '''sort array by merge with recursion'''

    if len(array) > 1:
        center = len(array) // 2                            # divide array in two
        left = array[:center]                               # define left side using slice
        right = array[center:]                              # define right side using slice

        sort_by_merge(left)                                 # recursively call sort function for left side of array
#        print(f'left side of {array}')
        sort_by_merge(right)                                # the same for right side
#        print(f'right side of {array}')

        index, jodex, kodex = 0, 0, 0                       # indexes to compare and interchange

        while index < len(left) and jodex < len(right):
            if left[index] < right[jodex]:
                array[kodex] = left[index]
                index += 1
            else:
                array[kodex] = right[jodex]
                jodex += 1
            kodex += 1

        while index < len(left):
            array[kodex] = left[index]
            index += 1
            kodex += 1

        while jodex < len(right):
            array[kodex] = right[jodex]
            jodex += 1
            kodex += 1


array = [i for i in range(0, 50)]
random.shuffle(array)
print(f'initial unsorted array in range [0, 50):\n{array}')

sort_by_merge(array)
print(f'sorted initial array {array}')
