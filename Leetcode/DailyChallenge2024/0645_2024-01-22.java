class Solution {
    public int[] findErrorNums(int[] nums) {
        int n = nums.length;
        int xorAll = 0;
        int xorArray = 0;

        for (int i = 1; i <= n; i++) {
            xorAll ^= i;
        }

        for (int num : nums) {
            xorArray ^= num;
        }

        int xorResult = xorArray ^ xorAll;

        int rightmostSetBit = xorResult & -xorResult;

        int xorSet = 0;
        int xorNotSet = 0;

        for (int i = 1; i <= n; i++) {
            if ((i & rightmostSetBit) != 0) {
                xorSet ^= i;
            } else {
                xorNotSet ^= i;
            }
        }

        for (int num : nums) {
            if ((num & rightmostSetBit) != 0) {
                xorSet ^= num;
            } else {
                xorNotSet ^= num;
            }
        }

        for (int num : nums) {
            if (num == xorSet) {
                return new int[]{xorSet, xorNotSet};
            }
        }

        return new int[]{xorNotSet, xorSet};
    }
}