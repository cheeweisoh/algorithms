import bisect

class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        sched = [[startTime[i], endTime[i], profit[i]] for i in range(len(startTime))]
        sched.sort(key = lambda x: x[1])
        totalProfit = [0] * (len(startTime) + 1)
        
        for i, (s, e, p) in enumerate(sched):
            idx = bisect.bisect_right(sched, s, hi=i, key=lambda x: x[1])
            totalProfit[i+1] = max(totalProfit[i], totalProfit[idx] + p)
        
        return totalProfit[-1]