class Solution:
    def largestGoodInteger(self, num: str) -> str:
        """Largest 3-Same-Digit Number in String

        Args:
            num (str): string representing a large integer

        Returns:
            str: maximum good integer (substring of len 3 containing one unique digit) or empty string if no such integer exists
        """
        ans = ''
        count = 1
        
        for i in range(1, len(num)):
            if num[i] == num[i-1]:
                count += 1
                if count == 3:
                    ans = max(ans, num[i] * 3)
            else:
                count = 1
        
        return ans