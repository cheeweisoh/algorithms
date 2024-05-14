# import collections
# import math
# import random
# import heapq
# import string
# import bisect
# from structures import *


class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if (
                r < 0
                or r >= nrow
                or c < 0
                or c >= ncol
                or grid[r][c] == 0
                or (r, c) in visited
            ):
                return 0

            visited.add((r, c))

            left = dfs(r, c - 1)
            right = dfs(r, c + 1)
            up = dfs(r - 1, c)
            down = dfs(r + 1, c)

            visited.remove((r, c))

            return grid[r][c] + max(left, right, up, down)

        ans = 0

        for row in range(nrow):
            for col in range(ncol):
                if grid[row][col] and (row, col) not in visited:
                    ans = max(ans, dfs(row, col))

        return ans


def main():
    soln = Solution()
    grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
    print(soln.getMaximumGold(grid))


if __name__ == "__main__":
    main()
