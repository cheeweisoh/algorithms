import collections
import math
import random
import heapq
import string
import bisect

class Solution:
    def rob(self, nums: list[int]) -> int:
        mem = {}
        
        def dfs(nums):
            n = len(nums)
            
            if n in mem.keys():
                return mem[n]
            
            if n == 2:
                return max(nums[0], nums[1])
            elif n == 1:
                return nums[0]
            elif n == 0:
                return 0
            
            temp = max(nums[0] + dfs(nums[2:]), dfs(nums[1:]))
            mem[n] = temp
            
            return temp
        
        return dfs(nums)

def main():
    soln = Solution()
    for nums in [
        [1,2,3,1],
        [2,7,9,3,1],
    ]:
        print(soln.rob(nums))

if __name__ == "__main__":
    main()
