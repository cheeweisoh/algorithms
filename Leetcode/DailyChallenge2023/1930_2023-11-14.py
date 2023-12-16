import string

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """Unique Length-3 Palindromic Subsequences

        Args:
            s (str): string

        Returns:
            int: number of unique palindromes of length three that are a subsequence of s
        """
        ans = 0
        
        for i in string.ascii_lowercase:
            left, right = s.find(i), s.rfind(i)
            
            if left != -1 & right != -1:
                ans += len(set(s[left+1: right]))
                
        return ans