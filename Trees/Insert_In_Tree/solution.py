


class Node:

    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def insert_node(root, new_val):

    if root is None:
        return Node(new_val)

    if root.val == new_val:
        return root

    if root.val < new_val:
        root.right = insert_node(root.right, new_val)
    else:
        root.left = insert_node(root.left, new_val)

    return root




a = Node(2)
a = insert_node(a, 3)
a = insert_node(a,4)

print (a)
