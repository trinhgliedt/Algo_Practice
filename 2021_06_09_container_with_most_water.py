# Given non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i. ai) and (i, 0)
# find two lines, which together with x-axis forms a container, such that the container containts the most water.
def containerWithMostWater(arr):
    # real question: find the maximum difference between x position multiplied by the height
    i, j = 0, len(arr)-1
    maxWater = 0
    while i < j:
        minHeight = min(arr[i], arr[j])
        water = minHeight*(j-i)
        maxWater = max(water, maxWater)
        if arr[i] < arr[j]:
            i += 1
        else:
            j -= 1
    return maxWater


arr1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(containerWithMostWater(arr1))
