import collections

# import math
# import random
# import heapq

# import string
# import bisect
# from structures import *


class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        minFreq = collections.Counter(words[0])

        for word in words[1:]:
            minFreq &= collections.Counter(word)

        return list(minFreq.elements())


def main():
    soln = Solution()
    words = ["bella", "label", "roller"]
    print(soln.commonChars(words))


if __name__ == "__main__":
    main()
