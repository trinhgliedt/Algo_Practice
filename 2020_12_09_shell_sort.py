# The shell sort, sometimes called the “diminishing increment sort,” improves on the insertion
# sort by breaking the original list into a number of smaller sublists, each of which is sorted using
# an insertion sort. The unique way that these sublists are chosen is the key to the shell sort.
# Instead of breaking the list into sublists of contiguous items, the shell sort uses an increment i,
# sometimes called the gap, to create a sublist by choosing all items that are i items apart.
# This can be seen in Figure 5.18. This list has nine items. If we use an increment of three,
# there are three sublists, each of which can be sorted by an insertion sort. After completing
# these sorts, we get the list shown in Figure 5.19. Although this list is not completely sorted,
# something very interesting has happened. By sorting the sublists, we have moved the items
# closer to where they actually belong.
# Figure 5.20 shows a final insertion sort using an increment of one; in other words, a standard
# insertion sort. Note that by performing the earlier sublist sorts, we have now reduced the total
# number of shifting operations necessary to put the list in its final order. For this case, we need
# only four more shifts to complete the process.
def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
    print("After increments of size", sublist_count, "The list is",
    a_list)
    sublist_count = sublist_count // 2
def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
    while position >= gap and a_list[position - gap] >current_value:
        a_list[position] = a_list[position - gap]
        position = position - gap
        a_list[position] = current_value
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(a_list)
print(a_list)