# Given a linked list, swap every two adjacent nodes and return its head. 
# You must solve the problem without modifying the values in 
# the list's nodes (i.e., only nodes themselves may be changed.)
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # --- BASE CASE ---

        if head is None or head.next is None:
            return head
        
        seconed = head.next

        new_head = self.swapPairs(head.next.next)

        head.next = new_head
        seconed.next = head

        return seconed

        # --- TIME COMPLEXITY ---
        # O(N) Because the number of steps scales linearly (takes N/2 steps) and still grows

        # --- SPACE COMPLEXITY ----
        # O(N) need an extra call stack

        
        