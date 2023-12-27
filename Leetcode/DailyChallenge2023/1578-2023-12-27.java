class Solution {
    public int minCost(String colors, int[] neededTime) {
        int idx = 0;
        int totalTime = 0;

        for (int i = 1; i < neededTime.length; i++) {
            if (colors.charAt(i) != colors.charAt(i - 1)) {
                idx = i;
            }
            else {
                if (neededTime[i] < neededTime[idx]) {
                    totalTime += neededTime[i];
                }
                else {
                    totalTime += neededTime[idx];
                    idx = i;
                }
            }
        }

        return totalTime;
    }
}