import soloution


def test_if_string_is_palidrome():

    #arrange
    sol = soloution.Solution()
    s = "A man, a plan, a canal: Panama"
    expected = True

    #act
    result = sol.isPalindrome(s)

    #assert
    assert expected == result


if __name__ == "__main__":
    test_if_string_is_palidrome() 



def test_if_string_is_not_palidrome():

    #arrange
    sol = soloution.Solution()
    s = "man, a plan, a canal: Panama"
    expected = False

    #act
    result = sol.isPalindrome(s)

    #assert
    assert expected == result


if __name__ == "__main__":
    test_if_string_is_palidrome() 



def test_if_string_is_empty():

    #arrange
    sol = soloution.Solution()
    s = ""
    expected = True

    #act
    result = sol.isPalindrome(s)

    #assert
    assert expected == result


if __name__ == "__main__":
    test_if_string_is_palidrome() 



def test_if_string_have_nonalphanumeric():

    #arrange
    sol = soloution.Solution()
    s = "$/%"
    expected = True

    #act
    result = sol.isPalindrome(s)

    #assert
    assert expected == result


if __name__ == "__main__":
    test_if_string_is_palidrome() 