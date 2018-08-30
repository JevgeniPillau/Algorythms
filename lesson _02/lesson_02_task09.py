'''9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.'''


print('define a maximum sum of sequence of numbers\n'
      'to see the result, please type in 0\n')
number = int(input('please type in a number: '))
max_sum = 0
max_elements = 0
while number != 0:
    elements = number
    summ = 0

    while number > 0:
        summ += number % 10
        number //= 10

    if summ > max_sum:
        max_sum = summ
        max_elements = elements
    number = int(input('please type in a number: '))


print(f'Sequence of numbers {max_elements} have maximum sum of numbers {max_sum}')