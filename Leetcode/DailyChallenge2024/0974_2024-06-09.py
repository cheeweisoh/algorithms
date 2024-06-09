import collections

class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> bool:
        mem = collections.defaultdict(int)
        mem[0] = 1
        total = 0
        ans = 0

        for i in range(len(nums)):
            total += nums[i]
            rem = total % k
            ans += mem[rem]
            mem[rem] += 1

        return ans
