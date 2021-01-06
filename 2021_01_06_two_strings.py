# https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

# Given two strings, determine if they share a common substring. A substring may be as small as one character.

# Example


# These share the common substring .



# These do not share a substring.

# Function Description

# Complete the function twoStrings in the editor below.

# twoStrings has the following parameter(s):

# string s1: a string
# string s2: another string
# Returns

# string: either YES or NO
# Input Format

# The first line contains a single integer , the number of test cases.

# The following  pairs of lines are as follows:

# The first line contains string .
# The second line contains string .
# Constraints

#  and  consist of characters in the range ascii[a-z].
# Output Format

# For each pair of strings, return YES or NO.

# Sample Input

# 2
# hello
# world
# hi
# world
# Sample Output

# YES
# NO
# Explanation

# We have  pairs to check:

# , . The substrings  and  are common to both strings.
# , .  and  share no common substrings.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings2(s1, s2):
    exclusionCheck = []
    for c in s1:
        if c in s2:
            return "YES"
        elif c not in s2:
            exclusionCheck.append(True)
    return "NO" if all(exclusionCheck) else "YES"

def twoStrings(s1, s2):
    intSec = set(s1).intersection(set(s2))
    return "YES" if len(intSec) > 0 else "NO"

print(twoStrings("cherry", "apple"))
print(twoStrings("cherry", "banana"))
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     q = int(input())

#     for q_itr in range(q):
#         s1 = input()

#         s2 = input()

#         result = twoStrings(s1, s2)

#         fptr.write(result + '\n')

#     fptr.close()