from redundant_connection import RedundantConnection


def test_redundant_connection():
    redundant_connection = RedundantConnection()

    first = [[1, 2], [1, 3], [2, 3]]
    assert list(redundant_connection.find_redundant_connection(first)) == [2, 3]

    second = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    assert list(redundant_connection.find_redundant_connection(second)) == [1, 4]
