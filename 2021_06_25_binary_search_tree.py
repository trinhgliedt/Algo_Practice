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
    if root.data < node.data:
        if root.right is None:
            root.right = node
        else:
            insert(root.right, node)
    else:
        if root.left is None:
            root.left = node
        else:
            insert(root.left, node)


def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)


tree = Node(5)
#	         5
#       /  	      \
#     3	            7
#   /   \        /     \
#  2     4      6        8
insert(tree, Node(3))
insert(tree, Node(2))
insert(tree, Node(4))
insert(tree, Node(7))
insert(tree, Node(6))
insert(tree, Node(8))

preorder(tree)
