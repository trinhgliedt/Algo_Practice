# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem


import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#
import collections


def climbingLeaderboard(ranked, player, result=[]):
    # Write your code here
    # My solution: Only got 12 pts on Hackerrank
    ranked.append(player[0])
    my_set = set(ranked)
    sorted_set = sorted(my_set, reverse=True)
    result.append(sorted_set.index(player[0])+1)
    player.pop(0)
    print(player, sorted_set, result)
    while len(player) > 0:
        climbingLeaderboard(ranked, player, result)
    return result

    # Other people's solution: they didn't even mutate the original list.
    # So what I didn't get at first is that the player scores will only go up and not down.
    # scores_set = list(set(ranked))
    # scores_set.sort(reverse=True)
    # result = []
    # l = len(scores_set)
    # for s in player:
    #     while (l > 0) and (s >= scores_set[l-1]):
    #         print(s, l, scores_set, scores_set[l-1])
    #         l -= 1
    #     result.append(l+1)
    #     print(result)
    # return result


print(climbingLeaderboard([100, 90, 90, 80], [70, 80, 105, 20]))
print(climbingLeaderboard([100, 90, 90, 80], [70, 80, 105]))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     ranked_count = int(input().strip())

#     ranked = list(map(int, input().rstrip().split()))

#     player_count = int(input().strip())

#     player = list(map(int, input().rstrip().split()))

#     result = climbingLeaderboard(ranked, player)

#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()
