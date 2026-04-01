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
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

class AncestorStatus:
    def __init__(self, ancestor_node: Optional[Node] = None, found: bool = False):
        self.ancestor_node = ancestor_node
        self.found = found

    def __str__(self):
        node_val = self.ancestor_node.value if self.ancestor_node else "None"
        return f"Status: Found={self.found}, Ancestor={node_val}"


class FirstCommonAncestor:
    def first_common_ancestor(
        self,
        root: Optional[Node],
        first_node: Node,
        second_node: Node,
    ) -> Optional[Node]:
        result = self.first_common_ancestor_aux(root, first_node, second_node)
        print(result)
        return result.ancestor_node

    def first_common_ancestor_aux(
        self,
        root: Optional[Node],
        first_node: Node,
        second_node: Node,
    ) -> Optional[AncestorStatus]:
        if not root:
            return AncestorStatus()
        
        leftResult = self.first_common_ancestor_aux(root.left, first_node, second_node)
        if leftResult.ancestor_node:
            return leftResult
        
        rightResult = self.first_common_ancestor_aux(root.right, first_node, second_node)
        if rightResult.ancestor_node:
            return rightResult
        
        if leftResult.found and rightResult.found:
            return AncestorStatus(root, True)
        
        current_status = AncestorStatus()
        if root is first_node or root is second_node:
            current_status.found = True

        if (leftResult.found or rightResult.found) and current_status.found:
            current_status.ancestor_node = root

        if leftResult.found or rightResult.found:
            current_status.found = True
        return current_status
        
    def post_order(self, root: Optional[Node]) -> Optional[list]:
        result = []
        self._traverse(root, result)
        return result

    def _traverse(self, root: Optional[Node], result: list):
        if root:
            self._traverse(root.left, result)
            self._traverse(root.right, result)
            result.append(root.value)
