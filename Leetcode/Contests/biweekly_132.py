import collections
import math
import itertools
import heapq
import structures


####################################################################################


class Solution:
    def clearDigits(self, s: str) -> str:
        lastChar = 0
        curr = 0

        while curr < len(s):
            if s[curr].isalpha():
                lastChar = curr
                curr += 1
            else:
                s = s[:lastChar] + s[curr + 1 :]
                lastChar -= 1
                curr -= 1

        return s


print("Question 1")
soln = Solution()
print(soln.clearDigits("abc"))
print(soln.clearDigits("cb34"))


####################################################################################


class Solution:
    def findWinningPlayer(self, skills: list[int], k: int) -> int:
        i, curr = 0, 0

        for j in range(1, len(skills)):
            if skills[i] < skills[j]:
                curr = 0
                i = j
            curr += 1
            if curr == k:
                break
        return i


print("\nQuestion 2")
soln = Solution()
print(soln.findWinningPlayer([4, 2, 6, 3, 9], 2))
print(soln.findWinningPlayer([2, 5, 4], 3))
print(soln.findWinningPlayer([16, 4, 7, 17], 562084119))


####################################################################################


class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        n = len(nums)
        dp = [[1] * (k + 1) for _ in range(n)]

        for i in range(n):
            for j in range(k + 1):
                for l in range(i):
                    if nums[l] == nums[i]:
                        dp[i][j] = max(dp[i][j], dp[l][j] + 1)
                    elif j > 0:
                        dp[i][j] = max(dp[i][j], dp[l][j - 1] + 1)

        return max(max(row) for row in dp)


print("\nQuestion 3")
soln = Solution()
print(soln.maximumLength([1, 2, 1, 1, 3], k=2))
print(soln.maximumLength([1, 2, 3, 4, 5, 1], k=0))


####################################################################################


class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        n = len(nums)
        dp = [[1] * (k + 1) for _ in range(n)]

        ans = 0
        for j in range(k + 1):
            max1 = 1
            numMap = {nums[0]: 0}

            for i in range(1, n):
                if i > 0 and j > 0:
                    max1 = max(max1, dp[i - 1][j - 1] + 1)
                dp[i][j] = max(dp[i][j], max1)

                if nums[i] in numMap:
                    dp[i][j] = max(dp[i][j], dp[numMap[nums[i]]][j] + 1)

                numMap[nums[i]] = i
                ans = max(ans, dp[i][j])

        return ans


print("\nQuestion 4")
soln = Solution()
print(soln.maximumLength([1, 2, 1, 1, 3], k=2))
print(soln.maximumLength([1, 2, 3, 4, 5, 1], k=0))
