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
    def is_subtree_rec(self, first: Optional[Node], second: Optional[Node]) -> bool:
      if not first:
        return False
      if not second:
        return True
      if first.value == second.value:
        return self.is_same(first, second)
      else:
        return self.is_subtree(first.left, second) or self.is_subtree(first.right, second)
      
    def is_same(self, first: Optional[Node], second: Optional[Node]) -> bool:
       if not first and not second: 
          return True
       if not first or not second:
          return False
       return (first.value == second.value) and self.is_same(first.left, second.left) and self.is_same(first.right, second.right)
    
    def is_subtree(self, first: Optional[Node], second: Optional[Node]) -> bool:
      s1 = "".join(self.pre_order(first))
      s2 = "".join(self.pre_order(second))

      return s2 in s1
      
    def pre_order(self, root: Optional[Node]) -> Optional[list]:
      if not root:
         return ["#"]
      list = [f"{root.value}"]
      list.extend(self.pre_order(root.left))
      list.extend(self.pre_order(root.right))
      return list

