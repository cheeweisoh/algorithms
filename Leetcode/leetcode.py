# import collections
# import bisect
# import math
# import random
# import heapq
# import string
# from typing import Optional
# from structures import ListNode, TreeNode


class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        ls, rs = [0], [0]

        curr = 0
        for i in boxes[:-1]:
            if i == "1":
                curr += 1
            rs.append(rs[-1] + curr)

        curr = 0
        for i in boxes[:0:-1]:
            if i == "1":
                curr += 1
            ls.append(ls[-1] + curr)
        ls = ls[::-1]

        res = []
        for i in range(len(boxes)):
            res.append(ls[i] + rs[i])

        return res


def main():
    soln = Solution()
    boxes = "001011"
    print(soln.minOperations(boxes))


if __name__ == "__main__":
    main()
