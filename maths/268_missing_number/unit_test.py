import solution


def test_missing_number():

    nums = [0,2,3,4]
    expected = 1

    s = solution.Solution()
    result = s.missingNumber(nums)

    assert result == expected



