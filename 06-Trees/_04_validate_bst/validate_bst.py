"""
Determina si un árbol binario es un árbol binario de búsqueda válido:
 - El subárbol izquierdo de un nodo contiene solamente nodos <= que él.
 - El subárbol derecho de un nodo contiene solamente nodos > que él.
 - Ambos subárboles deben ser a su vez árboles binarios de búsqueda.

Ejemplo 1:
 Input:
        4
     5     7
   1   3
 8

 Output: false

Ejemplo 2:
 Input:
        4
     2     7
   1   3  5

 Output: true
"""
from typing import Optional


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None


class ValidateBST:
    def is_valid_bst(self, root: Optional[Node]) -> bool:
        raise NotImplementedError("Not implemented yet")
