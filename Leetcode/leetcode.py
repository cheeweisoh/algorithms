import collections

# import math
# import random
# import heapq

# import string
# import bisect
# from structures import *


class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        posDict = {}
        for pos, num in enumerate(arr2):
            posDict[num] = pos
        for num in arr1:
            if num not in posDict.keys():
                posDict[num] = 1001 + num

        ans = sorted(arr1, key=lambda x: posDict[x])
        return ans


def main():
    soln = Solution()
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    print(soln.relativeSortArray(arr1, arr2))


if __name__ == "__main__":
    main()
