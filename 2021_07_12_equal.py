# https: // www.hackerrank.com/challenges/equal/problem
# Christy is interning at HackerRank. One day she has to distribute some chocolates to her colleagues. She is biased towards her friends and plans to give them more than the others. One of the program managers hears of this and tells her to make sure everyone gets the same number.

# To make things difficult, she must equalize the number of chocolates in a series of operations. For each operation, she can give  pieces to all but one colleague. Everyone who gets a piece in a round receives the same number of pieces.

# Given a starting distribution, calculate the minimum number of operations needed so that every colleague has the same number of pieces.

# Example

# represents the starting numbers of pieces for each colleague. She can give  pieces to the first two and the distribution is then . On the next round, she gives the same two  pieces each, and everyone has the same number: . Return the number of rounds, .

# Function Description

# Complete the equal function in the editor below.

# equal has the following parameter(s):

# int arr[n]: the integers to equalize
# Returns

# int: the minimum number of operations required
# Input Format

# The first line contains an integer, the number of test cases.

# Each test case has  lines.
# - The first line contains an integer, the number of colleagues and the size of .
# - The second line contains  space-separated integers, , the numbers of pieces of chocolate each colleague has at the start.

# Constraints


# The number of chocolates each colleague has initially < .

# Sample Input

# STDIN       Function
# ----- --------
# 1           t = 1
# 4           arr[] size n = 4
# 2 2 3 7     arr = [2, 2, 3, 7]
# Sample Output

# 2
# Explanation

# Start with
# Add  to all but the 3rd element
# Add  to all but the 4th element

# Two operations were required.

# Sample Input 1

# 1
# 3
# 10 7 12
# Sample Output 1

# 3
# Explanation 1

# Start with
# Add  to the first two elements
# Add  to the last two elements
# Add  to the last two elements

# Three operations were required.
def equal(arr):
    # Write your code here
    # giving chocolates so all are equal is the same as taking chocolates from the people with more so that all would have equal amount
    # we can take so that all would have the minimum amount, or take more so that all would have less than minimum amount
    min_element = min(arr)
    move_counts = []
    # the most amount to take is so that everyone has min-4. If we do min-5 then it's the same as min
    for i in range(5):
        move_count = 0
        for a in arr:
            diff = a - (min_element - i)
            # take 5
            move_count += diff//5
            # if there's left, take 2
            move_count += (diff % 5)//2
            # if there's left, take one each
            move_count += (diff % 5) % 2//1
            print(i, a, move_count)
        move_counts.append(move_count)
        print(move_counts)
    return min(move_counts)


print(equal([2, 2, 3, 7]))
