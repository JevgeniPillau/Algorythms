'''7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.'''

a = int(input('lenght of first segment: '))
b = int(input('lenght of second segment: '))
c = int(input('lenght of third segment: '))
if a <= b+c or b <= a+c or c <= a+b:
    print('with those segments triangle is not possible')
elif a == b == c:
    print('its equilateral triangle')
elif a == b or a == c or b == c:
    print('its isosceles triangle')
else:
    print('its a regular triangle')