class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    if matrix[i][j] == 1:
                        dp[i][j] = 1
                else:
                    if (
                        matrix[i][j] == 1
                        and matrix[i - 1][j] >= 1
                        and matrix[i][j - 1] >= 1
                        and matrix[i - 1][j - 1] >= 1
                    ):
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    elif matrix[i][j] == 1:
                        dp[i][j] = 1

        res = sum(sum(dp[i]) for i in range(m))

        return res
