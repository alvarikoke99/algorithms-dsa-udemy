from typing import List


class BinarySearch:
    def binary_search(self, array: List[int], target: int) -> int:
        return self._binary_search(array, 0, len(array) - 1, target)

    def _binary_search(self, array: List[int], left: int, right: int, target: int) -> int:
        if right >= left:
            mid = left + (right - left) // 2

            # Elemento presente en el elemento central del array.
            if array[mid] == target:
                return mid

            # Si el elemento es menor que el central, se debe encontrar a su izquierda.
            if array[mid] > target:
                return self._binary_search(array, left, mid - 1, target)

            # En caso contrario solo puede encontrarse en la mitad derecha.
            return self._binary_search(array, mid + 1, right, target)

        # El elemento no se ha encontrado.
        return -1


class BinarySearchIterative:
    def binary_search(self, array: List[int], target: int) -> int:
        left = 0
        right = len(array) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if array[mid] == target:
                return mid

            if array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
