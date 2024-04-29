class Solution {
    public int minOperations(int[] nums, int k) {
        int finalXOR = 0;

        for (int num : nums) {
            finalXOR = finalXOR ^ num;
        }

        int ans = 0;

        while (k > 0 || finalXOR > 0) {
            if ((k % 2) != (finalXOR % 2)) {
                ans++;
            }

            k /= 2;
            finalXOR /= 2;
        }

        return ans;
    }
}
