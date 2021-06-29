# https://leetcode.com/problems/binary-tree-postorder-traversal/
# Given the root of a binary tree, return the postorder traversal of its nodes' values.


# Example 1:


# Input: root = [1,null,2,3]
# Output: [3,2,1]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]
# Example 4:


# Input: root = [1,2]
# Output: [2,1]
# Example 5:


# Input: root = [1,null,2]
# Output: [2,1]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import AnyStr


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return
        ans = []
        s1 = []
        s2 = []

        s1.append(root)

        while s1:
            x = s1[-1]
            s1.pop()
            s2.append(x)

            if x.left:
                s1.append(x.left)
            if x.right:
                s1.append(x.right)

        while s2:
            y = s2[-1]
            s2.pop()
            ans.append(y.val)
        return ans
