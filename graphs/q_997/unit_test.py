import solution


def test_find_judge_in_the_town():

    #arrange
    n = 3
    trust = [[1,3],[2,3]]
    judge = solution.Solution()
    expected_result = 3

    #act
    actual_result = judge.findJudge(n, trust)

    #assert
    assert actual_result == expected_result, f' the {actual_result} is equal to {expected_result} 🥳'


if __name__ == "__main__":
    test_find_judge_in_the_town()





