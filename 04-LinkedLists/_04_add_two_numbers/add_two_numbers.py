import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '_00_linkedlist'))
from single_linked_list import Node
from typing import Optional


"""
Escribe un algoritmo que realice la suma de dos listas que representan
dos enteros positivos. Las listas están en posición invertida.

Ejemplo:
 Input: 1->2->4, 5->2->8
 Output: 6->4->2->1
 6421 + 825 = 7246
"""


class AddTwoNumbers:

    def add_two_numbers(self, list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
        raise NotImplementedError("Not implemented yet")
