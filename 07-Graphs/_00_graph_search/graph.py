from enum import Enum
from collections import deque
from typing import Dict, Optional


class GraphNodeStatus(Enum):
    UNVISITED = "UNVISITED"
    VISITING = "VISITING"
    VISITED = "VISITED"


class GraphNode:
    def __init__(self, value: str, adjacents: Optional[Dict[str, 'GraphNode']] = None):
        self.value = value
        self.adjacents: Dict[str, 'GraphNode'] = adjacents if adjacents is not None else {}
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


class BreadthFirstSearch:
    @staticmethod
    def breadth_first_search(graph: Graph, target: str) -> bool:
        for node in graph.nodes.values():
            if BreadthFirstSearch._single_bfs_helper(node, target):
                return True
        return False

    @staticmethod
    def _single_bfs_helper(node: GraphNode, target: str) -> bool:
        queue: deque = deque()
        queue.append(node)

        while queue:
            current_node = queue.popleft()

            if current_node.value == target:
                return True

            current_node.status = GraphNodeStatus.VISITED

            for adj in current_node.adjacents.values():
                if adj.status == GraphNodeStatus.UNVISITED:
                    queue.append(adj)

        return False


class DepthFirstSearch:
    @staticmethod
    def depth_first_search(graph: Graph, target: str) -> bool:
        for node in graph.nodes.values():
            if DepthFirstSearch._recursive_dfs_helper(node, target):
                return True
        return False

    @staticmethod
    def _recursive_dfs_helper(current_node: GraphNode, target: str) -> bool:
        if current_node.value == target:
            return True

        current_node.status = GraphNodeStatus.VISITED

        for node in current_node.adjacents.values():
            if node.status != GraphNodeStatus.VISITED:
                if DepthFirstSearch._recursive_dfs_helper(node, target):
                    return True

        return False
