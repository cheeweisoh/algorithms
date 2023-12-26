import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;

class Solution {
    HashMap<List<Integer>, Integer> mem = new HashMap<>();
    int MOD = 1000000007;

    private int dfs(int n, int k, int t) {
        List<Integer> currKey = new ArrayList<>();
        currKey.add(n);
        currKey.add(t);
        
        if (mem.containsKey(currKey)) {
            return mem.get(currKey);
        }

        if (n == 0 && t == 0) {
            return 1;
        }
        if (n == 0 || t == 0) {
            return 0;
        }

        int ways = 0;
        for (int i = 1; i <= k; i++) {
            ways = (ways + dfs(n - 1, k, t - i)) % MOD;
        }
        mem.put(currKey, ways);

        return ways;
    }

    public int numRollsToTarget(int n, int k, int target) {
        return dfs(n, k, target);
    }
}
