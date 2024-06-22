class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        prefixSum = [0 for _ in range(len(nums) + 1)]
        prefixSum[0] = 1
        curr = 0
        ans = 0

        for i in range(len(nums)):
            nums[i] %= 2

        for num in nums:
            curr += num
            if curr >= k:
                # if curr > k, prefixSum[curr-k] give the number of combinations to remove curr-k odd numbers from the front
                ans += prefixSum[curr - k]
            prefixSum[curr] += 1

        return ans
