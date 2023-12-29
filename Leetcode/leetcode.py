import collections
import math
import random
import heapq
import string

class Solution:    
    def minDifficulty(self, jobDifficulty: list[int] , d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        elif len(jobDifficulty) == d:
            return sum(jobDifficulty)
        
        mem = {}
        
        def dfs(idx, d, curr_max):
            if idx == len(jobDifficulty) and d == 0:
                return 0
            elif idx == len(jobDifficulty) or d == 0:
                return float('inf')
            
            if (idx, d, curr_max) in mem.keys():
                return mem[(idx, d, curr_max)]
            
            curr_max = max(curr_max, jobDifficulty[idx])
            ans = min(dfs(idx+1, d, curr_max), dfs(idx+1, d-1, -1) + curr_max)
            mem[(idx, d, curr_max)] = ans
            
            return ans
            
        return dfs(0, d, -1)


def main():
    soln = Solution()
    
    for jobDifficulty, d in [
        [[6,5,4,3,2,1], 2],
        [[9,9,9], 4],
        [[1,1,1], 3]
    ]:
        print(soln.minDifficulty(jobDifficulty, d))

if __name__ == "__main__":
    main()