# https://leetcode.com/problems/kth-smallest-element-in-a-bst/?__cf_chl_jschl_tk__=4573980ab4f8168484bec3e8b56f7467e8e1f72a-1624894539-0-Ac2OsaZ-KPvurN-v6A90IU300WH-dDzVLve8BzKgL6M5nf47S6-iX__YSifcUABmqdOtlMsFSdX7B_oAfsOxfrlIzDHbN4uS7QwnfH-BUu__YlyuNMgT1Cvaf1AcaFj9rwKekX3YbXpRFzWfWEX21f8EDQJc99B6zQ4BtVggTdnV-6MCZ8MncRquh4Cp3uCnmH3PaIcNPO9IG3UUhAs4c2eoawNq1dR1XwWWno6wOKvCxlFSCsrEk9ivqEFrCAGESvD5MHLWrse712-GA2fEwiZ0IkqahyaYb_00vyKQ_ubiwCxBhTvnCyt5wR5WJ0sbHBi1pdqPGZBQxMMwlFqdpHDW_PmOTFXKscD41q_hP-StkRZk1rJ_NaBXRCw3OyAGBxaX928BszUceAXR7Rk_pi-jMFQHewuhEhIASWkbTkiDVC-fb7gw8xfPXgfYyAxQcw
# 230. Kth Smallest Element in a BST
# Medium

# Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.


# Example 1:


# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:


# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3


# Constraints:

# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104


# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.res = None

        # self.inorder(root)
        if root is not None:
            self.inorder(root.left)
            self.k -= 1
            if self.k == 0:
                self.res = root.val
                return
            self.inorder(root.right)
        return self.res

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            self.k -= 1
            if self.k == 0:
                self.res = root.val
                return
            self.inorder(root.right)
