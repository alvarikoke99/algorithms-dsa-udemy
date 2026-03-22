"""
Dada la raíz de un árbol binario, devuelve el árbol binario invertido.

Ejemplo:
 Input:
       4
    2     7
  1   3  6  9

 Output:
       4
    7     2
  9   6  3  1
"""
from typing import Optional


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None


class InvertBinaryTree:
    def invert_tree(self, root: Optional[Node]) -> Optional[Node]:
        raise NotImplementedError("Not implemented yet")
