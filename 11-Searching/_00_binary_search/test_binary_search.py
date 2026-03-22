from binary_search import BinarySearch, BinarySearchIterative


def test_binary_search():
    binary_search = BinarySearch()
    array = [1, 3, 4, 7, 8, 9, 12, 15, 24, 35, 95]

    assert binary_search.binary_search(array, 1) == 0
    assert binary_search.binary_search(array, 4) == 2
    assert binary_search.binary_search(array, 12) == 6
    assert binary_search.binary_search(array, 95) == 10

    assert binary_search.binary_search(array, 0) == -1
    assert binary_search.binary_search(array, 6) == -1
    assert binary_search.binary_search(array, 13) == -1
    assert binary_search.binary_search(array, 100) == -1


def test_binary_search_iterative():
    binary_search_iterative = BinarySearchIterative()
    array = [1, 3, 4, 7, 8, 9, 12, 15, 24, 35, 95]

    assert binary_search_iterative.binary_search(array, 1) == 0
    assert binary_search_iterative.binary_search(array, 4) == 2
    assert binary_search_iterative.binary_search(array, 12) == 6
    assert binary_search_iterative.binary_search(array, 95) == 10

    assert binary_search_iterative.binary_search(array, 0) == -1
    assert binary_search_iterative.binary_search(array, 6) == -1
    assert binary_search_iterative.binary_search(array, 13) == -1
    assert binary_search_iterative.binary_search(array, 100) == -1
