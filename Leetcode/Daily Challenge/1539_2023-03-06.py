class Solution:
    def findKthPositive(self, arr: list, k: int) -> int:
        """Kth Missing Positive Number

        Args:
            arr (list): array of positive integers in strictly increasing order
            k (int): integer

        Returns:
            int: k-th positive integer that is missing from arr
        """
        l = 0
        r = len(arr)
        
        if k < arr[0]:
            return k
        
        while l < r:
            mid = (l+r) // 2
            
            if arr[mid] - (mid+1) < k:
                l = mid + 1
            else:
                r = mid
                
        return l+k