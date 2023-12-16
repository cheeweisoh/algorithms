class Solution:
    def maxProfit(self, prices: list) -> int:
        """Best Time to Buy and Sell Stock

        Args:
            prices (list): array where prices[i] is the price of a given stock on the i-th day

        Returns:
            ans (int): maximum profit, 0 if no profit is achievable
        """
        if len(prices) == 0:
            return 0
        
        ans = 0
        curr = prices[0]
        
        for i in range(1, len(prices)):
            curr_profit = prices[i] - curr
            ans = max(ans, curr_profit)
            curr = min(curr, prices[i])
            
        return ans