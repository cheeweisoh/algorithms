class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []

        def dfs(idx, curr):
            ans.append(curr)
            for i in range(idx, len(nums)):
                dfs(i + 1, curr + [nums[i]])

        dfs(0, [])

        return ans
