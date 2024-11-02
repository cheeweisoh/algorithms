# import collections
# import math
# import random
# import heapq
# import string
# import bisect
# from typing import Optional
# from structures import ListNode, TreeNode


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s = sentence.split(" ")

        for i in range(1, len(s)):
            print(s[i - 1][-1], s[i][0])
            if s[i - 1][-1] != s[i][0]:
                return False

        return s[0][0] == s[-1][-1]


def main():
    soln = Solution()
    sentence = "ab a"
    print(soln.isCircularSentence(sentence))
    sentence = "Leetcode is cool"
    print(soln.isCircularSentence(sentence))


if __name__ == "__main__":
    main()
