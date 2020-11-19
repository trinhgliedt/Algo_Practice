# Nth-Largest
# Given an array, return the Nth-largest element:
# there should be (N - 1) elements that are larger.
def nthLargest(arr, n):
    if n > len(arr):
        print("The array you provided doesn't have a/an "+ str(n) + "th element")
        return None
    else:
        maxItem = arr[0]; maxArr = []
        for item in arr:
            if item > maxItem:
                maxItem = item
        maxArr.append(maxItem)

        for j in range (2, n+1):
            prevMax = float('-inf')
            for item in arr:
                if item > prevMax and item < maxArr[-1]:
                    prevMax = item
            maxArr.append(prevMax)
        return maxArr[-1]

print(nthLargest([5,3,2,9,15,20,6], 3))
print(nthLargest([5,3,2,9,15,20,6], 5))
print(nthLargest([2],1))
print(nthLargest([],2))
