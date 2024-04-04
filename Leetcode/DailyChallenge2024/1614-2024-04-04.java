class Solution {
    public int maxDepth(String s) {
        int currDepth = 0, maxDepth = 0;

        for (char i : s.toCharArray()) {
            if (i == '(') {
                currDepth++;
                maxDepth = Math.max(maxDepth, currDepth);
            } else if (i == ')') {
                currDepth--;
            }
        }

        return maxDepth;
    }
}
