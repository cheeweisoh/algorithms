class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0

        for i in set(s):
            l, r = s.find(i), s.rfind(i)

            if l != -1 and r != -1:
                res += len(set(s[l + 1 : r]))

        return res
