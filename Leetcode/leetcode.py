import collections
import math
import random
import heapq
import string


class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        counts = collections.defaultdict(int)
        ans = [[]]
        
        for i in nums:
            counts[i] += 1
            if counts[i] > len(ans):
                ans.append([])
            
            ans[counts[i] - 1].append(i)
        
        return ans


def main():
    soln = Solution()
    for nums in [[1, 3, 4, 1, 2, 3, 1], [1, 2, 3, 4]]:
        print(soln.findMatrix(nums))


if __name__ == "__main__":
    main()

