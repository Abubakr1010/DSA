# 704. Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[left] < target:
                left =  mid + 1
            else:
                right = mid - 1
        
        return -1
    
# 69. Sqrt(x)
def mySqrt(x):
    if x == 0 or x == 1:
        return x  # Base cases