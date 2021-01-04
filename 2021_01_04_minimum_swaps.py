# https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
# You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array in ascending order.

# For example, given the array  we perform the following steps:

# i   arr                         swap (indices)
# 0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
# 1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
# 2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
# 3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
# 4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
# 5   [1, 2, 3, 4, 5, 6, 7]
# It took  swaps to sort the array.

# Function Description

# Complete the function minimumSwaps in the editor below. It must return an integer representing the minimum number of swaps to sort the array.

# minimumSwaps has the following parameter(s):

# arr: an unordered array of integers
# Input Format

# The first line contains an integer, , the size of .
# The second line contains  space-separated integers .

# Constraints

# Output Format

# Return the minimum number of swaps to sort the given array.

# Sample Input 0

# 4
# 4 3 1 2
# Sample Output 0

# 3
# Explanation 0

# Given array 
# After swapping  we get 
# After swapping  we get 
# After swapping  we get 
# So, we need a minimum of  swaps to sort the array in ascending order.

# Sample Input 1

# 5
# 2 3 4 1 5
# Sample Output 1

# 3
# Explanation 1

# Given array 
# After swapping  we get 
# After swapping  we get 
# After swapping  we get 
# So, we need a minimum of  swaps to sort the array in ascending order.

# Sample Input 2

# 7
# 1 3 5 2 4 6 7
# Sample Output 2

# 3
# Explanation 2

# Given array 
# After swapping  we get 
# After swapping  we get 
# After swapping  we get 
# So, we need a minimum of  swaps to sort the array in ascending order.
#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# Complete the minimumSwaps function below.
def minimumSwaps1(arr):
    # list comprehension: make a new list where value is decreased by 1 to make index-matching more intuitive
    # so that our values go from 0 to N-1, just like our indices.  (Not necessary but makes it easier to understand.)
    moves = 0
    arr1 = [i-1 for i in arr]
    # print("-----",arr1)

    # iterate through each value in the array
    IdxOfCorrectV = 0
    for cp, tp in enumerate(arr1):
        # cp is the current position of value, while tp is the original position of value which is also the target position of value
        # find the first value that is not at the right place (which means cp-tp != 0), then switch it with the value that should be at that position (which means value = cp of the current index)
        if cp - tp != 0:
            print("line 99 cp:",cp)
            # loop from cp+1 to the end of the array
            # which will make O^(n.log(n))
            for i, v in enumerate(arr1[(cp+1):]):
                if v == cp:
                    # print("arr1[(cp+1):]:",arr1[(cp+1):],"i:",i,"v:",v)
                    IdxOfCorrectV = i + v + 1
            # this is a loop. Which makes O^n^2
            # IdxOfCorrectV = arr1.index(cp)
            temp = tp
            arr1[cp] = cp
            arr1[IdxOfCorrectV] = temp
            moves += 1
            # print("cp:", cp, "tp:", tp, "IdxOfCorrectV:",IdxOfCorrectV, "moves:",moves)
            # print(arr1,"-------")
    return moves


def minimumSwaps(arr):
    ref_arr = sorted(arr)
    # Make a dict of array to refer to during swap
    # key: value (which is the target index)
    # value: index (which is the current location)
    indexDict = {v:i for i, v in enumerate(arr)}
    swaps = 0
    for i, v in enumerate(arr):
        correct_value = ref_arr[i]
        if v != correct_value:
            to_swap_ix = indexDict[correct_value]
            arr[to_swap_ix], arr[i] = arr[i], arr[to_swap_ix]
            # Now update the dict too
            indexDict[v] = to_swap_ix
            indexDict[correct_value] = i
            swaps += 1
    return swaps


print(minimumSwaps([1,3,5,2,4,6,7]))
# print(minimumSwaps([4,3,1,2]))
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input())

#     arr = list(map(int, input().rstrip().split()))

#     res = minimumSwaps(arr)

#     fptr.write(str(res) + '\n')

#     fptr.close()
