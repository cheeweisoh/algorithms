import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public String getSignature(String s) {
        int[] counts = new int[26];
        for (char c : s.toCharArray()) {
            counts[c - 'a']++;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 26; i++) {
            if (counts[i] != 0) {
                sb.append((char) ('a' + i)).append(counts[i]);
            }
        }

        System.out.println(sb.toString());

        return sb.toString();
    }

    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> ans = new ArrayList<>();
        Map<String, List<String>> groups = new HashMap<>();

        for (String s : strs) {
            groups.computeIfAbsent(getSignature(s), k -> new ArrayList<>()).add(s);
        }

        ans.addAll(groups.values());

        return ans;
    }
}