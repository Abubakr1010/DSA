# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?
from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # --EDGE CASES --
        # if nums is empty return []

        if nums is None:
            return []

        heap = []

        for n in nums:
            heapq.heappush(heap,n)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

         # -- TIME COMPLEXITY --
         # O(N log K) becaouse it depend on k len
         # O(K) becaouse we are creating extra heap with K len

