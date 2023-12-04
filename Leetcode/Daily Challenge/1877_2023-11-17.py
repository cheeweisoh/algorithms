class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        """Minimize Maximum Pair Sum in Array

        Args:
            nums (list[int]): array of numbers of even length

        Returns:
            int: minimized maximum pair sum
        """
        nums.sort()
        n = len(nums)
        max_sum = 0
        
        for i in range(n // 2):
            curr_sum = nums[i] + nums[n - i - 1]
            
            if curr_sum > max_sum:
                max_sum = curr_sum
        
        return max_sum