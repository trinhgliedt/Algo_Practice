from collections import deque
import itertools
import collections

# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem


def numPlayers(k, scores):
    l = len(scores)
    if len(scores) > 0:
        lowest = scores[0]
    else:
        lowest = -1
    rank = []
    numOfPlayers = 0
    if len(rank) == l:
        return numOfPlayers
    for i in range(1, len(scores)):
        if scores[i] < lowest:
            lowest = scores[i]
    # count number of lowest
    count = 0
    newScores = []
    for s in scores:
        if s == lowest:
            count += 1
        if s > lowest:
            newScores.append(s)
    for n in range(count):
        rank.append(len(rank)+1)
    countPlayers = 0
    for r in rank:
        if r >= k:
            countPlayers += 1
    for i in range(len(scores)):
        lowest = min(lowest, numPlayers(k, newScores))


def numPlayers(k, scores):
    count = collections.Counter(scores)
    ans, curRank = 0, 1
    for k, v in sorted(count.items(), reverse=True):
        if curRank > k:
            break
        ans += v
        curRank += v
    return ans


# print(numPlayers(3, [100, 50, 50, 25]))
# print(numPlayers(4, [20, 40, 60, 80, 10]))

# https: // leetcode.com/problems/least-number-of-unique-integers-after-k-removals/


def deleteProducts(ids, m):
    counts = sorted([(i, ids.count(i)) for i in set(ids)], key=lambda x: x[1])
    num = len(counts)

    for item in counts:

        if (m - item[1]) >= 0:
            num -= 1
            m -= item[1]
        else:
            break

    return num

# https://leetcode.com/discuss/interview-question/221639/


def finMinDistance(h, w, n):
    arr = []
    for i in range(h):
        for j in range(w):
            arr.append((i, j, 0))

    ans = float("inf")
    for points in itertools.combinations(arr, n):
        q = deque([])
        visited = set()
        for m, n, dist in points:
            q.append((m, n, dist))
            visited.add((m, n))
        distAns = 0
        distArr = []
        while q:
            i, j, dist = q.popleft()
            distAns = max(dist, distAns)
            for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= x < h and 0 <= y < w and (x, y) not in visited:
                    q.append((x, y, dist+1))
                    visited.add((x, y))
        ans = min(distAns, ans)

    return ans
