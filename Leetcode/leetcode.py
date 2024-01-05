import collections
import math
import random
import heapq
import string


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        mem = [-1] * len(nums)
        mem[-1] = 1

        for i in range(len(nums) - 2, -1, -1):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    mem[i] = max(mem[i], mem[j] + 1)
            if mem[i] == -1:
                mem[i] = 1

        return max(mem)


def main():
    soln = Solution()
    for nums in [
        [10, 9, 2, 5, 3, 7, 101, 18],
        [0, 1, 0, 3, 2, 3],
        [7, 7, 7, 7, 7, 7, 7],
    ]:
        print(soln.lengthOfLIS(nums))


if __name__ == "__main__":
    main()
