from typing import List


def swap(array: List[int], i: int, j: int) -> None:
    array[i], array[j] = array[j], array[i]
