# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
      
      # --- BASE CASE ---
      if not root:
        return 0

      left = self.maxDepth(root.left)
      right = self.maxDepth(root.right)

      max_depth = max(left, right) + 1

      return max_depth

      # --- TIME COMPLEXITY ---
      # O(N) number of nodes

      # --- SPACE COMPLEXITY ---
      # O(H) sdepends on height of tree becaouse of each call stack


      
        