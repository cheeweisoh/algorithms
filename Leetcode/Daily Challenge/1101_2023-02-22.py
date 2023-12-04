class Solution:
    def shipWithinDays(self, weights: list, days: int) -> int:
        """_summary_

        Args:
            weights (list): weights[i] is the weight of the i-th package
            days (int): days that packages must be shipped out

        Returns:
            ans (int): least weight capacity of the ship that will result in all the packages being shipped out
        """
        left = 0
        right = 0
        for i in weights:
            left = max(left, i)
            right += i
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if self.check(weights, days, mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

    def check(self, weights: list, days: int, capacity: int) -> bool:
        required_days = 1
        curr_weight = 0
        for i in weights:
            if curr_weight + i > capacity:
                required_days += 1
                curr_weight = 0
            curr_weight += i
        if required_days > days:
            return False
        return True