# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        # TIME COMPLEXITY O(N+M)
        # SPACE COMPLEXITY O(N)
        # FIRST CHECK IF LIST OR B IS EMPTY
        # CREATING POINTERS


        if not headA or not headB:
            return None

        visited_value = set()
        p1 = headA
        p2 = headB

        while p1:
            visited_value.add(p1)
            p1 = p1.next
        
        while p2:
            if p2 in visited_value:
                return p2
            p2 = p2.next
        return None





        