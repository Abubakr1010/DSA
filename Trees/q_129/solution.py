# Definition for a binary tree node.
# You are given the root of a binary tree containing digits from 0 to 9 only.

# Each root-to-leaf path in the tree represents a number.

# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. 
# Test cases are generated so that the answer will fit in a 32-bit integer.

# A leaf node is a node with no children.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def curr(node, integers= ""):

            if node is None:
                return 0

            # --- BASE CASE ---

            if not node.left and not node.right:
                return int(integers + str(node.val))

            left = curr(node.left, integers + str(node.val))
            right = curr(node.right, integers + str(node.val))

            return left + right
        
        return curr(root, "")

        # --- TIME COMPLEXITY ---
        # O(N) height of tree will determine time

         # --- SPACE COMPLEXITY ---
        # O(N) A new call stack created on every recursin call


        






        

        




        
        