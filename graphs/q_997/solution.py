from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

      if n is None:
        return -1

      scores = [0] * (n+1)

      for a,b in trust:
        scores[a] -= 1
        scores[b] += 1

      for i in range(1, n+1):
        if scores[i] == n-1:
            return i
      return -1 


      # --- TIME COMPLEXITY ---
      # O(V+E) depends on number of vertex
      # --- SPACE COMPLEXITY ---
      # O(V) number ov vertex creates score

      

    


        