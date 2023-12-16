import java.util.HashMap;

class Solution{
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> characterMap = new HashMap<>();

        for (int i = 0; i < s.length(); i++){
            char currSChar = s.charAt(i);
            characterMap.put(currSChar, characterMap.getOrDefault(currSChar, 0) + 1);

            char currTChar = t.charAt(i);
            characterMap.put(currTChar, characterMap.getOrDefault(currTChar, 0) - 1);
        }

        for (int value : characterMap.values()) {
            if (value != 0) {
                return false;
            }
        }

        return true;
    }

    public boolean isAnagramFaster(String s, String t){
        char[] sArray = s.toCharArray();
        char[] tArray = t.toCharArray();
        int[] count = new int[26];

        for (char c: sArray) {
            count[c - 'a']++;
        }

        for (char c: tArray) {
            int index = c - 'a';
            count[index]--;

            if (count[index] < 0) {
                return false;
            }
        }

        return true;
    }
}