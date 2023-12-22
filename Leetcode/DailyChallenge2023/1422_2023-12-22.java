class Solution {
    public int maxScore(String s){
        int leftScore = (s.charAt(0) == '0') ? 1 : 0;
        int rightScore = s.substring(1).replaceAll("0", "").length();
        int finalScore = leftScore + rightScore;

        for (int i = 1; i < s.length() - 1; i++) {
            if (s.charAt(i) == '0') {
                leftScore ++;
            }
            else if (s.charAt(i) == '1'){
                rightScore --;
            }

            finalScore = Math.max(finalScore, leftScore + rightScore);
        }

        return finalScore;
    }
}