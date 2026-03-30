import pytest
from .two_sum import TwoSum


def test_two_sum():
    array = [9, 2, 5, 6]
    two_sum = TwoSum()
    result = two_sum.two_sum(array, 7)
    assert (result[0] == 1 and result[1] == 2) or (result[0] == 2 and result[1] == 1)
    assert two_sum.two_sum(array, 50) is None
