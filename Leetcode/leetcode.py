# import collections
# import math
# import random
# import heapq

# import string
# import bisect
# from structures import *


class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        miss = 1
        ans = 0
        i = 0

        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += (miss - 1) + 1
                ans += 1
            print(miss, i, ans)

        return ans


def main():
    soln = Solution()
    nums = [1, 5, 10]
    n = 20
    print(soln.minPatches(nums, n))


if __name__ == "__main__":
    main()
