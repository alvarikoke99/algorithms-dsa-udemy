from generate_parenthesis import GenerateParenthesis


def test_generate_parenthesis():
    gp = GenerateParenthesis()

    result = gp.generate_parenthesis(3)
    assert "((()))" in result
    assert "(()())" in result
    assert "(())()" in result
    assert "()(())" in result
    assert "()()()" in result
    assert len(result) == 5
