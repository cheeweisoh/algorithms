import java.util.HashMap;

class Solution {
    public int maxSubarrayLength(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int l = 0, r = 0, ans = 0;

        while (r < nums.length) {
            map.put(nums[r], map.getOrDefault(nums[r], 0) + 1);

            while (map.get(nums[r]) > k) {
                map.put(nums[l], map.get(nums[l]) - 1);
                l++;
            }
            ans = Math.max(ans, r - l + 1);
            r++;
        }

        return ans;
    }
}
