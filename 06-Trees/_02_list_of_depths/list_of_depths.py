"""
Implementa un algoritmo que devuelva una lista enlazada con los nodos de cada nivel. Si el árbol tiene
N niveles debes devolver N listas enlazadas.

Ejemplo:
 Input:
       4
    2     7
  1   3  6  9

 Output:
   4
   2->7
   1->3->6->9
"""
from typing import List, Optional


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None


class ListOfDepths:
    def list_of_depths(self, root: Optional[Node]) -> List[List[Node]]:
        raise NotImplementedError("Not implemented yet")
