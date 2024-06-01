# import collections
# import math
# import random
# import heapq

# import string
# import bisect
# from structures import *


class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0

        for i in range(1, len(s)):
            print(i)
            ans += abs(ord(s[i]) - ord(s[i-1]))

        return ans


def main():
    soln = Solution()
    s = "hello"
    print(soln.scoreOfString(s))


if __name__ == "__main__":
    main()
