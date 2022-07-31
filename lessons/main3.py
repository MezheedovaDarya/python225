# try:
#     n = int(input('Ведите делимое: '))
#     m = int(input('Ведите делитель: '))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print('Некорректные данные')
# else:
#     print('Все нормально. Вы ввели числа', n, 'и', m)
# finally:
#     print('Конец программы')
# except ValueError:
#     print('Вы ввели не целое число')
# except ZeroDivisionError:
#     print('Нельзя делить на 0')


# a = input('Введите первое значение: ')
# b = input('Введите второе значение: ')
# try:
#     a = int(a)
#     b = int(b)
# except ValueError:
#     a = str(a)
#     b = str(b)
# finally:
#     print(a + b)

# while условие:
#     блок инструкций

# i = 10
# while i >= 5:
#     print('i =', i)
#     i -= 1

# i = 1
# while i <= 20:
#     if i % 2:
#         print(i, end=' ')
#     i += 1

# n = int(input('введите символы: '))
# i = 0
# while i < n:
#     print('*', end='')
#     i += 1

# n = int(input('введите символы: '))
# while n > 0:
#     print('*', end='')
#     n -= 1


# n = int(input('Введите первое значение диапазона "от": '))
# m = int(input('Введите второе значение диапазона "до": '))
# res = 0
# while n <= m:
#     if n % 2:
#         res += n
#         print(n, end=' ')
#     n += 1
# print('Сумма целых нечетных чисел: ', res)


# n = input('Введите целое число: ')
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print('Число не целое')
#         n = input('Введите целое число: ')
#
# if n % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')


# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=' ')
#     if i == 5:
#         break
#     i += 1
# print('\nЦикл завершен')

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input('Введите положительное целое число: '))
#     if not n < 0:
#         break
# print(n)


# res = 1
# while True:
#     n = int(input('Введите число: '))
#     if n == 0:
#         break
#     res *= n
# print('Результат: ', res)


# i = 0
# while i < 10:
#     print(i)
#     i += 1
# else:
#     print('Цикл окончен, i =', i)
