from collections import Counter


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        c = Counter(candidates)

        def dfs(s, n, curr):
            if s == target:
                return ans.append(curr)
            if s > target or n < 1:
                return

            for i in range(0, c[n] + 1):
                dfs(s + i * n, n - 1, curr + [n] * i)

        dfs(0, 50, [])
        return ans
