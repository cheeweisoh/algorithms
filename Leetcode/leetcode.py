# import collections
# import bisect
# import math
# import random
# import heapq
# import string
# from typing import Optional
# from structures import ListNode, TreeNode


class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        prefix_sum = [0] * (len(s) + 1)

        for start, end, dir in shifts:
            change = 1 if dir else -1
            prefix_sum[start] += change
            prefix_sum[end + 1] -= change

        print(prefix_sum)

        res = list(s)
        curr = 0
        for i in range(len(s)):
            curr += prefix_sum[i]
            res[i] = chr(ord("a") + (ord(res[i]) - ord("a") + curr) % 26)

        return "".join(res)


def main():
    soln = Solution()
    s = "xuwdbdqik"
    shifts = [
        [4, 8, 0],
        [4, 4, 0],
        [2, 4, 0],
        [2, 4, 0],
        [6, 7, 1],
        [2, 2, 1],
        [0, 2, 1],
        [8, 8, 0],
        [1, 3, 1],
    ]
    print(soln.shiftingLetters(s, shifts))


if __name__ == "__main__":
    main()
