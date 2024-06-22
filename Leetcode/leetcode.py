# import collections
# import math

# import random
# import heapq

# import string
# import bisect
# from structures import *


class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        prefixSum = [0 for _ in range(len(nums) + 1)]
        prefixSum[0] = 1
        curr = 0
        ans = 0

        for i in range(len(nums)):
            nums[i] %= 2

        for num in nums:
            curr += num
            if curr >= k:
                ans += prefixSum[curr - k]
            prefixSum[curr] += 1

        return ans


def main():
    soln = Solution()
    nums = [1, 1, 2, 1, 1]
    k = 3
    print(soln.numberOfSubarrays(nums, k))


if __name__ == "__main__":
    main()
