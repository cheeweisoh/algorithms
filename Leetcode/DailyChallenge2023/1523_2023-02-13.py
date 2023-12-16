class Solution:
    def countOdds(self, low: int, high: int) -> int:
        """Count Odd Numbers in an Interval Range

        Args:
            low (int): non-negative integer
            high (int): non-negative integer

        Returns:
            odds (int): count of odd numbers between low and high (inclusive)
        """
        odds = (high - low) // 2
        
        if high % 2 or low % 2:
            odds += 1
        
        return odds