# import collections
# import math
# import random
# import heapq

# import string
# import bisect
# from structures import TreeNode


class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        total = sum(chalk)
        remain = k % total

        for i in range(len(chalk)):
            if remain < chalk[i]:
                return i
            else:
                remain -= chalk[i]


def main():
    soln = Solution()
    chalk = [3, 4, 1, 2]
    k = 25
    print(soln.chalkReplacer(chalk, k))


if __name__ == "__main__":
    main()
