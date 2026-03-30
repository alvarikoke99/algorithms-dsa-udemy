from collections import deque
"""
¿Cómo diseñarías un Stack que además de las operaciones de push y pop también
contase con una operación para obtener el mínimo?
"""


class StackMin:
    def __init__(self):
        self._min_stack: deque = deque()
        self._stack: deque = deque()

    def push(self, data: int) -> None:
        self._stack.append(data)
        if not self._min_stack or data <= self._min_stack[-1]:
            self._min_stack.append(data)

    def pop(self) -> int:
        val = self._stack.pop()
        if self._min_stack[-1] == val:
            self._min_stack.pop()

    def min(self) -> int:
        if not self._min_stack:
            return -1
        return self._min_stack[-1]