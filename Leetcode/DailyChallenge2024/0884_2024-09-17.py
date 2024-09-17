from collections import Counter


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        s1Words, s2Words = s1.split(), s2.split()
        allWords = s1Words + s2Words
        wordCount = Counter(allWords)

        res = []
        for i in wordCount:
            if wordCount[i] == 1:
                res.append(i)

        return res
