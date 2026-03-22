import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '_00_linkedlist'))
from single_linked_list import Node
from typing import Optional


"""
Escribe un algoritmo que intercambie parejas de nodos adyacentes sin
modificar el valor interno de los nodos.

Ejemplo:
 Input: 1->2->4->6->8
 Output: 2->1->6->4->8
"""


class SwapNodesInPairs:

    def swap_nodes_in_pairs(self, head: Optional[Node]) -> Optional[Node]:
        raise NotImplementedError("Not implemented yet")
