# import collections
# import math
# import random
# import heapq

# import string
# import bisect
# from structures import *


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []

        def dfs(idx, curr):
            ans.append(curr)
            for i in range(idx, len(nums)):
                dfs(i + 1, curr + [nums[i]])

        dfs(0, [])

        return ans


def main():
    soln = Solution()
    nums = [1, 2, 3]
    print(soln.subsets(nums))


if __name__ == "__main__":
    main()
