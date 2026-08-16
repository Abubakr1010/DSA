

class Node():
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def successor(curr):
    curr = curr.right
    while curr is not None and curr.left is not None:
        curr = curr.left
    return curr


def delete_node(root, key):

    if root is None:
        return None

    if root.val < key:
        root.right = delete_node(root.right, key)
    elif root.val > key:
        root.left = delete_node(root.left, key)
    else:
        if root.right is None:
            return root.left
        if root.left is None:
            return  root.right

        #if it has two child only than
        succ = successor(root)
        root.val = succ.val
        root.right = delete_node(root.right, succ.val)

    return root




        

   




        