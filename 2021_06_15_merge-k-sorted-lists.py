# https: // leetcode.com/problems/merge-k-sorted-lists/

# Hard
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.


# Example 1:

# Input: lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
# Output: [1, 1, 2, 3, 4, 4, 5, 6]
# Explanation: The linked-lists are:
# [
#     1 -> 4 -> 5,
#     1 -> 3 -> 4,
#     2 -> 6
# ]
# merging them into one sorted list:
# 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []


# Constraints:

# k == lists.length
# 0 <= k <= 10 ^ 4
# 0 <= lists[i].length <= 500
# -10 ^ 4 <= lists[i][j] <= 10 ^ 4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length won't exceed 10 ^ 4.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        cur = ListNode(0)
        ans = cur

        while l1 and l2:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next

            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next

        while l1:
            cur.next = l1
            l1 = l1.next
            cur = cur.next
        while l2:
            cur.next = l2
            l2 = l2.next
            cur = cur.next
        return ans.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        i = 0
        last = len(lists) - 1
        j = last

        while last != 0:
            i = 0
            j = last

            while j > i:
                lists[i] = self.mergeTwoLists(lists[i], lists[j])
                i += 1
                j -= 1
                last = j
        return lists[0]
