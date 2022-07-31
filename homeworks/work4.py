n = 12
i = 0
while True:
    a = int(input('введите число: '))
    if a == 0:
        print('Вы прекратили пытаться')
        print('Количество попыток: ', i)
        break
    if a < n:
        print('Число меньше загаданного')
    elif a == n:
        print('Вы угадали!')
        print('Количество попыток: ', i)
        break
    else:
        print('Число больше загаданного')
    i += 1
