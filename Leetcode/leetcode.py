# import collections
import math

# import random
# import heapq

# import string
# import bisect
# from structures import TreeNode


class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        currTime = customers[0][0]
        totalTime = 0
        n = len(customers)

        for a, t in customers:
            startTime = max(a, currTime)
            currTime = startTime + t
            totalTime += currTime - a

        return totalTime / n


def main():
    soln = Solution()
    customers = [[2, 3], [6, 3], [7, 5], [11, 3], [15, 2], [18, 1]]
    print(soln.averageWaitingTime(customers))


if __name__ == "__main__":
    main()
