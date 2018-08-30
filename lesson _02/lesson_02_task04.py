''' 4. Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры. '''

num = int(input('type in number of elements in range (1 -0.5 0.25 -0.125 ...): '))
first_element_in_range = 1
sum = 0
for i in range(num):
    sum += first_element_in_range
    first_element_in_range /= -2
print(sum)