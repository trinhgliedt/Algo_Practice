

def binarySearch(arr, searchValue):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left+right)//2
        if arr[mid] == searchValue:
            return mid
        elif arr[mid] < searchValue:
            left = mid + 1
        elif arr[mid] > searchValue:
            right = mid-1

    return -1


myArr = [1, 2, 3, 4, 5]
print(binarySearch(myArr, 1))
print(binarySearch(myArr, 2))
print(binarySearch(myArr, 3))
print(binarySearch(myArr, 4))
