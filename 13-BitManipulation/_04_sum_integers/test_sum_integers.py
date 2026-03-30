import pytest
from .sum_integers import SumIntegers


def test_sum_integers():
    sum_integers = SumIntegers()
    assert sum_integers.get_sum(2, 5) == 7
    assert sum_integers.get_sum(1, 3) == 4
    assert sum_integers.get_sum(10, 13) == 23
    assert sum_integers.get_sum(3, -8) == -5
    assert sum_integers.get_sum(-3, -7) == -10
