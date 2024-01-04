import java.util.HashMap;
import java.util.Map;

class Solution {
    public int minOperations(int[] nums) {
        int ans = 0;
        Map<Integer, Integer> counts = new HashMap<>();

        for (int i : nums) {
            counts.put(i, counts.getOrDefault(i, 0) + 1);
        }

        for (int c : counts.values()) {
            if (c == 1) {
                return -1;
            }
            ans += Math.floorDiv(c, 3);

            if (c % 3 != 0) {
                ans ++;
            }
        }

        return ans;
    }
}