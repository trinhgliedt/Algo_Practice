# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    hgSums = []
    i, j = 0, 0
    for i in range(4):
        for j in range(4):
            hourGlass = 0
            hourGlass = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            # print("i:",i,"j:",j,"sum:",hourGlass)
            hgSums.append(hourGlass)
    # print(hgSums)
    return max(hgSums)

print(hourglassSum([[1,1,1,0,0,0],\
                    [0,1,0,0,0,0],\
                    [1,1,1,0,0,0],\
                    [0,0,2,4,4,0],\
                    [0,0,0,2,0,0],\
                    [0,0,1,2,4,0]]))
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     arr = []

#     for _ in range(6):
#         arr.append(list(map(int, input().rstrip().split())))

#     result = hourglassSum(arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()
