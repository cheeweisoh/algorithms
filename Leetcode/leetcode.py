# import collections
# import math
# import random
# import heapq
# import string
# import bisect
# from typing import Optional
# from structures import ListNode, TreeNode


class Solution:
    def minimumSteps(self, s: str) -> int:
        steps, blacks = 0, 0
        for i in s:
            if i == "0":
                steps += blacks
            else:
                blacks += 1

        return steps


def main():
    soln = Solution()
    s = "100"
    print(soln.minimumSteps(s))


if __name__ == "__main__":
    main()
