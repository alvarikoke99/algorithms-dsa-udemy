from typing import List, Dict, Optional
from enum import Enum

class Graphnode_numStatus(Enum):
    UNVISITED = 1
    VISITING = 2
    VISITED = 3


class Graphnode_num:
    def __init__(self, value: str):
        self.value = value
        self.adjacents: Dict[str, Graphnode_num] = {}
        self.status = Graphnode_numStatus.UNVISITED

    def add_neighbor(self, node_num: 'Graphnode_num') -> None:
        if node_num.value not in self.adjacents:
            self.adjacents[node_num.value] = node_num

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, Graphnode_num):
            return False
        return self.value == other.value


class Graph:
    def __init__(self):
        self.node_nums: Dict[str, Graphnode_num] = {}

    def get_or_create_node_num(self, name: str) -> Graphnode_num:
        node_num = self.node_nums.get(name)
        if node_num is None:
            node_num = Graphnode_num(name)
            self.node_nums[name] = node_num
        return node_num

    def add_edge(self, start: str, end: str) -> None:
        start_node_num = self.get_or_create_node_num(start)
        end_node_num = self.get_or_create_node_num(end)
        start_node_num.add_neighbor(end_node_num)

    def clear(self):
        for n in self.node_nums.values():
            n.status = Graphnode_numStatus.UNVISITED


"""
Tenemos N ciudades y queremos calcular el número de provincias existentes.
Una provincia la forman todas las ciudades que están conectadas entre sí.

Ejemplo:
 Input:

    a b c
  a 1 1 0
  b 1 1 0
  c 0 0 1

 Output: 2
"""


class NumberOfProvinces:
    def number_of_provinces(self, is_connected: List[List[int]]) -> int:
        size = len(is_connected)
        visited = [0] * size
        counter = 0

        for node in range(size):
            if not visited[node]:
                counter += 1
                self.dfs(is_connected, visited, node)
        return counter


    
    def dfs(self, is_connected: List[List[int]], visited: List[List[int]], node: int):
        for other in range(len(is_connected[node])):
            if node != other and is_connected[node][other] and not visited[other]:
                    visited[other] = 1
                    self.dfs(is_connected, visited, other)