# The insertion sort, although still 𝑂(𝑛2), works in a slightly different way. It always maintains
# a sorted sublist in the lower positions of the list. Each new item is then “inserted” back into the
# previous sublist such that the sorted sublist is one item larger.
# We begin by assuming that a list with one item (position 0) is already sorted. On each pass, one
# for each item 1 through 𝑛 − 1, the current item is checked against those in the already sorted
# sublist. As we look back into the already sorted sublist, we shift those items that are greater
# to the right. When we reach a smaller item or the end of the sublist, the current item can be
# inserted.
def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
    while position > 0 and a_list[position - 1] > current_value:
        a_list[position] = a_list[position - 1]
        position = position - 1
    a_list[position] = current_value
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(a_list)
print(a_list)