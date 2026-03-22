"""
Dado un árbol binario, devuelve el camino con mayor suma acumulada.

Nota: Un camino en un árbol es una secuencia de nodos conectados en la que el
mismo nodo no puede aparecer dos veces. El camino no tiene por qué pasar por la
raíz.

Ejemplo 1:
 Input:
       2
    1     3
 -5     -1

 Output:
   6 (path 1-2-3)

Ejemplo 2:
 Input:
      -12
    5     3
        1   4

 Output:
   8 (path 1-3-4)
"""
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None


class BinaryTreeMaxPathSum:
    def max_path_sum(self, root: Optional[TreeNode]) -> int:
        raise NotImplementedError("Not implemented yet")
