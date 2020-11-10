# Binary Search
# Given a sorted liay and a value, return whether
# that value is present in the liay. Do not
# sequentially iterate the entire liay. Instead,
# ‘divide and conquer’, taking advantage of the fact
# that the liay is sorted.
import math
def binarySearch(li, x):
    if  x < li[0] or x > li[len(li)-1]:
        return False;
    if  x == li[0] or x == li[len(li)-1]:
        return True;
    begP = 0; endP = len(li) - 1
    while (begP <= endP):
        midP = math.floor((endP - begP)/2)
        if x == li[midP]:
            return True
        if x < li[midP]: #go left
            endP = midP - 1
        elif x > li[midP]: #go right
            begP = midP + 1
    return False

print(binarySearch([1,5,8,9,10,15,20], 5))
print(binarySearch([1,5,8,9,10,15,20], 20))
print(binarySearch([1,5,8,9,10,15,20], 2))