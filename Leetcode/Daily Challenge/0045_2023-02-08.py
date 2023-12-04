class Solution:
    def jump(self, nums: list) -> int:
        """Jump Game II

        Args:
            nums (list): array of integers of length n

        Returns:
            steps (int): minimum number of jumps to reach nums[n-1]
        """
        n, start, end, maxend, steps = len(nums), 0, 0, 0, 0
        
        for i in range(n-1):
            maxend = max(maxend, i + nums[i])
            
            if i == end:
                steps += 1
                end = maxend
        
        return steps