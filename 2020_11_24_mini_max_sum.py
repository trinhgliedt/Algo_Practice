# Hacker Rank:
# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# Example

# The minimum sum is  and the maximum sum is . The function prints

# 16 24
# Function Description

# Complete the miniMaxSum function in the editor below.

# miniMaxSum has the following parameter(s):

# arr: an array of  integers
# Print

# Print two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.

# Input Format

# A single line of five space-separated integers.

# Constraints
# 1 <= arr[i] <= 10^9

# Output Format

# Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

# Sample Input

# 1 2 3 4 5
# Sample Output

# 10 14
# Explanation

# The numbers are , , , , and . Calculate the following sums using four of the five integers:

# Sum everything except , the sum is 2+3+4+5 = 14.
# Sum everything except , the sum is 1+3+4+5 = 13.
# Sum everything except , the sum is 1+2+4+5 = 12.
# Sum everything except , the sum is 1+2+3+5 = 11.
# Sum everything except , the sum is 1+2+3+4 = 10.
# Hints: Beware of integer overflow! Use 64-bit Integer.
def miniMaxSum(arr): 
    # find sum for all 5 integer
    sum5 = sum(arr)
    # sum of 4 values = sum of 5 values less one value
    # iterate thru the array to make the sum4, and at the same time find min4sum and max4sum
    min4Sum = max4Sum = sum5-arr[0]
    for i in range (1, 5):
        if sum5-arr[i] > max4Sum:
            max4Sum = sum5-arr[i] 
        if sum5-arr[i] < min4Sum:
            min4Sum = sum5-arr[i] 
    print(str(min4Sum) + " " + str(max4Sum))

miniMaxSum([1,2,3,4,5]);
miniMaxSum([1,3,5,7,9]);
miniMaxSum([10**9, 10**9, 10**9, 10**9, 10**9, 10**9]);

