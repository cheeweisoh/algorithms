import collections
import math
import itertools
import heapq
import structures


####################################################################################


class Solution:
    def countCompleteDayPairs(self, hours: list[int]) -> int:
        pass


print("Question 1")
soln = Solution()


####################################################################################


class Solution:
    pass


print("\nQuestion 2")
soln = Solution()


####################################################################################


class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        spellCount = {}
        for i in power:
            spellCount[i] = spellCount.get(i, 0) + 1

        sortedPower = sorted(spellCount.keys())
        dp = [0] * len(sortedPower)

        for i in range(len(sortedPower)):
            prevBest = 0
            currPower = sortedPower[i]

            j = i - 1
            while j >= 0 and sortedPower[j] >= sortedPower[i] - 2:
                j -= 1
            if j >= 0:
                prevBest = dp[j]

            dp[i] = max(prevBest + currPower * spellCount[currPower], dp[i - 1])

        return dp[-1]


print("\nQuestion 3")
soln = Solution()
print(soln.maximumTotalDamage([1, 1, 3, 4]))
print(soln.maximumTotalDamage([7, 1, 6, 6]))


####################################################################################

class Solution:
    pass


print("\nQuestion 4")
soln = Solution()
print(soln.countOfPeaks([3, 1, 4, 2, 5], [[2, 3, 4], [1, 0, 4]]))
print(soln.countOfPeaks([4, 1, 4, 2, 1, 5], [[2, 2, 4], [1, 0, 2], [1, 0, 4]]))
print(soln.countOfPeaks([8, 5, 9, 3, 5], [[1, 2, 4], [1, 0, 1], [2, 2, 4]]))
print(soln.countOfPeaks([8, 10, 10, 9, 10], [[2, 0, 1], [2, 2, 7], [1, 0, 2]]))
