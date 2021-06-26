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


def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data)
        inorder(node.right)


def preorder(node):
    if node is not None:
        print(node.data)
        preorder(node.left)
        preorder(node.right)


def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data)


root = Node(4)

root.left = Node(5)
root.right = Node(6)
root.left.left = Node(7)

# inorder(root)
# preorder(root)
postorder(root)
