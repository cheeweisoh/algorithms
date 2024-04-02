import java.util.Arrays;

class Solution {
    public boolean isIsomorphic(String s, String t) {
        int[] charMapS = new int[200];
        int[] charMapT = new int[200];
        Arrays.fill(charMapS, -1);
        Arrays.fill(charMapT, -1);

        for (int i = 0; i < s.length(); i++) {
            int charS = (int) s.charAt(i);
            int charT = (int) t.charAt(i);
            
            if (charMapS[charS] != charMapT[charT]) {
                return false;
            }

            charMapS[charS] = i + 1;
            charMapT[charT] = i + 1;
        }

        return true;
    }
}
