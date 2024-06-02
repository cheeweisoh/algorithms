# import collections
# import math
# import random
# import heapq

# import string
# import bisect
# from structures import *


class Solution:
    def reverseString(self, s: list[str]) -> None:
        l, r = 0, len(s)-1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r += 1


def main():
    soln = Solution()
    s = ["h", "e", "l", "l", "o"]
    print(soln.reverseString(s))


if __name__ == "__main__":
    main()
