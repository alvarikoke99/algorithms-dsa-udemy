from typing import List


class MergeSort:
    @staticmethod
    def sort(array: List[int]) -> None:
        helper = [0] * len(array)
        MergeSort._sort(array, helper, 0, len(array) - 1)

    @staticmethod
    def _sort(array: List[int], helper: List[int], low: int, high: int) -> None:
        if low < high:
            middle = (low + high) // 2
            MergeSort._sort(array, helper, low, middle)        # Ordena lado izquierdo
            MergeSort._sort(array, helper, middle + 1, high)  # Ordena lado derecho
            MergeSort._merge(array, helper, low, middle, high) # Mezcla ambos

    @staticmethod
    def _merge(array: List[int], helper: List[int], low: int, middle: int, high: int) -> None:
        # Copia ambas mitades en el array auxiliar
        for i in range(low, high + 1):
            helper[i] = array[i]

        helper_left = low
        helper_right = middle + 1
        current = low

        # Itera el array auxiliar. Compara la mitad izquierda y la derecha, copiando el menor
        # elemento de las dos mitades al array original.
        while helper_left <= middle and helper_right <= high:
            if helper[helper_left] <= helper[helper_right]:
                array[current] = helper[helper_left]
                helper_left += 1
            else:
                array[current] = helper[helper_right]
                helper_right += 1
            current += 1

        # Copia el resto del lado izquierdo en el target array.
        remaining = middle - helper_left
        for i in range(remaining + 1):
            array[current + i] = helper[helper_left + i]
