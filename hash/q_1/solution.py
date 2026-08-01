#You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # --- EDGE CASES ---
        # if list is empty return list

        # --- IMPLEMENTATION ---

        if nums is None:
            return []

        seen = {}

        for i, n in enumerate(nums):
            contain = target - n
            if contain in seen:
                return [seen[contain], i]
            seen[n] = i
        return []

        # --- TIME COMPLEXITY ---
        # O(N) becaouse for loop iterate over each num

        # --- SPACE COMPLEXITY ---
        # O(N) it store new num as keys