class Solution:
    def singleNonDuplicate(self, nums: list) -> int:
        """Single Element in a Sorted Array

        Args:
            nums (list): sorted array consiting of integers where each element appears exactly twice, except for one element which appears exactly once

        Returns:
            int: single element that appears only once
        """
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if mid % 2:
                mid -= 1
            
            if nums[mid] == nums[mid+1]:
                left = mid + 2
            else:
                right = mid
            
        return nums[left]