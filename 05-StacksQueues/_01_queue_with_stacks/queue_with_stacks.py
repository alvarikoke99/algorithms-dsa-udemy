from collections import deque
from typing import Optional

from PIL.ImageOps import invert

"""
Implementa una clase MyQueue utilizando dos stacks.

Como Stack usaremos deque, que proporciona las operaciones de una cola doblemente terminada,
permitiéndola usar como Pila o Cola (solo las operaciones de Pila están permitidas en este ejercicio).
"""


class QueueWithStacks:
    def __init__(self):
        self.stack: deque = deque()
        self.inverse_stack: deque = deque()

    # O(1)
    def add(self, value: int) -> None:
        self.stack.append(value)

    # O(N) worst case
    def peek(self) -> Optional[int]:
        if self.is_empty():
            return None
        self._dump_elem_into_second_stack()
        return self.inverse_stack[-1]

    # O(N) worst case
    def remove(self) -> Optional[int]:
        if self.is_empty():
            return None
        self._dump_elem_into_second_stack()
        return self.inverse_stack.pop()

    def _dump_elem_into_second_stack(self):
        if not self.inverse_stack:
            while self.stack:
                self.inverse_stack.append(self.stack.pop())

    # O(1)
    def is_empty(self) -> bool:
        return self.size() == 0

    # O(1)
    def size(self) -> int:
        return len(self.stack + self.inverse_stack)