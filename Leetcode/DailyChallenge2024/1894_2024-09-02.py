class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        total = sum(chalk)
        remain = k % total

        for i in range(len(chalk)):
            if remain < chalk[i]:
                return i
            else:
                remain -= chalk[i]
