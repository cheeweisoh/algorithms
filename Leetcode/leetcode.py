import collections
import math
import random
import heapq
import structures
import string

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ''
        count = 1
        
        for i in range(1, len(num)):
            if num[i] == num[i-1]:
                count += 1
                if count == 3:
                    ans = max(ans, num[i] * 3)
            else:
                count = 1
        
        return ans

soln = Solution()
for num in ['6777133339', '2300019', '42352338']:
    print(soln.largestGoodInteger(num))
