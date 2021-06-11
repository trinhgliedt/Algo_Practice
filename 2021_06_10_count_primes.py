# https://leetcode.com/problems/count-primes/
# Count the number of prime numbers less than a non-negative number, n.


# Example 1:

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# Example 2:

# Input: n = 0
# Output: 0
# Example 3:

# Input: n = 1
# Output: 0


# Constraints:
# 0 <= n <= 5 * 106

import math


class Solution(object):
    # this function works, but it's too slow and exceeded Leetcode's time limit
    def countPrimes1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        # elif 1 < n <= 3:
        #     return n
        count = 0
        primes = []
        for i in range(2, n):
            isPrime = True
            for j in range(2, i):
                if i % j == 0:
                    isPrime = False
                    break

            if isPrime == True:
                count += 1
                primes.append(i)
        print(primes)
        return count

    def countPrimes(self, n):
        if n < 2:
            return 0
        isPrime = [False, False]
        isPrime = isPrime + [True for i in range(2, n)]
        for i in range(2, math.ceil(math.sqrt(n))):
            if isPrime[i]:
                for multiples_of_i in range(i*i, n, i):
                    isPrime[multiples_of_i] = False

            # print(isPrime)
        return sum(isPrime)


s = Solution()
print(s.countPrimes(4))
# print(s.countPrimes(2))
print(s.countPrimes(10))
