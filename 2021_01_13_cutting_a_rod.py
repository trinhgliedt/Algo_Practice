# Cutting a Rod | DP-13
# Difficulty Level : Medium
#  Last Updated : 13 Nov, 2020

# Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n. Determine the maximum value obtainable by cutting up the rod and selling the pieces. For example, if length of the rod is 8 and the values of different pieces are given as following, then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6)

# length   | 1   2   3   4   5   6   7   8
# --------------------------------------------
# price    | 1   5   8   9  10  17  17  20
# And if the prices are as following, then the maximum obtainable value is 24 (by cutting in eight pieces of length 1)

# length   | 1   2   3   4   5   6   7   8
# --------------------------------------------
# price    | 3   5   8   9  10  17  17  20

import numpy as np


def cut_rod(price, n):
    if n <= 0:
        return 0
    max_val = -1

    val = 0
    for i in range(0, n):
        val = price[i] + cut_rod(price, n - i - 1)
        if max_val < val:
            max_val = val
        # print("i:", i, "n:", n, "max_val:", max_val)
    return max_val


def cut_rod2(price, n):
    val = [0 for x in range(n+1)]
    val[0] = 0

    for i in range(1, n+1):
        max_val = -1
        for j in range(i):
            max_val = max(max_val, price[j] + val[i-j-1])
            # print("i:", i, "j:", j, "max_val:", max_val, "val:", val)
        val[i] = max_val
        # print("i:", i, "val:", val)

    return val[n]


# Driver code
arr = [1, 5, 8, 9, 10, 17, 17, 20]
arr1 = [3, 5, 8, 9, 10, 17, 17, 20]
arr2 = [5, 5, 8, 9, 10, 17, 17, 20]
size = len(arr)
# print("Maximum Obtainable Value is", cut_rod(arr1, size))
print("Maximum Obtainable Value is", cut_rod2(arr1, size))


def rodCut(price, n):
    if n <= 0:
        return 0
    max_val = -1

    # val = 0
    for i in range(n):
        # val = price[i] + rodCut(price, n-1-i)
        max_val = max(max_val, price[i] + rodCut(price, n-1-i))

    return max_val


# print("Maximum Obtainable Value is", rodCut(arr1, size))
