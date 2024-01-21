class Solution {
    public int rob(int[] nums) {
        int r = 0;
        int nr = 0;

        for (int i : nums) {
            int rNew = nr + i;
            int nrNew = Math.max(r, nr);
            r = rNew;
            nr = nrNew;
        }

        return Math.max(r, nr);
    }
}