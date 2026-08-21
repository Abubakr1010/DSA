# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head

        # --- TIME COMPLEXITY ---
        # O(N) becaouse it depend on N number of nodes

        # --- SPACE COMPLEXITY ---
        # O(N) becaouse it is head heavy and call stack is created inside



 
        