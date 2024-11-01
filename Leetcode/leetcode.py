# import collections
# import math
# import random
# import heapq
# import string
# import bisect
# from typing import Optional
# from structures import ListNode, TreeNode


class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) <= 2:
            return s

        res = [s[0], s[1]]

        for i in s[2:]:
            if i != res[-1] or i != res[-2]:
                res.append(i)

        return "".join(res)


def main():
    soln = Solution()
    s = "aaabaaaa"
    print(soln.makeFancyString(s))


if __name__ == "__main__":
    main()
