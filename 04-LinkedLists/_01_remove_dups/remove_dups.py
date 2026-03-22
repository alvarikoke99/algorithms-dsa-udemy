import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '_00_linkedlist'))
from single_linked_list import Node


"""
Escribe un algoritmo para eliminar los elementos duplicados en una Lista enlazada

Ejemplo:
 Input: 1->2->2->3->4->1
 Output: 1->2->3->4

Follow-up: ¿Cuál sería tu solución si no pudieras utilizar memoria adicional?
"""


class RemoveDups:

    def remove_dups(self, head: Node) -> None:
        raise NotImplementedError("Not implemented yet")
