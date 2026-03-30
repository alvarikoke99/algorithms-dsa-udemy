class Node:
    def __init__(self, value: int = None):
        self.value = value
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def append_to_tail(self, value: int) -> None:
        if self.head is None:
            self.head = Node(value)
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(value)

    def init_list(self, value: Node) -> None:
        self.head = value

    def delete_node(self, value: int) -> None:
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        # 4-3-1
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def print_list(self) -> None:
        if self.head is None:
            print("END")
            return
        current = self.head
        while current.next is not None:
            print(f"{current.value} -> ", end="")
            current = current.next
        print(f"{current.value} -> END")
