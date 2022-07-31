# --------------
# КОРТЕЖ (tuple)
# --------------
# ()
# tuple()

# lst = [10, 20, 30]
# tpl = (10, 20, 30)

# print(lst.__sizeof__())  # посмотреть сколько байт занимает в памяти
# print(tpl.__sizeof__())
#
# a = (1, 2, 3, 4, 5, 6)
# print(a)
# print(type(a))
# b = tuple((1, 2, 3, 4, 5, 6))
# print(b)
# print(type(b))

# t = (1,)
# print(type(t))

# s1 = tuple(int(input('--> ')) for i in range(5))
# print(s1)

# s = input('-> ')
# print(tuple(s))

# import random as r
#
# mas = [r.randint(0, 100) for i in range(10)]
# tpl = tuple(mas)
# print(mas)
#
# mas = tuple(r.randint(0, 100) for i in range(10))
# print(mas)


# s = tuple(2**i for i in range(1, 13))
# print(s)

# t1 = tuple('Hello')
# t2 = tuple(' World')
# t3 = t1 + t2
# print(t3)
# print(len(t3))
# print(t3.count('l'))
# print(t3.index('l', 4))
#
# for i in t3:
#     print(i, end='')


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1)+ 1
#             return tpl[first:second]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))


# ----------------------------------------------------------------------------------------------------------------------

# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'wrld'])
# print(t, id(t))
# t[4][0] = 'new'
# t[4].append('hi')
# print(t, id(t))


# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t   # распаковка кортежа
# print(x, y, z)


# def get_user():
#     name = 'Tom'
#     age = 19
#     is_married = False
#     return name, age, is_married
#
#
# user1, user2, user3 = get_user()
# print(user1)
# print(user2)
# print(user3)
# print(get_user())


# t = (1, 2, 3)
# del t
# print(t)


# lst = [1, 2, 3, 4, 5, 6]
# print(type(lst))
# print(lst)
# tpl = tuple(lst)
# print(type(tpl))
# print(tpl)
# print(list(tpl))


# countries = (
#     ('Германия', 20.2, (('Берлин', 3.326), ('Гамбург', 1.728))),
#     ('Франция', 66, (('Париж', 2.2), ('Марсель', 1.6)))
# )
#
# for country in countries:
#     country_name, country_population, cities = country
#     print('\nСтрана:', country_name, 'Население =', country_population)
#     for city in cities:
#         city_name, city_population = city
#         print('\tГород:', city_name, 'Население =', city_population)


# -------------------------------------------------------------------------------------
# МНОЖЕСТВА (set) - неупорядоченная коллекция которая хранит только уникальные значения
# -------------------------------------------------------------------------------------
# {}
# set()

# s = {4, 5, 6, 7, 3, 4, 5, 2, 3, 5}
# print(type(s))
# print(len(s))
# print(s)

# s = set()
# print(type(s))

# s = set('Hello')
# print(s)


# c = [1, 3, 5, 2, 7, 2, 2, 6, 3, 4, 6, 2]
# print(c)
# s = set(c)
# print(s)
# c = list(s)
# print(c)


# numbers = [1, 3, 5, 2, 7, 2, 2, 6, 3, 4, 6, 2]
# s = list({x for x in numbers if x % 2 == 0})
# print(s)


# def to_set(el):
#     # st = set(el)
#     # return st, len(st)
#
#     # return set(el), len(set(el))
#
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 2, 4, 2]))


# t = {'red', 'green', 'blue'}
# # print('green' not in t)
# for i in t:
#     print(i)


# r = ['ab_1', 'ab_2', 'bc_1', 'bc_2']
# a = {i for i in r}
# print(a)

r = ['ab_1', 'ab_2', 'bc_1', 'bc_2']
# a = {i for i in r if 'a' not in i}

print(a)

