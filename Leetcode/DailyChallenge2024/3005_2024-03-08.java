class Solution {
    public int maxFrequencyElements(int[] nums) {
        int[] freq = new int[101];
        int maxFreq = 0;
        int f = 0;

        for (int i : nums) {
            freq[i]++;
            
            if (freq[i] == maxFreq) {
                f++;
            }

            if (freq[i] > maxFreq) {
                f = 1;
                maxFreq = freq[i];
            }
        }
        return f * maxFreq;
    }
}