from typing import Optional


class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None


"""
Dada una lista enlazada, inviértela de k en k nodos.

Ejemplo 1:
 Input:
   head: 1->2->3->4->5->6->7
   k: 3
 Output: 3->2->1->6->5->4->7

Ejemplo 2:
 Input:
   head: 1->2->3->4->5->6->7
   k: 4
 Output: 4->3->2->1->5->6->7
"""


class ReverseNodesKGroup:

    def reverse_k_group(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        raise NotImplementedError("Not implemented yet")
