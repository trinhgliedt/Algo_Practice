# Page 55 algo book
# Second-Largest
# Return the second-largest element of an array.
def secondLargest(li):
    maxV = max(li)
    maxPos = li.index(maxV)
    li[maxPos] = float("-inf")
    secondMax = max(li)
    li[maxPos] = maxV
    return secondMax
print(secondLargest([5,3,2,9,4,5,10,2]))