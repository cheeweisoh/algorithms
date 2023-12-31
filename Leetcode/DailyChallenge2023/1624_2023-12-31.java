import java.util.HashMap;

class Solution {
    public int maxLengthBetweenEqualCharacters(String s) {
        HashMap<Character, Integer> firstLetters = new HashMap<>();
        int ans = -1;

        for (int i = 0; i < s.length(); i++) {
            char currChar = s.charAt(i);
            if (firstLetters.containsKey(currChar)) {
                ans = Math.max(ans, i - firstLetters.get(currChar) - 1);
            }
            else {
                firstLetters.put(currChar, i);
            }
        }

        return ans;
    }
}