from typing import List
from search_utils import swap


class SelectionSort:
    @staticmethod
    def sort(array: List[int]) -> None:
        for i in range(len(array) - 1):
            # En cada iteración seleccionamos el mínimo y lo movemos al inicio de la parte
            # desordenada del array.
            min_index = SelectionSort._find_minimum_element_index(array, i)
            swap(array, i, min_index)

    @staticmethod
    def _find_minimum_element_index(array: List[int], start: int) -> int:
        min_index = start
        for i in range(start + 1, len(array)):
            if array[i] < array[min_index]:
                min_index = i
        return min_index
