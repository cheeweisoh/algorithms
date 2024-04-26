import java.util.Arrays;

class Solution {
    public int minFallingPathSum(int[][] grid) {
        int n = grid.length, ans = Integer.MAX_VALUE;
        int[][] dp = new int[n][n];
        for (int row[] : dp) {
            Arrays.fill(row, -1);
        }

        for (int j = 0; j < n; j++) {
            dp[0][j] = grid[0][j];
        }

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int temp = Integer.MAX_VALUE;

                for (int k = 0; k < n; k++) {
                    if (k != j) {
                        temp = Math.min(temp, grid[i][j] + dp[i - 1][k]);
                    }

                    dp[i][j] = temp;
                }
            }
        }

        for (int j = 0; j < n; j++) {
            ans = Math.min(ans, dp[n-1][j]);
        }

        return ans;
    }
}