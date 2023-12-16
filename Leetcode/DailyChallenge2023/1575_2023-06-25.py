class Solution:
    def countRoutes(self, locations: list, start: int, finish: int, fuel: int) -> int:
        """Count All Possible Routes

        Args:
            locations (list): locations[i] represents the location of city i
            start (int): starting city
            finish (int): ending city
            fuel (int): amount of fuel available

        Returns:
            int: number of all possible routes from start to finish, modulo 10**9+7
        """
        n = len(locations)
        dp = [[-1] * (fuel + 1) for _ in range(n)]
        
        def helper(curr_loc, curr_fuel):
            ans = 0
            if curr_fuel < 0:
                return 0
            if dp[curr_loc][curr_fuel] != -1:
                return dp[curr_loc][curr_fuel]
            if curr_loc == finish:
                ans += 1
            
            for i in range(n):
                if i != curr_loc:
                    req_fuel = abs(locations[curr_loc] - locations[i])
                    ans = (ans + helper(i, curr_fuel-req_fuel)) % (10**9+7)
            dp[curr_loc][curr_fuel] = ans
            return ans
        
        return helper(start, fuel)