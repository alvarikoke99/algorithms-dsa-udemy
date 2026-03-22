from collections import deque
from typing import Optional

"""
Implementa una clase MyQueue utilizando dos stacks.

Como Stack usaremos deque, que proporciona las operaciones de una cola doblemente terminada,
permitiéndola usar como Pila o Cola (solo las operaciones de Pila están permitidas en este ejercicio).
"""


class QueueWithStacks:
    def __init__(self):
        self.first_stack: deque = deque()
        self.second_stack: deque = deque()

    def add(self, value: int) -> None:
        raise NotImplementedError("Not implemented yet")

    def peek(self) -> Optional[int]:
        raise NotImplementedError("Not implemented yet")

    def remove(self) -> Optional[int]:
        raise NotImplementedError("Not implemented yet")

    def is_empty(self) -> bool:
        raise NotImplementedError("Not implemented yet")

    def size(self) -> int:
        raise NotImplementedError("Not implemented yet")
