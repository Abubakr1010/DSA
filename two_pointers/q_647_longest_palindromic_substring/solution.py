class Solution:
    def countSubstrings(self, s: str) -> int:

        # --- EDGE CASE ---
        if s is None:
            return 0
        
        # --- SOULUTION ---
        counter = 0

        l = len(s)
      

        for i in range(l):
            for j in range(i, l):
                substring = s[i:j+1]
                if substring == substring[::-1]:
                    counter += 1
        return counter

        # --- TIME COMPLEXITY ---
        # O(N3) becaluse of nested loop and reversing substring slice
        # --- SPACE COMPLEXITY ---
        # O(1) becaouse counter is auxilary global variable
        # which is just saving the updated count

        
           

        