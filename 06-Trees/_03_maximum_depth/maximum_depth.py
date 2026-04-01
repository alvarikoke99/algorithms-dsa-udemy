"""
Dada la raíz de un árbol binario, devuelve su profundidad máxima.

Ejemplo:
 Input:
        4
     2     7
   1   3
 8

 Output: 4
"""
from typing import Optional
from collections import deque


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None


class MaximumDepth:
    def max_depth(self, root: Optional[Node]) -> int:
        if not root:
            return 0
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))
    
    def max_depth_iterative(self, root: Optional[Node]) -> int:
        if not root:
            return 0
        
        q = deque([root])
        depth = 0
        
        while q:
            depth += 1
            
            for _ in range(len(q)):
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
        return depth