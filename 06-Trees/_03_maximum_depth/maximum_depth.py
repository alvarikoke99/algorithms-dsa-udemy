"""
Dada la raíz de un árbol binario, devuelve su profundidad máxima.

Ejemplo:
 Input:
        4
     2     7
   1   3
 8

 Output: 4
"""
from typing import Optional


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None


class MaximumDepth:
    def max_depth(self, root: Optional[Node]) -> int:
        raise NotImplementedError("Not implemented yet")
