# 7 becomes left child of 5
#		           4
#		       /       \
#		      5	        6
#	      /  \      /   \
#      7   None  None  None
#     / \
#  None  None

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


def insert(root, node):
    if root is None:
        root = node
        return
    if root.data < root.data:
        if root.right is None:
            root.right = node


root = Node(4)

root.left = Node(5)
root.right = Node(6)
root.left.left = Node(7)
