import math

# num1 = math.sqrt(16)  # квадрат из числа
# num2 = math.ceil(3.2)  # округление в большую сторону
# num3 = math.floor(3.2)  # округление в меньшую сторону
#
# print(num1)
# print(num2)
# print(num3)
#
# print(dir(math))  # посмотреть все функции math

# ----------------------------------------------------------------------------------------------------------------------
# r = int(input('введите радиус окружности: '))
# print('длинна окружности:', round(2 * math.pi * r, 2))
# ----------------------------------------------------------------------------------------------------------------------

import time


seconds = time.time()
print('секунды сначала эпохи: ', seconds)

locale_time = time.ctime()
print('местное время: ', locale_time)

res = time.localtime()
print('localtime: ', res)
print(res.tm_mday, '.', res.tm_mon, '.', res.tm_year, sep='')
print(time.strftime('Today is %B %d, %Y.'))  # Today is July 23, 2022.
print(time.strftime('%m/%d%Y, %H:%M:%S'))  # 07/23/2022, 11:13:27

# -----------
# Примеры
# -----------
# 1) Показывает напоминание спустя время
text = input('Название напоминания: ')
locale_time = float(input("Через сколько минут: "))
locale_time = locale_time * 60  # делаем из минут секунды
time.sleep(locale_time)  # задержка времени на кол-во указанное в переменной local_time
print(text)

# 2) Посчитает время выполнения программы
start = time.time()  # с погрешностью
time.sleep(5)
finish = time.time()
res = finish - start
print(res, 'seconds')

# 2.2) Посчитает время выполнения программы
start = time.monotonic()  # без погрешности
time.sleep(5)
finish = time.monotonic()
res = finish - start
print(res, 'seconds')

# ----------------------------------------------------------------------------------------------------------------------
import locale  # меняет локализацию питона под язык и культуру другой страны

locale.setlocale(locale.LC_ALL, 'ru')

print(time.strftime('Сегодня: %B %d, %Y.'))


# ----------------------------------------------------------------------------------------------------------------------
# ФУНКЦИЯ
# -------

# def symbol(a, b, c):
#     for i in range(a):
#         if i % 2 == 0:
#             print(b, end='')
#         else:
#             print(c, end='')
#     print()
#
#
# symbol(9, '+', '-')
# symbol(7, 'X', '0')


# def get_sum(a, b):
#     return a + b
#
#
# res = get_sum(1, 8)
# print(res)


# def rs(a, b):
#     if a > b:
#         return a - b
#     else:
#         return a + b
#
#
# print(rs(11, 9))




