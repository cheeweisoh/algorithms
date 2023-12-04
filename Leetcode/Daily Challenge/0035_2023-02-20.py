class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        """Search Insert Position

        Args:
            nums (list): sorted array of distinct integers
            target (int): target value

        Returns:
            int: index if target is found, else index it would be if it were inserted in order
        """
        low = 0
        high = len(nums)
        
        while low < high:
            mid = (low+high) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid
                
        return low