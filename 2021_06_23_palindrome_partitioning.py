# https://leetcode.com/problems/palindrome-partitioning/
# Medium
# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

# A palindrome string is a string that reads the same backward as forward.


# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:

# Input: s = "a"
# Output: [["a"]]


# Constraints:

# 1 <= s.length <= 16
# s contains only lowercase English letters.

class Solution:
    def isPalin(self, seg):
        i, j = 0, len(seg) - 1
        while i < j:
            if seg[i] != seg[j]:
                return False
            i += 1
            j += 1
        return True

    def dfs(self, s: str):
        if (len(s) == 0 and len(self.temp) > 0):
            self.res.append(self.temp[:])
            return
        n = len(s) + 1
        for i in range(1, n):
            seg = s[0:i]
            if self.isPalin(seg):
                self.temp.append(seg)
                self.dfs(s[i:])
                self.temp.pop()

    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.temp = []
        self.dfs(s)
        return self.res
