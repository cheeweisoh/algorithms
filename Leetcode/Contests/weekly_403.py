import collections
import math
import itertools
import heapq
import structures


####################################################################################


class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        ans = float("inf")
        nums.sort()

        for i in range(len(nums) // 2):
            ans = min(ans, (nums[i] + nums[len(nums) - 1 - i]) / 2)

        return ans


print("Question 1")
soln = Solution()
print(soln.minimumAverage([7, 8, 3, 4, 15, 13, 4, 1]))


####################################################################################


class Solution:
    def minimumArea(self, grid: list[list[int]]) -> int:
        x0, y0, x1, y1 = len(grid), len(grid[0]), -1, -1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    x0 = min(x0, i)
                    y0 = min(y0, j)
                    x1 = max(x1, i)
                    y1 = max(y1, j)

        return (x1 - x0 + 1) * (y1 - y0 + 1)


print("\nQuestion 2")
soln = Solution()
print(soln.minimumArea([[0, 1, 0], [1, 0, 1]]))
print(soln.minimumArea([[0, 0], [1, 0]]))


####################################################################################


class Solution:
    def maximumTotalCost(self, nums: list[int]) -> int:
        addSum, subSum = nums[0], nums[0]

        for i in nums[1:]:
            addSum, subSum = max(addSum, subSum) + i, addSum - i

        return max(addSum, subSum)


print("\nQuestion 3")
soln = Solution()
print(soln.maximumTotalCost([1, -2, 3, 4]))


####################################################################################


class Solution:
    def minimumSum(self, grid: list[list[int]]) -> int:

        def get(a, b, c, d):
            # solution from part 2
            if b < a or d < c:
                return 1e9
            x0, y0, x1, y1 = 1e9, 1e9, -1, -1
            for i in range(a, b + 1):
                for j in range(c, d + 1):
                    if grid[i][j]:
                        x0 = min(x0, j)
                        y0 = min(y0, i)
                        x1 = max(x1, j)
                        y1 = max(y1, i)
            return (x1 - x0 + 1) * (y1 - y0 + 1)

        ans = 1e9
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                # type 3
                ans = min(
                    ans,
                    get(0, i, 0, m - 1)
                    + get(i + 1, n - 1, 0, j)
                    + get(i + 1, n - 1, j + 1, m - 1),
                )
                # type 2
                ans = min(
                    ans,
                    get(0, i, 0, j)
                    + get(0, i, j + 1, m - 1)
                    + get(i + 1, n - 1, 0, m - 1),
                )
                # type 5
                ans = min(
                    ans,
                    get(0, n - 1, 0, j)
                    + get(0, i, j + 1, m - 1)
                    + get(i + 1, n - 1, j + 1, m - 1),
                )
                # type 6
                ans = min(
                    ans,
                    get(0, n - 1, j + 1, m - 1)
                    + get(0, i, 0, j)
                    + get(i + 1, n - 1, 0, j),
                )
        # type 1
        for i in range(n):
            for j in range(i, n):
                ans = min(
                    ans,
                    get(0, i, 0, m - 1)
                    + get(i + 1, j, 0, m - 1)
                    + get(j + 1, n - 1, 0, m - 1),
                )
        # type 4
        for i in range(m):
            for j in range(i, m):
                ans = min(
                    ans,
                    get(0, n - 1, 0, i)
                    + get(0, n - 1, i + 1, j)
                    + get(0, n - 1, j + 1, m - 1),
                )
        return ans


print("\nQuestion 4")
soln = Solution()
