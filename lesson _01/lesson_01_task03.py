'''3. По введенным пользователем координатам двух точек вывести уравнение прямой, проходящей через эти точки.'''

print('point A coordinates')
x1 = float(input('X1 = '))
y1 = float(input('Y1 = '))
 
print('point B coordinates')
x2 = float(input('X2 = '))
y2 = float(input('Y2 = '))
 
print('line equation according to coordinates given:')
k = (y1 - y2) / (x1 - x2)
b = y2 - k*x2
#print(" y = %.2f*x + %.2f" % (k, b))
print(f' y = {k}*x + {b}')