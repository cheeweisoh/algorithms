
class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:

        def dfs(idx, curr):
            if idx == len(nums):
                return curr

            include = dfs(idx + 1, curr ^ nums[idx])
            exclude = dfs(idx + 1, curr)

            return include + exclude

        return dfs(0, 0)
