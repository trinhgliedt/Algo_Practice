# https: // leetcode.com/problems/reverse-linked-list/

# Easy

# Given the head of a singly linked list, reverse the list, and return the reversed list.


# Example 1:


# Input: head = [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]
# Example 2:


# Input: head = [1, 2]
# Output: [2, 1]
# Example 3:

# Input: head = []
# Output: []


# Constraints:

# The number of nodes in the list is the range[0, 5000].
# -5000 <= Node.val <= 5000


# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

# Accepted
# 1, 447, 136
# Submissions
# 2, 177, 664
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        helperNode = None
        while head is not None:
            next = head.next
            head.next = helperNode
            helperNode = head
            head = next
        return helperNode


s = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

answer = s.reverseList(node1)
while answer != None:
    print(answer.val)
    answer = answer.next
