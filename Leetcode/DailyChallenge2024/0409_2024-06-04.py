class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = set()
        ans = 0

        for i in s:
            if i in counts:
                counts.remove(i)
                ans += 2
            else:
                counts.add(i)

        if counts:
            ans += 1

        return ans
