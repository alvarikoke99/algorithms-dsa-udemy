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
        if not head or not head.next:
            return head

        rest = head.next.next
        head.next.next = head
        head = head.next
        head.next.next = self.swap_nodes_in_pairs(rest)

        return head

    def swap_nodes_iter(self, head: Optional[Node]) -> Optional[Node]:
        if not head or not head.next:
            return head

        p1 = head
        p2 = head.next
        result = current = Node(-1)

        while p2:
            current.next = Node(p2.value)
            current.next.next = Node(p1.value)
            current = current.next.next
            p1 = p1.next.next
            p2 = p2.next.next

        if p1:
            current.next = Node(p1.value)

        return result.next