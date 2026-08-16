

class Node:

    def __init__(self,val):
        self.left = None
        self.right = None
        self.value = val

    # left > root > right
    def inorder_traverse(self, root):

        if root is None:
            return None

        self.inorder_traverse(root.left)
        print(root.val)
        self.inorder_traverse(root.right)

        return root

    # root > left > right
    def preorder_traverse(self, root):

        if root is None:
            return None

        print (root.val)
        self.preorder_traverse(root.left)
        self.preorder_traverse(root.right)

        return root


    # left > right > root
    def postoreder_traverse(self, root):

        if root is None:
            return None

        self.postoreder_traverse(root.left)
        self.postoreder_traverse(root.right)
        print(root.val)

        return root

    def list_inorder_traverse(self, root, result=None):

        if result is None:
            result = []

        if root is not None:
            self.list_inorder_traverse(root.left, result)
            result.append(root.val)
            self.list_inorder_traverse(root.right, result)

        return root
        


