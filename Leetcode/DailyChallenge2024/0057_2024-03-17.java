import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> ans = new ArrayList<>();
        int newStart = newInterval[0];
        int newEnd = newInterval[1];
        boolean inserted = false;

        for (int[] inv : intervals) {
            int currStart = inv[0];
            int currEnd = inv[1];

            if (currEnd < newStart || inserted) {
                ans.add(new int[]{currStart, currEnd});
                continue;
            }

            newStart = Math.min(currStart, newStart);
            if (currStart > newEnd) {
                ans.add(new int[]{newStart, newEnd});
                ans.add(new int[]{currStart, currEnd});
                inserted = true;
                continue;
            }

            if (newEnd <= currEnd) {
                ans.add(new int[]{newStart, currEnd});
                inserted = true;
            }
        }

        if (!inserted) {
            ans.add(new int[]{newStart, newEnd});
        }

        return ans.toArray(new int[ans.size()][]);
    }
}