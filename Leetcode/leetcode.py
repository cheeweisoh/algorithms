import collections

# import math
# import random
# import heapq

# import string
# import bisect
# from structures import *


class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        sortedHeights = sorted(heights)
        ans = 0

        for i in range(len(heights)):
            if heights[i] != sortedHeights[i]:
                ans += 1

        return ans


def main():
    soln = Solution()
    heights = [1, 1, 4, 2, 1, 3]
    print(soln.heightChecker(heights))


if __name__ == "__main__":
    main()
