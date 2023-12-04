class Solution:
    def tallestBillboard(self, rods: list) -> int:
        """Tallest Billboard

        Args:
            rods (list): lengths of rods that can be welded together

        Returns:
            int: largest possible height of billboard installation
        """
        total = sum(rods)
        dp = [-1] * (total + 1)
        dp[0] = 0
        
        for rod in rods:
            temp_dp = dp[:]
            
            for i in range(total):
                if temp_dp[i] < 0:
                    continue
                
                dp[i+rod] = max(dp[i+rod], temp_dp[i])
                dp[abs(i-rod)] = max(dp[abs(i-rod)], temp_dp[i]+min(i,rod))
                
        return dp[0]