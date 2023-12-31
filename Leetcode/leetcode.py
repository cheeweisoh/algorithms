import collections
import math
import random
import heapq
import string


class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        if len(words) == 1:
            return True
        
        s = "".join(words)
        count = collections.Counter(s)

        for val in count.values():
            if val % len(words) != 0:
                return False
        return True


def main():
    soln = Solution()

    for words in [
        ["abc", "aabc", "bc"],
        ["ab", "a"],
        ["a", "b"],
        ["caaaaa","aaaaaaaaa","a","bbb","bbbbbbbbb","bbb","cc","cccccccccccc","ccccccc","ccccccc","cc","cccc","c","cccccccc","c"],
    ]:
        print(soln.makeEqual(words))


if __name__ == "__main__":
    main()

