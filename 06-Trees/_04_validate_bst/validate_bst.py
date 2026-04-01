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
      return self.is_valid_bst_aux(root, None, None)
    
    def is_valid_bst_aux(self, root: Optional[Node], min: Optional[int], max: Optional[int]) -> bool:
      if not root:
        return True
      if min is not None and root.value <= min:  
        return False 
      if max is not None and root.value > max:
         return False
      return self.is_valid_bst_aux(root.left, min, root.value) and self.is_valid_bst_aux(root.right, root.value, max)
