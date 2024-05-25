import collections
# import math
# import random
# import heapq

# import string
# import bisect
# from structures import *


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        wordSet = set(wordDict)
        memo = collections.defaultdict(list)

        def dfs(s):
            if not s:
                return [[]]

            if s in memo:
                return memo[s]

            for endIndex in range(1, len(s) + 1):
                word = s[:endIndex]
                if word in wordSet:
                    for subsentence in dfs(s[endIndex:]):
                        memo[s].append([word] + subsentence)
            return memo[s]

        dfs(s)

        return [" ".join(words) for words in memo[s]]


def main():
    soln = Solution()
    s = "catsanddog"
    wordDict = ["cat","cats","and","sand","dog"]
    print(soln.wordBreak(s, wordDict))


if __name__ == "__main__":
    main()
