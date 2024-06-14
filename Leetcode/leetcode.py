# import collections
# import math
# import random
# import heapq

# import string
# import bisect
# from structures import *


class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        nums.sort()
        ans = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                ans += nums[i - 1] - nums[i] + 1
                nums[i] = nums[i - 1] + 1
            print(nums)

        return ans


def main():
    soln = Solution()
    nums = [3, 2, 1, 2, 1, 7]
    print(soln.minIncrementForUnique(nums))


if __name__ == "__main__":
    main()
