class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(st, seen):
            if st == len(s):
                return 0
            ans = 0

            for en in range(st + 1, len(s) + 1):
                sub = s[st:en]
                if sub not in seen:
                    seen.add(sub)
                    ans = max(ans, 1 + backtrack(en, seen))
                    seen.remove(sub)
            return ans

        return backtrack(0, set())
