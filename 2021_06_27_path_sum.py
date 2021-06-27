# https://leetcode.com/problems/path-sum/
# Easy
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.


# Example 1:


# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Example 2:


# Input: root = [1,2,3], targetSum = 5
# Output: false
# Example 3:

# Input: root = [1,2], targetSum = 0
# Output: false
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasSum(self, root, targetSum, cur):
        if root is None:
            return False
        cur += root.val
        if cur == targetSum and root.left is None and root.right is None:
            return True
        return self.hasSum(root.right, targetSum, cur) or self.hasSum(root.left, targetSum, cur)

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        return self.hasSum(root, targetSum, 0)
