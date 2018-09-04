'''1. Проанализировать скорость и сложность одного - трёх любых алгоритмов, разработанных в рамках домашнего
задания первых трех уроков.'''

'''6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.'''

from random import randrange
import cProfile


def gen_array(arr_length):

    array = [0] * arr_length
    for i in range(arr_length):
        array[i] = int(randrange(0, 10000))
#        print(f'{array[i]}', end=' ')
    return array


new_array = gen_array(10)
print(new_array)


# def seek_min_max():
#     min_id = 0
#     max_id = 0
#     for j in range(1, new_array):
#         if new_array[j] < new_array[min_id]:
#             min_id = j
#         elif new_array[j] > new_array[max_id]:
#             max_id = j
# #    print(f'minimal number in array = {new_array[min_id]}\n'
# #          f'maximal number in array = {new_array[max_id]}')
#         if min_id > max_id:
#             min_id, max_id = max_id, min_id
#     return min_id, max_id
#
#
# print(seek_min_max())

#
#     elements_sum = 0
#     for i in range(min_id+1, max_id):
#         elements_sum += array[i]
# #    print(f'sum of elements between min and max  = {elements_sum}')
#     return elements_sum
#
#
# res_array = sum_between_min_max(1000)
# print(f'sum of elements between min and max  = {res_array}')

cProfile.run(gen_array)

[1835, 353, 8716, 1904, 7301, 5190, 5602, 4567, 5290, 1406]
Traceback (most recent call last):
  File "/home/jp/PycharmProjects/Algorythms/lesson _04/lesson_04_task1.py", line 52, in <module>
    cProfile.run(gen_array)
  File "/usr/lib/python3.7/cProfile.py", line 16, in run
    return _pyprofile._Utils(Profile).run(statement, filename, sort)
  File "/usr/lib/python3.7/profile.py", line 53, in run
    prof.run(statement)
  File "/usr/lib/python3.7/cProfile.py", line 95, in run
    return self.runctx(cmd, dict, dict)
  File "/usr/lib/python3.7/cProfile.py", line 100, in runctx
    exec(cmd, globals, locals)
TypeError: exec() arg 1 must be a string, bytes or code object
         2 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


