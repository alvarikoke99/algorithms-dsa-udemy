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
        if not head:
            return None

        p1 = p2 = head
        cont = 0
        while cont < n:
            if not p1:
                return None
            p1 = p1.next
            cont +=1

        while p1:
            p1 = p1.next
            p2 = p2.next

        return p2