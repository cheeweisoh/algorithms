# import collections
# import math
# import random
# import heapq

# import string
# import bisect
# from structures import *


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        count, idx = 0, 0

        while count < len(nums):
            print(count, idx, nums)
            if nums[idx] == 0:
                nums.pop(idx)
                nums.insert(0, 0)
                idx += 1
            elif nums[idx] == 2:
                nums.pop(idx)
                nums.insert(len(nums), 2)
            else:
                idx += 1
            count += 1


def main():
    soln = Solution()
    nums = [1, 2, 0]
    soln.sortColors(nums)
    print(nums)


if __name__ == "__main__":
    main()
