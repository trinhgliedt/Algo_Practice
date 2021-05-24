# Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.


# Example 1:

# Input: s = "aaabb", k = 3
# Output: 3
# Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
# Example 2:

# Input: s = "ababbc", k = 2
# Output: 5
# Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.


# Constraints:

# 1 <= s.length <= 104
# s consists of only lowercase English letters.
# 1 <= k <= 10^5

import collections


def longestSubstring1(s, k):
    # """
    # :type s: str
    # :type k: int
    # :rtype: int
    # """
    # make a hashmap of s:
    hMap = {}
    for char in s:
        hMap[char] = 1 if char not in hMap.keys() else (hMap[char] + 1)
    # data structure to save the qualified characters
    arr = []
    for key, val in hMap.items():
        if val >= k:
            arr.append(key)
    result = ""
    for char in s:
        if char in arr:
            result = result + char
        else:
            break
    print(result)
    return len(result)


def longestSubstring4(s, k):
    hMap = collections.Counter(s)
    print(hMap)
    best_substring_len = 0
    # for i in range(0, len(s)):
    #     for j in range(len(s), 0, -1):
    #         if i <= j:
    #             str = s[i:j]
    #             # print(i, j, str)
    #             # make a hash map of this substring
    #             hMap = collections.Counter(s)
    #             # for char in str:
    #             #     hMap[char] = 1 if char not in hMap else hMap[char] + 1
    #             print(hMap)
    #             # print(all(hMap.values() > 0))
    #             # print(all([count > 0 for count in [0, 2, 3] if count > 0]))
    #             # print([count > 0 for count in [0, 2, 3] if count > 0])
    #             qualified_chars = [
    #                 count for count in hMap.values() if count >= k]
    #             # print(qualified)
    #             if len(qualified_chars) == len(hMap.keys()):
    #                 best_substring_len = len(str) if len(
    #                     str) > best_substring_len else best_substring_len
    return best_substring_len


def longestSubstring3(self, s: str, k: int) -> int:

    if k > len(s):

        # k is too large, larger than the length of s
        # Quick response for invalid k
        return 0

    # just for the convenience of self-recursion
    f = self.longestSubstring

    # dictionary
    # key: unique character
    # value: occurrence
    char_occ_dict = collections.Counter(s)

    # Scan each unique character and check occurrence
    for character, occurrence in char_occ_dict.items():

        if occurrence < k:

            # If occurrence of current character is less than k,
            # find possible longest substring without current character in recursion

            return max(f(sub_string, k) for sub_string in s.split(character))

    # -------------------------------

    # If occurrences of all characters are larger than or equal to k
    # the length of s is the answer exactly

    return len(s)


class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        counter = collections.Counter(s)
        if all(counter[i] >= k for i in counter):
            return len(s)

        start, longest = 0, 0
        for i in xrange(len(s)):
            if counter[s[i]] < k:
                longest = max(longest, self.longestSubstring(s[start:i], k))
                start = i + 1

        longest = max(longest, self.longestSubstring(s[start:], k))
        return longest


# print(longestSubstring("aaabb", 3))
# print(longestSubstring("ababbc", 2))
print(longestSubstring("ababacb", 3))
# print(longestSubstring("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 1))
