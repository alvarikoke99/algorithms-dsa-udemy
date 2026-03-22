import pytest
from group_anagrams import GroupAnagrams


def contains_all(anagrams, group):
    for g in anagrams:
        if all(w in g for w in group):
            return True
    return False


def test_group_anagrams():
    group_anagrams = GroupAnagrams()
    empty = group_anagrams.group_anagrams([])
    assert len(empty) == 0

    anagrams = group_anagrams.group_anagrams(["saco", "arresto", "programa", "rastreo", "caso"])
    assert len(anagrams) == 3
    assert contains_all(anagrams, ["programa"])
    assert contains_all(anagrams, ["caso", "saco"])
    assert contains_all(anagrams, ["arresto", "rastreo"])
