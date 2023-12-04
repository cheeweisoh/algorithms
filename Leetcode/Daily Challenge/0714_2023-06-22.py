class Solution:
    def maxProfit(self, prices: list, fee: int) -> int:
        """Best Time to Buy and Sell Stock with Transaction Fee

        Args:
            prices (list): prices[i] is the price of a given stock on the i-th day
            fee (int): transaction fee

        Returns:
            int: maximum profit that you can achieve
        """
        n = len(prices)
        dp = [[0] * 2 for _ in range(n+1)]
        
        for i in range(n-1, -1, -1):
            print(i)
            for j in range(2):
                if j == 1:
                    dp[i][j] = max(dp[i+1][j], dp[i+1][0] - prices[i])
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i+1][1] + prices[i] - fee)
            print(dp)
                
        return dp[0][1]