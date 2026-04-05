from enum import Enum
from typing import Dict, List, Optional

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

"""
Dada una lista de proyectos y las dependencias entre ellos, devuelve un orden de
compilación válido para dichos proyectos.

La lista de dependencias es una lista de pares de strings (a, b), que indican que el
proyecto b depende del a (el a debe ser compilado con antelación).

Ejemplo 1:
 Input:
   projects: a, b, c, d
   dependencies: [(a, b), (a, c), (a, d), (c, b), (d, b), (d, c)]
 Output: a, d, c, b

Ejemplo2:
 Input:
   projects: a, b, c, d
   dependencies: [(a, b), (b, c), (c, d), (d, a)]
 Output: Lanza excepción. No se puede construir ya que se forma un ciclo.
"""


class BuildOrder:
    def build_order(self, projects: List[str], dependencies: List[List[str]]) -> List[str]:
        graph = self.build_graph(projects, dependencies)
        ordered_projects = []

        for node in graph.nodes.values():
          self.dfs(node, ordered_projects)

        ordered_projects.reverse()
        return ordered_projects

    def dfs(self, node: GraphNode, sorted_projects: List[str]):
        if not node:
            return
        
        if node.status is GraphNodeStatus.UNVISITED:
          node.status = GraphNodeStatus.VISITING

          for neighbour in node.adjacents.values():
              self.dfs(neighbour, sorted_projects)

          node.status = GraphNodeStatus.VISITED
          sorted_projects.append(node.value)

        if node.status is GraphNodeStatus.VISITING:
          raise Exception
    
    def build_graph(self, projects: List[str], dependencies: List[List[str]]) -> Graph:
      g = Graph()

      for p in projects:
          g.get_or_create_node(p)

      for restriction in dependencies:
          g.add_edge(restriction[0], restriction[1])

      return g
