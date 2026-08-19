# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # --- Base Case ---
        # if head is None return -> None

        if head is None:
            return None

        if head.val == val:
            return self.removeElements(head.next, val)
        else:
            head.next = self.removeElements(head.next, val)
        return head

        # --- TIME COMPLEXITY ---
        # O(N) because length of n number nodes matter
        # --- SPACE COMPLEXITY ---
        # O(N) because of stack frame created by inside function call