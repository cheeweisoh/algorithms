import java.util.ArrayList;
import java.util.List;

class Solution {
    public int findRotateSteps(String ring, String key) {
        char[] ringArray = ring.toCharArray();
        List<Integer>[] ringPositions = new List[26];

        for (int i = 0; i < ringArray.length; i++) {
            int c = ringArray[i] - 'a';
            if (ringPositions[c] == null) {
                ringPositions[c] = new ArrayList<>();
            }
            ringPositions[c].add(i);
        }

        int[][] dp = new int[key.length()][ringArray.length];

        return helper(0, 0, ringPositions, key.toCharArray(), ringArray, dp);
    }

    private int helper(int index, int pos, List<Integer>[] ringPositions, char[] key, char[] ringArray, int[][] dp) {
        if (index == key.length) {
            return 0;
        }

        if (dp[index][pos] > 0) {
            return dp[index][pos];
        }

        char target = key[index];
        List<Integer> possiblePositions = ringPositions[target - 'a'];
        int minSteps = Integer.MAX_VALUE;

        for (int nextPos : possiblePositions) {
            int steps = Math.min(Math.abs(nextPos - pos), ringArray.length - Math.abs(nextPos - pos));
            int totalSteps = steps + helper(index + 1, nextPos, ringPositions, key, ringArray, dp);
            minSteps = Math.min(minSteps, totalSteps);
        }

        return dp[index][pos] = minSteps + 1;
    }
}