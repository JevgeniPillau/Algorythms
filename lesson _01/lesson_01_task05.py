'''5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.'''

print('define range between user provided letters')
a = ord(input('first letter: '))
b = ord(input('second letter: '))
a = a - ord('a') + 1
b = b - ord('a') + 1
print(f'letters positions are {a} and {b}')
print(f'letters between {a} and {b}: ', abs(a-b)-1)