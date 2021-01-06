# https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
# Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in the array.

# Example


# Queries are interpreted as follows:

#     a b k
#     1 5 3
#     4 8 7
#     6 9 1
# Add the values of  between the indices  and  inclusive:

# index->	 1 2 3  4  5 6 7 8 9 10
# 	[0,0,0, 0, 0,0,0,0,0, 0]
# 	[3,3,3, 3, 3,0,0,0,0, 0]
# 	[3,3,3,10,10,7,7,7,0, 0]
# 	[3,3,3,10,10,8,8,8,1, 0]
# The largest value is  after all operations are performed.

# Function Description

# Complete the function arrayManipulation in the editor below.

# arrayManipulation has the following parameters:

# int n - the number of elements in the array
# int queries[q][3] - a two dimensional array of queries where each queries[i] contains three integers, a, b, and k.
# Returns

# int - the maximum value in the resultant array
# Input Format

# The first line contains two space-separated integers  and , the size of the array and the number of operations.
# Each of the next  lines contains three space-separated integers ,  and , the left index, right index and summand.

# Constraints

# Sample Input

# 5 3
# 1 2 100
# 2 5 100
# 3 4 100
# Sample Output

# 200
# Explanation

# After the first update the list is 100 100 0 0 0.
# After the second update list is 100 200 100 100 100.
# After the third update list is 100 200 200 200 100.

# The maximum value is .

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    # generate a list of n item with value of 0:
    # arr = [0]*n
    # for q in queries:
    #     # since queries are based on 1-indexed array, decrease the index by 1 to convert to 0-indexed array
    #     for i in range(q[0]-1,q[1]):
    #         arr[i] += q[2]
    # return max(arr) 
    # the above works or small cases but exceeded time limit for large test cases      
    array = [0] * (n + 1)
    
    for query in queries: 
        a = query[0] - 1
        b = query[1]
        k = query[2]
        array[a] += k
        array[b] -= k
        
    max_value = 0
    running_count = 0
    for i in array:
        running_count += i
        if running_count > max_value:
            max_value = running_count
            
    return max_value
# The idea here is to not actually access every element the query would modify as it takes up too much time. First we build an array of n+1 0's. For each query, we will add k to the value at index a - 1 (to convert to 0 indexed array), and subtract the value of k from the value at index b (this is the same as b + 1 if the array were 0 indexed which is what we want). Thus the non-zero values of the array represent how the 0s between them differ from what comes before and after.

# For example if we start with this array: [0, 0, 0, 0, 0]

# And our query is: (a=1, b=3, k=100)

# We would modify the array to the following: [100, 0, 0, -100, 0].

# The 100 tells us that its value and every value that comes after it is 100 greater than what comes before (in this case nothing, so all these values are 100). The -100, tells us that it and every value that comes after it are 100 LESS than what came before. This way we only have to perform 2 operations in O(1) time for each query, regardless of how many values it modifies.

# Then to find the max value, we can simply initialize two counter variables to 0 and run through the entire array, adding each element to one of the counters and then checking to see if the number is the largest number we've seen. Then we simply return the counter with the max value we've seen. Voila!



print(arrayManipulation(10, [[1,5,3],[4,8,7],[6,9,1]]))
print(arrayManipulation(5, [[1,2,100],[2,5,100],[3,4,100]]))
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     nm = input().split()

#     n = int(nm[0])

#     m = int(nm[1])

#     queries = []

#     for _ in range(m):
#         queries.append(list(map(int, input().rstrip().split())))

#     result = arrayManipulation(n, queries)

#     fptr.write(str(result) + '\n')

#     fptr.close()
