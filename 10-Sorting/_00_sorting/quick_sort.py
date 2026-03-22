from typing import List
from search_utils import swap

"""
Dividimos la lista en dos recursivamente, una parte con los elementos más pequeños que el pivote
y la otra mitad con los más grandes.

O(n log(n)) tiempo medio y O(n^2) peor caso porque el pivote podría estar lejos de la mediana.
Si el pivote seleccionado es siempre el mayor o menor número estaríamos haciendo un bubble sort.
"""


class QuickSort:
    @staticmethod
    def sort(array: List[int]) -> None:
        QuickSort._sort(array, 0, len(array) - 1)

    @staticmethod
    def _sort(array: List[int], low: int, high: int) -> None:
        if low < high:
            # Índice de partition, arr[p] se encuentra ahora en la posición correcta.
            index = QuickSort._partition(array, low, high)
            # Ordenamos los elementos antes y después de la partición de forma separada.
            QuickSort._sort(array, low, index - 1)
            QuickSort._sort(array, index + 1, high)

    @staticmethod
    def _partition(array: List[int], low: int, high: int) -> int:
        """
        Toma el último elemento como pivote, lo coloca en su posición correcta y
        posiciona los elementos menores que él a su izquierda y los mayores a la derecha.
        """
        pivot = array[high]
        # Índice del menor elemento. Indica la posición correcta del pivote hasta el momento.
        i = low - 1

        for j in range(low, high):
            if array[j] < pivot:
                # Incrementamos el índice del menor elemento si el actual es menor que el pivote.
                i += 1
                swap(array, i, j)

        # Movemos el pivote a la posición correcta.
        swap(array, i + 1, high)
        return i + 1
