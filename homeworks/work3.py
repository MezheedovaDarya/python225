userChoice = input('\n1)"r" - Применяет унарный минус '
                   '\n2)"+" - сложение\n3)"-" - вычитание\n4)"/" - деление с остатком\n5)"*" - умножение'
                   '\n6)"%" - деление по модулю (остаток от деления)\n7)"<" - минимальное из двух чисел'
                   '\n8)">" - максимальное из двух чисел\nВведите знак необходимой математической операции: ')
try:
    if userChoice == 'r':
        num1 = int(input('Введите первое число: '))
        num2 = int(input('Введите второе число: '))

        num1 = - num1
        num2 = - num2
        print('Результат: ', num1, ',', num2)
    elif userChoice == '+':
        num1 = int(input('Введите первое число: '))
        num2 = int(input('Введите второе число: '))

        print('Результат', num1, '+', num2, '=', num1 + num2)
    elif userChoice == '-':
        num1 = int(input('Введите первое число: '))
        num2 = int(input('Введите второе число: '))

        print('Результат', num1, '-', num2, '=', num1 - num2)
    elif userChoice == '/':
        num1 = int(input('Введите первое число: '))
        num2 = int(input('Введите второе число: '))

        print('Результат', num1, '/', num2, '=', num1 / num2)
    elif userChoice == '*':
        num1 = int(input('Введите первое число: '))
        num2 = int(input('Введите второе число: '))

        print('Результат', num1, '*', num2, '=', num1 * num2)
    elif userChoice == '%':
        num1 = int(input('Введите первое число: '))
        num2 = int(input('Введите второе число: '))

        print('Результат', num1, '%', num2, '=', num1 % num2)
    elif userChoice == '<':
        num1 = int(input('Введите первое число: '))
        num2 = int(input('Введите второе число: '))
        if num1 < num2:
            print('Минимальное число =', num1)
        else:
            print('Минимальное число =', num2)
    elif userChoice == '>':
        num1 = int(input('Введите первое число: '))
        num2 = int(input('Введите второе число: '))
        if num1 > num2:
            print('Максимальное число =', num1)
        else:
            print('Максимальное число =', num2)
    else:
        print('Вы ввели неверный знак математической операции')
except ValueError:
    print('Вы ввели не целое число')




