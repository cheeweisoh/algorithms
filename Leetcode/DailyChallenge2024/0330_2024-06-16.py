class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        miss = 1
        ans = 0
        i = 0

        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += (miss - 1) + 1
                ans += 1
            print(miss, i, ans)

        return ans
