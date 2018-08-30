'''1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.'''



print('Program will return sum and product of multiply of numbers in three-digit number')
x = int(input('Insert three-digit number: '))
x = list(str(x))
xa = int(x[0])
xb = int(x[1])
xc = int(x[2])
s = xa+xb+xc
if xa or xb or xc !=0:
    m = xa*xb*xc
else:
    m = 0
print(f'product of multiply is: {m}')
print(f'sum of numbers is: {s}')
