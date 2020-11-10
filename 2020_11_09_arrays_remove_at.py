# RemoveAt
# Given an array and an index into the array,
# remove and return the array value at that index.
# Do this without using any built-in array methods
# except pop() . Think of PopFront(arr) as
# equivalent to RemoveAt(arr,0) .
def removeAt(myList, index):
    # copy all the array value by one to the left
    # then, pop the last one
    l = len(myList)
    temp = myList[0]
    for i in range(index, l, 1):
        myList[i-1] = myList[i]
    myList.pop()
    print(myList)
    return temp

def removeAt2(myList, index):
    temp = myList[index]
    myList.pop(index)
    print(myList)
    return temp

print(removeAt([5,3,4,2,8], 3))
print(removeAt2([5,3,4,2,8], 3))