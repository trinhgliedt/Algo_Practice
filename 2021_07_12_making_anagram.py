# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
# A student is taking a cryptography class and has found anagrams to be very useful. Two strings are anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency. For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

# The student decides on an encryption scheme that involves two large strings. The encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Determine this number.

# Given two strings,  and , that may or may not be of the same length, determine the minimum number of character deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.

# Example


# Delete  from  and  from  so that the remaining strings are  and  which are anagrams. This takes  character deletions.

# Function Description

# Complete the makeAnagram function in the editor below.

# makeAnagram has the following parameter(s):

# string a: a string
# string b: another string
# Returns

# int: the minimum total characters that must be deleted
# Input Format

# The first line contains a single string, .
# The second line contains a single string, .

# Constraints

# The strings  and  consist of lowercase English alphabetic letters, ascii[a-z].
# Sample Input

# cde
# abc
# Sample Output

# 4
# Explanation

# Delete the following characters from the strings make them anagrams:

# Remove d and e from cde to get c.
# Remove a and b from abc to get c.
# It takes  deletions to make both strings anagrams.
from collections import Counter


def makeAnagram(a, b):
    # Write your code here
    # if both strings are empty, return 0
    if a == "" and b == "":
        return 0
    # if one string is empty, return length of the non-empty string
    if a == "" and b >= "":
        return len(b)
    if a != "" and b == "":
        return len(a)

    # make a hash map of the first string, hMapA
    hMapA = Counter(a)
    # make a hash map of the second string, hMapB
    hMapB = Counter(b)
    # make a variable for delCount
    delCount = 0

    # 1. iterate through keys, values of hMapA:
    # 2. for each key: check if key exists in hMapB:
    # 3. if key doesn't exist: increase delCount by val (which is the number of occurrence)
    # 4. if key exists but val is smaller than in hMapB: increase delCount by val in hMapB - val in hMapA
    def checkXinY(xMap, yMap):
        delta = 0
        for char, occur in xMap.items():
            if char not in yMap:
                delta += occur
            elif char in yMap and occur < yMap[char]:
                delta += yMap[char] - occur
        return delta
    delCount += checkXinY(hMapA, hMapB)
    # repeat step 1-4 for hMapB
    delCount += checkXinY(hMapB, hMapA)
    return delCount


print(makeAnagram("cde", "dcf"))
print(makeAnagram("", ""))
print(makeAnagram("cde", ""))
