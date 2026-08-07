# Definition for singly-linked list.

# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # --- EDGE CASE ---
        # if no value in head or only one value

        if head is None or not head.next:
            return head
        
        left = right = head

        while right and right.next:
            left = left.next
            right = right.next.next
        return left

        # --- TIME COMPLEXITY ---
        # O(N) because n number of nodes time will determine to find middle node
        
        # --- SPACE COMPLEXITY ---
        # O(1) becaouse no extra space it take as left and right are only pointer 
           
        