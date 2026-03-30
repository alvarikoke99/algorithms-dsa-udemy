from typing import List
from .search_utils import swap


class BubbleSort:
    @staticmethod
    def sort(array: List[int]) -> None:
        for i in range(len(array) - 1):
            for j in range(len(array) - i - 1):
                if array[j] > array[j + 1]:
                    swap(array, j, j + 1)
