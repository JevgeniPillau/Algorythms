'''4. Определить, какое число в массиве встречается чаще всего.'''

from random import random

arr_length = int(input('Please insert desired array length\n'
                       'in range from 5 to 50: '))                               # user input for array length
print()
array = [[0] * arr_length for i in range(arr_length)]                            # generate an array
for i in range(arr_length):
    array[i] = int(random() * 20)
print(array)

number = array[0]
max_frequency = 1
for i in range(arr_length - 1):
    frequency = 1
    for k in range(i + 1, arr_length):
        if array[i] == array[k]:
            frequency += 1
    if frequency > max_frequency:
        max_frequency = frequency
        number = array[i]

if max_frequency > 1:
    print(f'{number} appears in array {max_frequency} times')
else:
    print('All elements of array are unique')