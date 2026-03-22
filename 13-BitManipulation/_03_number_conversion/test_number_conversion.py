import pytest
from number_conversion import NumberConversion


def test_number_conversion():
    n = NumberConversion()
    assert n.number_of_bits_to_flip_to_convert(5, 8) == 3
    assert n.number_of_bits_to_flip_to_convert(8, 8) == 0
    assert n.number_of_bits_to_flip_to_convert(5, 7) == 1
