import pytest
from number_of_one_bits import NumberOfOneBits


def test_number_of_one_bits():
    n = NumberOfOneBits()
    assert n.number_of_one_bits(3) == 2
    assert n.number_of_one_bits(8) == 1
    assert n.number_of_one_bits(7) == 3
