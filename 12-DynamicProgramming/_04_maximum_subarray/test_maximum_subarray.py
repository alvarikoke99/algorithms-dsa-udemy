from .maximum_subarray import MaximumSubarray


def test_maximum_subarray():
    max_ = MaximumSubarray()
    assert max_.max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_.max_sub_array([5, 4, -1, 7, 8]) == 23
