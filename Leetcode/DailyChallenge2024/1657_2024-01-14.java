import java.util.Arrays;

class Solution {
    public boolean closeStrings(String word1, String word2) {
        int[] count1 = new int[26];
        int[] count2 = new int[26];

        for (char i : word1.toCharArray()) {
            count1[i - 'a']++;
        }

        for (char i : word2.toCharArray()) {
            count2[i - 'a']++;
        }

        for (int i = 0; i < 26; i++){
            if ((count1[i] == 0 && count2[i] != 0) || count1[i] != 0 && count2[i] == 0){
                return false;
            }
        }

        Arrays.sort(count1);
        Arrays.sort(count2);

        for (int i = 0; i < 26; i++){
            if (count1[i] != count2[i]) {
                return false;
            }
        }

        return true;
    }
}