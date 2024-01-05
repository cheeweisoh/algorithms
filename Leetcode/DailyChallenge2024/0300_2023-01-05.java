import java.util.Arrays;

class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] mem = new int[nums.length];
        mem[nums.length - 1] = 1;

        for (int i = nums.length - 2; i >= 0; i--) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] < nums[j]) {
                    mem[i] = Math.max(mem[i], mem[j] + 1);
                }
            }
            if (mem[i] == 0) {
                mem[i] = 1;
            }
        }

        int ans = Arrays.stream(mem).max().getAsInt();

        return ans;
    }
}
