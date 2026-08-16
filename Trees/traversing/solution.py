

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
        print(root.value)
        self.inorder_traverse(root.right)

        return root

    # root > left > right
    def preorder_traverse(self, root):

        if root is None:
            return None

        print (root.value)
        self.preorder_traverse(root.left)
        self.preorder_traverse(root.right)

        return root


    # left > right > root
    def postoreder_traverse(self, root):

        if root is None:
            return None

        self.postoreder_traverse(root.left)
        self.postoreder_traverse(root.right)
        print(root.value)

        return root

        


