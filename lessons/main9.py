# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))
#
#
# def change(lst):
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.insert(0, start)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))

# ----------------------------------------------------------------------------------------------------------------------
# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(is_greater(10, 5))
# print(is_greater(5, 15))


# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if 'A' <= ch <= "Z":
#             has_upper = True
#         elif 'a' <= ch <= 'z':
#             has_lower = True
#         elif '0' <= ch <= '9':
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     else:
#         if len(password) < 8:
#             print('Количество символов слишком маленькое ')
#
#     return False
#
#
# p = input('Введите пароль: ')
# if check_password(p):
#     print('Это надежный пароль')
# else:
#     print('Это ненадежный пароль')


# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, d=2))


# def symbol(elements=20, sign='-'):
#     for i in range(elements):
#         print(sign, end='')
#     print()
#
#
# symbol(10, '+')
# symbol(5, '*')
# symbol(15, '#')
# symbol(7)
# symbol()


# def digits_sum(n, event = True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if event and cur_digit % 2 == 0:
#             s += cur_digit
#         elif not event and cur_digit % 2 != 0:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print('Сумма четных цифр: ')
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
# print('Сумма нечетных цифр: ')
# print(digits_sum(9874023, event=False))
# print(digits_sum(38271, event=False))
# print(digits_sum(123456789, event=False))


# def display_info(name, age):
#     print('Name:', name, '\nAge:', age)
#     print("*" * 20)
#
#
# display_info('Ira', 20)
# display_info(20, 'Ira')
# display_info(age=23, name='Igor')
# display_info('Ira', age=23, name='Igor')  # так нельзя, в имени 2 значения


# ----------------------------------------------------------------------------------------------------------------------
# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(lt1 == lt2)  # True
# print(lt1 is lt2)  # False
# print(id(lt1))
# print(id(lt2))

# lt1 = 6
# lt2 = 6
# print(lt1 == lt2)  # True
# print(lt1 is lt2)  # True
# print(id(lt1))
# print(id(lt2))

# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1.append(4)
# print(lt1)
# print(id(lt1))
# lt1.pop(1)
# print(lt1)
# print(id(lt1))


s = 'Hello '
print(id(s))  # s = s + 'World'
s += 'World'
print(s)
print(id(s))





