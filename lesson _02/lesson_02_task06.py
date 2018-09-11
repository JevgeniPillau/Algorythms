'''6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться, больше или меньше загаданного введенное пользователем число.
Если за 10 попыток число не отгадано, то вывести его.'''


from random import randrange
print('My Dear player, its time to hunt a golden duck,\n'
      'i have chosen just one random duck from the pack of 100\n'
      'if you shut down that one duck, you will get a reward\n')
print('And one more thing, my Dear player,\n'
      'you have only 10 shots to win the hunt\n')
num = randrange(0, 100)
# print(num)
shot_counter = 1

while shot_counter <= 10:
    try:
        user_num = int(input(f'your {shot_counter} shot: '))
        shot_counter += 1
        if user_num > num:
            print('Oh my Dear, my duck have smaller number in the pack')
        elif user_num == num:
            print('\nwell done!\n       you\'ve won!\n'
                  'you have hunted down the golden duck\n'
                  f'and earned {num} credits')
            break
        else:
            print('Oh my Dear, my duck have bigger number in the pack')
    except ValueError:
        print('\nplease type in a duck number, you inserted something else\n')
else:
    print('\nsorry, ammo depleted, game over!\n'
          f'golden duck was {num} in the pack')
