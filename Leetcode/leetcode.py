import collections
import math
import random
import heapq
import string
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

def main():
    soln = Solution()
    for startTime, endTime, profit in [
        # [[1,2,3,3], [3,4,5,6], [50,10,40,70]],
        # [[1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60]],
        # [[1,1,1], [2,3,4], [5,6,4]],
        [[6,15,7,11,1,3,16,2], [19,18,19,16,10,8,19,8], [2,9,1,19,5,7,3,19]]         
    ]:
        print(soln.jobScheduling(startTime, endTime, profit))

if __name__ == "__main__":
    main()
