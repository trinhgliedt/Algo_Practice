# given an array of integers, return true if the following conditions are fulfilled:
# length of the array is >= 3
# there exists some index i such that:
# a[0] < a[1] < ... < a[i]
# a[i] > a[i+1] > ... > a[a.size - 1]
def validMountain(arr):
    # find the top of the mountain
    i = 1
    while (i < len(arr) and arr[i-1] < arr[i]):
        i += 1
    if i == 1 or i == len(arr):
        return False
    while (i < len(arr) and arr[i-1] > arr[i]):
        i += 1
    return i == len(arr)


arr1 = [2, 3, 5, 1, 0]
arr2 = [1, 5, 2, 6, 8]
print(validMountain(arr1))
print(validMountain(arr2))
