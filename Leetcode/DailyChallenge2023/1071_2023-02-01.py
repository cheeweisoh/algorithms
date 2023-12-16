import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """Greatest Common Divisor of Strings

        Args:
            str1 (str): string 1
            str2 (str): string 2

        Returns:
            ans (str): largest string such that it divides both str1 and str2
        """
        if str1 + str2 != str2 + str1:
            return ""
        
        ans = str1[:math.gcd(len(str1), len(str2))]
        return ans