# import collections
# import math
# import random
# import heapq

# import string
# import bisect
# from structures import *


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = set()
        ans = 0

        for i in s:
            if i in counts:
                counts.remove(i)
                ans += 2
            else:
                counts.add(i)

        if counts:
            ans += 1

        return ans


def main():
    soln = Solution()
    s = "abccccdde"
    print(soln.longestPalindrome(s))


if __name__ == "__main__":
    main()
