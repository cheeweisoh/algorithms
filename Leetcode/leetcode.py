# import collections
# import math
# import random
# import heapq
# import string
# import bisect
# from typing import Optional
# from structures import ListNode, TreeNode


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1, s2 = sorted(
            [sentence1.split(" "), sentence2.split(" ")], key=lambda x: len(x)
        )
        s, e = 0, 0

        while s < len(s1) and s1[s] == s2[s]:
            s += 1

        while e < len(s1) and s1[len(s1) - e - 1] == s2[len(s2) - e - 1]:
            e += 1

        return s + e >= len(s1)


def main():
    soln = Solution()
    s1 = "My name is Hey"
    s2 = "My Hey"
    print(soln.areSentencesSimilar(s1, s2))


if __name__ == "__main__":
    main()
