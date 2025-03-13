# =================================================bubble_sort=================================================#

# Асимптотическая сложность алгоритма - O(N * logN)

# 1. необходимо преобразовать бинарное дерево в кучу
# 2. поменять местами самый первый элемент с последним
# 3. вернуть бинарное дерево к куче

def heap_sort(lst) -> list[int]:
    make_heap(lst)

    i = 0
    while i < len(lst):
        last = (len(lst) - 1) - i

        lst[0], lst[last] = lst[last], lst[0]

        remake_heap(lst, latest_index=last)

        i += 1

    return lst


def make_heap(lst: list) -> None:
    i = 0
    while i < len(lst):
        # Перемещение очередного элемента в корень
        index = i
        while index != 0:
            # Ищем родительский индекс
            parent_index = (index - 1) // 2

            # Если значение дочернего элемента <= родительскому -> прерываем цикл
            if lst[index] <= lst[parent_index]:
                break

            # Меняем родительский элт с дочерним
            lst[index], lst[parent_index] = lst[parent_index], lst[index]

            # Меняем текущий индекс на родительский
            index = parent_index
        i += 1


def remake_heap(lst: list, latest_index: int) -> None:
    i = 0
    while True:
        child1_i = 2 * i + 1
        child2_i = 2 * i + 2

        if child1_i >= latest_index:
            child1_i = i
        if child2_i >= latest_index:
            child2_i = i

        if (
                (lst[i] >= lst[child1_i])
                and
                (lst[i] >= lst[child2_i])
        ):
            break

        if lst[child1_i] > lst[child2_i]:
            swap_child_i = child1_i
        else:
            swap_child_i = child2_i

        lst[i], lst[swap_child_i] = lst[swap_child_i], lst[i]

        i = swap_child_i


print(heap_sort([1, 5, 12, 563, 2112, 5623, 22, 4352, 19234]))
