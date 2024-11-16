# import collections
# import math
# import random
# import heapq
# import string
# import bisect
# from typing import Optional
# from structures import ListNode, TreeNode


class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        if k == 1:
            return nums

        win_size = 1
        res = [-1] * (len(nums) - k + 1)
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                win_size += 1
                if win_size == k:
                    res[i - k + 1] = nums[i]
                    win_size -= 1
            else:
                win_size = 1

        return res


def main():
    soln = Solution()
    nums = [1, 2, 3, 4, 3, 2, 5]
    k = 3
    print(soln.resultsArray(nums, k))
    nums = [3, 2, 3, 2, 3, 2]
    k = 2
    print(soln.resultsArray(nums, k))


if __name__ == "__main__":
    main()
