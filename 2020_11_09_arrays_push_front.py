# PushFront
# Given an array and an additional value, insert this
# value at the beginning of the array. Do this
# without using any built-in array methods.
def pushFront(myList, x):
    # game plan: duplicate the last value in the array, 
    # then, copy all value to the right
    # then, assign the first array value to be the inserted value
    temp = myList[len(myList)-1]
    myList.append(temp)
    l = len(myList)
    for i in range(l - 1, 0, -1):
        myList[i] = myList[i-1]
    myList[0] = x
    return myList

print(pushFront([5,3,4,2,8], 9))
