class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        res = 0
        n = len(pref)

        for w in words:
            if len(w) >= n and w[:n] == pref:
                res += 1

        return res
