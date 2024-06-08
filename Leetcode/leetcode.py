# import collections
# import math
# import random
# import heapq

# import string
# import bisect
# from structures import *


class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        mem = {0: -1}
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            rem = total % k

            if rem in mem:
                if i - mem[rem] > 1:
                    return True
            else:
                mem[rem] = i

        return False


def main():
    soln = Solution()
    nums = [0]
    k = 1
    print(soln.checkSubarraySum(nums, k))

    nums = [23, 2, 6, 4, 7]
    k = 6
    print(soln.checkSubarraySum(nums, k))

    nums = [23, 2, 4, 6, 6]
    k = 7
    print(soln.checkSubarraySum(nums, k))


if __name__ == "__main__":
    main()
