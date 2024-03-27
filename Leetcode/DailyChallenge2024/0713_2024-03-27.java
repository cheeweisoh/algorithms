class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        if (k <= 1) {
            return 0;
        }

        int n = nums.length;
        int left = 0, right = 0, prod = 1, count = 0;

        while (right < n) {
            prod *= nums[right];
            while (prod >= k) {
                prod /= nums[left++];
            }
            count += 1 + (right - left);
            right++;
        }

        return count;
    }
}