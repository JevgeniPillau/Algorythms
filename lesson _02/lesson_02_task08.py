'''8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.'''

seq = int(input('how many sequences of numbers will be?: '))
num = int(input('what number i will count?: '))
counter = 0
for i in range(1, seq + 1):
    var = int(input(f'Sequence {str(i)}: '))
    while var > 0:
        if var % 10 == num:
            counter += 1
        var = var // 10

print(f'You have inserted {counter} number {num}')
