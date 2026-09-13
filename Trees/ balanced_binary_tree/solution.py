# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # --- EDGE CASE ---
        if root is None:
            return True

        # --- BASE CASE ---
        def single_node(node):

            if node is None:
                return 0

            left = single_node(node.left)
            if left == -1:
                return -1

            right = single_node(node.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1
            
            return max(left,right) + 1
        
        return single_node(root) != -1

        # --- TIME COMPLEXITY ---
        # O(N) depend on number of nodes

        # --- SPACE COMPLEXITY ---
        # O(H) depends on height of tree because of call stack


    


      
        





















        
        
        

        