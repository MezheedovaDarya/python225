# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)


# age = int(input('Введите свой возраст: '))
# if age >= 18:
#     print('Доступ на сайт разрешен')
# else:
#     pass
#     print('Доступ на сайт запрещен')

# a = 15
# b = 5
# if a > b:
#     print('a > b')
# elif a < b:
#     print('b > a')
# else:
#     print('a = b')


# a = int(input('Введите первую сторону: '))
# b = int(input('Введите вторую сторону: '))
# c = int(input('Введите третью сторону: '))
# if a == b == c:
#     print('реугольник равносторонний')
# elif a == b or a == c or b == c:
#     print('Треугольник равнобедренный')
# else:
#     print('Треугольник разносторонний')


# day = int(input('Введите день недели (цифрой): '))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5):
#     print('Рабочий день - ', end='')
#     if day == 1:
#         print('Понедельник')
#     if day == 2:
#         print('Вторник')
#     if day == 3:
#         print('Среда')
#     if day == 4:
#         print('Четверг')
#     if day == 5:
#         print('Пятница')
# elif day == 6 or day == 7:
#     print('Выходной день - ', end='')
#     if day == 6:
#         print('Суббота')
#     if day == 7:
#         print('Воскресенье')
# else:
#     print('Такого дня недели не существует')


# month = int(input('Введите числом номер месяца: '))
# if 3 <= month <= 5:
#     print('Весна - ', end="")
#     if month == 3:
#         print('Март')
#     if month == 4:
#         print('Апрель')
#     if month == 5:
#         print('Май')
# elif 6 <= month <= 8:
#     print('Лето - ', end="")
#     if month == 6:
#         print('Июнь')
#     if month == 7:
#         print('Июль')
#     if month == 8:
#         print('Август')
# elif 9 <= month <= 11:
#     print('Осень - ', end="")
#     if month == 9:
#         print('Сентябрь')
#     if month == 10:
#         print('Октябрь')
#     if month == 11:
#         print('Ноябрь')
# elif month == 12 or month == 1 or month == 2:
#     print('Зима - ', end="")
#     if month == 12:
#         print('Декабрь')
#     if month == 1:
#         print('Январь')
#     if month == 2:
#         print('Февраль')
# else:
#     print('Такого месяца не сущесвует!')


# n = int(input('Введите количество ворон: '))
# if 0 <= n <= 9:
#     if n == 1:
#         print('На ветке', n, 'ворона')
#     if 2 <= n <= 4:
#         print('На ветке', n, 'вороны')
#     else:
#         print('На ветке', n, 'ворон')
# else:
#     print('Ошибка ввода данных')


a, b = 10, 20

minim = 'a == b' if a == b else ("a > b" if a > b else "b > a")
print(minim)
