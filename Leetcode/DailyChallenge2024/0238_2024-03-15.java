import java.util.Arrays;

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n];
        Arrays.fill(ans, 0);

        int zeros = 0;
        int prod = 1;

        for (int i : nums) {
            if (i == 0) {
                zeros++;
            } else {
                prod *= i;
            }
        }

        if (zeros == 1) {
            for (int i = 0; i < n; i++) {
                ans[i] = nums[i] == 0 ? prod : 0;
            }
        } else if (zeros == 0) {
            for (int i = 0; i < n; i++) {
                ans[i] = prod / nums[i];
            }
        }

        return ans;
    }
}