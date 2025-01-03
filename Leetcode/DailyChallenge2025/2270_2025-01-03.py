class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        total = sum(nums)
        curr = 0
        res = 0

        for n in nums[:-1]:
            curr += n
            if curr >= total - curr:
                res += 1

        return res
