import collections

# import math
# import random
import heapq

# import string
# import bisect
# from structures import *


class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:

        def dfs(idx, curr):
            if idx == len(nums):
                return curr

            print(nums[idx])
            include = dfs(idx + 1, curr ^ nums[idx])
            exclude = dfs(idx + 1, curr)

            return include + exclude

        return dfs(0, 0)


def main():
    soln = Solution()
    nums = [5, 1, 6]
    print(soln.subsetXORSum(nums))


if __name__ == "__main__":
    main()
