# Reverse Array
# Given a numerical array, reverse the order of the
# values. The reversed array should have the same
# length, with existing elements moved to other
# indices so that the order of elements is reversed.
import math
def reverseArr(li):
    l = len(li); temp = 0
    for i in range(0, math.floor((l-1)/2)+1):
        temp = li[i]
        li[i] = li[l-1-i]
        li[l-1-i] = temp
    return li;
print(reverseArr([1, 2, 3, 4, 5, 6]))
print(reverseArr([1, 2, 3, 4, 5]))