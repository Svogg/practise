def quick_sort(array, start, end):
    """
    Быстрая сортировка c использованием двух стеков.
    """

    if start >= end:
        return

    # Используем первый элемент в качестве разделителя.
    # Не самый оптимальный вариант, особенно если массив почти отсортирован.
    divider = array[start]

    # Помещаем элементы до и после от разделителя.
    before, after = [], []
    i = start + 1
    while i < end + 1:
        if array[i] < divider:
            before.append(array[i])
        else:
            after.append(array[i])
        i += 1

    # Помещаем элементы до разделителя обратно в массив.
    index = start
    while len(before) > 0:
        array[index] = before.pop()
        index += 1

    # Вставляем разделитель.
    array[index] = divider

    # Запоминаем, что это средняя точка.
    midpoint = index

    # Добавляем элементы после разделителя,
    index += 1
    while len(after) > 0:
        array[index] = after.pop()
        index += 1

    # Сортируем две половинки массива.
    quick_sort(array, start, midpoint - 1)
    quick_sort(array, midpoint + 1, end)


def simple_quicks_sort(array):
    if len(array) <= 1:
        return array

    divider = array[0]

    less = [i for i in array if i < divider]
    equal = [i for i in array if i == divider]
    more = [i for i in array if i > divider]

    return simple_quicks_sort(less) + equal + simple_quicks_sort(more)


data = [7, 8, 9, 4, 6, 5, 10, 3, 2, 1]
print(simple_quicks_sort(data))
# Первый вызов функции, указываем первый и последний элементы массива.
quick_sort(data, 0, len(data) - 1)
print(data)