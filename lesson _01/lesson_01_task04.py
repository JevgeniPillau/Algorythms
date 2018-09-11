'''4. Написать программу, которая генерирует в указанных пользователем границах:
случайное целое число;
случайное вещественное число;
случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.'''

from random import randint, random, uniform
print('returns random integer from2 user defined range')
int_from = int(input('range from - '))
int_to = int(input('range to - '))
int_result = randint(int_from, int_to)
print(int_result)
print()
print('returns random float number from user defined range')
float_from = float(input('range from - '))
float_to = float(input('range to - '))
float_result = round(uniform(float_from, float_to), 2)
print(float_result)
print()
print('returns random letter from user defined range')
start_range = ord(input('first letter: '))
print(start_range)
stop_range = ord(input('second letter: '))
print(stop_range)
letter = int(random() * (stop_range - start_range + 1)) + start_range
print(chr(letter))