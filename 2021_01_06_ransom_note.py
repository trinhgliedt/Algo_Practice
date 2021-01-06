# https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
# Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting. He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use only whole words available in the magazine. He cannot use substrings or concatenation to create the words he needs.

# Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.

# For example, the note is "Attack at dawn". The magazine contains only "attack at dawn". The magazine has all the right words, but there's a case mismatch. The answer is .

# Function Description

# Complete the checkMagazine function in the editor below. It must print  if the note can be formed using the magazine, or .

# checkMagazine has the following parameters:

# magazine: an array of strings, each a word in the magazine
# note: an array of strings, each a word in the ransom note
# Input Format

# The first line contains two space-separated integers,  and , the numbers of words in the  and the ..
# The second line contains  space-separated strings, each .
# The third line contains  space-separated strings, each .

# Constraints

# .
# Each word consists of English alphabetic letters (i.e.,  to  and  to ).
# Output Format

# Print Yes if he can use the magazine to create an untraceable replica of his ransom note. Otherwise, print No.

# Sample Input 0

# 6 4
# give me one grand today night
# give one grand today
# Sample Output 0

# Yes
# Sample Input 1

# 6 5
# two times three is not four
# two times two is four
# Sample Output 1

# No
# Explanation 1

# 'two' only occurs once in the magazine.

# Sample Input 2

# 7 4
# ive got a lovely bunch of coconuts
# ive got some coconuts
# Sample Output 2

# No
# Explanation 2

# Harold's magazine is missing the word .

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    mHMap = {}
    nHMap = {}
    for w in magazine:
        if w not in mHMap:
            mHMap[w] = 1
        else:
            mHMap[w] += 1
    for w in note:
        if w not in nHMap:
            nHMap[w] = 1
        else:
            nHMap[w] += 1
    check = []
    for k in nHMap.keys():
        if k not in mHMap:
            print("No")
            return
        elif nHMap[k] <= mHMap[k]:
            check.append(True)
        elif nHMap[k] > mHMap[k]:
            print("No")
            return
    print("Yes") if all(check) else print("No")
    return


from collections import Counter

def ransom_note(magazine, ransom):
    return (Counter(ransom) - Counter(magazine)) == {}

# The result of counters' operator substraction is a counter that shows how many more values magazine is missing to match those present in ransom. When an empty dict is returned, every element in rasom is present enough times in magazine.

# Counter(ransom)= Counter({'ive': 1, 'got': 1, 'some': 1, 'coconuts': 1})
# Counter(magazine) = Counter({'ive': 1, 'got': 1, 'a': 1, 'lovely': 1, 'bunch': 1, 'of': 1, 'coconuts': 1})
#  Counter(ransom) - Counter(magazine) = Counter({'some': 1})
checkMagazine(['give','me','one','grand','today','night'],['give','me','one','grand','today'])
checkMagazine(['ive','got','a','lovely','bunch','of','coconuts'],['ive','got','some','coconuts'])
print(ransom_note(['give','me','one','grand','today','night'],['give','me','one','grand','today']))
print(ransom_note(['ive','got','a','lovely','bunch','of','coconuts'],['ive','got','some','coconuts']))


# if __name__ == '__main__':
#     mn = input().split()

#     m = int(mn[0])

#     n = int(mn[1])

#     magazine = input().rstrip().split()

#     note = input().rstrip().split()

#     checkMagazine(magazine, note)