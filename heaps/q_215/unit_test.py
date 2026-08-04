import solution as solution


def test_if_multiple_same_integers():

    #arrange
    s = solution.Solution()
    n = [2,5,4,6,6,6]
    k = 2
    expected = 6

    result = s.findKthLargest(n, k)

    assert result == expected

