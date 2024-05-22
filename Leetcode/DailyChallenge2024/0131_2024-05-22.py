class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]
    
    def partition(self, s: str) -> list:
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
