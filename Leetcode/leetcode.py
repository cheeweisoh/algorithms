# import collections
# import math
# import random
# import heapq
# import string
# import bisect
# from structures import *


class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        happiness.sort(reverse=True)
        totalSum = 0
        turns = 0

        for i in range(k):
            totalSum += max(happiness[turns] - turns, 0)
            turns += 1

        return totalSum


def main():
    soln = Solution()
    happiness = [1, 2, 3]
    k = 2
    print(soln.maximumHappinessSum(happiness, k))


if __name__ == "__main__":
    main()
