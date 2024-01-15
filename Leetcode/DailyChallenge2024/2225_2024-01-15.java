import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> findWinners(int[][] matches) {
        int[] losses = new int[100001];

        for (int i = 0; i < matches.length; i++) {
            int winner = matches[i][0];
            int loser = matches[i][1];
            
            if (losses[winner] == 0) {
                losses[winner] = -1;
            }

            if (losses[loser] == -1) {
                losses[loser] = 1;
            } else {
                losses[loser] ++;
            }
        }

        List<Integer> noLosses = new ArrayList<>();
        List<Integer> oneLoss = new ArrayList<>();

        for (int i = 1; i < losses.length; i++) {
            if (losses[i] == -1) {
                noLosses.add(i);
            } else if (losses[i] == 1) {
                oneLoss.add(i);
            }
        }

        List<List<Integer>> ans = new ArrayList<>();
        ans.add(noLosses);
        ans.add(oneLoss);

        return ans;
    }
}