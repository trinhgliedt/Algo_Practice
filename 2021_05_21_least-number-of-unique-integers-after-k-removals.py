# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/
import collections


class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        # """
        # :type arr: List[int]
        # :type k: int
        # :rtype: int
        # """
        # make a hashmap from the array
        hmap = collections.Counter(arr)
        # edge case: quick exit if array contain 1 item, or if k=0
        if k == 0:
            return len(hmap)
        elif k > 0 and len(arr) == 1:
            return 0
        # sort the hashmap by value, high to low, still keeping keys, values
        # make an array of the values (which contains frequency of the elements)
        frequency = sorted(hmap.values(), reverse=True)
        # make an array of the keys (which contains the unique elements). Expect this array to have indexes aligning
        # with the values array so that we can use common index. This array of keys make it easier to understand, but it's actually not needed, cos we'll operate on the array for frequency only.
        # k is the number of elements to be removed.
        # to leave the least of unique integers, we'll remove the ones with least frequency first
        # which means we'll sum the frequency of the elements, from lowest to highest, until it's >=k
        accum_sum = 0
        print(hmap, frequency, accum_sum)

        for i in range(len(frequency)-1, -1, -1):
            accum_sum += frequency[i]
            print("accum_sum", accum_sum)
        # if the summed frequency at index i exactly equals k then the remaining elements will equal i
            if accum_sum == k:
                return i
        # if the summed frequency at index i is larger than k then the remaining elements will equal i+1
            elif accum_sum > k:
                return i+1
            # print(frequency, accum_sum)


my_sol = Solution()
# print(my_sol.findLeastNumOfUniqueInts([5, 5, 4], 1))
# print(my_sol.findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], 3))
# print(my_sol.findLeastNumOfUniqueInts([2, 1, 1, 3, 3, 3], 3))
# print(my_sol.findLeastNumOfUniqueInts([1], 1))
print(my_sol.findLeastNumOfUniqueInts([1, 2, 3], 3))
