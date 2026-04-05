from enum import Enum
from typing import Dict, List, Set
from collections import defaultdict

class GraphNodeStatus(Enum):
    UNVISITED = 1
    VISITING = 2
    VISITED = 3


class GraphNode:
    def __init__(self, value: str):
        self.value = value
        self.adjacents: Dict[str, GraphNode] = {}
        self.status = GraphNodeStatus.UNVISITED

    def add_neighbor(self, node: 'GraphNode') -> None:
        if node.value not in self.adjacents:
            self.adjacents[node.value] = node

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, GraphNode):
            return False
        return self.value == other.value


class Graph:
    def __init__(self):
        self.nodes: Dict[str, GraphNode] = {}

    def get_or_create_node(self, name: str) -> GraphNode:
        node = self.nodes.get(name)
        if node is None:
            node = GraphNode(name)
            self.nodes[name] = node
        return node

    def add_edge(self, start: str, end: str) -> None:
        start_node = self.get_or_create_node(start)
        end_node = self.get_or_create_node(end)
        start_node.add_neighbor(end_node)

    def clear(self):
        for n in self.nodes.values():
            n.status = GraphNodeStatus.UNVISITED

    def __str__(self):
        string = ""
        for num, node in self.nodes.items():
            string += f"NODE: {num} -> "
            for a in node.adjacents:
                string += f"|{a}"
            string += "\n"
        return string



"""
Dado un grafo formado tras añadir una arista entre dos nodos de un árbol, devuelve
la arista que puede ser eliminada para volver a formar un árbol.

En caso de existir múltiples soluciones, devuelve la última arista del input.

Ejemplo 1:
 Input: [[1,2],[1,3],[2,3]]
 Output: [2,3]

Ejemplo 2:
 Input: [[1,2],[2,3],[3,4],[1,4],[1,5]]
 Output: [1,4]
"""


class RedundantConnection:
    def find_redundant_connection(self, edges: List[List[int]]) -> List[int]:
        graph: Dict[Set[int]] = defaultdict(set)
        redundant = []
        for edge in edges:
            if self.check_path(graph, edge[0], edge[1], set()):
                redundant = edge
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        return redundant

    def check_path_obj(self, current: GraphNode, target: GraphNode) -> bool:
        if not current:
            return False
        if current is target:
            return True
        
        current.status = GraphNodeStatus.VISITED
        
        for neigbour in current.adjacents.values():
            if neigbour.status is not GraphNodeStatus.VISITED: 
                if self.check_path(neigbour, target):
                    return True
        return False
    
    def check_path(self, graph: List[Set[int]], current: int, target: int, visited: Set[int] = None) -> bool:
        if current == target:
            return True
        visited.add(current)
        for neighbour in graph[current]:
            if neighbour not in visited: # Avoid loops as graph is bi-directional
                if self.check_path(graph, neighbour, target, visited):
                    return True
        return False
