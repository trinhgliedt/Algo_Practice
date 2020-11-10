# PopFront
# Given an array, remove and return the value at
# the beginning of the array. Do this without using
# any built-in array methods except pop() .
def popFront(myList):
    # copy all the array value by one to the left
    # then, pop the last one
    l = len(myList)
    temp = myList[0]
    for i in range(1, l, 1):
        myList[i-1] = myList[i]
    myList.pop()
    print(myList)
    return temp

def popFront2(myList):
    temp = myList[0]
    myList.pop(0)
    print(myList)
    return temp

# print(popFront([5,3,4,2,8]))
print(popFront2([5,3,4,2,8]))
