# https: // leetcode.com/problems/minimum-window-substring/

# hard

# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t(including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# A substring is a contiguous sequence of characters within the string.


# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.


# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        len1 = len(s)
        len2 = len(t)

        if len1 < len2:
            return ""

        hashPat, hashStr = {}, {}

        for i in range(0, len2):
            if hashPat.get(t[i]) is None:
                hashPat[t[i]] = 0
            hashPat[t[i]] += 1

        count = 0
        left = 0
        startIndex = -1
        minLen = float("inf")

        for right in range(0, len1):
            if hashStr.get(s[right]) is None:
                hashStr[s[right]] = 0
            hashStr[s[right]] += 1

            if hashPat.get(s[right]) is None:
                hashPat[s[right]] = 0
            if hashStr.get(s[right]) <= hashPat.get(s[right]):
                count += 1

            if(count == len2):
                while hashStr.get(s[left]) > hashPat.get(s[left]):
                    hashStr[s[left]] -= 1
                    left += 1

                windowLen = right - left + 1
                if minLen > windowLen:
                    minLen = windowLen
                    startIndex = left

        if startIndex == -1:
            return ""
        return s[startIndex: startIndex+minLen]


s = Solution()
print(s.minWindow(s="ADOBECODEBANC", t="ABC"))
print(s.minWindow(s="a", t="a"))
print(s.minWindow(s="a", t="aa"))
