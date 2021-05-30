# Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
# For example: given the set [5, 2, 1, 3] and s=9 the answer is YES because the subset [5, 3, 1] sums to 9
def subset_sum(m, intList):
    # make the table:
    subset = [[False for _ in range(m+1)] for _ in range(len(intList)+1)]
