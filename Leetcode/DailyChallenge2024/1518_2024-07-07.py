class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange:
            temp = numBottles // numExchange
            ans += temp
            numBottles = temp + (numBottles % numExchange) 

        return ans
