'''9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).'''

a = int(input('first number is: '))
b = int(input('second number is: '))
c = int(input('third number is: '))
if c < b < a or a < b < c:
    print('second number in the middle')
elif a < c < b or b < c < a:
    print('third number in middle')
elif b < a < c or c < a < b:
    print('first number in middle')
else:
    print('two or all of numbers are even')