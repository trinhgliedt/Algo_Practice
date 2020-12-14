# Leetcode
# 5. Longest Palindromic Substring
# Example 1:

# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
# Example 3:

# Input: s = "a"
# Output: "a"
# Example 4:

# Input: s = "ac"
# Output: "a"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters (lower-case and/or upper-case),

class Solution(object):
    def longestPalindrome(self, s):
        # :type s: str
        # :rtype: str
        # Return if string is empty
        if not s: return s
        res = ""
        for i in range(len(s)):
            j = i + 1
            # While j is less than length of string
            # AND res is *not* longer than substring s[i:]
            while j <= len(s) and len(res) <= len(s[i:]):
                # If substring s[i:j] is a palindrome
                # AND substring is longer than res
                if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(res):
                    res = s[i:j]
                j += 1

        return res

s = Solution()
s1 = "babad"
s2 = "cbbd"
s3 = "ac"
s4 = ""
print(s.longestPalindrome(s1))
print(s.longestPalindrome(s2))
print(s.longestPalindrome(s3))
print(s.longestPalindrome(s4))