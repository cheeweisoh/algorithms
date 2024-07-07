import collections
import math
import itertools
import heapq
import structures


####################################################################################


class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        shifted = k % len(s)

        return s[shifted:] + s[:shifted]


print("Question 1")
soln = Solution()


####################################################################################


class Solution:
    def validStrings(self, n: int) -> list[str]:
        ans = []

        def nextChar(s: str) -> str:
            nonlocal ans
            if len(s) == n:
                ans.append(s)
                return
            if s[-1] == "1":
                nextChar(s + "0")
            nextChar(s + "1")

        nextChar("0")
        nextChar("1")
        return ans


print("\nQuestion 2")
soln = Solution()


####################################################################################


class Solution:
    def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])
        prefixSum = [[0] * (n + 1) for _ in range(m + 1)]
        seenX = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefixSum[i][j] = (
                    prefixSum[i - 1][j] + prefixSum[i][j - 1] - prefixSum[i - 1][j - 1]
                )
                seenX[i][j] = 1 if seenX[i - 1][j] or seenX[i][j - 1] else 0
                if grid[i - 1][j - 1] == "X":
                    prefixSum[i][j] += 1
                    seenX[i][j] = 1
                elif grid[i - 1][j - 1] == "Y":
                    prefixSum[i][j] -= 1

        print(prefixSum)
        print(seenX)

        ans = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if prefixSum[i][j] == 0 and seenX[i][j]:
                    ans += 1
        return ans


print("\nQuestion 3")
soln = Solution()
print(soln.numberOfSubmatrices([["X", "Y", "."], ["Y", ".", "."]]))
print(soln.numberOfSubmatrices([["X", "X"], ["X", "Y"]]))
print(soln.numberOfSubmatrices([[".", "."], ["Y", "X"]]))


####################################################################################


class Solution:
    pass


print("\nQuestion 4")
soln = Solution()
