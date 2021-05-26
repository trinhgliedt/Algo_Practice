def linear_search1(arr, n):
    for i in range(len(arr)):
        if arr[i] == n:
            return i
    return -1


def linear_search(arr, n, i=0):
    if i == len(arr):
        return -1
    elif n == arr[i]:
        return i
    return linear_search(arr, n, i+1)


print(linear_search([5, -4, 3, 9, 4, 0, -12, 7], 8))
print(linear_search([5, -4, 3, 9, 4, 0, -12, 7], 9))
