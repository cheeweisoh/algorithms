# import collections
import bisect

# import math
# import random
# import heapq
# import string
# from typing import Optional
# from structures import ListNode, TreeNode


class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        events.sort(key=lambda x: x[1])
        curr_max = []
        curr_max_val = 0
        res = 0

        for _, e, v in events:
            curr_max_val = max(curr_max_val, v)
            curr_max.append((e, curr_max_val))

        print(curr_max)

        for s, e, v in events:
            res = max(res, v)

            idx = bisect.bisect_left(curr_max, (s, 0)) - 1
            print(idx)
            if idx >= 0:
                res = max(res, v + curr_max[idx][1])

        return res


def main():
    soln = Solution()
    events = [[1, 3, 2], [4, 5, 2], [2, 4, 3]]
    print(soln.maxTwoEvents(events))


if __name__ == "__main__":
    main()
