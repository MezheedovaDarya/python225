import math

z = int(input('Введите 1 для нахождения площади квадрата\nВведите 2 для нахождения площади треугольника\nВведите 3 для '
              'нахождения площади круга\nВведите цифру: '))


def rectangle(a, b):
    s = a * b
    return s


def triangle(a, b):
    s = (a * b) / 2
    return s


def circle(a):
    s = (math.pi * a)**2
    return s


if z == 1:
    x = int(input('Введите основание: '))
    y = int(input('Введите высоту: '))
    print("Площадь прямоугольника =", rectangle(x, y))
elif z == 2:
    x = int(input('Введите основание: '))
    y = int(input('Введите высоту: '))
    print("Площадь треугольника =", triangle(x, y))
elif z == 3:
    x = int(input('Введите радиус: '))
    print("Площадь круга =", round(circle(x), 2))
else:
    print('Вы дэбил и ввели неверную цифру. Перечитайте условие.')