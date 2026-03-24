"""
Dada una matriz, escribe un algoritmo para establecer ceros en la fila F y columna C si existe un
0 en la celda F:C

Ejemplo:
 Input: 2 1 3 0 2
        7 4 1 3 8
        4 0 1 2 1
        9 3 4 1 9

 Output: 0 0 0 0 0
         7 0 1 0 8
         0 0 0 0 0
         9 0 4 0 9

Temporal: O(F*C + z*F)
Espacial: O(C)
"""
from typing import List


class ZeroMatrix:

    def zero_matrix(self, matrix: List[List[int]]) -> None:
        zero_columns = set()
        row_len = len(matrix[0])
        for i, row in enumerate(matrix):
            for j, value in enumerate(matrix[i]):
                if value == 0:
                    matrix[i] = [0] * row_len
                    zero_columns.add(j)
                    break

        for column in zero_columns:
            for i, row in enumerate(matrix):
                matrix[i][column] = 0