'''2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).'''

print('count even and odd numbers in sequence')

evens_counter = 0
odds_counter = 0

num = int(input('type in number: '))

while num != 0:
    if num % 2 == 0:
        evens_counter += 1
    else:
        odds_counter += 1
    num = num // 10

print(f'in yor number evens are {evens_counter} and odds are {odds_counter}')