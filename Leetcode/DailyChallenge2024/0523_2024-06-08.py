class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        mem = {0: -1}
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            rem = total % k

            if rem in mem:
                if i - mem[rem] > 1:
                    return True
            else:
                mem[rem] = i

        return False

