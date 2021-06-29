# https://leetcode.com/problems/valid-parentheses/
# Easy
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.


# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
# Example 4:

# Input: s = "([)]"
# Output: false
# Example 5:

# Input: s = "{[]}"
# Output: true
class Solution:
    def isEqual(self, c1, c2):
        if c1 == "(" and c2 == ")":
            return True
        if c1 == "{" and c2 == "}":
            return True
        if c1 == "[" and c2 == "]":
            return True
        return False

    def isValid(self, s: str) -> bool:
        st = []
        for char in s:
            if len(st) != 0:
                li = st[-1]
                if self.isEqual(li, char):
                    st.pop()
                    continue
            st.append(char)
        return len(st) == 0

# ()[]{}
