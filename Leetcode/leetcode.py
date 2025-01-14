from collections import defaultdict

# import bisect
# import math
# import random
# import heapq
# import string
# from typing import Optional
# from structures import ListNode, TreeNode


class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        counts = defaultdict(int)
        res = []

        for i in range(len(A)):
            counts[A[i]] += 1
            counts[B[i]] += 1

            curr = 0
            for j in counts.values():
                if j == 2:
                    curr += 1
            res.append(curr)

        return res


def main():
    soln = Solution()
    A = [2, 3, 1]
    B = [3, 1, 2]
    print(soln.findThePrefixCommonArray(A, B))


if __name__ == "__main__":
    main()
