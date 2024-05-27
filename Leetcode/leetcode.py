# import collections
# import math
# import random
# import heapq

# import string
# import bisect
# from structures import *


class Solution:
    def specialArray(self, nums: list[int]) -> int:
        counts = [0] * (len(nums) + 1)

        for i in nums:
            if i >= len(counts):
                counts = [x + 1 for x in counts]
            else:
                counts[: i + 1] = [x + 1 for x in counts[: i + 1]]
        print(counts)

        for j in range(len(counts)):
            if j == counts[j]:
                return j

        return -1


def main():
    soln = Solution()
    nums = [3, 5]
    print(soln.specialArray(nums))


if __name__ == "__main__":
    main()
