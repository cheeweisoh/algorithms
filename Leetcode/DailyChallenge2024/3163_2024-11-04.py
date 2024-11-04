class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        curr_count = 1

        for i in range(1, len(word)):
            if curr_count == 9 or word[i] != word[i - 1]:
                comp += str(curr_count) + word[i - 1]
                curr_count = 1
            else:
                curr_count += 1

        comp += str(curr_count) + word[-1]

        return comp
