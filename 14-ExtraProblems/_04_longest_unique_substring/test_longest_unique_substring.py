from .longest_unique_substring import LongestUniqueSubstring


def test_longest_unique_substring():
    l = LongestUniqueSubstring()

    assert l.length_of_longest_substring("aabcdefed") == 6
    assert l.length_of_longest_substring("ccccccc") == 1
    assert l.length_of_longest_substring("aabcdefedabcdefghie") == 9
