# import collections
# import math
# import random
# import heapq
# import string
# import bisect
# from structures import *


class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        score = (1 << (ncol - 1)) * nrow

        for i in range(1, ncol):
            currVal = 1 << (ncol - 1 - i)
            sameBit = 0

            for j in range(nrow):
                if grid[j][i] == grid[j][0]:
                    sameBit += 1

            score += max(sameBit, nrow - sameBit) * currVal

        return score


def main():
    soln = Solution()
    grid = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
    print(soln.matrixScore(grid))


if __name__ == "__main__":
    main()
