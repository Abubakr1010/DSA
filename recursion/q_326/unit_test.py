import solution



def test_if_not_divisble_retrun_false():

    s = solution.Solution()
    n = 28

    result = s.isPowerOfThree(n)

    assert result is False


def test_if_divisible_return_true():

    s = solution.Solution()
    n = 27

    result = s.isPowerOfThree(n)

    assert result is True


def test_if_divisible_negative_number_return_false():

    s = solution.Solution()
    n = -1

    result = s.isPowerOfThree(n)

    assert result is False