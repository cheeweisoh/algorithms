class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        int[] occurs = new int[2001];
        int[] seen = new int[arr.length + 1];

        for (int i : arr) {
            occurs[i + 1000]++;
        }

        for (int i : occurs) {
            if (i != 0 && seen[i] == 1) {
                return false;
            }

            seen[i] = 1;
        }

        return true;
    }
}
