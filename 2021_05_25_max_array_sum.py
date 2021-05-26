# https://www.hackerrank.com/challenges/max-array-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming

def maxSubsetSum(arr):
    n = len(arr)
    accum_sums = [0]*n
    accum_sums[0] = arr[0]
    accum_sums[1] = max(arr[1], accum_sums[0])
    # print(accum_sums)
    for i in range(2, n):
        accum_sums[i] = max(arr[i], accum_sums[i-1], arr[i] + accum_sums[i-2])
    # print(accum_sums)

    return accum_sums[-1]


print(maxSubsetSum([-2, 1, 3, -4, 5]))
print(maxSubsetSum([3, 7, 4, 6, 5]))
print(maxSubsetSum([3, 5, -7, 8, 10]))
