class Solution{
    public int[][] onesMinusZeros(int[][] grid) {
        int numRows = grid.length;
        int numCols = grid[0].length;

        int[] onesRows = new int[numRows];
        int[] onesCols = new int[numCols];


        for (int i=0; i<numRows; i++){
            for (int j=0; j<numCols; j++){
                if (grid[i][j] == 1){
                    onesRows[i] ++;
                    onesCols[j] ++;
                }
            }
        }

        int[][] diffMatrix = new int[numRows][numCols];

        for (int i=0; i<numRows; i++){
            for (int j=0; j<numCols; j++){
                diffMatrix[i][j] = 2 * onesRows[i] + 2 * onesCols[j] - numRows - numCols;
            }
        }

        return diffMatrix;
    }
}