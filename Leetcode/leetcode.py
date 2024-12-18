# import collections
# import bisect
# import math
# import random
import heapq

# import string
# from typing import Optional
# from structures import ListNode, TreeNode


class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        h = []

        for p, t in classes:
            heapq.heappush(h, (p / t - ((p + 1) / (t + 1)), p, t))

        for _ in range(extraStudents):
            _, cp, ct = heapq.heappop(h)
            heapq.heappush(
                h, ((cp + 1) / (ct + 1) - (cp + 2) / (ct + 2), cp + 1, ct + 1)
            )

        res = 0
        for _, cp, ct in h:
            res += cp / ct

        return res / len(classes)


def main():
    soln = Solution()
    classes = [[2, 4], [3, 9], [4, 5], [2, 10]]
    extraStudents = 4
    print(soln.maxAverageRatio(classes, extraStudents))


if __name__ == "__main__":
    main()
