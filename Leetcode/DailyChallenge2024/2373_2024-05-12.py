class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        ans = [[0 for _ in range(n - 2)] for _ in range(n - 2)]

        for i in range(1, n - 1):
            for j in range(1, n - 1):
                temp = 0

                for k in range(i - 1, i + 2):
                    for m in range(j - 1, j + 2):
                        temp = max(temp, grid[k][m])

                ans[i - 1][j - 1] = temp

        return ans
