# https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen

# There is a string, , of lowercase English letters that is repeated infinitely many times. Given an integer, , find and print the number of letter a's in the first  letters of the infinite string.

# Example


# The substring we consider is , the first  characters of the infinite string. There are  occurrences of a in the substring.

# Function Description

# Complete the repeatedString function in the editor below.

# repeatedString has the following parameter(s):

# s: a string to repeat
# n: the number of characters to consider
# Returns

# int: the frequency of a in the substring
# Input Format

# The first line contains a single string, .
# The second line contains an integer, .

# Constraints

# For  of the test cases, .
# Sample Input

# Sample Input 0

# aba
# 10
# Sample Output 0

# 7
# Explanation 0
# The first  letters of the infinite string are abaabaabaa. Because there are  a's, we return .

# Sample Input 1

# a
# 1000000000000
# Sample Output 1

# 1000000000000
# Explanation 1
# Because all of the first  letters of the infinite string are a, we return .

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    if len(s) == 0:
        return 0
    # number of letter a in (the repeated string at n letter) will equal
    # number of letter a in one string
        # will do this step last

    # times floor division of n//len(string)
    f = n//(len(s))
    # plus number of letter a in modular of n divided by len(string)
        # find modular of n divided by len(string)
    m = n%len(s)

    # count number of letter a in the given string
    # aCountInRemainder = 0
    # for i in range(m):
    #     if s[i] == "a":
    #         aCountInRemainder += 1
    aCountInRemainder = s[:m].count('a')
    
    aCountEachRep = aCountInRemainder
    # for i in range(m, len(s)):
    #     if s[i] == "a":
    #         aCountEachRep += 1
    aCountEachRep = aCountInRemainder + s[m:].count('a')
    return aCountEachRep*f + aCountInRemainder

# print(repeatedString("aba", 10))
# print(repeatedString("abac", 5))
print(repeatedString("nbhiweuhdaaaaaa", 1000000000000))
# print(repeatedString("a", 1000000000000))
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     n = int(input())

#     result = repeatedString(s, n)

#     fptr.write(str(result) + '\n')

#     fptr.close()
