# Leetcode
#  Longest Substring Without Repeating Characters
#  Given a string s, find the length of the longest substring without repeating characters.

#  Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Example 4:

# Input: s = ""
# Output: 0


# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # :type s: str
        # :rtype: int
        dic = {}
        res = 0
        j = 0
        # make a dictionary of characters in the string, with key being each character,
        # value being the location of the first appearance of that character in the string
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = i
                # print("char not in dict: s[i]:",
                #       s[i], ", i:", i, ", dic:", dic)

            else:
                # if the character already in this dictionary, mark its position in variable j.
                # j is the count of the substring that has no repetitive character
                j = max(j, dic[s[i]]+1)
                # Then, replace its old position with its new position
                dic[s[i]] = i
            print("s[i]:", s[i], ", j:", j, ", i:", i, ", dic:", dic)
            res = max(res, i-j+1)
            print("res:", res)
        return res


t = Solution()
s1 = 'abcabcbb'
s2 = "bbbbb"
s3 = "pwwkew"
s4 = "pwwkewo"
# print(t.lengthOfLongestSubstring(s1))
# print(t.lengthOfLongestSubstring(s2))
# print(t.lengthOfLongestSubstring(s3))
print(t.lengthOfLongestSubstring(s4))
