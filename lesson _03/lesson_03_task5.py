'''5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.'''

from random import random

arr_length = int(input('Please insert desired array length\n'
                       'in range from 5 to 50: '))
array = []
for i in range(arr_length):
    array.append(int(random() * 100) - 50)
print(array)

i = 0
index = -1
while i < arr_length:
    if array[i] < 0 and index == -1:
        index = i
    elif array[i] < 0 and array[i] > array[index]:
        index = i
    i += 1

print(index + 1, ':', array[index])
