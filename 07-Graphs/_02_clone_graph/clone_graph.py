from typing import List, Optional, Dict
from collections import deque


"""
Devuelve una copia profunda (clon) de un grafo conexo y no dirigido. Puedes
utilizar la clase Node que se ve a continuación, más simple que Graph.

Ejemplo:
 Input: Nodo de grafo conexo y no dirigido (desde él se puede llegar a los demás)
 Output: Un clon de ese grafo (nuevos Nodos, no las mismas referencias).
"""


class Node:
    def __init__(self, val: int = 0):
        self.val = val
        self.neighbors: List['Node'] = []


class CloneGraph:
    def clone_graph(self, node: Optional[Node]) -> Optional[Node]:
        return self.clone(node, dict())

    def clone(self, node: Optional[Node], map: Optional[Dict[Node]]) -> Optional[Node]:
        if not node:
            return None
        
        if node.val in map:
            return map[node.val]
        
        copy = Node(node.val)
        map[node.val] = copy

        for neighbour in node.neighbors:
            copy.neighbors.append(self.clone(neighbour, map))

        
        return copy