 
#  Interval List Intersections
#  Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

# Return the intersection of these two interval lists.

# (Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

# Example 1:
# Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# Note:

# 0 <= A.length < 1000
# 0 <= B.length < 1000
# 0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9

class Solution(object):
    def intervalIntersection(self, A, B):
        i, j = 0,0
        res = []
        while i < len(A) and j < len(B):
            itv_1 = A[i]
            itv_2 = B[j]
            
            # no intersaction because itv1 starts after itv2 ends, so move itv2 to next
            if itv_1[0] > itv_2[1]:
                j+=1
            # no intersaction because itv2 starts after itv1 ends, so move itv1 to next
            elif itv_2[0] > itv_1[1]:
                i+=1
            # intersaction found
            else:
                res.append([max(itv_1[0], itv_2[0]), min(itv_1[1], itv_2[1])])
                
                # move whichever ending earlier cursor to next.
                if itv_1[1] > itv_2[1]:
                    j+=1
                else:
                    i+=1
                    
        return res
