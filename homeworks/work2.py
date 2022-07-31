n = int(input('Введите количесво копеек цифрой от 1 до 99: '))
if 0 <= n <= 99:
    if n == 1 or n % 10 == 1 and n != 11:
        print(n, 'копейка')
    if 2 <= n <= 4 or 2 <= n % 10 <= 4 and n != 12 and n != 13 and n != 14:
        print(n, 'копейки')
    else:
        print(n, 'копеек')
else:
    print('Ошибка ввода данных')
