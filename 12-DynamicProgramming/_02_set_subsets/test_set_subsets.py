from set_subsets import SetSubsets


def test_set_subsets():
    set_subsets = SetSubsets()

    set_ = [1, 2, 3]
    result = set_subsets.subsets(set_)
    assert [1, 2, 3] in result
    assert [1, 2] in result
    assert [1, 3] in result
    assert [2, 3] in result
    assert [1] in result
    assert [2] in result
    assert [3] in result
    assert [] in result
    assert len(result) == 8
