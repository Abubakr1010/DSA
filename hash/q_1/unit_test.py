from solution import Solution


def test_sum_not_found():

    #arrange
    s = Solution()
    nums = [2,4,6,7]
    target = 12

    #act
    result = s.twoSum(nums, target)

    #asssert
    assert result == []



def test_sum_found():

    #arrange
    s = Solution()
    nums = [2,3,6,7]
    target = 5

    #act
    result = s.twoSum(nums, target)

    #asssert
    assert result == [0,1]



def test_empty_nums():

    #arrange
    s = Solution()
    nums = []
    target = 5

    #act
    result = s.twoSum(nums, target)

    #asssert
    assert result == []
