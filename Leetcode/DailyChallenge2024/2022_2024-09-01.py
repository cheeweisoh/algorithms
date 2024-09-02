class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if len(original) != m * n:
            return []

        ans = []
        for i in range(m):
            ans.append(original[i * n : (i + 1) * n])

        return ans
