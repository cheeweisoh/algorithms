import collections
# import math
# import random
# import heapq

# import string
# import bisect
# from structures import *


class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> bool:
        mem = collections.defaultdict(int)
        mem[0] = 1
        total = 0
        ans = 0

        for i in range(len(nums)):
            total += nums[i]
            rem = total % k
            ans += mem[rem]
            mem[rem] += 1


        return ans


def main():
    soln = Solution()
    nums = [4, 5, 0, -2, -3, 1]
    k = 5
    print(soln.subarraysDivByK(nums, k))

    nums = [5]
    k = 9
    print(soln.subarraysDivByK(nums, k))


if __name__ == "__main__":
    main()
