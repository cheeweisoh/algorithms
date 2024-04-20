// import java.util.ArrayList;
// import java.util.List;

// class Solution {
//     public int[][] findFarmland(int[][] land) {
//         List<int[]> output = new ArrayList<>();
        
//         for (int i = 0; i < land.length; i++) {
//             for (int j = 0; j < land[0].length; j++) {
//                 if (land[i][j] == 1) {
//                     int[] arr = {i, j, i, j};
//                     helper(i, j, arr, land);
//                     output.add(arr);
//                 }
//             }
//         }

//         int[][] ans = new int[output.size()][4];
        
//         for (int i = 0 ; i < output.size(); i++) {
//             ans[i] = output.get(i);
//         }

//         return ans;
//     }

//     private void helper(int i, int j, int[] arr, int[][] land) {
//         if (i < 0 || j < 0 || i > land.length - 1 || j > land[0].length - 1 || land[i][j] != 1) return;

//         land[i][j] = 0;
//         if (i < arr[0]) {
//             arr[0] = i;
//         }
//         if (j < arr[1]) {
//             arr[1] = j;
//         }
//         if (i > arr[2]) {
//             arr[2] = i;
//         }
//         if (j > arr[3]) {
//             arr[3] = j;
//         }

//         helper(i + 1, j, arr, land);
//         helper(i - 1, j, arr, land);
//         helper(i, j + 1, arr, land);
//         helper(i, j - 1, arr, land);
//     }
// }