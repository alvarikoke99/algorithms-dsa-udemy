from typing import List, Optional


"""
Devuelve una copia profunda (clon) de un grafo conexo y no dirigido. Puedes
utilizar la clase Node que se ve a continuación, más simple que Graph.

Ejemplo:
 Input: Nodo de grafo conexo y no dirigido (desde él se puede llegar a los demás)
 Output: Un clon de ese grafo (nuevos Nodos, no las mismas referencias).
"""


class Node:
    def __init__(self):
        self.val: int = 0
        self.neighbors: List['Node'] = []


class CloneGraph:
    def clone_graph(self, node: Optional[Node]) -> Optional[Node]:
        raise NotImplementedError("Not implemented yet")
