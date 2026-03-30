from .valid_parenthesis import ValidParenthesis


def test_valid_parenthesis():
    valid_parenthesis = ValidParenthesis()

    assert valid_parenthesis.is_valid("([]){}")
    assert not valid_parenthesis.is_valid("({)}")
