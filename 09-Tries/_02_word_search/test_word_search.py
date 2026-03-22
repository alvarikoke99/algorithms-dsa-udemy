from word_search import WordSearch


def test_word_search():
    word_search = WordSearch()

    board = [
        ['p', 'e', 'r', 'o'],
        ['a', 't', 'a', 'e'],
        ['t', 'e', 'l', 'v'],
        ['o', 'f', 'l', 'v']
    ]

    words = ["pero", "pato", "comida", "veo", "pata"]
    expected_words = sorted(["pero", "pato", "veo", "pata"])

    result = word_search.find_words(board, words)
    result.sort()
    assert list(result) == expected_words
