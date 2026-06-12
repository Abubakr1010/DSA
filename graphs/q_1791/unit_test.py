import solution

def test_find_center():
    #arrange
    sol = solution.Solution()
    edges = [[1,5],[2,5],[3,5]]
    expected_result = 5

    #act
    result = sol.findCenter(edges)

    #assert
    assert result == expected_result, f"Expected center to be {expected_result} but we have {result}"
    

if __name__ == "__main__":
    test_find_center() 