# import collections
# import math
# import random
# import heapq

# import string
# import bisect
# from structures import *


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        start = 0
        currCost = 0
        maxLen = 0

        for end in range(len(s)):
            currCost += abs(ord(s[end]) - ord(t[end]))

            while currCost > maxCost:
                currCost -= abs(ord(s[start]) - ord(t[start]))
                start += 1

            maxLen = max(maxLen, end - start + 1)

        return maxLen


def main():
    soln = Solution()
    s = "abcd"
    t = "bcdf"
    maxCost = 3
    print(soln.equalSubstring(s, t, maxCost))


if __name__ == "__main__":
    main()
