from enum import Enum
from typing import Dict, Optional


class GraphNodeStatus(Enum):
    UNVISITED = "UNVISITED"
    VISITING = "VISITING"
    VISITED = "VISITED"


class GraphNode:
    def __init__(self, value: str):
        self.value = value
        self.adjacents: Dict[str, 'GraphNode'] = {}
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


"""
Dado un grafo dirigido y dos nodos, determina si hay un camino start-end

Ejemplo: (Matriz de adyacencia que hemos visto en la teoría):

     0 1 2 3 4

  0  0 0 0 0 0
  1  0 0 0 0 0
  2  0 1 0 0 0
  3  0 0 1 0 0
  4  0 1 0 1 0

isRouteBetween(2, 4) = false
isRouteBetween(3, 1) = true
isRouteBetween(0, 1) = false
isRouteBetween(0, 0) = true
"""


class RouteBetweenNodes:
    def is_route_between(self, g: Graph, start: GraphNode, end: GraphNode) -> bool:
        raise NotImplementedError("Not implemented yet")
