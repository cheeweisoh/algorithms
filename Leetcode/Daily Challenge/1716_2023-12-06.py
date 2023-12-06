class Solution:
    def totalMoney(self, n: int) -> int:
        """Calculate Money in Leetcode Bank

        Args:
            n (int): number of days

        Returns:
            int: total amount of money after n days
        """
        complete_weeks = n // 7
        complete_weeks_money = (complete_weeks * 28) + ((complete_weeks * (complete_weeks - 1) * 7) // 2)
        
        remaining_days = n - (complete_weeks * 7)
        remaining_money = sum(range(complete_weeks+1, complete_weeks+remaining_days+1))
        
        return complete_weeks_money + remaining_money