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
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         if x == 0 or x == 1:
#             return x

#         low,high = 0,x
#         ans = 0

#         while low <= high:
#             mid = (low+high)//2

#             if mid * mid == x:
#                 return mid

#             elif mid * mid < x:
#                 ans = mid
#                 low = mid + 1

#             else:
#                 high = mid - 1

#         return ans

# 34. Find First and Last Position of Element in Sorted Array
# incomplete
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findBound(isLeft: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    bound = mid  # Potential answer found
                    if isLeft:
                        right = mid - 1  # Keep searching left
                    else:
                        left = mid + 1   # Keep searching right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return bound

        left_index = findBound(True)
        right_index = findBound(False)

        return [left_index, right_index]
