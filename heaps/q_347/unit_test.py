import solution


def test_if_k_len_greater_than_nums():

    s = solution.Solution()
    nums = [1,1,1,2,2,3]
    k = 7
    expected = []

    result = s.topKFrequent(nums, k)

    assert result == expected



