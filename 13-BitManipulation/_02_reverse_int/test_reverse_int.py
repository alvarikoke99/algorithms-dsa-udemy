import pytest
from .reverse_int import ReverseInt


def test_reverse_int():
    r = ReverseInt()
    assert r.reverse_bits(43261596) == 964176192
    assert r.reverse_bits(-5) == -536870913
