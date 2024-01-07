import java.util.HashMap;

class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        int n = nums.length;
        int total = 0;
        
        HashMap<Integer, Integer>[] mem = new HashMap[n];
        for (int i = 0; i < n; i++) {
            mem[i] = new HashMap<>();
        }

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                long diffLong = (long) nums[i] - nums[j];

                if (diffLong > Integer.MAX_VALUE || diffLong < Integer.MIN_VALUE) {
                    continue;
                }

                int diff = (int) diffLong;
                mem[i].put(diff, mem[i].getOrDefault(diff, 0) + 1);

                if (mem[j].containsKey(diff)) {
                    mem[i].put(diff, mem[i].get(diff) + mem[j].get(diff));
                    total += mem[j].get(diff);
                }
            }
        }        
        
        return total;
    }
}