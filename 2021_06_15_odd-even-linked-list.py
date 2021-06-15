# https://leetcode.com/problems/odd-even-linked-list/
# Medium
# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time complexity.


# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]
# Example 2:


# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]


# Constraints:

# n == number of nodes in the linked list
# 0 <= n <= 104
# -106 <= Node.val <= 106

# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        odd = head
        even = odd.next
        evenList = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = evenList
        return head


s = Solution()
node10 = ListNode(10)
node20 = ListNode(20)
node30 = ListNode(30)
node40 = ListNode(40)
node50 = ListNode(50)

node10.next = node20
node20.next = node30
node30.next = node40
node40.next = node50

answer = s.oddEvenList(node10)

while answer != None:
    print(answer.val)
    answer = answer.next
