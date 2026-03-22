"""
Determina si el árbol second es subárbol del árbol first.

Ejemplo 1:
 Input:
   first:
        4
     5     7
   1   3
 8

   second:
        4
     2     7
   1   3  5

 Output: false

Ejemplo 2:
 Input:
   first:
        4
     5     7
   1   3
 8

   second:
        5
     1     3
   8

Output: true
"""
from typing import Optional


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None


class IsSubTree:
    def is_subtree(self, first: Optional[Node], second: Optional[Node]) -> bool:
        raise NotImplementedError("Not implemented yet")
