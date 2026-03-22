from word_break import WordBreak


def test_word_break():
    word_break = WordBreak()

    assert word_break.word_break("applepenapple", ["apple", "pen"])
    assert not word_break.word_break("catsandog", ["cats", "dog", "sand", "and", "cat"])
