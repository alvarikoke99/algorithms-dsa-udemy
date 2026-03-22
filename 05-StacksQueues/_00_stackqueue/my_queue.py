class MyEmptyQueueException(Exception):
    pass


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next: "Node" = None


class MyQueue:
    def __init__(self):
        self._first: Node = None
        self._last: Node = None

    def add(self, value: int) -> None:
        new_last = Node(value)
        if self._last is not None:
            self._last.next = new_last
        self._last = new_last
        if self._first is None:
            self._first = self._last

    def remove(self) -> int:
        if self._first is None:
            raise MyEmptyQueueException()
        first_value = self._first.value
        self._first = self._first.next
        if self._first is None:
            self._last = None
        return first_value

    def peek(self) -> int:
        if self._first is None:
            raise MyEmptyQueueException()
        return self._first.value

    def is_empty(self) -> bool:
        return self._first is None
