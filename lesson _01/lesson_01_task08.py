'''8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.'''

print('Tool to determine if inserted year is leap-year')
year = int(input('insert year: '))
if year%4 != 0:
     print(year, '- is regular year')
elif year%100 == 0:
    if year%400 == 0:
        print(year,'- is leap-year')
    else:
         print(year, '- is regular year')
else:
    print(year, '- is leap-year')