''' 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться
при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя. '''

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
