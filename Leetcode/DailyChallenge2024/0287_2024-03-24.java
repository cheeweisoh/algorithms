class Solution {
    public int findDuplicate(int[] nums) {
        int slow = 0, fast = 0, ans = 0;

        while (true) {
            slow = nums[slow];
            fast = nums[nums[fast]];
            if (slow == fast) {
                break;
            }
        }

        while (ans != slow) {
            ans = nums[ans];
            slow = nums[slow];
        }

        return ans;
    }
}
