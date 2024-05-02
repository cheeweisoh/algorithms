class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if word[i] == ch:
                ans = word[: i + 1][::-1] + word[i + 1 :]
                return ans

        return word


soln = Solution()
word = "abcdefd"
ch = "d"
print(soln.reversePrefix(word, ch))
