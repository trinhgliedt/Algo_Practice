# https://leetcode.com/problems/network-delay-time/
from typing import List
from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        g = defaultdict(list)

        for u, v, cost in times:
            g[u].append((cost, v))

        min_heap = [(0, K)]
        visited = set()
        distance = {i: float("inf") for i in range(1, N+1)}
        distance[K] = 0

        while min_heap:
            cur_dist, u = heapq.heappop(min_heap)
            if u in visited:
                continue
            visited.add(u)

            if len(visited) == N:
                return cur_dist

            for direct_dist, v in g[u]:
                if cur_dist + direct_dist < distance[v] and v not in visited:
                    distance[v] = cur_dist + direct_dist
                    heapq.heappush(min_heap, (distance[v], v))
        return -1
