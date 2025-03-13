#=================================================Linked_List=================================================#

class Node:
    """
    Реализация самого контейнера списка.
    """

    def __init__(self, value=None) -> None:
        """
        value - значение хранящееся в структуре.
        next_node - ссылка на следующую ноду.
        """
        self.value = value
        self.next_node = None

    def __str__(self):
        return str(self.value)


# node1 = Node(235)
# node2 = Node(138)
# node1.next_node = node2
# print(node1, node1.next_node.value)


class LinkedList:
    """
    Реализация структуры связанного списка.
    """

    def __init__(self) -> None:
        self.top: Node | None = None
        self.tail: Node | None = None

    def fast_append(self, value):
        """
        Добавление нового элемента в конец связного списка.
        Время работы O(1).
        """
        new_node = Node(value)

        if self.top is None:  # Если нет головы СП, то и нет хвоста.
            self.top, self.tail = new_node, new_node
            return

        self.tail.next_node = new_node
        self.tail = new_node

    def base_append(self, value):
        """
        Добавление нового элемента в конец связного списка.
        Время работы O(N).
        """

        # Если нет первого элемента, то создаем и завершаем работу.
        if self.top is None:
            self.top = Node(value)
            return

        # Перебираем по очереди все элементы, чтобы найти последний
        current = self.top
        while current.next_node is not None:
            current = current.next_node

        # Создаем ссылку для последнего элемента на новый
        current.next_node = Node(value)
        self.tail = current.next_node

    def prepend(self, value):
        """
        Добавление эл-та в начало списка.
        Время работы O(1).
        """

        self.top, self.top.next_node = Node(value), self.top

    def insert(self, prev_value, value) -> None:
        """
        Добавление эл-та после предыдущего.
        Время работы O(N).
        """
        current = self.top.next_node
        while current is not None:
            if current.value == prev_value:
                new_node = Node(value)
                new_node.next_node, current.next_node = current.next_node, new_node
                return
            current = current.next_node

    def delete(self, value) -> None:
        """
        Удаляет эл-т из СП.
        Время работы O(N).
        """
        current = self.top.next_node
        prev = self.top

        if prev.value == value:
            self.top = self.top.next_node

        while current is not None:
            if current.value == value:
                prev.next_node = current.next_node
                return

            prev = current
            current = current.next_node

    def __str__(self):
        current = self.top
        values = "["

        while current is not None:
            end = ", " if current.next_node else ""
            values += str(current) + end
            current = current.next_node

        return values + "]"


linked_list = LinkedList()

linked_list.base_append(12)
linked_list.base_append(13)
linked_list.fast_append(1234)
linked_list.fast_append(12123)
# linked_list.prepend(235)
# linked_list.base_append(14)
# linked_list.insert(14, 123456)
# linked_list.base_append(15)
#
# linked_list.base_append(16)
# linked_list.base_append(17)
# linked_list.delete(235)



print(linked_list)
