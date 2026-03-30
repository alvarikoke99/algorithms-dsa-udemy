import pytest
from .zero_matrix import ZeroMatrix


def test_zero_matrix():
    zero_matrix = ZeroMatrix()

    matrix = [
        [2, 1, 3, 0, 2],
        [7, 4, 1, 3, 8],
        [4, 0, 1, 2, 1],
        [9, 3, 4, 1, 9],
    ]
    zeroed_matrix = [[0, 0, 0, 0, 0], [7, 0, 1, 0, 8], [0, 0, 0, 0, 0], [9, 0, 4, 0, 9]]
    zero_matrix.zero_matrix(matrix)
    assert matrix == zeroed_matrix

    matrix2 = [[2, 0, 2], [0, 2, 1], [9, 3, 4]]
    zeroed_matrix2 = [[0, 0, 0], [0, 0, 0], [0, 0, 4]]
    zero_matrix.zero_matrix(matrix2)
    assert matrix2 == zeroed_matrix2
