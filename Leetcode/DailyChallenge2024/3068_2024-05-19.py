class Solution:
    def maximumValueSum(self, nums: list[int], k: int, edges: list[list[int]]) -> int:
        cnt, min_diff = 0, float("inf")

        for i, v in enumerate(nums):
            if v ^ k > v:
                nums[i] ^= k
                cnt += 1
            min_diff = min(min_diff, nums[i] - (nums[i] ^ k))

        return sum(nums) - (min_diff if cnt & 1 else 0)
