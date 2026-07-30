#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # --- EDGE CASE ---
        # if len of any string greater than other return false

        if len(s) != len(t):
            return False

        s_count = Counter(s)

        for k in t:
            if k not in s_count:
                return False
            
            s_count[k] -= 1

            if s_count[k] < 0:
                return False
            
        return True

            
         # --- TIME COMPLEXITY ---
         # O(N) counting string will take n length of string
         # O(1) This is becaouse hashmap store no more than 26 lower charachter 



        

        