class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) <= 2:
            return s

        res = [s[0], s[1]]

        for i in s[2:]:
            if i != res[-1] or i != res[-2]:
                res.append(i)

        return "".join(res)
