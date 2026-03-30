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
        if not list1:
            return list2
        if not list2:
            return list1

        ordered = Node()
        current = ordered
        while list1 and list2:
            if list1.value <= list2.value:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if not list1:
            current.next = list2
        else:
            current.next = list1

        return ordered.next