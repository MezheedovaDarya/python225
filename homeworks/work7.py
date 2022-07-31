# 1)
import random as r
#
# 1) Написать программу, которая случайным образом заполняет двумерный список размерностью 3х4 цифрами от -20 до 10.
# Необходимо найти количество отрицательных элементов.
# x = [[r.randint(-20, 10) for i in range(3)] for j in range(4)]
# y = 0
# for row in x:
#     for i in row:
#         print(i, end='\t\t')
#         if i < 0:
#             z = row.count(i)
#             y += z
#     print()
#
# print('количество отрицательных элементов:', y)


# 2)Написать программу, которая случайным образом заполняет двумерный список размерностью 3х4 цифрами от 0 до 4. Найти
# произведение ненулевых элементов списка.
# x = [[r.randint(0, 4) for i in range(3)] for j in range(4)]
# y = 1
# for row in x:
#     for i in row:
#         if i > 0:
#             y *= i
#         print(i, end='\t\t')
#     print()
# print('Произведение ненулевых элементов:', y)


# 3) Написать программу, которая случайным образом заполняет двумерный список размерностью 6х6 цифрами от 0 до 10 и
# одномерный список из 6-ти чисел. Нужно нечетные строки двумерного списка заменить на одномерный список.
main_list = [[r.randint(0, 10) for i in range(6)] for j in range(6)]
sub_list = [r.randint(0, 10) for k in range(6)]


# print(main_list)

for row in range(len(main_list)):
    for i in range(len(main_list[row])):
        print(main_list[row][i], end='\t\t')
    print()

print(sub_list)

for row in range(len(main_list)):
    for i in range(len(main_list[row])):
        if row % 2 == 0:
            main_list[row] = sub_list
        print(main_list[row][i], end='\t\t')
    print()

