# Given the root of a binary tree, return the inorder traversal of its nodes' values.
from typing import Optional



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # --- BASE CASE ---

        result = []

        def helper(node):
            if not node:
                return
            helper(node.left)
            result.append(node.val)
            helper(node.right)

        helper(root)
        return result

        # --- TIME COMPLEXITY ---
        # O(N) It has to traverser all the nodes so number of nodes define time

        # --- SPACE COMPLEXITY ---
        # O(N) As new memory require for result






    
    