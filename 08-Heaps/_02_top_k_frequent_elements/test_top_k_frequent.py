from .top_k_frequent import TopKFrequent


def test_top_k_frequent():
    top_k_frequent = TopKFrequent()

    first_result = top_k_frequent.top_k_frequent([1, 1, 1, 2, 2, 3], 2)
    first_result.sort()
    assert first_result == [1, 2]

    assert top_k_frequent.top_k_frequent([1, 1, 2, 3, 3, 3], 1) == [3]
