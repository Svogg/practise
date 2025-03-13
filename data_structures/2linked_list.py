# =================================================2Linked_List=================================================#

class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next_node = None
        self.prev_node = None

    def __str__(self):
        return str(self.value)


class DuoLinkedList:
    def __init__(self) -> None:
        self.top: Node | None = Node()
        self.tail: Node | None = None

    def prepend(self, value) -> None:
        new_node = Node(value)
        if self.top.next_node is not None:
            self.top.next_node.prev_node = new_node

        new_node.next_node = self.top.next_node
        self.top.next_node = new_node
        new_node.prev_node = self.top

    def base_append(self, value) -> None:
        """
        Добавление нового элемента в конец дву-связного списка.
        Время работы O(N).
        """
        new_node = Node(value)

        if self.top is None:
            self.top, self.tail = new_node, new_node
            return

        current = self.top
        while current.next_node is not None:
            current = current.next_node

        current.next_node = new_node
        self.tail = new_node
        new_node.prev_node = current

    def fast_append(self, value) -> None:
        """
        Добавление нового элемента в конец дву-связного списка.
        Время работы O(1).
        """
        new_node = Node(value)

        if self.top is None:
            self.top, self.tail = new_node, new_node
            return

        self.tail.next_node = new_node
        self.tail = new_node
        new_node.prev_node = self.tail

    def insert(self, prev_value, value):

        current = self.top.next_node

        while current is not None:

            if current.value == prev_value:
                new_node = Node(value)
                new_node.prev_node = current
                new_node.next_node = current.next_node

                if current.next_node is not None:
                    current.next_node.prev_node = new_node
                current.next_node = new_node

                if current == self.tail:
                    self.tail = new_node

                return

            current = current.next_node

    def __str__(self):
        current = self.top
        values = "["

        while current is not None:
            end = ", " if current.next_node else ""
            values += str(current) + end
            current = current.next_node

        return values + "]"


duolinked_list = DuoLinkedList()


duolinked_list.base_append(1)
duolinked_list.base_append(2)
duolinked_list.base_append(3)
# duolinked_list.fast_append(4)
# duolinked_list.fast_append(5)
# duolinked_list.fast_append(6)
# duolinked_list.insert(4, 5)
duolinked_list.prepend(12)
duolinked_list.prepend(-2)
duolinked_list.prepend(25)
duolinked_list.prepend(35)
duolinked_list.prepend(-1)

print(duolinked_list)
