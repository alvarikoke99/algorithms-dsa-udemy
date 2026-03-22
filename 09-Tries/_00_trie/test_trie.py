from trie import Trie


def test_trie():
    trie = Trie()

    trie.insert("Day")
    trie.insert("Night")
    trie.insert("Week")
    trie.insert("Year")
    trie.insert("Yellow")
    trie.insert("Dark")

    assert trie.search("Day")
    assert trie.search("Night")
    assert trie.search("Week")
    assert trie.search("Year")
    assert trie.search("Yellow")
    assert trie.search("Dark")
    assert trie.search("Ye")
    assert trie.search("Da")
    assert trie.search("Wee")

    assert not trie.search("Weee")
    assert not trie.search("Morning")
    assert not trie.search("Darke")
    assert not trie.search("Yellowstone")
