# given an array of integers, write a function to move all 0's to the end while maintaining the relative order of the other elements
def moveZeroes(arr):
    # j is to keep track of non-zero elements
    j = 0
    # move the non-zero elements to the beginning of the array
    for num in arr:
        if num != 0:
            arr[j] = num
            j += 1
        print(arr)
    #  len - k is the number of zeros. Set all array items from k onwards to zero
    for i in range(j, len(arr)):
        arr[i] = 0
    return arr


arr1 = [5, 0, 6, 2, 0, 0, 7, 1]
print(moveZeroes(arr1))
