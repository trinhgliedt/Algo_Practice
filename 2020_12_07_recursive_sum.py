# Suppose that you want to calculate the sum of a list of numbers such
# as: [1, 3, 5, 7, 9]. An iterative function that computes the sum is shown below. The function
# uses an accumulator variable (the_sum) to compute a running total of all the numbers in the
# list by starting with 0 and adding each number in the list.
def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])
print(list_sum([1,3,5,7,9]))


