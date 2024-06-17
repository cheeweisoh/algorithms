# import collections
import math

# import random
# import heapq

# import string
# import bisect
# from structures import *


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(math.sqrt(c))

        while l <= r:
            s = l * l + r * r
            if s == c:
                return True
            elif s < c:
                l += 1
            else:
                r -= 1

        return False


def main():
    soln = Solution()
    print(soln.judgeSquareSum(7))


if __name__ == "__main__":
    main()
