import java.util.HashMap;
import java.util.Map;

class Solution {
    public int majorityElement(int[] nums) {
        int numsMajority = nums.length / 2;
        Map<Integer, Integer> numsCount = new HashMap<>();

        for (int i : nums) {
            numsCount.put(i, numsCount.getOrDefault(i, 0) + 1);
        }

        int ans = 0;

        for (Map.Entry<Integer, Integer> entry : numsCount.entrySet()) {
            if (entry.getValue() > numsMajority) {
                ans = entry.getKey();
                break;
            }
        }

        return ans;
    }
}