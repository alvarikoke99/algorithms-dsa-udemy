import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '_00_linkedlist'))
from single_linked_list import Node
from typing import Optional


"""
Dada una lista enlazada simple y un valor N, devuelve el nodo N empezando por el final

Ejemplo:
 Input: 1->2->4->6, 2
 Output: 4
"""


class NthNodeToLast:

    def nth_node_to_last(self, head: Optional[Node], n: int) -> Optional[Node]:
        raise NotImplementedError("Not implemented yet")
