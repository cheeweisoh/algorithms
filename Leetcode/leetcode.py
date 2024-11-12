# import collections
# import math
# import random
# import heapq
# import string
# import bisect
# from typing import Optional
# from structures import ListNode, TreeNode


class Solution:
    def maximumBeauty(self, items: list[list[int]], queries: list[int]) -> list[int]:
        items.sort(key=lambda x: x[0])
        queries_sort = [[i, q] for i, q in enumerate(queries)]
        queries_sort.sort(key=lambda x: x[1])
        print(queries_sort)

        res = [0] * len(queries)
        c = 0
        curr_max = 0

        for pos, q in queries_sort:
            print(pos, q)
            while c < len(items) and q >= items[c][0]:
                curr_max = max(curr_max, items[c][1])
                c += 1
            res[pos] = curr_max

        return res


def main():
    soln = Solution()
    items = [
        [193, 732],
        [781, 962],
        [864, 954],
        [749, 627],
        [136, 746],
        [478, 548],
        [640, 908],
        [210, 799],
        [567, 715],
        [914, 388],
        [487, 853],
        [533, 554],
        [247, 919],
        [958, 150],
        [193, 523],
        [176, 656],
        [395, 469],
        [763, 821],
        [542, 946],
        [701, 676],
    ]
    queries = [
        885,
        1445,
        1580,
        1309,
        205,
        1788,
        1214,
        1404,
        572,
        1170,
        989,
        265,
        153,
        151,
        1479,
        1180,
        875,
        276,
        1584,
    ]
    print(soln.maximumBeauty(items, queries))


if __name__ == "__main__":
    main()
