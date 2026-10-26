# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
 
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
         
        slow = head
        fast = head

        while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
        
        prev = None
        curr = slow.next
        slow.next = None

        while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
        first = head
        second = prev

        while second:
                tmp1, tmp2 = first.next, second.next
                first.next = second
                second.next = tmp1
                first = tmp1
                second = tmp2

    
    # --- TIME COMPLEXITY ---
    # O(N) traversing list at contant time

    # --- SPACE COMPLEXITY ---
    # O(1) Using few variable modified the list as they use constant memory



                

