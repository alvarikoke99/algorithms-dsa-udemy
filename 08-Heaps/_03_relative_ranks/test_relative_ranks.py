from .relative_ranks import RelativeRanks


def test_relative_ranks():
    relative_ranks = RelativeRanks()

    scores = [10, 3, 8, 9, 4]
    result = ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]
    assert list(relative_ranks.find_relative_ranks(scores)) == result
