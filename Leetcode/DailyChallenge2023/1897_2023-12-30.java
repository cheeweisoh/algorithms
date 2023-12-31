import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean makeEqual(String[] words) {
        if (words.length == 1) {
            return true;
        }
        
        String s = String.join("", words);
        Map<Character, Integer> counts = new HashMap<>();
        
        for (int i = 0; i < s.length(); i++) {
            counts.merge(s.charAt(i), 1, Integer::sum);
        }

        for (int c : counts.values()) {
            if (c % words.length != 0) {
                return false;
            }
        }

        return true;
    }
}
