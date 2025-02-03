class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        inc, dec = 1, 1

        if n == 1:
            return 1

        # iterate through the array
        for i in range(1, n):
            # if the next element is larger, increase size of inc
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1
            # if the next element is smaller, increase size of dec
            elif nums[i] < nums[i - 1]:
                inc = 1
                dec += 1
            # if the next element is equal, reset
            else:
                inc = dec = 1

            # check the current longest possible subarray
            res = max(res, inc, dec)

        return res
