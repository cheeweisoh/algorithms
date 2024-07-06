# import collections
import math

# import random
# import heapq

# import string
# import bisect
# from structures import TreeNode


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        completeCycle = n * 2 - 2
        remainTime = time % completeCycle
        noDiff = abs(n - 1 - remainTime)
        noFromStart = n - noDiff

        return noFromStart


def main():
    soln = Solution()
    n = 4
    time = 5
    print(soln.passThePillow(n, time))


if __name__ == "__main__":
    main()
