import solution


def test_check_if_empty_string():

    s = ""
    word_count = [""]
    expected = True

    result = solution.wordBreak(s , word_count)
    assert result == expected
