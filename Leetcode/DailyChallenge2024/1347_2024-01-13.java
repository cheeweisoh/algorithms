class Solution {
    public int minSteps(String s, String t) {
        int[] countS = new int[26];
        int[] countT = new int[26];

        for (char i : s.toCharArray()) {
            countS[i - 'a']++;
        }

        for (char i : t.toCharArray()) {
            countT[i - 'a']++;
        }

        int steps = 0;
        for (int i = 0; i < 26; i++) {
            steps += Math.abs(countS[i] - countT[i]);
        }

        return steps/2;
    }   
}