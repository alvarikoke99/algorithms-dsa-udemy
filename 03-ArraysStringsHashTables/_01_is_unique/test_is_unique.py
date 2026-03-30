import pytest
from .is_unique import IsUnique


def test_is_unique():
    is_unique = IsUnique()
    assert is_unique.is_unique("abcde")
    assert is_unique.is_unique("aAbBcCdDeE")
    assert not is_unique.is_unique("abcded")
