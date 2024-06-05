import collections 

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        minFreq = collections.Counter(words[0])

        for word in words[1:]:
            minFreq &= collections.Counter(word)

        return list(minFreq.elements())
