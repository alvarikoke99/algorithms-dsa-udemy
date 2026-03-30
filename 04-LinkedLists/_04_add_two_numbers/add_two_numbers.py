from single_linked_list import Node
from typing import Optional


"""
Escribe un algoritmo que realice la suma de dos listas que representan
dos enteros positivos. Las listas están en posición invertida.

Ejemplo:
 Input: 1->2->4->6, 5->2->8
 Output: 6->4->2->1
 6421 + 825 = 7246
"""


class AddTwoNumbers:

    def add_two_numbers(self, list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
        if not list1:
            return list2
        if not list2:
            return list1

        result = current = Node(-1)
        carry = 0

        while list1 or list2:
            sum = carry
            
            if list1:
                sum += list1.value
                list1 = list1.next

            if list2:
                sum += list2.value
                list2 = list2.next

            carry = sum // 10
            sum = sum % 10
            
            current.next = Node(sum)
            current = current.next

        if carry > 0:
            current.next = Node(carry)

        return result.next