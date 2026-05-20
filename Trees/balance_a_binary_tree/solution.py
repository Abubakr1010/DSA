# 1382. Balance a Binary Search Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #right some formulas
        # for height check max(left , right) +1
        # for balance factor if abs(left - right) > 1 return unbalance which is -1

        #first we will add all nodes

        sorted_nodes = []

        def sort(node):

            if not node:
                return

            sort(node.left)
            sorted_nodes.append(node)
            sort(node.right)
        
        sort(root)

        # lets balance tree here
        def balance_tree(left_idx, right_idx):
            if left_idx > right_idx:
                 return None

            mid = (left_idx + right_idx) // 2
            current_node = sorted_nodes[mid]

            current_node.left= balance_tree(left_idx, mid-1)
            current_node.right= balance_tree(mid+1, right_idx)

            return current_node

        return balance_tree(0, len(sorted_nodes) - 1)

            
