# We now turn our attention to using a divide and conquer strategy as a way to improve the
# performance of sorting algorithms. The first algorithm we will study is the merge sort. Merge
# sort is a recursive algorithm that continually splits a list in half. If the list is empty or has one
# item, it is sorted by definition (the base case). If the list has more than one item, we split the
# list and recursively invoke a merge sort on both halves. Once the two halves are sorted, the
# fundamental operation, called a merge, is performed. Merging is the process of taking two
# smaller sorted lists and combining them together into a single, sorted, new list. Figure 5.22
# shows our familiar example list as it is being split by merge_sort. Figure 5.23 shows the
# simple lists, now sorted, as they are merged back together.
# The merge_sort function shown below begins by asking the base case question. If the length
# of the list is less than or equal to one, then we already have a sorted list and no more processing
# is necessary. If, on the other hand, the length is greater than one, then we use the Python
# slice operation to extract the left and right halves. It is important to note that the list may not
# have an even number of items. That does not matter, as the lengths will differ by at most one.
def merge_sort(a_list):
    print("Splitting ", a_list)
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i = i + 1
            else:
                a_list[k] = right_half[j]
                j = j + 1
            k = k + 1
        while i < len(left_half):
            a_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            a_list[k] = right_half[j]
            j = j + 1
            k = k + 1
    print("Merging ", a_list)

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(a_list)
print(a_list)