import math

class Solution:
    def minEatingSpeed(self, piles: list, h: int) -> int:
        """Koko Eating Bananas

        Args:
            piles (list): piles[i] is the number of bananas inthe i-th pile
            h (int): number of hours to finish eating all bananas

        Returns:
            int: minimum number of bananas eaten per hour
        """
        l = 1
        r = max(piles)
        res = r
        
        while l <= r:
            mid = (l + r) // 2
            
            hours = 0
            for i in piles:
                hours += math.ceil(i / mid)
            
            if hours <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return res