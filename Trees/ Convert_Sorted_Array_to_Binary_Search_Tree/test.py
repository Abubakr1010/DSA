from solution import TreeNode, Solution


def test_sortedArrayToBST():

   # arrange
    sol = Solution()
    nums = [-10, -3, 0, 5, 9]

    # act
    result = sol.sortedArrayToBST(nums)

    # assert
    assert result.val == 0
    assert sol.sortedArrayToBST([]) is None
    print ("Tests passed")

if __name__ == "__main__":
    test_sortedArrayToBST() 

