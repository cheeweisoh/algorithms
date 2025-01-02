class Solution:
    def check_vowel(self, char: str) -> int:
        return 0x208222 >> (ord(char) & 0x1F) & 1

    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        prefix_sum = [0]
        curr_sum = 0
        res = []

        for word in words:
            if self.check_vowel(word[0]) and self.check_vowel(word[-1]):
                curr_sum += 1
            prefix_sum.append(curr_sum)

        for s, e in queries:
            res.append(prefix_sum[e + 1] - prefix_sum[s])

        return res
