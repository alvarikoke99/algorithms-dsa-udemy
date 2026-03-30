from .kth_largest import KthLargest


def test_kth_largest_element():
    kth_largest = KthLargest(4, [1, 2, 3, 4, 5])

    assert kth_largest.add(6) == 3
    assert kth_largest.add(2) == 3
    assert kth_largest.add(1) == 3
    assert kth_largest.add(8) == 4
