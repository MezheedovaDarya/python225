def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst


print(change([1, 2, 3]))
print(change([9, 12, 33, 54, 105]))
print(change(['с', 'л', 'о', 'н']))


# второй способ почему-то работает некорректно
def change(lst):
    start = lst.pop()
    end = lst.pop(0)
    lst.insert(0, start)
    lst.insert(-1, end)
    return lst


print(change([1, 2, 3]))
print(change([9, 12, 33, 54, 105]))
print(change(['с', 'л', 'о', 'н']))
