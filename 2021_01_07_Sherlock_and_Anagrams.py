# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
# Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

# Example

# The list of all anagrammatic pairs is  at positions  respectively.

# Function Description

# Complete the function sherlockAndAnagrams in the editor below.

# sherlockAndAnagrams has the following parameter(s):

# string s: a string
# Returns

# int: the number of unordered anagrammatic pairs of substrings in 
# Input Format

# The first line contains an integer , the number of queries.
# Each of the next  lines contains a string  to analyze.

# Constraints



#  contains only lowercase letters in the range ascii[a-z].

# Sample Input 0

# 2
# abba
# abcd
# Sample Output 0

# 4
# 0
# Explanation 0

# The list of all anagrammatic pairs is  and  at positions  and  respectively.

# No anagrammatic pairs exist in the second query as no character repeats.

# Sample Input 1

# 2
# ifailuhkqq
# kkkk
# Sample Output 1

# 3
# 10
# Explanation 1

# For the first query, we have anagram pairs  and  at positions  and  respectively.

# For the second query:
# There are 6 anagrams of the form  at positions  and .
# There are 3 anagrams of the form  at positions  and .
# There is 1 anagram of the form  at position .

# Sample Input 2

# 1
# cdcd
# Sample Output 2

# 5
# Explanation 2

# There are two anagrammatic pairs of length :  and .
# There are three anagrammatic pairs of length :  at positions  respectively.

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    anagram_dict = {}
    count = 0
    for i in range(1, len(s)):
        for j in range(len(s)-i+1):
            current_sorted = str(sorted(s[j:j+i]))
            if (current_sorted not in anagram_dict):
                anagram_dict[current_sorted] = 1
            else:
                count += anagram_dict[current_sorted]
                anagram_dict[current_sorted] += 1
            print("i:",i,"j:",j,",s[",j,":",j+i,"]:",s[j:j+i],"---- anagram_dict:",anagram_dict)
    return count

print(sherlockAndAnagrams("tomato"))
# print(sherlockAndAnagrams("ifailuhkqq"))
# print(sherlockAndAnagrams("kkk"))
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     q = int(input())

#     for q_itr in range(q):
#         s = input()

#         result = sherlockAndAnagrams(s)

#         fptr.write(str(result) + '\n')

#     fptr.close()