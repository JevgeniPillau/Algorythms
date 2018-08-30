'''6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.'''


print('find a letter by position number in alphabet')
pos_num = int(input('position number: '))
pos_num = ord('a') + pos_num - 1
print('letter is - ', chr(pos_num))