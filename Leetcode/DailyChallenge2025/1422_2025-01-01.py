class Solution:
    def maxScore(self, s: str) -> int:
        res = 0 if s[0] == "1" else 1
        res += s[1:].count("1")

        nres = res
        for i in s[1:-1]:
            if i == "0":
                nres += 1
            else:
                nres -= 1
            res = max(res, nres)

        return res
