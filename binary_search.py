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
left = 0
        right = len(nums)-1
        bound = -1

        while left <= right:
            mid = (left+right)//2
            if nums[mid]==target:
                bound = mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return bound

