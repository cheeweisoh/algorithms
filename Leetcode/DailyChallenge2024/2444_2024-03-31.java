class Solution {
    public long countSubarrays(int[] nums, int minK, int maxK) {
        int minCurr = -1, maxCurr = -1, l =-1, r = 0;
        long ans = 0;

        while (r < nums.length){
            if (nums[r] < minK || nums[r] > maxK) {
                minCurr = r;
                maxCurr = r;
                l = r;
            }

            minCurr = nums[r] == minK ? r : minCurr;
            maxCurr = nums[r] == maxK ? r : maxCurr;
            ans += Math.min(minCurr, maxCurr) - l;
            r++;
        }

        return ans;
    }
}
