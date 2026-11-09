


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        

        def get_leaf(root):
            # --- BASE COMPLEXITY ---
            if root is None:
                return []

            if root.left is None and root.right is None:
                return [root.val]
        
            return get_leaf(root.left) + get_leaf(root.right)
    

        return get_leaf(root1) == get_leaf(root2)

    
    # --- TIME COMPLEXITY ---
    # O(N1 + N2) depends on height of the tree

    # --- SPACE COMPLEXITY ---
    # O(H1 + H2 + L1 + L2) number of leaf nodes added