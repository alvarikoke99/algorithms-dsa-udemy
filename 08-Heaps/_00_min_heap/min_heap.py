import math


class MinHeap:
    def __init__(self, size: int):
        self._max_size = size
        self._size = 0
        self._heap = [0] * size

    def _parent_index(self, i: int) -> int:
        return (i - 1) // 2

    def _left_child_index(self, i: int) -> int:
        return (i * 2) + 1

    def _right_child_index(self, i: int) -> int:
        return (i * 2) + 2

    def _is_leaf(self, i: int) -> bool:
        return self._right_child_index(i) >= self._size and self._left_child_index(i) >= self._size

    def insert(self, element: int) -> None:
        if self._size >= self._max_size:
            return
        self._heap[self._size] = element
        current = self._size

        while self._heap[current] < self._heap[self._parent_index(current)]:
            self._swap(current, self._parent_index(current))
            current = self._parent_index(current)

        self._size += 1

    def extract_min(self) -> int:
        if self._size <= 0:
            return -math.inf

        popped = self._heap[0]
        self._size -= 1
        self._heap[0] = self._heap[self._size]
        self._min_heapify(0)
        return popped

    def _min_heapify(self, i: int) -> None:
        if not self._is_leaf(i):
            if (self._heap[i] > self._heap[self._left_child_index(i)] or
                    self._heap[i] > self._heap[self._right_child_index(i)]):
                if self._heap[self._left_child_index(i)] < self._heap[self._right_child_index(i)]:
                    self._swap(i, self._left_child_index(i))
                    self._min_heapify(self._left_child_index(i))
                else:
                    self._swap(i, self._right_child_index(i))
                    self._min_heapify(self._right_child_index(i))

    def print_heap_pretty(self) -> None:
        for i in range(self._size // 2):
            print(f"Parent : {self._heap[i]}", end="")
            if self._left_child_index(i) < self._size:
                print(f" Left : {self._heap[self._left_child_index(i)]}", end="")
            if self._right_child_index(i) < self._size:
                print(f" Right :{self._heap[self._right_child_index(i)]}", end="")
            print()

    def print_heap(self) -> None:
        print(self._heap[:self._size])

    def _swap(self, x: int, y: int) -> None:
        self._heap[x], self._heap[y] = self._heap[y], self._heap[x]
