import collections

# import math
# import random
# import heapq
# import string
# import bisect
# from typing import Optional
# from structures import ListNode, TreeNode


class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        # time complexity: O(n)
        # for loop: O(n)
        # while loops: total of O(n), each i is only appended and popped once
        # all deque operations take O(1)

        # calculate prefix sums
        curr = 0
        prefix_sum = [0]

        for i in nums:
            curr += i
            prefix_sum.append(curr)

        # deque tracks the possible starting points
        dq = collections.deque()
        res = len(nums) + 1

        for i in range(len(nums) + 1):
            # if sum between range i and dq[0] satisfy, calculate min length
            while dq and prefix_sum[i] - prefix_sum[dq[0]] >= k:
                res = min(res, i - dq[0])
                dq.popleft()
            # if current sum is less than prev sum, curr position must be a negative number
            # remove starting index of negative number (we should never start an ans w a neg number)
            while dq and prefix_sum[i] <= prefix_sum[dq[-1]]:
                dq.pop()

            dq.append(i)

        return res if res <= len(nums) else -1


def main():
    soln = Solution()
    nums = [2, -1, 2, -1, -1]
    k = 3
    print(soln.shortestSubarray(nums, k))


if __name__ == "__main__":
    main()
