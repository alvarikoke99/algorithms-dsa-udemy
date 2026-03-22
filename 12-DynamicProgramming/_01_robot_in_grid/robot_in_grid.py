"""
Un robot está en la esquina superior izquierda (0,0) de un tablero m x n. En el tablero hay celdas
transitables (true) y no transitables (false). Encuentra un camino válido para ir a la esquina
inferior izquierda con el robot, sabiendo que solo se puede mover hacia abajo y hacia la derecha.

Ejemplo 1:
 Input:
   [
     [true,true,true,true]
     [false,false,false,true]
     [true,true,false,true]
     [true,true,false,true]
   ]

 Output: [(0,0), (0,1), (0,2), (0,3), (1,3), (2,3), (3,3)]

Ejemplo 2:
 Input:
   [
     [true,true,true,true]
     [false,true,true,true]
     [true,true,false,false]
     [true,true,true,true]
   ]

 Output: [(0,0), (0,1), (1,1), (2,1), (3,1), (3,2), (3,3)]
"""
from typing import List, Optional
from typing import Tuple


class Cell:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Cell):
            return False
        return self.row == other.row and self.col == other.col

    def __hash__(self) -> int:
        prime = 31
        result = 1
        result = prime * result + self.row
        result = prime * result + self.col
        return result

    def __repr__(self) -> str:
        return f"Cell({self.row}, {self.col})"


class RobotInGrid:
    def get_path(self, grid: List[List[bool]]) -> Optional[List[Cell]]:
        raise NotImplementedError("Not implemented yet")
