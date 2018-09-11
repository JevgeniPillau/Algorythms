'''2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.

Например, пользователь ввёл A2 и C4F. 
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. 
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]. 
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''
from collections import deque
# import cProfile
#
# print('two functions that do sum and multiplication on hex numbers\n')

# without functions
######################
hex_num_1 = deque(input('insert 1-st hex number: '))
hex_num_2 = deque(input('\t\tinsert 2-nd hex number: '))
hex_num_1.extendleft('x0')
hex_num_2.extendleft('x0')
int_num_1 = int(''.join(hex_num_1), 16)
int_num_2 = int(''.join(hex_num_2), 16)
print('~' * 100)
print(f'inserted hex numbers in decimal view {int_num_1, int_num_2}')
sum_int = int_num_1 + int_num_2
mult_int = int_num_1 * int_num_2
sum_hex = 'x%X' % sum_int
mult_hex = 'x%X' % mult_int
print(f'decimal sum of {int_num_1} and {int_num_2} is {sum_int}')
print(f'decimal multiplication of {int_num_1} and {int_num_2} is {mult_int}')
# print(f'sum of {hex_num_1} and {hex_num_2} is {sum_hex} ')
# print(f'result of multiplication of {hex_num_1} and {hex_num_2} is {mult_hex}')
sum_hex = deque(sum_hex)
mult_hex = deque(mult_hex)
sum_hex.popleft()
mult_hex.popleft()
print(f'hex sum of two inserted hex numbers in {sum_hex}')
print(f'hex multiplication of two inserted hex numbers in {mult_hex}')
print('~' * 100)


# def do_hex_sum():
#     '''Return sum of two hex numbers in deque view'''
#     hex_num_1 = deque(input('insert 1-st hex number: '))
#     hex_num_2 = deque(input('\t\tinsert 2-nd hex number: '))
#     hex_num_1.extendleft('x0')
#     hex_num_2.extendleft('x0')
#     int_num_1 = int(''.join(hex_num_1), 16)
#     int_num_2 = int(''.join(hex_num_2), 16)
#     sum_int = int_num_1 + int_num_2
#     sum_hex = 'x%X' % int(sum_int)
#     sum_hex = deque(sum_hex)
#     sum_hex.popleft()
#     return f'sum of two hex numbers in {sum_hex} view'
#
#
# res = do_hex_sum()
# print(res)

# cProfile.run('do_hex_sum()')

# insert 1-st hex number: a23e4
# 		insert 2-nd hex number: cc5f
#          15 function calls in 19.147 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   19.147   19.147 <string>:1(<module>)
#         2    0.000    0.000    0.000    0.000 codecs.py:319(decode)
#         1    0.000    0.000   19.147   19.147 lesson_05_task2.py:41(do_hex_sum)
#         2    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
#         1    0.000    0.000   19.147   19.147 {built-in method builtins.exec}
#         2   19.147    9.574   19.147    9.574 {built-in method builtins.input}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         2    0.000    0.000    0.000    0.000 {method 'extendleft' of 'collections.deque' objects}
#         2    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
#         1    0.000    0.000    0.000    0.000 {method 'popleft' of 'collections.deque' objects}


# insert 1-st hex number: a2
# 		insert 2-nd hex number: c7
#          15 function calls in 6.014 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    6.013    6.013 <string>:1(<module>)
#         2    0.000    0.000    0.000    0.000 codecs.py:319(decode)
#         1    0.000    0.000    6.013    6.013 lesson_05_task2.py:41(do_hex_sum)
#         2    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
#         1    0.000    0.000    6.014    6.014 {built-in method builtins.exec}
#         2    6.013    3.007    6.013    3.007 {built-in method builtins.input}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         2    0.000    0.000    0.000    0.000 {method 'extendleft' of 'collections.deque' objects}
#         2    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
#         1    0.000    0.000    0.000    0.000 {method 'popleft' of 'collections.deque' objects}




# def do_hex_mult():
#     '''Return sum of two hex numbers in deque collection'''
#     hex_num_1 = deque(input('insert 1-st hex number: '))
#     hex_num_2 = deque(input('\t\tinsert 2-nd hex number: '))
#     hex_num_1.extendleft('x0')
#     hex_num_2.extendleft('x0')
#     int_num_1 = int(''.join(hex_num_1), 16)
#     int_num_2 = int(''.join(hex_num_2), 16)
#     mult_int = int_num_1 * int_num_2
#     mult_hex = 'x%X' % int(mult_int)
#     mult_hex = deque(mult_hex)
#     mult_hex.popleft()
#     return f'multiplication of two hex numbers in {mult_hex} view'
#
#
# print(do_hex_mult())

# cProfile.run('do_hex_mult()')

# insert 1-st hex number: a23e4
# 		insert 2-nd hex number: cc5f
#          15 function calls in 27.219 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   27.219   27.219 <string>:1(<module>)
#         2    0.000    0.000    0.000    0.000 codecs.py:319(decode)
#         1    0.000    0.000   27.219   27.219 lesson_05_task2.py:101(do_hex_mult)
#         2    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
#         1    0.000    0.000   27.219   27.219 {built-in method builtins.exec}
#         2   27.219   13.610   27.219   13.610 {built-in method builtins.input}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         2    0.000    0.000    0.000    0.000 {method 'extendleft' of 'collections.deque' objects}
#         2    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
#         1    0.000    0.000    0.000    0.000 {method 'popleft' of 'collections.deque' objects}

# insert 1-st hex number: a2
# 		insert 2-nd hex number: c7
#          15 function calls in 4.090 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    4.090    4.090 <string>:1(<module>)
#         2    0.000    0.000    0.000    0.000 codecs.py:319(decode)
#         1    0.000    0.000    4.090    4.090 lesson_05_task2.py:101(do_hex_mult)
#         2    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
#         1    0.000    0.000    4.090    4.090 {built-in method builtins.exec}
#         2    4.090    2.045    4.090    2.045 {built-in method builtins.input}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         2    0.000    0.000    0.000    0.000 {method 'extendleft' of 'collections.deque' objects}
#         2    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
#         1    0.000    0.000    0.000    0.000 {method 'popleft' of 'collections.deque' objects}

