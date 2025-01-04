# import collections
# import bisect
# import math
# import random
# import heapq
# import string
# from typing import Optional
# from structures import ListNode, TreeNode


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0

        for i in set(s):
            l, r = s.find(i), s.rfind(i)

            if l != -1 and r != -1:
                res += len(set(s[l + 1 : r]))

        return res


def main():
    soln = Solution()
    s = "aabca"
    print(soln.countPalindromicSubsequence(s))


if __name__ == "__main__":
    main()
