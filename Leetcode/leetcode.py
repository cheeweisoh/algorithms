import collections
import math
import random
import heapq
import string
import bisect


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]):
        n = len(nums)
        total = 0
        mem = [collections.defaultdict(int) for _ in range(n)]
        
        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                mem[i][diff] += 1
                
                if mem[j][diff]:
                    mem[i][diff] += mem[j][diff]
                    total += mem[j][diff]
        
        return total

def main():
    soln = Solution()
    for nums in [
        [2,4,6,8,10],
        [7,7,7,7,7]
    ]:
        print(soln.numberOfArithmeticSlices(nums))

if __name__ == "__main__":
    main()
