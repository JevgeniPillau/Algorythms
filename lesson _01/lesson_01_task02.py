'''2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.
logic OR 5 - 101     logic AND 101   logic XOR 101
         6 - 110               110             110
             ---               ---             ---
    result   111 - 7           100 - 4         011 - 3'''

x = 5
y = 6
print('x = 5')
print('y = 6')
 
bit_or = x | y
bit_and = x & y
bit_xor = x ^ y
 
print(f'result for: 5 OR 6 is - {bin(bit_or)}')
print(f'result for: 5 AND 6 is - {bin(bit_and)}')
print(f'result for: 5 XOR 6 is - {bin(bit_xor)}')
print(f'bit shift right in 2 digit for 5 - {bin(x>>2)}')
print(f'bit shift left in 2 digit for 5 - {bin(x<<2)}')