class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        sortedHeights = sorted(heights)
        ans = 0

        for i in range(len(heights)):
            if heights[i] != sortedHeights[i]:
                ans += 1

        return ans
