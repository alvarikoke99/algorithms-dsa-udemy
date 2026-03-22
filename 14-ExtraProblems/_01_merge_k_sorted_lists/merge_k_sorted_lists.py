from typing import List, Optional


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


"""
Dado un array de listas enlazadas, cada una de ellas ordenada de forma ascendente,
combínalas para devolver una única lista enlazada ordenada.

Nota: No está permitido almacenar todos los valores de los nodos para ordenarlos de forma
separada y crear una nueva lista enlazada a partir de ese resultado.

Ejemplo:
 Input:
   [
      1->4->5,
      1->3->4,
      2->6
   ]
  Output:
    1->1->2->3->4->4->5->6
"""


class MergeKSortedLists:

    def merge_k_lists(self, lists: List[Optional[Node]]) -> Optional[Node]:
        raise NotImplementedError("Not implemented yet")
