# import collections
# import math

# import random
# import heapq

# import string
# import bisect
# from structures import TreeNode


class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        count = 0
        for i in arr:
            if i % 2 != 0:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0

        return False

def main():
    soln = Solution()
    arr = [1,2,34,3,4,5,7,23,12]
    print(soln.threeConsecutiveOdds(arr))


if __name__ == "__main__":
    main()
