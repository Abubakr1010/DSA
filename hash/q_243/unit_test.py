import solution


def test_string_greater_in_len():

    #arrange
    a = solution.Solution()
    s = "anagram"
    t = "nagram"

    #arrange
    result = a.isAnagram(s,t)

    #arrange
    assert result is False 


def test_string_same_in_len():

    #arrange
    a = solution.Solution()
    s = "anagram"
    t = "nagaram"

    #arrange
    result = a.isAnagram(s,t)

    #arrange
    assert result is True


def test_string_diff_char():

    #arrange
    a = solution.Solution()
    s = "anagham"
    t = "nagaram"

    #arrange
    result = a.isAnagram(s,t)

    #arrange
    assert result is False


