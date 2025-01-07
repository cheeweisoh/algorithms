# import collections
# import bisect
# import math
# import random
# import heapq
# import string
# from typing import Optional
# from structures import ListNode, TreeNode


class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        words.sort(key=lambda x: len(x), reverse=True)
        res = set()
        n = len(words)

        for i in range(n):
            for j in range(i + 1, n):
                if words[i].find(words[j]) != -1:
                    res.add(words[j])

        return list(res)


def main():
    soln = Solution()
    words = ["leetcoder", "leetcode", "od", "hamlet", "am"]
    print(soln.stringMatching(words))


if __name__ == "__main__":
    main()
