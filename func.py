def summa(list): # Сумма элементов списка
    if list == []:
        return 0
    else:
        return list[0] + summa(list[1:])

# print(summa([1, 2, 3, 4]))

def counter(list):  # Количество элементов в списке
    if list ==[]:
        return 0
    else:
        return 1 + counter(list[1:])

# print(counter([1, 2, 3, 4, 5]))

def fact(x):  # Факториал числа через рекурсию
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)

# print(fact(5))

def max_number(list):  # Максимальное число в списке с помощью рекурсии
    if len(list) == 2:
        if list[0] > list[1]:
            return list[0]
        else:
            return list[1]
    sub_max = max_number(list[1:])
    if list[0] > sub_max:
        return list[0]
    else:
        return sub_max

# print(max_number([1, 8, 12, 24]))

def quicksort(list):  # Быстрая сортировка
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        less = [i for i in list[1:] if i > pivot]
        greater = [i for i in list[1:] if i < pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

# print(quicksort([10, 5, 16, 12, 18]))  # [18, 16, 12, 10, 5]

