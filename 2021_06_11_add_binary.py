# https://leetcode.com/problems/add-binary/

# Given two binary strings a and b, return their sum as a binary string.


# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"


# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

# For example: in decimal addition, if you add 8 + 2 you get ten, which you write as 10; in the sum this gives a digit 0 and a carry of 1. Something similar happens in binary addition when you add 1 and 1; the result is two (as always), but since two is written as 10 in binary, we get, after summing 1 + 1 in binary, a digit 0 and a carry of 1.

# Therefore in binary:
# 0 + 0 = 0
# 0 + 1 = 1
# 1 + 0 = 1
# 1 + 1 = 10 (which is 0 carry 1)
# Example. Suppose we would like to add two binary numbers 10 and 11. We start from the last digit. Adding 0 and 1, we get 1 (no carry). That means the last digit of the answer will be one. Then we move one digit to the left: adding 1 and 1 we get 10. Hence, the answer is 101. Note that binary 10 and 11 correspond to 2 and 3 respectively. And the binary sum 101 corresponds to decimal 5: is the binary addition corresponds to our regular addition.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a)-1, len(b)-1
        # 010101 --> a
        # 111111 --> b

        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result.append(str(total % 2))
            carry = total//2
        return "".join(reversed(result))


s = Solution()
print(s.addBinary("110", "010"))
#  110
#  010
# 1000
