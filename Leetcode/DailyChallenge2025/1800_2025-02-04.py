class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        curr_sum = nums[0]
        res = curr_sum

        # iterate through the array
        for i in range(1, len(nums)):
            # if the curr number is still in accending order, increase the current sum
            if nums[i] > nums[i - 1]:
                curr_sum += nums[i]
            # else reset the current sum
            else:
                curr_sum = nums[i]

            # check if current sum is the largest
            res = max(res, curr_sum)

        return res
