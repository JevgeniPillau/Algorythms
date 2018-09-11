'''1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Для анализа возьмите любые 1-3 ваших программы. Результаты анализа вставьте в виде комментариев к коду.
P.S. Напишите в комментариях версию Python и разрядность ОС.'''

'''from lesson_02_task1'''

while True:
    print()
    try:
        a = int(input('first number: '))
        b = int(input('second number: '))
    except ValueError:
        print('please type in number, you inserted something else')
    c = str(input('operation symbol: '))
    oper_symbols = ('0', '+', '-', '*', '/')
    print()
    if c == '0':
        break
    else:
        if c in oper_symbols:
            if c == '+':
                d = a + b
                print(f'sum of {a} and {b} = ', d)
            elif c == '-':
                d = a - b
                print(f'difference of {a} and {b} = ', d)
            elif c == '*':
                d = a * b
                print(f'result of multiplication of {a} and {b} = ', d)
            elif c == '/':
                if b == 0:
                    print('division on zero is not allowed')
                else:
                    d = a / b
                    print(f'division of {a} and {b} = ', d)
        else:
            print('Please type correct operation symbol: + or - or / or *')