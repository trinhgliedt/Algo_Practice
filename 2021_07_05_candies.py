# https://www.hackerrank.com/challenges/candies/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming
# Alice is a kindergarten teacher. She wants to give some candies to the children in her class.  All the children sit in a line and each of them has a rating score according to his or her performance in the class.  Alice wants to give at least 1 candy to each child. If two children sit next to each other, then the one with the higher rating must get more candies. Alice wants to minimize the total number of candies she must buy.

# Example


# She gives the students candy in the following minimal amounts: . She must buy a minimum of 10 candies.

# Function Description

# Complete the candies function in the editor below.

# candies has the following parameter(s):

# int n: the number of children in the class
# int arr[n]: the ratings of each student
# Returns

# int: the minimum number of candies Alice must buy
# Input Format

# The first line contains an integer, , the size of .
# Each of the next  lines contains an integer  indicating the rating of the student at position .

def candies(n, arr):
    # Write your code here
    res = [1] * n
    # forward check
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            res[i] = res[i-1]+1
    print(res)

    # backward check
    for i in range(n-1, 0, -1):
        if arr[i-1] > arr[i] and res[i-1] <= res[i]:
            res[i-1] = res[i] + 1
    print(arr)
    print(res)
    return sum(res)


print(candies(10, [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]))
