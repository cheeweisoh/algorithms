# import collections
# import math
# import random
# import heapq
# import string
# import bisect
# from typing import Optional
# from structures import ListNode, TreeNode


class Solution:
    def longestSquareStreak(self, nums: list[int]) -> int:
        res = 1
        mem = {}
        nums.sort()

        for i in nums:
            ir = i**0.5
            if ir in mem:
                mem[i] = mem[ir] + 1
                if mem[i] > res:
                    res = mem[i]
            else:
                mem[i] = 1

        return res if res != 1 else -1


def main():
    soln = Solution()
    nums = [2, 3, 5, 6, 7]
    print(soln.longestSquareStreak(nums))


if __name__ == "__main__":
    main()
