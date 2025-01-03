# import collections
# import bisect
# import math
# import random
# import heapq
# import string
# from typing import Optional
# from structures import ListNode, TreeNode


class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        total = sum(nums)
        curr = 0
        res = 0

        for n in nums[:-1]:
            curr += n
            if curr >= total - curr:
                res += 1

        return res


def main():
    soln = Solution()
    nums = [10, 4, -8, 7]
    print(soln.waysToSplitArray(nums))


if __name__ == "__main__":
    main()
