# The quick sort uses divide and conquer to gain the same advantages as the merge sort, while
# not using additional storage. As a trade-off, however, it is possible that the list may not be
# divided in half. When this happens, we will see that performance is diminished.
# A quick sort first selects a value, which is called the pivot value. Although there are many
# different ways to choose the pivot value, we will simply use the first item in the list. The role
# of the pivot value is to assist with splitting the list. The actual position where the pivot value
# belongs in the final sorted list, commonly called the split point, will be used to divide the list
# for subsequent calls to the quick sort.
def quick_sort(a_list):
    quick_sort_helper(a_list, 0, len(a_list) - 1)
def quick_sort_helper(a_list, first, last):
    if first < last:
        split_point = partition(a_list, first, last)
        quick_sort_helper(a_list, first, split_point - 1)

def partition(a_list, first, last):
    pivot_value = a_list[first]
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
            left_mark = left_mark + 1
        while a_list[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1
        if right_mark < left_mark:
            done = True
        else:
            temp = a_list[left_mark]
            a_list[left_mark] = a_list[right_mark]
            a_list[right_mark] = temp
    temp = a_list[first]
    a_list[first] = a_list[right_mark]
    a_list[right_mark] = temp

    return right_mark

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(a_list)
print(a_list)