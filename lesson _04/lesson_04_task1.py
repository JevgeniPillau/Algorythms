'''1. Проанализировать скорость и сложность одного - трёх любых алгоритмов, разработанных в рамках домашнего
задания первых трех уроков.'''

'''6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.'''

from random import randrange
import cProfile


def build_array(arr_length):
    array = [0] * arr_length
    for i in range(arr_length):
        array[i] = int(randrange(0, 1000))
#        print(f'{array[i]}', end=' ')
    return array


cProfile.run('build_array(100000000)')

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

