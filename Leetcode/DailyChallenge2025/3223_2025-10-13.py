class Solution:
    def minimumLength(self, s: str) -> int:
        c = set(s)
        res = 0

        for i in c:
            f = s.count(i)
            if f % 2:
                res += 1
            else:
                res += 2

        return res
