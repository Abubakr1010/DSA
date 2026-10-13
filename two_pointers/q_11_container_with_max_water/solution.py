class Solution:
    def maxArea(self, height: list[int]) -> int:

        # --- EDGE CASE ---
        if height is None:
            return 0
        
        # --- SOLUTION ---
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            width = right - left
            new_height = min(height[left], height[right])
            water = width * new_height

            if water > max_water:
                max_water = water
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
          
        return max_water

        # --- TIME COMPLEXITY ---
        # O(N) number of heights depends making linear time complexity
        # --- SPACE COMPLEXITY ---
        # A(1) as max_water only retain contain memory
        