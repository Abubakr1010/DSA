import solution
import pytest


def test_float_avg():

    #arrange
    s = solution.Solution()
    nums = [2.2,4,7,8.23,9]
    k = 4
    expected = 7.0576

    #act
    result = s.findMaxAverage(nums, k)  

    #assert
    assert result == pytest.approx(expected, abs=1e-4)


def test_negative_float_avg():

    #arrange
    s = solution.Solution()
    nums = [2.2,4,7,-8.23,9]
    k = 4
    expected = 2.94250

    #act
    result = s.findMaxAverage(nums, k)  

    #assert
    assert result == pytest.approx(expected, abs=1e-4)



