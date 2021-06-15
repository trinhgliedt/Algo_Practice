# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Medium
# Given the head of a linked list, remove the nth node from the end of the list and return its head.


# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]


# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz


# Follow up: Could you do this in one pass?

# Accepted
# 902,941
# Submissions
# 2,482,657

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ans = ListNode(0)
        ans.next = head

        first = ans
        second = ans
        for i in range(1, n+2):
            first = first.next

        while first is not None:
            first = first.next
            second = second.next

        second.next = second.next.next

        return ans.next


s = Solution()
node1 = ListNode(1)
node3 = ListNode(3)
node5 = ListNode(5)
node7 = ListNode(7)

node1.next = node3
node3.next = node5
node5.next = node7

answer = s.removeNthFromEnd(node1, 2)

while answer != None:
    print(answer.val)
    answer = answer.next
