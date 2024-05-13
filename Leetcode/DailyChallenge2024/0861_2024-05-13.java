class Solution {
    public int matrixScore(int[][] grid) {
        int nrow = grid.length, ncol = grid[0].length;
        int score = (1 << (ncol - 1)) * nrow;

        for (int i = 1; i < ncol; i++) {
            int currVal = 1 << (ncol - 1 - i);
            int sameBit = 0;

            for (int j = 0; j < nrow; j++) {
                if (grid[j][i] == grid[j][0]) {
                    sameBit++;
                }
            }

            score += Math.max(sameBit, nrow - sameBit) * currVal;
        }

        return score;
    }
} 
