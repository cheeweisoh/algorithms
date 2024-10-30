class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0, 0] for _ in range(n)]

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i][0] = max(dp[i][0], dp[j][0] + 1)
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i, -1):
                if nums[i] > nums[j]:
                    dp[i][1] = max(dp[i][1], dp[j][1] + 1)

        res = float("inf")
        for s, e in dp:
            if s and e:
                res = min(res, n - (s + e + 1))

        return res
