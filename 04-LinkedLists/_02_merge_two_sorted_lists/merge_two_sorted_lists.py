import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '_00_linkedlist'))
from single_linked_list import Node
from typing import Optional


"""
Escribe un algoritmo para combinar dos listas enlazadas simples ordenadas.
El resultado debe ser una única lista enlazada ordenada. Devuelve su head.

Ejemplo:
 Input: 1->2->4->6, 2->3->5
 Output: 1->2->2->3->4->5->6
"""


class MergeTwoSortedLists:

    def merge_two_lists(self, list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
        raise NotImplementedError("Not implemented yet")
