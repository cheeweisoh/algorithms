class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Check Palindrome

        Args:
            s (str): string to be checked

        Returns:
            bool : returns true if s is a palindrome, false otherwise
        """
        return s == s[::-1]
    
    def partition(self, s: str) -> list:
        """Palindrome Partitioning

        Args:
            s (str): string to be split

        Returns:
            ans (list): all possible partitionings of s such that every substring is a palindrome
        """
        ans = []
        
        def dfs(i, curr) -> None:
            nonlocal ans
            if i == len(s):
                ans.append(curr)
                return
            
            for j in range(i, len(s)):
                next = s[i:j+1]
                if self.isPalindrome(next):
                    dfs(j+1, curr + [s[i:j+1]])
                    
        dfs(0, [])
        return ans