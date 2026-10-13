import solution




def test_check_water_with_same_height():

    height = [1,1]
    func = solution.Solution()
    expected = 1

    result = func.maxArea(height)

    assert result == expected



def test_check_water_with_no_height():

    height = []
    func = solution.Solution()
    expected = 0

    result = func.maxArea(height)

    assert result == expected