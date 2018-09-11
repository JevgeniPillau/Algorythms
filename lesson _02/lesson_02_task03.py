''' 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843. '''

print('reverse number inserted by user')
num = int(input('type in number to reverse: '))
rev_num = 0
while num > 0:
    rev_num = rev_num*10 + num % 10
    num = num//10
print(f'result of reverse is {rev_num}')
