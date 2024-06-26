# import collections
# import math

# import random
# import heapq

# import string
# import bisect
# from structures import *


class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        n = len(nums)
        flipped = 0
        ans = 0
        fp = [0] * n

        for i in range(n):
            print(i, flipped)
            if i >= k:
                flipped ^= fp[i - k]
            if flipped == nums[i]:
                if i + k > n:
                    return -1
                fp[i] = 1
                flipped ^= 1
                ans += 1
            print(i, flipped, fp[i - k])

        return ans


def main():
    soln = Solution()
    nums = [0, 0, 0, 1, 0, 1, 1, 0]
    k = 3
    print(soln.minKBitFlips(nums, k))


if __name__ == "__main__":
    main()
