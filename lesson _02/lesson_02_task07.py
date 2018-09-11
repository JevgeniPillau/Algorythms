'''7. Написать программу, доказывающую или проверяющую,
что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n – любое натуральное число.'''

print('prove that 1+2+...+n = n(n+1)/2 equation is true')
number = int(input('type in a number: '))
eq_left_side = 0
for i in range(1, number + 1):
    eq_left_side += i
eq_right_side = number * (number + 1) // 2
print(eq_left_side)
print(eq_right_side)