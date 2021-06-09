# given an array of intergers of size n, find maximum sum of K consecutive elements
def maxSum(arr, k):
    n = len(arr)
    window_sum = sum([arr[i] for i in range(k)])
    max_sum = window_sum

    for j in range(0, n-k):
        window_sum = window_sum - arr[j] + arr[j+k]
        max_sum = max(window_sum, max_sum)
    return max_sum


arr1 = [5, 3, 15, 1, 10, 7]
print(maxSum(arr1, 2))
