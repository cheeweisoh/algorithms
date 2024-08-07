# import collections
import math

# import random
# import heapq

# import string
# import bisect
# from structures import TreeNode


class Solution:
    def minOperations(self, logs: list[str]) -> int:
        count = 0

        for i in logs:
            if i == "./":
                print(count)
                continue
            elif i == "../":
                count = max(count - 1, 0)
            else:
                count += 1

        return max(count, 0)


def main():
    soln = Solution()
    logs = ["./", "wz4/", "../", "mj2/", "../", "../", "ik0/", "il7/"]
    print(soln.minOperations(logs))


if __name__ == "__main__":
    main()
