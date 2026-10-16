class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        
        # --- SOLUTION ---
        n = len(nums)
        expected_sum = n * (n+1) // 2
        return expected_sum - sum(nums)
        
        # --- TIME COMPLEXITY ---
        # O(N) depends on the range of nums

        # --- SPACE COMPLEXITY
        # A(1) as it return the expected one only

        


