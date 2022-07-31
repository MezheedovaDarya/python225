# Добавить в конец списка лишние элементы
a = [1, 2, 3]
b = [11, 12, 13, 4, 2]
c = []

for i in range(len(b)):
    if i < len(a):
        c.append(a[i])
        c.append(b[i])
    else:
        c.append(b[i])
print(c)

# альтернативный вариант
a = [1, 2, 3]
b = [11, 12, 13, 4, 2]
c = []
print("a =", a)
print("b =", b)
if len(b) > len(a):
    for i in range(len(a)):  # от 0 до 3
        c.append(a[i])
        c.append(b[i])
    for i in range(len(a), len(b)):  # от 3 до 5
        c.append(b[i])
else:
    for i in range(len(b)):
        c.append(a[i])
        c.append(b[i])
    for i in range(len(b), len(a)):
        c.append(a[i])
print("c =", c)

# ----------------------------------------------------------------------------------------------------------------------
# Дан список. Выведите те его элементы, которые встречаются в списке только 1 раз. Элементы нужно выводить в том порядке
# в котором они встречаются в списке.
a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
for i in range(len(a)):
    b = a.count(a[i])
    if b == 1:
        print(a[i], end=' ')


