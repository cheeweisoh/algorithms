class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """Edit Distance

        Args:
            word1 (str): string 1
            word2 (str): string 2

        Returns:
            int: minimum number of operations (insert, delete, replace) required to convert word1 to word2
        """
        
        dp = [[float('inf')] * (len(word2)+1) for _ in range(len(word1)+1)]
        
        for j in range(len(word2)+1):
            dp[-1][j] = len(word2) - j
        
        for i in range(len(word1)+1):
            dp[i][-1] = len(word1) - i
        
        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):                
                curr1 = word1[i]
                curr2 = word2[j]
                
                
                if curr1 != curr2:
                    dp[i][j] = min(dp[i][j+1], dp[i+1][j], dp[i+1][j+1]) + 1
                else:
                    dp[i][j] = dp[i+1][j+1]
                
        return dp[0][0]