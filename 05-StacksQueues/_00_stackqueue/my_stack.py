class MyEmptyStackException(Exception):
    pass


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next: "Node" = None


class MyStack:
    def __init__(self):
        self._top: Node = None

    def push(self, value: int) -> None:
        new_top = Node(value)
        new_top.next = self._top
        self._top = new_top

    def pop(self) -> int:
        if self._top is None:
            raise MyEmptyStackException()
        top_value = self._top.value
        self._top = self._top.next
        return top_value

    def peek(self) -> int:
        if self._top is None:
            raise MyEmptyStackException()
        return self._top.value

    def is_empty(self) -> bool:
        return self._top is None
