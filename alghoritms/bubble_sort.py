#=================================================bubble_sort=================================================#

# Асимптотическая сложность алгоритма - O(N^2)

# Быстрее всего работает на небольшом массиве данных [5, 15]

def bubble_sort(lst: list) -> list:
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                is_sorted = False

    return lst


def quick_bubble_sort(lst: list) -> list:
    is_sorted = False
    n = 1
    while not is_sorted:
        is_sorted = True
        for i in range(len(lst) - n):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                is_sorted = False

        n += 1

    return lst


print(bubble_sort([2, 3, 9, 1234, 9, 20]))
print(quick_bubble_sort([2, 3, 9, 1234, 9, 20]))


