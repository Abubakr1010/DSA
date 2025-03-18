#All leetcode solutions related sliding window


# # 1652. Defuse the Bomb

# class Solution:
#     def decrypt(self, code: List[int], k: int) -> List[int]:
#         n = len(code)
#         if k == 0:
#             return [0] * n  # If k == 0, replace all numbers with 0

#         decrypted = [0] * n  # Initialize the result array

#         for i in range(n):
#             total = 0
#             if k > 0:  # Sum next k elements
#                 for j in range(1, k + 1):
#                     total += code[(i + j) % n]  # Circular indexing
#             else:  # Sum previous |k| elements
#                 for j in range(1, abs(k) + 1):
#                     total += code[(i - j) % n]  # Circular indexing
#             decrypted[i] = total  # Store the sum

#         return decrypted


# Testing and learning basic slidng window cocept

# def max_sum_sub_array(arr, k):
#     max_sum = float('inf')
#     window_sum = sum(arr[:k])
#     max_sum = window_sum

#     for i in range(len(arr) - k):
#         window_sum = window_sum - arr[i] + arr[i + k]
#         max_sum = max(max_sum, window_sum)

#     return max_sum

# arr = [2,1,5,1,3,2]
# k = 3

# print (max_sum_sub_array(arr, k))



# 209. Minimum Size Subarray Sum
# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         n = len(nums)
#         left = 0
#         min_value = float('inf')
#         current_sum = 0

#         for right in range(n):
#             current_sum += nums[right]

#             while current_sum >= target:
#                 min_value = min(min_value, right - left + 1)
#                 current_sum -= nums[left]
#                 left += 1

#         return min_value if min_value != float('inf') else 0




# 219. Contains Duplicate II
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for i in range(len(nums)):
            if nums[i] in window:
                return True

            window.add(nums[i])

            if len(window) > k:
                window.remove(nums[i - k])
            
        return False
    
#Q3





