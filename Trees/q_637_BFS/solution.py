# Given the root of a binary tree, return the average value of the nodes on each level 
# in the form of an array. Answers within 10-5 of the actual answer will be accepted.
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        # --- EDGE CASE ---

        if not root:
            return []

        # --- SOLUTION ---

        q = deque([root])
        t_avg = []

        while q:
            level_sum = 0
            level_size = len(q)

            for val in range(level_size):
                node = deque.popleft(q)
                level_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            t_avg.append(level_sum/level_size)

        return t_avg

        # --- TIME COMPLEXITY ---
        # O(N) Depnds on number of node

        # --- SPACE COMPLEXITY ---
        # O(N) q is for temperory space where as avg result stored take extra memory



            
            

