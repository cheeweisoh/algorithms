import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

class Solution {
    public List<List<Integer>> findMatrix(int[] nums) {
        Map<Integer, Integer> counts = new HashMap<>();
        List<List<Integer>> ans = new ArrayList<>();
        ans.add(new ArrayList<>());

        for (int i : nums) {
            counts.put(i, counts.getOrDefault(i, 0) + 1);

            if (counts.get(i) > ans.size()) {
                ans.add(new ArrayList<>());
            }

            ans.get(counts.get(i) - 1).add(i);
        }

        return ans;
    }
}