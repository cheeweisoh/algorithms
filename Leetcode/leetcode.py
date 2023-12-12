import collections
import math
import random
import heapq
import string

class Solution:
    def maxProduct(self, nums: list[int]):
        num1 = 0
        num2 = 0
        
        for i in nums:
            if i > num1:
                num1, num2 = i, num1
            elif i > num2:
                num2 = i
                
        return num1, num2

soln = Solution()
nums = [3,4,5,2]
print(soln.maxProduct(nums))
nums = [1,5,4,5]
print(soln.maxProduct(nums))
nums = [3,7]
print(soln.maxProduct(nums))