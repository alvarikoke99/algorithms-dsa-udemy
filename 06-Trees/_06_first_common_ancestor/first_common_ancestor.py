"""
Devuelve el primer ancestro común de dos nodos.

Ejemplo:
 Input:
        4
     5     7
   1   3
 8

 firstCommonAncestor(1, 7) = 4
 firstCommonAncestor(1, 4) = null
 firstCommonAncestor(1, 3) = 5
"""
from typing import Optional


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None


class FirstCommonAncestor:
    def first_common_ancestor(
        self,
        root: Optional[Node],
        first_node: Optional[Node],
        second_node: Optional[Node],
    ) -> Optional[Node]:
        raise NotImplementedError("Not implemented yet")
