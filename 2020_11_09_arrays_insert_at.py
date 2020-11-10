# InsertAt
# Given an array, index, and additional value, insert
# the value into the array at the given index. Do this
# without using built-in array methods. You can
# think of PushFront(arr,val) as equivalent to
# InsertAt(arr,0,val) .
def insertAt(li, index, x):
    # game plan: duplicate the last value in the array,
    # then, iterate from index to the end, copy all value to the right
    # then, assign the array value at index to be the inserted value
    if index <= len(li):
        temp = li[len(li)-1]
        li.append(temp)
        l = len(li)
        for i in range (l-1, index-1, -1):
            li[i] = li[i-1]
        li[index-1] = x
        return li
    message = "Can't process. Please provide an index that is smaller than " + str(len(li))
    return message

print(insertAt([5,3,4,2,8], 3, 9))
print(insertAt([5,3,4,2,8], 10, 9))
