# 643. Maximum Average Subarray I

# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and 
# return this value. Any answer with a calculation error less than 10-5 will be accepted.

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # --- EDGE CASE ---
        # if k size > nums return False

        # --- SOLUTION ---

        if k > len(nums):
            return 0.00

        cur_sum = sum(nums[:k])
        max_sum= cur_sum
        

        for right in range(k, len(nums)):
            cur_sum += nums[right] - nums[right-k]
            max_sum = max(cur_sum, max_sum)
        return max_sum / k

          # --- TIME COMLEXITY ---
          # O(N)
          # --- SPACE COMLEXITY ---
          # O(1)





        