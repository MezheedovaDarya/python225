#
# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print('цикл окончен')


# n = int(input('Количество символов: '))
# sim = input('Тип символа: ')
# orient = int(input('0 - горизонтальная\n1 - вертикальная\nориентация линии: '))
# i = 0
# while i < n:
#     if orient == 0:
#         print(sim, end=' ')
#     elif orient == 1:
#         print(sim)
#     else:
#         print('Вы ввели неверную ориентацию')
#         break
#     i += 1


# kol = int(input('Введите количество чисел последовательности: '))  # 5
# i = 1
# n = float(input('Введите число: '))  # 4
# summa = n  # 4
# minim = n  # 4
# maxim = n  # 4
# while i < kol:
#     n = float(input('Введите число: '))  # 2 3
#     summa += n  # summa = summa +n  4+2=6+3=9
#     if maxim < n:
#         maxim = n
#     if minim > n:
#         minim = n  # minim = 2
#     i += 1
# print('Среднее арифметическое равно: ', summa / kol)
# print('Минимальное число равно: ', minim)
# print('Максимальное число равно: ', maxim)


# ВЛОЖЕННЫЙ ЦИКЛ
# i = 1
# while i < 5:
#     print('Внешний цикл: i =', i)
#     j = 1
#     while j < 4:
#         print('\tВнутренний цикл: j=', j)
#         j += 1
#     i += 1


# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, '*', j, '=', i * j, end='\t\t')
#         j += 1
#     print()  # пустой принт делает перенос на новую строку
#     i += 1

# i = 0
# while i < 3:  # отвечает за кол-во строк
#     j = 0
#     while j < 6:  # отвечает за кол-во элементов в строке
#         print('@', end='')
#         j += 1
#     print()
#     i += 1


# i = 0
# while i < 5:
#     j = 0
#     while j < 20:
#         if i % 2 == 0:
#             print('+', end='')
#         else:
#             print('-', end='')
#         j += 1
#     print()
#     i += 1

# FOR
# for i in range(start, stop, step)

# for i in range(100, 0, -10):
#     print(i, end=' ')

# a = int(input('Введите целое число: '))
# for i in range(1, a):
#     if a % i == 0:
#         print(i, end=' ')

# for i in range(1, 100):
#     if i % 10 == i // 10:
#         print(i, end=' ')


# for i in range(3):
#     print(i, end=' ')
#     if i == 1:
#         break
# else:
#     print('done')


# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("-----")

# w = int(input('width: '))
# h = int(input('height: '))
# for i in range(h):
#     for j in range(w):
#         print('*', end='')
#     print()

# w = int(input('width: '))
# h = int(input('height: '))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print('*', end='')
#         else: print(' ', end='')
#     print()


# n = [i for i in range(6)]
# print(n)

# n = [i for i in 'Hello']
# print(n)


# Список
# n = [5, [6, 7, 8], 9, 'Hello', 5.6, True]
# # print(n)
# # print(type(n))
# # print(n[3])
# # print(n[3][1])
# # print(n[1][2])
#
# n[1] = 267  # изменить значение элемента
# print(n)
#
# n[0] += 100  # прибавить к значению элемента
# print(n)
# print(len(n))  # показать кол-во элементов (длину списка)


# b = list()
# print(b)

# s = [1, 2, 3]
# print([5] * 2)
