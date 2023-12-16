class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        """Flip String to Monotone Increasing

        Args:
            s (str): string of 0's and 1's

        Returns:
            ans (int): minimum number of flips to make s monotone increasing
        """
        ones = 0
        ans = 0
        
        for i in s:
            if i == '1':
                ones += 1
            elif ones > 0:
                ones -= 1
                ans += 1
                
        return ans