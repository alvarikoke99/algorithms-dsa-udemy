from .title_suggestions import TitleSuggestions


def test_title_suggestions():
    title_suggestions = TitleSuggestions()

    books = ["Whatever", "Book 1", "water", "Book 35"]
    prefixes = ["Wo", "Wa", "Boo", "fr"]

    assert list(title_suggestions.title_suggestions(books, prefixes, False)) == [False, False, True, False]
    assert list(title_suggestions.title_suggestions(books, prefixes, True)) == [False, True, True, False]
