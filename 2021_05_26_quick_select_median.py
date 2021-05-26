def median_algo(nums, k):
    # We have to split the list into chunks of 5 items
    chunks = [nums[i:i+5] for i in range(0, len(nums), 5)]
    # the median is the middle item in the sorted order
    medians = [sorted(chunk)[len(chunk)//2] for chunk in chunks]
    pivot_value = sorted(medians)[len(medians)//2]

    # PARTITION PHASE
    left_array = [n for n in nums if n < pivot_value]
    right_array = [m for m in nums if m > pivot_value]

    # SELECTION PHASE
    pivot_index = len(left_array)

    if k < pivot_index:
        # we have to consider the left array because
        # we are looking for smaller items
        return median_algo(left_array, k)
    elif k > pivot_index:
        # we have to consider the right array but we have to update k value
        # because we have created a new array
        return median_algo(right_array, k-len(left_array)-1)
    else:
        return pivot_value


def select(nums, k):
    return median_algo(nums, k-1)


x = [1, -5, 0, 10, 15, 20, 3, -1, 21, 22, 23]
print(select(x, 1))
print(select(x, 2))
print(select(x, 3))
print(select(x, 4))
