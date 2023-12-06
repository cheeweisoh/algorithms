import collections
import math
import random
import heapq
import structures
import string

class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        remain = n
        
        while remain > 1:
            ans += remain//2
            if (remain%2):
                remain = remain//2 + 1
            else:
                remain = remain//2
        
        return ans

soln = Solution()
for n in [7, 14]:
    print(soln.numberOfMatches(n))