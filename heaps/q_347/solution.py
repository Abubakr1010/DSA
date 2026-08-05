# Given an integer array nums and an integer k, return the k most frequent elements. 
# You may return the answer in any order.
from typing import List
import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         # --- EDGE CASE ---
        if k > len(nums):
            return []
        # --- SOLUTION ---
        hash = Counter(nums)
        heap = []

        for n, f in hash.items():
            heapq.heappush(heap, (f,n))
            if len(heap) > k:
                heapq.heappop(heap)
        return [n for f, n in heap]

        # --- TIME COMPLEXITY ---
        # O(N LOG K) becaouse k determine the size of heap
        # O(N) becaouse hash store the count of each integer



        


            
        
        