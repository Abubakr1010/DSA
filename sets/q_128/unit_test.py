from solution import longestConsecutive


def test_sequence():

    nums = [100,4,200,1,3,2]
    expected = 4
    result = longestConsecutive(nums)

    assert result == expected


def test_no_sequence():

    nums = []
    expected = 0
    result = longestConsecutive(nums)

    assert result == expected


def test_one_sequence():

    nums = [2,5,8]
    expected = 0
    result = longestConsecutive(nums)

    assert result == expected