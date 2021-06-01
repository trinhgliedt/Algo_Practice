# Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
# For example: given the set [5, 2, 1, 3] and s=9 the answer is YES because the subset [5, 3, 1] sums to 9
# A Dynamic Programming solution for subset
# sum problem Returns true if there is a subset of
# set[] with sun equal to given sum

# Returns true if there is a subset of set[]
# with sun equal to given sum
def isSubsetSum(set, n, sum):

    # The value of subset[i][j] will be
    # true if there is a
    # subset of set[0..j-1] with sum equal to i
    subset = ([[False for i in range(sum + 1)]
              for i in range(n + 1)])

    # If sum is 0, then answer is true
    for i in range(n + 1):
        subset[i][0] = True

    # If sum is not 0 and set is empty,
    # then answer is false
    for i in range(1, sum + 1):
        subset[0][i] = False

    # Fill the subset table in botton up manner
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j < set[i-1]:
                subset[i][j] = subset[i-1][j]
            if j >= set[i-1]:
                subset[i][j] = (subset[i-1][j] or
                                subset[i - 1][j-set[i-1]])

    # uncomment this code to print table
    # for i in range(n + 1):
    # for j in range(sum + 1):
    # print (subset[i][j], end =" ")
    # print()
    return subset[n][sum]
    # make the table:
    subset = [[False for _ in range(m+1)] for _ in range(len(intList)+1)]
# https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
