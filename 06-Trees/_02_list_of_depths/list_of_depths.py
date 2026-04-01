"""
Implementa un algoritmo que devuelva una lista enlazada con los nodos de cada nivel. Si el árbol tiene
N niveles debes devolver N listas enlazadas.

Ejemplo:
 Input:
       4
    2     7
  1   3  6  9

 Output:
   4
   2->7
   1->3->6->9
"""
from typing import List, Optional
from collections import deque


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None


class ListOfDepths:
    def list_of_depths(self, root: Optional[Node]) -> List[List[Node]]:
        q = deque([root])
        result = []
        while q:
            current_level = []
            for _ in range(len(q)):
                node = q.popleft()
                current_level.append(node)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            result.append(current_level)
        
        return result
    
    def list_of_depths2(self, root: Optional [Node]) -> List[List[Node]]:
        q = deque()
        q.append((0, root))
        list = []
        while q:
            level, node = q.popleft()

            if node.left: q.append((level+1, node.left))
            if node.right: q.append((level+1, node.right))

            if(len(list) < level+1): list.append([])
            list[level].append(node)
        return list
