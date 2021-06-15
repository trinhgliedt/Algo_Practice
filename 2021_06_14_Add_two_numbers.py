# https://leetcode.com/problems/add-two-numbers/
# Medium
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]


# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(None)
        pointer: ListNode = ans
        carry, sum = 0, 0
        while (l1 != None or l2 != None):
            sum = carry
            if l1 != None:
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next
            carry = int(sum/10)
            pointer.next = ListNode(sum % 10)
            pointer = pointer.next

        if carry > 0:
            pointer.next = ListNode(carry)

        return ans.next


s = Solution()

l1_node2 = ListNode(2)
l1_node4 = ListNode(4)
l1_node3 = ListNode(3)

l1_node2.next = l1_node4
l1_node4.next = l1_node3

l2_node5 = ListNode(5)
l2_node6 = ListNode(6)
l2_node4 = ListNode(4)

l2_node5.next = l2_node6
l2_node6.next = l2_node4

answer = s.addTwoNumbers(l1_node2, l2_node5)

while answer != None:
    print(answer.val)
    answer = answer.next
